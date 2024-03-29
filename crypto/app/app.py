#!/usr/bin/env python
#  -*- coding: utf-8 -*-
import argparse
import os
from http import HTTPStatus

import misaka as m
from flask import Flask, url_for
from flask_cors import CORS
from flask_restplus import Api, Resource, abort, apidoc, fields
from waitress import serve
from werkzeug.middleware.proxy_fix import ProxyFix

from ivonet.crypto.baudot_code import text_2_baudot, baudot_2_text
from ivonet.crypto.bifid import bifid_encrypt, bifid_decrypt
from ivonet.crypto.caesar import rot
from ivonet.crypto.morsecode import text_2_morse, morse_2_text
from ivonet.crypto.number_substitution import text_to_numbers, numbers_to_text
from ivonet.crypto.sms import Sms
from ivonet.math.hexadecimal import number_as_word
from ivonet.math.roman_numerals import roman
from ivonet.string.alphabet import base_26_encode_string
from ivonet.woorden import Woordenboek

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='ivonet-crypto',
          description='API for the ivonet crypto package')

ns = api.namespace('crypto', 'The ivonet-crypto namespace')

keyvalue = api.model('KeyValue', {
    'key': fields.String(readOnly=True, description='The key to encrypt with'),
    'value': fields.String(required=True, description='The value to encrypt')
})

value = api.model('Value', {
    'value': fields.String(readOnly=True, description='The required kind of text'),
})

if os.environ.get('PROD') == "1":
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=True, _scheme='https')

    Api.specs_url = specs_url

app.register_blueprint(apidoc.apidoc)


def key_value(key='key', body='value'):
    kv = api.payload
    return kv[key], kv[body]


def get_value(key='value'):
    payload = api.payload
    return payload[key]


@ns.route("/services")
class Services(Resource):
    @ns.doc("Lists all the endpoints")
    def get(self):
        services = {'/rot': m.html(rot.__doc__),
                    '/bifid/encrypt': m.html(bifid_encrypt.__doc__),
                    '/bifid/decrypt': m.html(bifid_decrypt.__doc__),
                    '/baudot/encrypt': m.html(baudot_2_text.__doc__),
                    '/baudot/decrypt': m.html(text_2_baudot.__doc__),
                    '/morse/encrypt': m.html(morse_2_text.__doc__),
                    '/morse/decrypt': m.html(text_2_morse.__doc__),
                    '/numbers/encrypt': m.html(numbers_to_text.__doc__),
                    '/numbers/decrypt': m.html(text_to_numbers.__doc__),
                    '/sms/encrypt': m.html(Sms.txt_2_sms.__doc__),
                    '/sms/decrypt': m.html(Sms.sms_2_txt.__doc__),
                    }
        return {'result': services}


@ns.route('/rot')
class Rot(Resource):

    @ns.doc("""Simple letter rotation function""")
    @ns.expect(value)
    def post(self):
        payload = api.payload
        try:
            return rot(payload['value']), HTTPStatus.OK
        except ValueError as e:
            abort(HTTPStatus.BAD_REQUEST, str(e))


@ns.route('/dutch/word')
class DutchWord(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.wb = Woordenboek()

    @ns.doc("""Checks if the given value is a word""")
    @ns.expect(value)
    def post(self):
        ww = lambda x: x.replace(",", "").replace("?", "").replace("!", "").replace(".", "")
        try:
            found = []
            notfound = []
            for w in get_value().split():
                if self.wb.is_word(ww(w)):
                    found.append(ww(w))
                else:
                    notfound.append(ww(w))
            return {'true': found, 'false': notfound}, HTTPStatus.OK
        except ValueError as e:
            abort(HTTPStatus.BAD_REQUEST, str(e))


@ns.route('/bifid/encrypt')
class BifidEncrypt(Resource):

    @ns.doc("""Encrypt with the Bifid algorithm""")
    @ns.expect(keyvalue)
    def post(self):
        kv = api.payload
        return {'result': bifid_encrypt(kv['key'], kv['value'])}, 200


@ns.route('/bifid/decrypt')
class BifidDecrypt(Resource):
    @ns.doc("""Decrypt with the Bifid algorithm""")
    @ns.expect(keyvalue)
    def post(self):
        kv = api.payload
        return {'result': bifid_decrypt(kv['key'], kv['value'])}, 200


@ns.route('/baudot/encrypt')
class BaudotEncrypt(Resource):

    @ns.doc("""Encrypt with the Baudot algorithm""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': text_2_baudot(get_value())}, 200
        except KeyError as e:
            abort(HTTPStatus.BAD_REQUEST,
                  "The provided 'letter' is not part of the Baudot code and can not be encrypted: " + str(e))


@ns.route('/baudot/decrypt')
class BaudotDecrypt(Resource):
    @ns.doc("""Decrypt with the Baudot algorithm""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': baudot_2_text(get_value()).strip()}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be something like: '01000 10000 01010'")


@ns.route('/morse/encrypt')
class MorseEncrypt(Resource):

    @ns.doc("""Encrypt with the morse code""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': text_2_morse(get_value())}, 200
        except KeyError as e:
            abort(HTTPStatus.BAD_REQUEST,
                  "The provided 'letter' is not part of the Morse code and can not be encrypted: " + str(e))


@ns.route('/morse/decrypt')
class MorseDecrypt(Resource):
    @ns.doc("""Decrypt with the morse code""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': morse_2_text(get_value()).strip()}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be morse code")


@ns.route('/numbers/encrypt')
class NumbersEncrypt(Resource):
    @ns.doc("""Encrypt with the provided text to numbers (number substitution)""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': text_to_numbers(get_value())}, 200
        except KeyError as e:
            abort(HTTPStatus.BAD_REQUEST,
                  "The provided 'letter' is not part of the number substitution alphabet and can not be encrypted: " +
                  str(e))


@ns.route('/numbers/decrypt')
class NumbersDecrypt(Resource):
    @ns.doc("""Decrypt with the provided code to text (number substitution)""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': numbers_to_text(get_value()).strip()}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be a number sequence")


@ns.route('/sms/encrypt')
class SmsEncrypt(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.sms = Sms()

    @ns.doc("""Encrypt with the provided text to SMS code""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': self.sms.txt_2_sms(get_value())}, 200
        except KeyError as e:
            abort(HTTPStatus.BAD_REQUEST,
                  "The provided 'letter' is not part of the SMS alphabet and can not be encrypted: " + str(e))


@ns.route('/sms/decrypt')
class SmsDecrypt(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.sms = Sms()

    @ns.doc("""Decrypt with the provided SMS code to possible words based on dutch dictionary""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': self.sms.sms_2_txt(get_value()).strip()}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be a sms sequence or it can not be decrypted.")

@ns.route('/base/26/encode')
class Base26Encode(Resource):
    @ns.doc("""Encodes a string to a base 26 encoded string. A = 0, B = 1, Z = 25, BA = 26, BB = 27, XYZ = 16197""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': base_26_encode_string(get_value())}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be a text.")

@ns.route('/base/26/decode')
class Base26Decode(Resource):
    @ns.doc("""Decodes a string from a base 26 encoded number.""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': base_26_encode_string(get_value())}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be a base 26 encoded string.")

@ns.route('/hexadecimal/word')
class HexadecimalAsWord(Resource):
    @ns.doc("""Transforms a number into a hexadecimal notation and transforms the digits to 'corresponding' letters.""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': number_as_word(get_value())}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be a number.")

@ns.route('/numerals/roman')
class RomanNumerals(Resource):
    @ns.doc("""Transforms a number to a roman numeral or to a number if already a roman numeral.""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': roman(get_value())}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be a number between 0 and 3999 or a roman numeral")

@ns.route('/numerals/roman')
class RomanNumerals(Resource):
    @ns.doc("""Transforms a number to a roman numeral or to a number if already a roman numeral.""")
    @ns.expect(value)
    def post(self):
        try:
            return {'result': roman(get_value())}, 200
        except KeyError:
            abort(HTTPStatus.BAD_REQUEST, "The provided value should be a number between 0 and 3999 or a roman numeral")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("python3 app.py")
    parser.add_argument('-b', '--bind', required=False, default="127.0.0.1",
                        help="IP to bind to e.g. 0.0.0.0. (default 127.0.0.1)")
    parser.add_argument('-p', '--port', required=False, default="8080",
                        help="Port to run on. (default 8080)")
    args = parser.parse_args()
    if os.getenv("DEBUG") == "1":
        app.run(host=args.bind, port=args.port, debug=True)
    else:
        serve(app, host=args.bind, port=args.port)

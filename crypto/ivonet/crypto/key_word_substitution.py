import string
from collections import OrderedDict


class KeyWordSubstitution:
    def __init__(self, keyword=None):
        self.permutation_dict = OrderedDict()
        if keyword:
            self.create_permutation_dict(keyword)

    def create_permutation_dict(self, keyword: str):
        alphabet = string.ascii_uppercase
        used_letters = set()
        self.permutation_dict = OrderedDict()

        # Add the letters from the keyword
        for letter in keyword:
            letter = letter.upper()
            if letter not in used_letters:
                if letter not in alphabet:
                    continue
                dst_letter = alphabet[len(used_letters)]
                self.permutation_dict[letter] = dst_letter
                used_letters.add(letter)

        # Add all other letters
        for letter in alphabet:
            if letter not in used_letters:
                dst_letter = alphabet[len(used_letters)]
                self.permutation_dict[letter] = dst_letter
                used_letters.add(letter)

    def get_permutation_alphabet(self):
        return ''.join(list(self.permutation_dict.keys()))

    def _print_permutation_dict(self):
        print(''.join(list(self.permutation_dict.keys())))
        print(''.join(list(self.permutation_dict.values())))

    def permute_message(self, original_msg):
        original_msg = original_msg.upper()
        permuted_letters = []
        for x in original_msg:
            if x in self.permutation_dict:
                permuted_letters.append(self.permutation_dict[x])
            else:
                permuted_letters.append(x)
        # print(original_msg)
        ret = ''.join(permuted_letters)
        return ret


if __name__ == '__main__':
    # kws = KeyWordSubstitution()
    # kws.create_permutation_dict('hoogste berg')
    # print()
    # msg = 'CGTGIGPDGM, DAFAIHJCHNK, DGPKBPOAS ZSS, DIOOIOOIJJI, DQMMLY-GLMCIFE, FASUW-IUAFSG, ' \
    #       'FGTJMGHSSN, FIVC, GBSXGFTSMSABGFT, HFYX, HGKJGHBUH, IKUJQ VAJPKJ, IMHHQ-RMAQQGFFAS, ' \
    #       'IMHSFBGFT, LDLZHFS, LUJGHD CHYH, QBQBOGOGHSSN, RHMFSH, RJVSIHSSN, STJHFA, SYNSHSSN, ' \
    #       'TFONKTP, TVTNTPQ, VBOQJNBGHSSN, VJPQJDHSSN, VLFEPOSBILFE, VUUMBGFT, WHCEL'
    # kws.permute_message(msg)
    #
    # kws.permute_message('NZR NNFVYT QJG IWQN IQFLLNJQ')
    # kws.permute_message('XS UOOH VSH DOG NWSB OZG XS VSH RCCF VSPH')
    # kws.permute_message('ANLNISUEWHTINSJECDNOENRBUEAKNLNHEEBB')
    # kws.permute_message('VROPRIDGIVDLWSEHVANBIVRWRWVAASIGMXCVOVRTQDPWPEECSZAIIROADMECANRT')
    # kws.permute_message('RM ELVGYZO RH SVG HRNKVO: QV YVMG LU LK GRQW LU QV YVMG GV OZZG. ZOH QV GV OZZG YVMG, NLVG QV ALITVM WZG QV LK GRQW EVIGIVPG')
    # kws.permute_message('TMAVFEKUOBOBRNRSEVVALCYAVNMAMASSWETIC')
    # kws.permute_message('PDULAF NAONPG NAIPRY PBEFDP ULDELQ NAPYAP RTGLEL PKWTAR NAPHTO UBDBGC XEABAB GXCNEW BABAGL GXENEW BACAGL GXENEW BABAGL GXCNEW BAEAGL GXBNEW BAEAGL GXCNEW BABAGL GXCNEW BABAGL GXENEW BACAGL GVENEW BABAGL GXBNEW BAEAGL GXBNEW BAEAGL GXENEW BABAGL GXCNEW BABAGL GXENEA NARKLO EDXEAC ABGXAZ')

    kws = KeyWordSubstitution()
    # kws.create_permutation_dict("koppelwoorden")
    # msg = "ZNAG, VHMELG, OCNAULG, OCNABLG, CNABLG, QPDNAGLG, DLSLG, UHHMBHFLG"
    # # msg = "ZIJN, WORDEN, BLIJVEN, BLIJKEN, LIJKEN, SCHIJNEN, HETEN, VOORKOMEN"
    # # for i in range(27):
    # print(msg)
    # msg = kws.permute_message(msg)
    # print(msg)
    #
    # msg = "YSHFW KGITX SSGWI EGIMB QZVTR OIXLM LYDSS Y".replace(" ", "")
    # kws.create_permutation_dict("VOORJELIGTOFFLIKKERTDENBVKERSTPUZZEL")
    # print(kws.permute_message(msg))
    #
    # kws.create_permutation_dict("substitutie")
    # print(kws.get_permutation_alphabet())

    # kws.create_permutation_dict("pietmondriaan")
    # kws.create_permutation_dict("victoryboogiewoogie")
    # kws.create_permutation_dict("broadwayboogiewoogie")
    # kws.create_permutation_dict("roodgeelblauw")
    # kws.create_permutation_dict("PieterCornelisMondriaan")
    # kws.create_permutation_dict("PieterCornelisMondriaan")
    # kws.create_permutation_dict("neoplasticisme")
    # kws.create_permutation_dict("primairekleuren")
    # kws.create_permutation_dict("destijl")
    # kws.create_permutation_dict("paintmodern")
    # kws.create_permutation_dict("mondriaandestijl")
    # kws.create_permutation_dict("abstraction")
    # print(kws.get_permutation_alphabet())
    # print(kws.permute_message("Sjlkpfpkha gmr eaqrypst Okkldh"))

    # kws.create_permutation_dict("burgemeester")
    # kws.create_permutation_dict("zangeres")
    # kws.create_permutation_dict("historicus")
    # kws.create_permutation_dict("ministerpresident")
    # kws.create_permutation_dict("scheikundige")
    # kws.create_permutation_dict("presentator")
    # kws.create_permutation_dict("Nobelprijswinnaar")
    # kws.create_permutation_dict("voetballer")
    # kws.create_permutation_dict("dirigent")
    # kws.create_permutation_dict("kunstenaar")
    # kws.create_permutation_dict("televisiepresentatrice")
    # kws.create_permutation_dict("acteur")
    # kws.create_permutation_dict("burgemeester")
    # kws.create_permutation_dict("pvda")
    # kws.create_permutation_dict("wimkok")
    # print(kws.permute_message("􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃CDQIAJNEQGVAJNKNDWDDQN􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))
    # print(kws.permute_message("􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃QMORLQDITAPOFMQHCDAH􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))
    # print(kws.permute_message("􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃FMKCMTSFHGQPSKKMQVCVCMGMNHGNSINCHGNMOMDDSCEHDN􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))
    # print(kws.permute_message("􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬􏰬􏱗􏰩􏱃AZCZDFPJQCJNDCSCYDCQFPJNCD􏰞􏰬􏱗􏰣􏰡􏰻􏰩􏰑􏱗􏰰􏰱􏰡􏰻􏰩􏰳􏰩􏰬􏰪􏰬"))

    kws.create_permutation_dict("LETTERONTWERPERS")
    print(kws.permute_message("BIFIDGERARDUNGER"))



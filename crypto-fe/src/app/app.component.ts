import {Component, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  services: Observable<string>;

  constructor(private http: HttpClient) {}


  public getServices() {
    this.services = this.http.get<string>("http://localhost:5000/crypto/services", {
      observe: 'body',
      responseType: 'json'
    }).pipe(source => this.services = source);
    // this.http.get<string>("http://localhost:5000/crypto/services", {
    //   observe: 'response',
    //   responseType: 'json'
    // }).toPromise()
    //   .then(value => this.services = value);
  }

  ngOnInit(): void {
    this.getServices();
  }
}

import {Component, OnInit} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {ServicesResult} from "./app.model";
import {Observable} from "rxjs";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  public services: Observable<ServicesResult>;

  constructor(private http: HttpClient) {
  }

  ngOnInit(): void {
    this.services = this.getServices();
  }

  public getServices(): Observable<ServicesResult> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };
    return this.http.get<ServicesResult>('http://localhost:8080/crypto/services', httpOptions);

  }

}

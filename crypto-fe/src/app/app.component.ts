import {Component} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private http: HttpClient) {
  }

  // public async getServices(): Promise<string> {
  //   return await this.http.get<string>("http://localhost:5000/crypto/services").toPromise();
  // }
}

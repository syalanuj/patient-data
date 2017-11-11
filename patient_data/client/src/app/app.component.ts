import { Component } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Response } from '@angular/http';
import { AppService } from './services/app.service';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  constructor (private appService: AppService) {}
  providers;
  //Have to provide empty values fro prod build
  parameters = {
    min_discharges: '',
    max_discharges: '',
    min_average_covered_charges: '',
    max_average_covered_charges: '',
    min_average_medicare_payments: '',
    max_average_medicare_payments: '',
    state: ''
  };
  
  ngOnInit() {
    this.getFilteredProviders(this.parameters);
  }
  filterProvider(){
    this.getFilteredProviders(this.parameters);
  }

  getFilteredProviders(parameters){
    this.appService.getFilteredProviders(parameters)
    .subscribe((response) => {
      this.providers = response
    },
    (error) => {
      console.log(error)
    });
  }
  
}

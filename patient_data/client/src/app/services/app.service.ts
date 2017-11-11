import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import 'rxjs/add/observable/of';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/finally';
import { Injectable } from '@angular/core';


import {
    Http,
    RequestOptions,
    RequestOptionsArgs,
    Response,
    Request,
    Headers,
    URLSearchParams,
    XHRBackend
} from '@angular/http';
import { HttpParams } from '@angular/common/http';
import { environment } from './../../environments/environment';

@Injectable()
export class AppService extends Http {
    private apiUrl = environment.apiUrl;
    
    constructor(backend: XHRBackend,
        defaultOptions: RequestOptions) {
            super(backend, defaultOptions);
        }
        
        getFilteredProviders(params):Observable<Response>{
            let httpParams  = new URLSearchParams();
            if (params) {
                params.min_discharges == undefined || params.min_discharges == '' ? httpParams : httpParams.append('min_discharges', params.min_discharges);
                params.max_discharges == undefined || params.max_discharges == '' ? httpParams : httpParams.append('max_discharges', params.max_discharges);
                params.min_average_covered_charges == undefined || params.min_average_covered_charges == '' ? httpParams : httpParams.append('min_average_covered_charges', params.min_average_covered_charges);
                params.max_average_covered_charges == undefined || params.max_average_covered_charges == '' ? httpParams : httpParams.append('max_average_covered_charges', params.max_average_covered_charges);
                params.min_average_medicare_payments == undefined || params.min_average_medicare_payments == '' ? httpParams : httpParams.append('min_average_medicare_payments', params.min_average_medicare_payments);
                params.max_average_medicare_payments == undefined  || params.max_average_medicare_payments == ''? httpParams : httpParams.append('max_average_medicare_payments', params.max_average_medicare_payments);
                params.state == undefined || params.state == '' ? httpParams : httpParams.append('state', params.state);
                
            }
            let reqoptions = new RequestOptions({ params: httpParams });
            return this.get('api/providers',reqoptions)
            .map((response) => {
                return response.json();
            })
            .catch(this.handleError.bind(this));
        }
        
        private handleError(e): Observable<Response> {
            console.log({ show: true, message: e.statusText, messageType: '' });
            return Observable.throw(e);
        }
        
        get(url: string,reqoptions: RequestOptions, options?: RequestOptionsArgs): Observable<Response> {
            return super.get((url), reqoptions)
            .catch(this.onCatch)
            .do((res: Response) => {
                this.onSuccess(res);
            }, (error: any) => {
                this.onError(error);
            })
            .finally(() => {
                //Hide Loader can be done
            });
            
        }
        
        private getFullUrl(url: string): string {
            return this.apiUrl + url;
        }
        private onCatch(error: any, caught: Observable<any>): Observable<any> {
            return Observable.throw(error);
        }
        
        private onSuccess(res: Response): void {
        }
        
        private onError(res: Response): void {
            console.log('Error, status code: ' + res.status);
        }
        private getRequestOptionArgs(options?: RequestOptionsArgs): RequestOptionsArgs {
            if (options == null) {
                options = new RequestOptions();
            }
            if (options.headers == null) {
                options.headers = new Headers();
            }
            //options.headers.append('Content-Type', 'application/json');
            // options.headers.append('Authorization', this.cookieService.getCookie('token') );
            return options;
        }
    }
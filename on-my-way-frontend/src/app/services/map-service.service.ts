import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class MapServiceService {
  constructor(private http: HttpClient) { }
  url = environment.mapbox.url

  
}

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Incident } from "../models/Incident.model";

@Injectable({
  providedIn: 'root'
})
export class MapServiceService {
  constructor(private http: HttpClient) { }
  url = environment.url
  
  async getAllIncidents (): Promise<Incident[]> {
    const data = await fetch(this.url+'/allIncidents') 
    return await data.json() ?? [];
  }
}

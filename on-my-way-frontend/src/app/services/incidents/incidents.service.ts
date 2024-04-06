import { Injectable } from '@angular/core';
import { DetailInformation } from "../../interfaces/detail-information";
import { Marker } from "../../interfaces/marker";
import { Markers } from "../../interfaces/markers";

@Injectable({
  providedIn: 'root'
})
export class IncidentsService {
  //Dummy Data
  protected markers: Markers = {
    type: 'FeatureCollection',
    features: [
      {
        "type": "Feature",
        "properties": {
          "database_id" : "660f4cf31b992f0421e319aa", 
          "severity": "Moderate",
          "dateTime": "06/04/24 12:34PM",
          "description": "A bird ate my dog"
        },
        "geometry": {
          "coordinates": [
            144.737079,
            -37.71903
          ],
          "type": "Point"
        }
      },
      {
        "type": "Feature",
        "properties": {
          "database_id" : "660f8f40ea786c0d77bbe7d0",
          "severity": "High",
          "dateTime": "06/04/24 12:34PM",
          "description": "High tide"
        },
        "geometry": {
          "coordinates": [
            145.292036,
            -37.538708
          ],
          "type": "Point"
        }
      },
      {
        "type": "Feature",
        "properties": {
          "database_id" : "660f8fc74a04d811586e3bc1",
          "severity": "Severe",
          "dateTime": "06/04/24 12:34PM",
          "description": "Active Fire"
        },
        "geometry": {
          "coordinates": [
            144.559295,
            -37.235965
          ],
          "type": "Point"
        }
      },
      {
        "type": "Feature",
        "properties": {
          "database_id" : "660f966c13d2f3afe6b1ebd9",
          "dateTime": "07/04/24 3:12PM",
          "description": "death",
          "severity": "Extreme"
        },
        "geometry": {
          "coordinates": [
            143.797244,
            -37.445687
          ],
          "type": "Point"
        }
      }
    ]
    };

  protected detail: DetailInformation = {
    "severity" : "Mild",
    "latitude" : -120.13,
    "longitude" : 3.891,
    "datetime" : "06/04/24 12:23PM",
    "description" : "I'm running low on food and can't eaily leave my house in the floods",
  }

  constructor() { }

  getAllIncidents() : Markers{
    return this.markers;
  }

  getIncidentDetails(id:string): DetailInformation {
    return this.detail
  }
}

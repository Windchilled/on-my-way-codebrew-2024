import { Component, OnInit, inject } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';
import { environment } from '../../../../environments/environment';
import { IncidentsService } from "../../../services/incidents/incidents.service";
import { Markers } from "../../../interfaces/markers";
import { Marker } from "../../../interfaces/marker";
import { MarkerComponent } from '../marker/marker.component';
import {NgFor} from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css'],
  imports: [MarkerComponent],
})

export class MapComponent implements OnInit { 
  markers?: Markers;
  markerArray: Marker[] = [];
  map: mapboxgl.Map | undefined;
  incidentsService: IncidentsService = inject(IncidentsService);

  
  // style = 'mapbox://styles/102560056/clumwz4op00gz01pw3jze5zy0';
  lat: number = -37.7983;
  lng: number = 144.9609;
  
  sw_bound = new mapboxgl.LngLat(110.8909, -39.2695);
  ne_bound = new mapboxgl.LngLat(154.1289, -9.9139); 
  bounds = new mapboxgl.LngLatBounds(this.sw_bound, this.ne_bound);

  ngOnInit() {
     this.map = new mapboxgl.Map({
        // accessToken: environment.mapbox.accessToken, // I have no clue why this doesn't work
        accessToken: 'pk.eyJ1IjoiMTAyNTYwMDU2IiwiYSI6ImNsdWtwYzB6bDBxcW4yaWsyYXFnY3d0MjIifQ.KMav3MKT5-f5hSZoKPliFQ',
        container: 'map',
        // style: this.style,
        zoom: 2,
        center: [this.lng, this.lat],
        maxBounds: this.bounds,
      });
      this.map.addControl(
        new mapboxgl.GeolocateControl({
            positionOptions: {
                enableHighAccuracy: true
            },
            trackUserLocation: true,
            showUserHeading: true
        })
      );
      this.map.dragRotate.disable();
      this.map.touchZoomRotate.disableRotation();
  }
  constructor(){
    this.markers = this.incidentsService.getAllIncidents();
    this.markerArray = this.markers.features;
  }
}

import { environment } from '../../../environments/environment';
import { Component, OnInit } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})

export class MapComponent implements OnInit { 
  map: mapboxgl.Map | undefined;
  style = 'mapbox://styles/102560056/clum0icne00w901ra02lxh2ft';
  lat: number = -37.7983;
  lng: number = 144.9609;
  
  sw_bound = new mapboxgl.LngLat(110.8909, -39.2695); //110.8909
  ne_bound = new mapboxgl.LngLat(154.1289, -9.9139); //154.1289
  bounds = new mapboxgl.LngLatBounds(this.sw_bound, this.ne_bound);

  ngOnInit() {
     this.map = new mapboxgl.Map({
        // accessToken: environment.mapbox.accessToken,
        accessToken: 'pk.eyJ1IjoiMTAyNTYwMDU2IiwiYSI6ImNsdWtwYzB6bDBxcW4yaWsyYXFnY3d0MjIifQ.KMav3MKT5-f5hSZoKPliFQ',
        container: 'map',
        style: this.style,
        zoom: 2,
        center: [this.lng, this.lat],
        maxBounds: this.bounds,
      });
  }
}

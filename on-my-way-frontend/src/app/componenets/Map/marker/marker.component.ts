import { Component, Input } from '@angular/core';
import { MatIconModule } from "@angular/material/icon";
import { Marker } from "../../../interfaces/marker";  


@Component({
  selector: 'app-marker',
  standalone: true,
  imports: [MatIconModule],
  templateUrl: './marker.component.html',
  styleUrl: './marker.component.css'
})
export class MarkerComponent {
  @Input() marker!: Marker;
}

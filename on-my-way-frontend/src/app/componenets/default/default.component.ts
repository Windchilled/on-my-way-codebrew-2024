import { Component } from '@angular/core';
import { DetailsComponent } from '../details/details.component';
import { MapModule } from '../map/map.component.model';

@Component({
  selector: 'app-default',
  standalone: true,
  imports: [MapModule],
  templateUrl: './default.component.html',
  styleUrl: './default.component.css'
})
export class DefaultComponent {

}

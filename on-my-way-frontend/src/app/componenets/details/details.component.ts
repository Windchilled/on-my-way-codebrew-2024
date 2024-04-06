import { Component, inject } from '@angular/core';
import { DetailInformation } from "../../interfaces/detail-information";
import { IncidentsService } from "../../services/incidents/incidents.service";

@Component({
  selector: 'app-details',
  standalone: true,
  imports: [],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css'
})
export class DetailsComponent {
  details?: DetailInformation;
  incidentsService: IncidentsService = inject(IncidentsService);

  constructor(){
    this.details = this.incidentsService.getIncidentDetails('660f4cf31b992f0421e319aa');
  }
}

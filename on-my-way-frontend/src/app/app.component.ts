import { Component } from '@angular/core';
import { FooterComponent } from './componenets/footer/footer.component';
import { DetailsComponent } from './componenets/details/details.component';
import { MapModule } from './componenets/Map/map-display/map.component.model';
import { SearchBarComponent } from './componenets/search-bar/search-bar.component';
import { ReportButtonComponent } from './componenets/Report/report-button/report-button.component';
import { MatIconModule } from "@angular/material/icon";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FooterComponent, DetailsComponent, MapModule, SearchBarComponent, ReportButtonComponent, MatIconModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'on-my-way';
}

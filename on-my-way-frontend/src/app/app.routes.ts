import { Routes } from '@angular/router';
import { NotFoundComponent } from './componenets/not-found/not-found.component';
import { DefaultComponent } from './componenets/default/default.component';

export const routes: Routes = [
    {path: '', component: DefaultComponent},
    {path: '**', component: NotFoundComponent}
];

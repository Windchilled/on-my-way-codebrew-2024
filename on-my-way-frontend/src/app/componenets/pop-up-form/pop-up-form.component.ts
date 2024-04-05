import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-pop-up-form',
  standalone: true,
  imports: [],

  templateUrl: './pop-up-form.component.html',
  styleUrl: './pop-up-form.component.css'
})


export class PopUpFormComponent {
    constructor(public formRef: MatDialogRef<PopUpFormComponent>) {}

    onNoClick(): void {
    this.formRef.close();
  }

}



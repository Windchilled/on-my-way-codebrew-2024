import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DefaultComponent } from './default.component';
import { DetailsComponent } from '../details/details.component';
import { MapComponent } from '../map/map.component';

describe('DefaultComponent', () => {
  let component: DefaultComponent;
  let fixture: ComponentFixture<DefaultComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DefaultComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DefaultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

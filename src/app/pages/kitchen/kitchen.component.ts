import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CloseScrollStrategy } from '@angular/cdk/overlay';

@Component({
  selector: 'app-kitchen',
  templateUrl: './kitchen.component.html',
  styleUrls: ['./kitchen.component.scss']
})
export class KitchenComponent implements OnInit {

  mainLightOn = false;
  mainLightId: number;
  barLightOn = false;
  barLightId: number;
  barLightValue = 50;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.http.get('http://192.168.1.19:3000/lights').subscribe((data: any) => {
      console.log(data);
      const switches = data.switches;

      switches.forEach((gswitch) => {
        if (gswitch.name === 'Main Light') {
          if (gswitch.power === 'ON') {
            this.mainLightOn = true;
          }
          this.mainLightId = gswitch.id;
        }
        if (gswitch.name === 'Bar Lights') {
          if (gswitch.power === 'ON') {
            this.barLightOn = true;
          }
          this.barLightValue = gswitch.brightness;
          this.barLightId = gswitch.id;
        }
      });
    });

    setTimeout(() => {
      console.log('Starting login...');
      const frameRef: HTMLIFrameElement | HTMLElement = document.getElementById('thermostatWindow');
      var innerDoc = frameRef.ownerDocument;
      console.log(frameRef);
      console.log(typeof(frameRef));
      const userNameInput = innerDoc.getElementById('UserName');
      // userNameInput.setAttribute('value', 'griffibr@gmail.com');
    }, 5000);
    // const formData = new FormData();
    // formData.set('UserName', 'griffibr@gmail.com');
    // formData.set('Password', 'ILike#23');
    // formData.set('RemeberMe', 'false');
    // formData.set('timeOffset', '480');

    // this.http.post(
    //   'https://www.mytotalconnectcomfort.com/portal?UserName=griffibr@gmail.com&Password=ILike#23&RememberMe=false&timeOffset=480',
    //   formData)
    //   .subscribe((result) => {
    //     console.log(result);
    //   });
  }

  onBarLightDimmer(event) {
    // this.getTrigger('bar_light_dim_' + event.value.toString());
    this.updateLight(this.barLightId, 'ON', event.value);
  }

  onMainLightToggle(event) {
    let action: string;
    if (event.checked) {
      action = 'ON';
    } else {
      action = 'OFF';
    }

    // this.getTrigger(action);
    this.updateLight(this.mainLightId, action);
  }

  onBarLightsToggle(event) {
    let action: string;
    if (event.checked) {
      action = 'ON';
    } else {
      action = 'OFF';
    }

    // this.getTrigger(action);
    this.updateLight(this.barLightId, action, this.barLightValue);
  }

  getTrigger(action: string) {
    this.http.get('https://maker.ifttt.com/trigger/' + action + '/with/key/bQuhnHoJv3Da4sTxK3F81R').subscribe(
      (data) => {
        console.log('Data: ' + data);
      },
      (error) => {
        console.error(error);
      }
    );
  }

  updateLight(id: number, action: string, dimmer = 50) {
    this.http.get('http://192.168.1.19:3000/light_update/' + id + '/' + action + '/' + dimmer.toString()).subscribe((result) => {
      console.log(result);
    });
  }
}

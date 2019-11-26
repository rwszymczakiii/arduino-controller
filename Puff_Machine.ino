#include <elapsedMillis.h>
#include <stdio.h>
int pvalve1Pin = 4; // Relay Valve 1
int pvalve2Pin = 5; // Relay Valve 2
int pvalve3Pin = 6; // Relay Valve 3
int pvalve4Pin = 7; // Relay Valve 4
int pvalve5Pin = 8; 
int pvalve6Pin = 9; 
int pvalve7Pin = 10; 
int pvalve8Pin = 11; 
int pvalve9Pin = 12; 
int pvalve10Pin = 13; 
int CurrentPin;
int LastPin;
int CurrentPump;
int MaxTime;
int CurrentCycle = 0;
char rec;
String startCode;
int MaxCycle;
int PumpsUsed;
int PuffDuration;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Arduino is ready!");
  pinMode(pvalve1Pin, OUTPUT); 
  pinMode(pvalve2Pin, OUTPUT); 
  pinMode(pvalve3Pin, OUTPUT); 
  pinMode(pvalve4Pin, OUTPUT); 
  pinMode(pvalve5Pin, OUTPUT);
  pinMode(pvalve6Pin, OUTPUT);
  pinMode(pvalve7Pin, OUTPUT);
  pinMode(pvalve8Pin, OUTPUT);
  pinMode(pvalve9Pin, OUTPUT);
  pinMode(pvalve10Pin, OUTPUT);
}

void loop() {
  while(Serial.available() > 0){
    rec = Serial.read();
    startCode += rec;

    if (rec=='$'){
      startCode.remove(startCode.length()-1,1);
      MaxCycle = startCode.substring(0,3).toInt();
      PumpsUsed = startCode.substring(3,6).toInt();
      PuffDuration = startCode.substring(6,startCode.length()).toInt();
      MaxTime = PumpsUsed * PuffDuration;
      CurrentPump = 0;
      CurrentPin = 1;
      elapsedMillis timeElapsed;
      
      while (MaxCycle > CurrentCycle) {
        digitalWrite(LED_BUILTIN, HIGH);
        // ------ Pump 1 -------------
        if (timeElapsed < PuffDuration && CurrentPump < PumpsUsed) { 
          CurrentPump = 1;
          CurrentPin = pvalve1Pin;
          digitalWrite(CurrentPin, HIGH); 
          Serial.print('a');
        }
        // ------ Pump 2 -------------
        else if (timeElapsed > PuffDuration && timeElapsed < PuffDuration * 2 && CurrentPump < PumpsUsed) { 
          CurrentPump = 2;
          LastPin = pvalve1Pin;
          CurrentPin = pvalve2Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);    
          Serial.print('b');
        }
        // ------ Pump 3 -------------
        else if (timeElapsed > PuffDuration * 2 && timeElapsed < PuffDuration * 3 && CurrentPump < PumpsUsed) {
          CurrentPump = 3;
          LastPin = pvalve2Pin;
          CurrentPin = pvalve3Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);
          Serial.print('c');
        }
        // ------ Pump 4 -------------
        else if (timeElapsed > PuffDuration * 3 && timeElapsed < PuffDuration * 4 && CurrentPump < PumpsUsed) { 
          CurrentPump = 4;
          LastPin = pvalve3Pin;
          CurrentPin = pvalve4Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);
          Serial.print('d');
        }
        // ------ Pump 5 -------------
        else if (timeElapsed > PuffDuration * 4 && timeElapsed < PuffDuration * 5 && CurrentPump < PumpsUsed) { 
          CurrentPump = 5;
          LastPin = pvalve4Pin;
          CurrentPin = pvalve5Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);
          Serial.print('e');
        }
        // ------ Pump 6 -------------
        else if (timeElapsed > PuffDuration * 5 && timeElapsed < PuffDuration * 6 && CurrentPump < PumpsUsed) {
          CurrentPump = 6;
          LastPin = pvalve5Pin;
          CurrentPin = pvalve6Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);
          Serial.print('f');
        }
        // ------ Pump 7 -------------
        else if (timeElapsed > PuffDuration * 6 && timeElapsed < PuffDuration * 7 && CurrentPump < PumpsUsed) { 
          CurrentPump = 7;
          LastPin = pvalve6Pin;
          CurrentPin = pvalve7Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);
          Serial.print('g');
        }
        // ------ Pump 8 -------------
        else if (timeElapsed > PuffDuration * 7 && timeElapsed < PuffDuration * 8 && CurrentPump < PumpsUsed) { 
          CurrentPump = 8;
          LastPin = pvalve7Pin;
          CurrentPin = pvalve8Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);
          Serial.print('h');
        }
        // ------ Pump 9 -------------
        else if (timeElapsed > PuffDuration * 8 && timeElapsed < PuffDuration * 9 && CurrentPump < PumpsUsed) {
          CurrentPump = 9;
          LastPin = pvalve8Pin;
          CurrentPin = pvalve9Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);
          Serial.print('i');
        }
        // ------ Pump 10 -------------
        else if (timeElapsed > PuffDuration * 9 && timeElapsed < PuffDuration * 10 && CurrentPump < PumpsUsed) {
          CurrentPump = 10;
          LastPin = pvalve9Pin;
          CurrentPin = pvalve10Pin;
          digitalWrite(CurrentPin, HIGH);
          digitalWrite(LastPin, LOW);
          Serial.print('j');
        }
        // ------ End Cycle -------------
        else if (timeElapsed >= MaxTime) {
          digitalWrite(pvalve1Pin, LOW);
          digitalWrite(pvalve2Pin, LOW);
          digitalWrite(pvalve3Pin, LOW);
          digitalWrite(pvalve4Pin, LOW);
          digitalWrite(pvalve5Pin, LOW);
          digitalWrite(pvalve6Pin, LOW);
          digitalWrite(pvalve7Pin, LOW);
          digitalWrite(pvalve8Pin, LOW);
          digitalWrite(pvalve9Pin, LOW);
          digitalWrite(pvalve10Pin, LOW);
          Serial.print('k');
          CurrentCycle++;
          CurrentPump = 0;
          CurrentPin = 0;
          timeElapsed = 0;
        }
      }
      Serial.end();
    }
  }
}
  
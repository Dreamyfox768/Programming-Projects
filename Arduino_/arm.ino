
#include <Stepper.h>

int MotorRevolution=2048;
int MotorSpeed=15;

Stepper stepperl (MotorRevolution, 13, 11,12,10);
Stepper stepper2 (MotorRevolution, 5, 7,6,4) ;
int Xpin=A0;
int Ypin=A1;
int Xvalue;
int Yvalue;

void setup() {
  Serial.begin (9600) ; 
  pinMode (Xpin, INPUT) ;
  pinMode (Ypin, INPUT) ;
  stepperl.setSpeed(MotorSpeed) ;
  stepper2.setSpeed(MotorSpeed) ;

} 

void loop () {
  Xvalue=analogRead (Xpin) ;
  Yvalue=analogRead (Ypin) ;
  Serial.println ("Xvalue:"+(String)Xvalue+" Yvalue: "+(String) Yvalue) ;


if (Xvalue>800) {stepperl.step (MotorRevolution/10) ;}
if(Xvalue<100) {stepperl.step(-MotorRevolution/10) ; }
if (Yvalue>800) {stepper2.step (MotorRevolution/10) ;}
if (Yvalue<100) {stepper2.step (-MotorRevolution/10) ;}
}

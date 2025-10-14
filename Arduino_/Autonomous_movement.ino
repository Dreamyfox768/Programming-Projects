int motorA_direction = 2;
int motoA_speed = 5;
int motorB_direction = 4;
int motoB_speed = 6;
int servo_rotation = 10;
int intrared_reciever = 3;
int light_sensorleft = A0;   
int light_sensorright = A3; 
int Obstacle_avoidanceleft = 1;
int Obstacle_avoidanceright = 2;
int Line_trackingleft = 7;
int Line_trackingright = 9;
int ultrasonic_trigger = 12;
int ultrasonic_echi = 13;



void setup(){
  pinMode(motorA_direction, OUTPUT);
  pinMode(motoA_speed, OUTPUT);
  pinMode(motorB_direction, OUTPUT);
  pinMode(motoB_speed, OUTPUT);
  pinMode(servo_rotation, OUTPUT);
  pinMode(intrared_reciever, INPUT);
  pinMode(A2, INPUT);
  pinMode(Line_trackingleft, INPUT);
  pinMode(Line_trackingright, INPUT);
  pinMode(ultrasonic_trigger, OUTPUT);
  pinMode(ultrasonic_echi, INPUT);
  pinMode(A0, INPUT);
  pinMode(A3, INPUT);
}

void loop() {
  moveBack(100);    // Move backward at speed 30
  delay(1000);      // Keep moving back for 700ms
  stopMotor();     // Stop motors
  delay(700);     // Wait for 1 second to verify the motors are stopped
  moveFoward(100);  // Move forward at speed 30 to check forward movement
  delay(1000);      // Keep moving forward for 700ms
  stopMotor();     // Stop motors again
  delay(700);     // Wait to verify stop

}



void moveBack(int speed) {
  digitalWrite(motorA_direction, HIGH);  // motorA is moving foward
  analogWrite(motoA_speed, speed);
  digitalWrite(motorB_direction, LOW);  // motorB  is moving foward, it is going same direction as
  analogWrite(motoB_speed, speed);
}

void moveFoward(int speed) {
  digitalWrite(motorA_direction, LOW);  // motorA is moving foward
  analogWrite(motoA_speed, speed);
  digitalWrite(motorB_direction, HIGH);  // motorB  is moving foward, it is going same direction as
  analogWrite(motoB_speed, speed);
}
void moveRight(int speed) {
  digitalWrite(motorA_direction, HIGH);  // motorA is moving foward
  analogWrite(motoA_speed, speed);
  digitalWrite(motorB_direction, HIGH);  // motorB  is moving foward, it is going same direction as
  analogWrite(motoB_speed, speed);
}
void moveLeft(int speed) {
  digitalWrite(motorA_direction, LOW);  // motorA is moving foward
  analogWrite(motoA_speed, speed);
  digitalWrite(motorB_direction, LOW);  // motorB  is moving foward, it is going same direction as
  analogWrite(motoB_speed, speed);
}
void stopMotor() {
  analogWrite(motoA_speed, 0);
  analogWrite(motoB_speed, 0);
}

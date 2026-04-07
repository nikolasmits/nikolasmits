//BUTTONS
const int leftButton = 2;
const int rightButton = 4;
leftButtonState = digitalRead(leftButton);
rightButtonState = digitalRead(rightButton);
int leftButtonState = 0;
int rightButtonState = 0;

//MOTORS
const int forwardmotorPin = 5;
const int leftMotor_direction = 12;
const int rightMotor_direction = 13;
const int leftMotor_speed = 3;
const int rightMotor_speed = 11;

//PHOTODIODE
const int photodiode = A3;
int V_threshold = 4;
int photodiodeVal = analogRead(photodiode);
int count = 0;

void setup() {

Serial.begin(9600);
//float V_current = photodiodeVal * (5 / 1023.0);
float Voltage = string(photodiodeVal,3);
pinMode(leftButton, INPUT);
pinMode(rightButton, INPUT);
pinMode(leftMotor_direction, OUTPUT);
pinMode(rightMotor, OUTPUT);
pinMode(motorPin, OUTPUT);
pinMode(leftMotor_speed, OUTPUT);
pinMode(rightMotor_speed, OUTPUT);
pinMode(photodiode, INPUT);
Serial.print("Photodiode Voltage= ");
Serial.print(photodiodeVal);
  
void movement(){

if(photodiodeVal >= V_threshold){
  Serial.println("Obstacle detected infront of robot");
   analogWrite(leftMotor_speed, 0);
   analogWrite(rightMotor_speed, 0);
   if(leftButtonState == 0 && rightButtonState == 1){
    Serial.println("Obstacle on the right of robot");
    leftButtonstate=0;
    rightButtonState=0;
    digitalWrite(leftMotor_direction, HIGH);
    digitalWrite(rightMotor_direction, LOW);
    analogWrite(leftMotor_speed, );
    analogWrite(rightMotor_speed, );
    if(photodiodeVal < V_threshold){
    Serial.println("No obstacle infront of robot");
    delay(2000);      
    digitalWrite(motortPin, HIGH);
    analogWrite(leftMotor_speed, 0);
    analogWrite(rightMotor_speed, 0);
    count = count + 1;
    if(count == 7){
      exit(0);
    }    
    }
    delay(1000);
    } 
    } else if(leftButtonState == 1 && rightButtonState == 0){
    Serial.println("Obstacle on the left of the robot");
    leftButtonstate=0;
    rightButtonState=0;
    digitalWrite(leftMotor_direction, LOW);
    digitalWrite(rightMotor_direction, HIGH);
    analogWrite(leftMotor_speed, );
    analogWrite(rightMotor_speed, );
    if(photodiodeVal < V_threshold){
    Serial.println("No obstacle infront of the robot");
    delay(2000);
    digitalWrite(motortPin, HIGH);
    analogWrite(leftMotor_speed, 0);
    analogWrite(rightMotor_speed, 0);
    delay(1000);
    count = count + 1;
    if(count == 7){
      exit(0);
    }
    }
    }

else if(photodiodeVal < V_threshold){
  Serial.println("No obstacle infront of robot");
  digitalWrite(motortPin, HIGH);
  analogWrite(leftMotor_speed, 0);
  analogWrite(rightMotor_speed, 0);
  delay(1000);

count = count + 1;  
if(count == 7){
  exit(0);
  }
}

//else if(photodiode >= Vth_upper){


//}

}

}

void loop() {

movement();

}

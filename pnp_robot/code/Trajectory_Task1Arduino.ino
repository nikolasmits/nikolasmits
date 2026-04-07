
#include <Servo.h>
#include <math.h>
#include <stdio.h>
 
// Arm Servo pins
#define Joint1Pin 2
#define Joint2Pin 3
#define Joint3Pin 4
#define GripperPin 11
 
// Servo Objects
Servo Joint1;
Servo Joint2;
Servo Joint3;
Servo Gripper;
 
// Global variables for trajectory and arm dimensions
double tf = 5.0; // Total time for one-way trip
double x0 = 0, xf = 9.58; // X start and end
double y0 = 17.7, yf = 9.58; // Y start and end
double z0 = -9.4, zf = -23.47; // Z start and end
 
double GripperOpen = 40; // Open gripper; Need to tune value
double GripperClose = 140; // Close gripper; Need to tune value
 
// Arm dimensions
const double L1 = 9.4; // Example values
const double L2 = 17.7; 
 
// Offsets in degrees
double theta1Offset = 3; // Degrees
double theta2Offset = 3; // Degrees
double theta3Offset = 35; // Degrees
 
// Function prototypes
void trajectoryPlanning(double t, double &x, double &y, double &z);
void inverseKinematics(double x, double y, double z, double &theta1_deg, double &theta2_deg, double &theta3_deg);
 
void setup() {
  Serial.begin(9600);
  Joint1.attach(Joint1Pin);
  Joint2.attach(Joint2Pin);
  Joint3.attach(Joint3Pin);
  Gripper.attach(GripperPin); 
 
  // Move to start position
  double startTheta1, startTheta2, startTheta3;
  inverseKinematics(x0, y0, z0, startTheta1, startTheta2, startTheta3);
  Joint1.write(int(startTheta1 + theta1Offset));
  Joint2.write(int(startTheta2 + theta2Offset));
  Joint3.write(int(startTheta3 + theta3Offset));
  Gripper.write(int(GripperOpen));
  
  delay(5000); // Delay to ensure arm reaches start position
 
  Gripper.write(int(GripperClose)); // Close gripper to grabbing the object
 
  delay(5000);
}
 
void loop() {
  // Move from start to end and back to start
  for(int direction = 0; direction < 2; direction++) {
    for (int i = 0; i <= 10 * tf; i++) {
      double t = (direction == 0) ? i * 0.1 : tf - i * 0.1; // Adjust time for direction
      double x, y, z;
      trajectoryPlanning(t, x, y, z);
 
      double theta1_deg, theta2_deg, theta3_deg;
      inverseKinematics(x, y, z, theta1_deg, theta2_deg, theta3_deg);
 
      // Apply offset and control the servos
      Joint1.write(int(theta1_deg + theta1Offset));
      Joint2.write(int(theta2_deg + theta2Offset));
      Joint3.write(int(theta3_deg + theta3Offset));
 
      delay(100);
    }
 
    if (direction == 0) {
      Gripper.write(int(GripperOpen)); // Open gripper to release the object at the end position
      delay(5000); 
    } else {
      delay(5000); 
    }
  }
  // After returning to the start position, prepare to grab the object again
  Gripper.write(int(GripperClose));
  delay(5000); // Wait for the gripper to close before starting the next cycle
}
 
 
void trajectoryPlanning(double t, double &x, double &y, double &z) {
  // Calculating the position for each axis
  double a2 = 3 * (xf - x0) / pow(tf, 2);
  double a3 = -2 * (xf - x0) / pow(tf, 3);
  x = x0 + a2 * pow(t, 2) + a3 * pow(t, 3);
 
  double b2 = 3 * (yf - y0) / pow(tf, 2);
  double b3 = -2 * (yf - y0) / pow(tf, 3);
  y = y0 + b2 * pow(t, 2) + b3 * pow(t, 3);
 
  double c2 = 3 * (zf - z0) / pow(tf, 2);
  double c3 = -2 * (zf - z0) / pow(tf, 3);
  z = z0 + c2 * pow(t, 2) + c3 * pow(t, 3);
}
 
void inverseKinematics(double x, double y, double z, double &theta1_deg, double &theta2_deg, double &theta3_deg) {
  double X = sqrt(x*x + y*y);
 
  double theta1 = atan2(y, x);
  theta1_deg = theta1 * (180 / PI);
 
  double beta = atan2(z, X);
  double cos_psi = (L1*L1 + X*X + z*z - L2*L2) / (2 * L1 * sqrt(X*X + z*z));
  double psi = acos(cos_psi);
  double theta2 = -(beta - psi);
  theta2_deg = theta2 * (180 / PI);
 
  double theta3 = acos((X*X + z*z - L1*L1 - L2*L2) / (2 * L1 * L2));
  theta3_deg = theta3 * (180 / PI);
}


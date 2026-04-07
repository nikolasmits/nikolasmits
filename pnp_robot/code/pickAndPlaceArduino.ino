#include <Servo.h>
#include <math.h>

// Arm Servo pins
#define Joint1Pin 2
#define Joint2Pin 3
#define Joint3Pin 4
#define GripperPin 11

//24 y, 7 x, 9 z
// Servo Objects
Servo Joint1;
Servo Joint2;
Servo Joint3;
Servo Gripper;

// Global variables for trajectory and arm dimensions
// MODIFY x0,y0 FOR START POSITION
// MODIFY xf,yf FOR END POSITION
// MODIFY z0 for HEIGHT PLACED DOWN
// MODIFY object_height
// MODIFY n

double object_height = 1.5;
double n = 3.0;
double ta = 5.0, ts = 10.0, tm = 15.0, tf = 20.0; // Total time for one-way trip
double x0 = 1.6, xa = x0, xh = 0, xf = -20; // X start, middle and end
double y0 = 15.7, ya = y0, yh = 17.7, yf = 7; // Y start, middle and end
double z0 = 8, za = z0 - n*object_height, zh = -9.4, zf = z0; // Z start, middle and end

double GripperOpen = 40; // Open gripper; Need to tune value
double GripperClose = 140; // Close gripper; Need to tune value

// Arm dimensions
const double L1 = 9.4; 
const double L2 = 17.7; 

// Offsets in degrees
double theta1Offset = 3; // Degrees
double theta2Offset = 3; // Degrees
double theta3Offset = 35; // Degrees

void trajectoryPlanning(double t, double &x, double &y, double &z, double tStart, double tEnd, double xs, double ys, double zs, double xt, double yt, double zt);
void inverseKinematics(double x, double y, double z, double &theta1_deg, double &theta2_deg, double &theta3_deg);

void setup() {
  Serial.begin(9600);
  Joint1.attach(Joint1Pin);
  Joint2.attach(Joint2Pin);
  Joint3.attach(Joint3Pin);
  Gripper.attach(GripperPin); 

  // Move to middle position
  double middleTheta1, middleTheta2, middleTheta3;
  inverseKinematics(xh, yh, zh, middleTheta1, middleTheta2, middleTheta3);
  Joint1.write(int(middleTheta1 + theta1Offset));
  Joint2.write(int(middleTheta2 + theta2Offset));
  Joint3.write(int(middleTheta3 + theta3Offset));
  Gripper.write(int(GripperOpen));
  
  delay(3000); // Delay to ensure arm reaches middle position
}

void loop() {
    static bool taskCompleted = false;
    if (taskCompleted) return;

    // From home to point above start position
    for (int i = 0; i <= 10 * ts; i++) {
        double t = i * 0.1; // Simulate time progression
        double x, y, z;
        trajectoryPlanning(t, x, y, z, 0, ts, xh, yh, zh, xa, ya, za);

        double theta1_deg, theta2_deg, theta3_deg;
        inverseKinematics(x, y, z, theta1_deg, theta2_deg, theta3_deg);

        Joint1.write(int(theta1_deg + theta1Offset));
        Joint2.write(int(theta2_deg + theta2Offset));
        Joint3.write(int(theta3_deg + theta3Offset));

        delay(100);
    }

    // From point above start position to start position
    for (int i = 0; i <= 10 * tm; i++) {
        double t = i * 0.1;
        double x, y, z;
        trajectoryPlanning(t, x, y, z, 0, tm, xa, ya, za, x0, y0, z0);

        double theta1_deg, theta2_deg, theta3_deg;
        inverseKinematics(x, y, z, theta1_deg, theta2_deg, theta3_deg);

        Joint1.write(int(theta1_deg + theta1Offset));
        Joint2.write(int(theta2_deg + theta2Offset));
        Joint3.write(int(theta3_deg + theta3Offset));

        delay(100);
    }

      delay(3000); // Delay to ensure arm reaches start position

      Gripper.write(int(GripperClose)); // Close gripper to grabbing the object
    
      delay(3000);

    // From t0 to tm
    for (int i = 0; i <= 10 * tm; i++) {
        double t = i * 0.1;
        double x, y, z;
        trajectoryPlanning(t, x, y, z, 0, tm, x0, y0, z0, xh, yh, zh);

        double theta1_deg, theta2_deg, theta3_deg;
        inverseKinematics(x, y, z, theta1_deg, theta2_deg, theta3_deg);

        Joint1.write(int(theta1_deg + theta1Offset));
        Joint2.write(int(theta2_deg + theta2Offset));
        Joint3.write(int(theta3_deg + theta3Offset));

        delay(100);
    }

    // From tm to tf
    for (int i = 0; i <= 10 * (tf - tm); i++) {
        double t = tm + i * 0.1;
        double x, y, z;
        trajectoryPlanning(t, x, y, z, tm, tf, xh, yh, zh, xf, yf, zf);

        double theta1_deg, theta2_deg, theta3_deg;
        inverseKinematics(x, y, z, theta1_deg, theta2_deg, theta3_deg);

        Joint1.write(int(theta1_deg + theta1Offset));
        Joint2.write(int(theta2_deg + theta2Offset));
        Joint3.write(int(theta3_deg + theta3Offset));

        delay(100);
    }

    Gripper.write(int(GripperOpen)); // Open gripper to release the object

    taskCompleted = true;
}

void trajectoryPlanning(double t, double &x, double &y, double &z, double tStart, double tEnd, double xs, double ys, double zs, double xt, double yt, double zt) {
    // Calculate trajectory based on current segment
    double dt = t - tStart; // Time since start of this segment
    double totalTime = tEnd - tStart; // Total time for this segment

    double a2 = 3 * (xt - xs) / pow(totalTime, 2);
    double a3 = -2 * (xt - xs) / pow(totalTime, 3);
    x = xs + a2 * pow(dt, 2) + a3 * pow(dt, 3);

    double b2 = 3 * (yt - ys) / pow(totalTime, 2);
    double b3 = -2 * (yt - ys) / pow(totalTime, 3);
    y = ys + b2 * pow(dt, 2) + b3 * pow(dt, 3);

    double c2 = 3 * (zt - zs) / pow(totalTime, 2);
    double c3 = -2 * (zt - zs) / pow(totalTime, 3);
    z = zs + c2 * pow(dt, 2) + c3 * pow(dt, 3);
}


void inverseKinematics(double x, double y, double z, double &theta1_deg, double &theta2_deg, double &theta3_deg) {
  double X = sqrt(x*x + y*y);

  double theta1 = atan2(y, x);
  theta1_deg = theta1 * (180 / M_PI);

  double beta = atan2(z, X);
  double cos_psi = (L1*L1 + X*X + z*z - L2*L2) / (2 * L1 * sqrt(X*X + z*z));
  double psi = acos(cos_psi);
  double theta2 = -(beta - psi);
  theta2_deg = theta2 * (180 / M_PI);

  double theta3 = acos((X*X + z*z - L1*L1 - L2*L2) / (2 * L1 * L2));
  theta3_deg = theta3 * (180 / M_PI);
}

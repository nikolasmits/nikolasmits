void setup() {
PBL = Pushbutton Left-hand side of robot
PBR = Pushbutton Right-hand side of robot
PVF = Photovoltage Front of robot
M1 = Left motor
M2 = Right motor
M3 = Front motor
M4 = Back motor
// Voltage across the photodiode which suggests the motor is close to the wall, when the voltage is above this minimum voltage there is a solid wall or the "comb-shaped irregular" wall in front of the robot.
Below threshold of photovoltage = Vmin

int i = 1;


}

void loop() {

While (i != 0) {
//There is a wall only infront of the robot
While (PBL and PBR are OFF && PVF < Vmin) {
        M3 and M4 are turned on to move left && M1 and M2 are turned off};
//There is a wall infront of the robot and on its right, thus it must move left
While((PBR is ON && PVF < Vmin && PBL OFF) {
        M3 and M4 are turned on to move the robot to the left && M1 and M2 are turned off}
//There is a wall infront of the robot and on its left, thus it must move to the right
While (PBL is ON && PVF < Vmin && PBR OFF) {
        M3 and M4 are turned on to move the robot to the right && M1 and M2 are turned off}
//There is no wall infront of the robot, thus it must move forwards
While (PVF < Vmin) {
        M1 and M2 are turned on && M3 and M4 are turned off;
//When Count == 7 the robot has passed 7 front walls, therefore, it has successfully exited the maze
        Count = Count + 1;
        If (count == 7) {
              exit(0);}
                  }
                    }
}

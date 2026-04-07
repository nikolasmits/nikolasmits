# Pick-and-Place Robot

## Overview
This project involved the design, assembly, modelling, and control of a robotic arm capable of completing a pick-and-place task. The robot was required to move from a home position to an object location, grasp the object, return through a controlled path, and release it at a new target position.

My primary contribution focused on the robot’s **kinematic modelling**, specifically the derivation and implementation of the **forward kinematics** and **inverse kinematics**, as well as contribution to the **trajectory planning** used to achieve smoother motion.

## Project Context
This was a university group project completed for the **ELEC0129 Introduction to Robotics** module. The assignment required students to build the robot, derive and verify forward kinematics, derive and verify inverse kinematics, implement trajectory planning, and demonstrate a full pick-and-place experiment. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## My Contribution
My main contribution to this project was the analytical modelling of the robot. I derived and implemented the **forward kinematics** and **inverse kinematics** required to describe and control the manipulator’s motion. This involved defining the robot geometry, working with transformation matrices, and developing the mathematical relationships between joint angles and end-effector position.

I also contributed to the **trajectory planning** stage, supporting the development of smooth motion between target positions using cubic polynomial profiles. Through this work, I helped connect the theoretical modelling of the robot with its practical motion during the pick-and-place task.

## System Description
The robotic manipulator consisted of a base rotation joint, two arm links, and an end-effector gripper, controlled using servo motors connected to a BotBoarduino/Arduino platform. The report defined the main arm lengths as **L1 = 9.4 cm** and **L2 = 17.7 cm**, which were then used in the kinematic derivations. :contentReference[oaicite:2]{index=2}

## Technical Work

### Forward Kinematics
I derived the forward kinematic model of the robot to determine the end-effector position from known joint angles. This was carried out using homogeneous transformation matrices and frame transformations. The resulting model provided the Cartesian position of the end effector as a function of joint variables and link lengths, and was experimentally checked against the physical robot. :contentReference[oaicite:3]{index=3}

### Inverse Kinematics
I also completed the inverse kinematics, deriving the joint angles required for a desired target position \((x, y, z)\). A geometric method was used, including trigonometric reasoning and the cosine rule, to obtain expressions for \(\theta_1\), \(\theta_2\), and \(\theta_3\), while accounting for multiple valid solutions such as elbow-up and elbow-down configurations. The derived equations were then validated experimentally using measured end-effector positions. :contentReference[oaicite:4]{index=4}

### Trajectory Planning
I contributed to the trajectory planning stage, where cubic polynomial profiles were used to generate smoother motion between points. This ensured zero velocity at the start and end of the movement and produced continuous position and velocity profiles for the robot’s motion. The report used this method to model position, velocity, and acceleration over time for the chosen movement path. :contentReference[oaicite:5]{index=5}

### Embedded Robotic Control
The final project integrated the kinematic modelling with Arduino/BotBoarduino-based servo control so the robot could execute a complete pick-and-place routine. The assignment brief also required correct servo setup, safe power configuration, and gripper operation as part of the full system implementation. :contentReference[oaicite:6]{index=6}

## Key Results
The project successfully demonstrated that the robot could move within its workspace, reach desired points, and perform a full pick-and-place task. The report records a **minimum positional error of 0 cm**, a **maximum positional error of 0.75 cm**, and a **typical error of 0.5 cm**, with error sources mainly linked to measurement uncertainty and the accumulation of kinematic approximation error through repeated motion. :contentReference[oaicite:7]{index=7}

## Engineering Skills Demonstrated
This project helped me develop and demonstrate skills in:
- **robot kinematics**: forward kinematics, inverse kinematics, workspace reasoning
- **mathematical modelling**: homogeneous transformation matrices and geometric derivation
- **trajectory planning**: cubic polynomial motion generation
- **robotics analysis**: linking joint-space motion to Cartesian end-effector behaviour
- **experimental validation**: verifying theoretical predictions against physical robot movement
- **problem solving in real systems**: understanding how modelling assumptions, calibration, and measurement tolerances affect practical performance
- **technical communication**: presenting derivations, results, and engineering reasoning in a formal report

## Tools and Technologies
- Arduino / BotBoarduino
- Servo motors
- MATLAB
- Homogeneous transformation matrices
- Geometric inverse kinematics
- Cubic polynomial trajectory planning
- Robotics experimentation and validation

## What I Learned
This project strengthened my understanding of how robotic theory translates into real hardware behaviour. In particular, it showed the importance of accurate kinematic modelling for controlling manipulator motion, while also highlighting how calibration, measurement tolerances, and physical implementation affect practical performance.

## Repository Contents
- `README.md` – project summary
- `report/` – final report
- `code/` – MATLAB / Arduino files
- `images/` – robot photographs and validation images

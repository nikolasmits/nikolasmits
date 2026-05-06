# Automated Component Embedding Integration for an FDM 3D Printer

## Overview
This project involved the development of a fully automated **pick-and-place component embedding system** for a modified **LulzBot TAZ 5 FDM 3D printer**. The aim was to remove the manual intervention normally required when embedding foreign components such as threaded fasteners or magnets into 3D printed parts during fabrication.

The final system combined four tightly integrated subsystems:

- an **active tool-changing mechanism**
- a **precision end-effector and wrist assembly**
- a **machine-vision verification system**
- and a **custom software pipeline** for pose extraction and G-code streaming

to enable automated mid-print retrieval, placement, and verification of embedded components.

## Project Context
This was completed as a **4th Year Project** in the UCL Department of Electronic and Electrical Engineering under the supervision of **Prof. Thomas Gilbert**. The project addressed a real bottleneck in hybrid additive manufacturing: while FDM printing is widely used for producing functional parts, embedding non-printed components still usually requires pausing the print, inserting the part manually, and then resuming the build.

The project therefore set out to automate the full embedding workflow on a low-cost, open-source printer platform. The report defined four main objectives:

- development of an **active tool-changing system**
- high-precision **end-effector control**
- **machine-vision-based process verification**
- and an efficient **digital extraction and G-code pipeline**

## My Contribution
This was a team 4th-year project, and my primary contribution focused on the **end-effector and wrist subsystem**.

I led the full development of:
- the **end-effector type selection**
- the **iterative FDM design of the gripper fingers**
- the **bevel-gear wrist assembly**
- **AS5600 magnetic encoder integration**
- and the complete **Arduino PID firmware** for motor calibration, closed-loop wrist positioning, and gripper actuation.

This part of the project demonstrates my ability to combine mechanical design, embedded sensing, control implementation, and experimental validation into a functional robotic subsystem.

## System Architecture
The final system was delivered through four integrated work streams:

1. **Tool-Changer**  
   An active docking gantry was developed to allow reliable swapping between the print head and pick-and-place end-effector on the Cartesian “bed-slinger” architecture of the TAZ 5.

2. **End-effector**  
   A lightweight servo-driven two-finger parallel gripper with a yaw-adjustable wrist was developed to pick, orient, and place small hardware components.

3. **Machine Vision**  
   A Raspberry Pi-based global shutter vision system was implemented to verify whether nut placement had succeeded.

4. **Software Pipeline**  
   A custom Python-based digital workflow was built to extract embedded component pose information from 3MF files and inject the required placement logic into the printing sequence.

## Engineering Problem
FDM printing is excellent for thermoplastic geometry, but functional assemblies often require non-printed hardware such as:
- magnets
- threaded fasteners
- or sensors

to be placed inside the printed structure. In most hobbyist and research workflows, this still depends on manually pausing the print, inserting the component by hand, and then restarting the machine.

That manual step introduces:
- a production bottleneck
- placement inconsistency
- and reduced scalability for hybrid manufacturing.

The project therefore addressed the broader challenge of making **embedded component fabrication autonomous** on a low-cost, open-source printer.

## Tool-Changer System
The tool-changing system was designed specifically for the constraints of a **Cartesian bed-slinger printer**, where mass and vibration management are more difficult than in architectures such as CoreXY.

### Mechanical approach
The report explains that passive magnetic couplings were rejected after force analysis showed that the undocking force would exceed the available dynamic linear force from the X-axis drive. This led to the adoption of an **active, gravity-held, pin-and-bushing exact-constraint design**.

The final toolchanger used:
- a modified X-carriage
- a toolhead backplate
- and an independent active gantry

to transfer the load vertically and avoid the high breakaway forces associated with lateral disengagement.

### Performance
The tool-changing system achieved:
- **100% success over a continuous 50-cycle stress test**
- positional repeatability of **±0.05 mm**
- and seamless layer continuity without visible shifting in printed parts.

This is a particularly strong result because it shows that the active docking architecture was not just designed conceptually, but validated experimentally under repeated operation.

## End-Effector and Wrist Subsystem
This was my main contribution and one of the strongest technical parts of the project.

### End-effector selection
Several end-effector strategies were compared, including:
- **electromagnetic grippers**
- **vacuum / suction systems**
- and **electromechanical finger grippers**

The two-finger parallel gripper was selected because it offered:
- material independence
- deterministic release
- self-centring geometry
- and compatibility with both steel nuts and non-ferromagnetic permanent magnets.

### Gripper design
The gripper was designed in Fusion 360 and FDM-printed in PLA. It used a **rack-and-pinion mechanism** driven by an SG90 micro-servo. The first iteration used **1 mm fingertips**, but these were too wide to enter nut cavities and introduced centreline misalignment. The final design reduced the fingertip thickness to **0.7 mm**, which enabled accurate insertion into small hexagonal cavities while preserving symmetric closure.

### Wrist design
The wrist provided **yaw rotation** of the gripper to orient hexagonal nuts correctly before insertion. It used a **compound bevel-gear assembly** driven by two SG90 servos, with the gear ratio chosen to balance output torque and angular range.

A particularly important design step was correcting the original gear ratio: the initial design only produced **54°** of wrist output rotation, which was insufficient for full unique orientation coverage of a hexagonal nut. By reducing the inner bevel gear tooth count, the design achieved **60.8°**, exceeding the required 60° minimum.

### Encoder integration
An **AS5600 magnetic rotary encoder** was integrated to measure wrist angle with absolute 12-bit resolution over I2C. This eliminated the need for a homing step and enabled real-time feedback for closed-loop control.

The encoder mounting was designed to maintain the required sensor-to-magnet air gap and alignment constraints, and each motor was swept across its PWM range to obtain calibration data for angle mapping.

### PID control
The wrist was controlled using a **closed-loop PID controller** implemented on an Arduino. This was necessary because:
- the servos’ internal potentiometer loops only regulated shaft position
- FDM-printed gears introduced backlash and non-linear dead zones
- and unit-to-unit servo variation made a shared open-loop mapping unreliable.

The controller used real-time angle feedback from the AS5600 to correct wrist yaw, with the control output mapped through motor-specific calibration functions to PWM commands.

### Results
The end-effector subsystem achieved:
- a **steady-state wrist error of 0.5°**
- and cavity insertion tolerance was met in **12 of 14 tested angle transitions**.

That is a strong engineering result because it shows the subsystem was not only mechanically functional, but quantified and validated under repeatable positioning tests.

## Machine Vision System
The machine-vision subsystem provided automated verification of whether nut placement had succeeded.

### Hardware choice
A **Raspberry Pi Global Shutter Camera** was selected over more expensive industrial cameras and rolling-shutter alternatives. The report justifies this on the basis of:
- lower cost
- direct embedded compatibility
- and the need to avoid motion-related distortion during image capture.

### Model choice
Because the available dataset was relatively small, the vision system used **transfer learning** with a **MobileNetV2** architecture rather than training a CNN from scratch. This reduced data and training requirements while still allowing effective classification of nut-placement success.

### Results
The machine-vision subsystem achieved:
- **80.43% validation accuracy**

and was able to identify misaligned or partially inserted components with sufficiently high reliability to act as a real-time verification stage.

## Software and Firmware Pipeline
A major strength of the project is that it did not stop at mechanical hardware. It also included a full digital workflow for integrating component placement into the print process.

### Geometry extraction
The software pipeline extracted embedded component geometry directly from **3MF files** exported from Fusion. This was important because 3MF retains more useful object and metadata structure than STL files, allowing embedded objects to be identified through naming conventions and separated from the main print geometry.

### Orientation estimation
The report explains that component orientation was derived by comparing a nominal reference mesh with the extracted embedded mesh. After removing translation via centroid alignment, the **Kabsch algorithm** was used to compute the rotation matrix that minimised least-squares alignment error. The resulting rotation was then converted into yaw, pitch, and roll for downstream control.

### G-code streaming
Because Marlin has limited support for conditional or event-driven behaviour, the project used **external coordination of the instruction stream** to manage pauses, tool changes, embedding actions, and resumption of printing.

### Computational efficiency
The extraction script processed embedded components in an average of **10 ms per object**, comfortably meeting the responsiveness target for the automated workflow.

## Validation Results
The report summarises the system-level performance across the integrated workflow:

- **Tool-changing reliability:** 100% success over 50-cycle stress test
- **Toolchanger positional repeatability:** ±0.05 mm
- **Wrist control accuracy:** 0.5° steady-state error
- **Machine-vision validation accuracy:** 80.43%
- **Pose extraction overhead:** 10 ms per object

Together, these results show that the project moved beyond separate prototype subsystems and achieved a credible integrated hybrid-manufacturing demonstrator.

## Why This Project Matters
What makes this project especially strong is its systems integration. It combines:
- additive manufacturing
- robotic manipulation
- embedded control
- machine vision
- and digital manufacturing software

into one complete workflow.

Rather than treating 3D printing, pick-and-place, and verification as separate research problems, the project demonstrates how they can be synchronised to automate **mid-print component embedding** on an affordable open-source platform. That makes it highly relevant to hybrid manufacturing, manufacturing automation, robotics, and embedded mechatronic systems.

## Engineering and Technical Skills Demonstrated
This project demonstrates skills in:
- **robotic end-effector design**
- **rack-and-pinion and bevel-gear mechanism design**
- **embedded sensing with magnetic encoders**
- **PID control implementation**
- **servo calibration and closed-loop actuation**
- **machine-vision system design**
- **transfer learning for embedded classification**
- **3MF geometry extraction**
- **rigid transformation and pose estimation**
- **G-code pipeline development**
- **firmware modification and printer integration**
- **system-level validation of multi-subsystem mechatronic platforms**

## Repository Contents
- `README.md` – project summary
- `report/` – final report
- `cad/` – end-effector, toolchanger, and tray CAD files
- `code/` – Python, Arduino, and firmware-related implementation
- `vision/` – machine vision scripts and model assets
- `images/` – subsystem photos, CAD renders, and validation figures

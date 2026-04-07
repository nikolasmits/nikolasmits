# Maze Solving Robot

## Overview
This project involved the design and implementation of a sensor-driven robot capable of navigating an unknown maze-like tunnel environment. The challenge was not simply to move a robot along a known route, but to create a system that could **sense walls, avoid unstable front obstacles, make navigation decisions, and progress through an unseen maze without hard-coding the path**.

The project combined:
- **sensor circuit design**
- **motor actuation design**
- **navigation pseudocode**
- **Arduino programming**
- and **physical robot implementation**

to develop a robot capable of solving a maze under uncertain conditions. :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}

## Project Context
This was a university robotics and electronics project completed as part of **Scenario B – Maze Solving Robot**. The project was structured in two stages:

- **Part 1 (12%)** focused on designing the sensing circuits, actuation circuits, and navigation pseudocode for the robot.
- **Part 2 (8%)** focused on **building the circuits and programming the actual robot** to solve the maze.

This means the project was not only a conceptual design exercise, but also an implementation-based robotics task involving physical circuit construction, Arduino programming, and robot demonstration. The preparation brief also required students to familiarise themselves with Arduino and optional TinkerCAD-based circuit simulation before implementation. :contentReference[oaicite:14]{index=14} :contentReference[oaicite:15]{index=15}

## My Contribution
My contribution focused on the robot’s **control logic, actuation design, and Arduino implementation**. I worked on the maze navigation pseudocode, contributed to the motor actuation design, and helped develop the control strategy that linked sensor inputs to forward and lateral robot movement.

This included designing how the robot should respond to:
- side-wall contact sensing,
- front obstacle detection,
- and unknown maze geometry requiring reactive decision-making rather than a pre-programmed path.

I also contributed to the Arduino implementation stage, where the sensing and actuation concepts were translated into embedded robot behaviour for the physical maze-solving task. :contentReference[oaicite:16]{index=16} :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18}

## Problem Definition
The robot had dimensions of approximately **20 cm × 20 cm** and used **four omni-directional wheels**. According to the brief, it needed only three motion types to solve the maze:
- **forward**
- **left**
- **right**

No rotation was required, and no diagonal motion was needed. The brief also notes that backward motion was not necessary, although it could be useful if the robot needed to recover distance from a front wall because of mechanical inaccuracies. :contentReference[oaicite:19]{index=19}

The challenge was therefore not full mapping, but a constrained navigation problem in which the robot had to:
1. detect side contact,
2. detect dangerous front obstacles,
3. decide when to shift left or right,
4. move forward safely when a clear path existed,
5. and continue this process until exiting the maze. :contentReference[oaicite:20]{index=20}

## Sensing Strategy

### Side-wall sensing
The brief required the design of circuits using **normally open pushbuttons** mounted on either side of the robot to detect rigid side walls, producing:
- **LOW** if not touched
- **HIGH** if touched

and making the result readable by the Arduino as a digital input. :contentReference[oaicite:21]{index=21}

This is a simple but robust engineering choice because the side walls were explicitly described as rigid and safe to touch.

### Front-wall sensing
For the front wall, the brief required a **non-contact proximity sensor** based on an **infrared LED and photodiode**. The photodiode had to be reverse-biased correctly and conditioned to produce a voltage linearly related to optical power, because the front walls were unstable and must not be hit. The brief also made clear that the sensor needed to cope with front-wall irregularities rather than assuming a perfectly flat surface. :contentReference[oaicite:22]{index=22}

In the pseudocode, this front signal appears as **PVF** (photovoltage front), and the navigation logic compares it to a threshold value **Vmin** to determine whether a front obstacle is present. :contentReference[oaicite:23]{index=23}

## Actuation and Motor Driver Design

### Forward motion
The brief states that **Motor 1 and Motor 2** were used for forward motion and that each motor required **0.12 A** to turn on, which exceeds the maximum current an Arduino digital pin can supply. This required transistor-based driver circuitry so the Arduino could control the motors safely using a battery-powered current path. :contentReference[oaicite:24]{index=24}

### Left / right motion
For lateral movement, the robot used two additional motors and required **bidirectional control**. My actuation write-up describes this as an **H-bridge bidirectional DC motor control** using BJTs, where selected transistor pairs drive current through the motor in opposite directions to move the robot left or right. The write-up also explains the role of:
- **NPN BJTs** as switches/current amplifiers,
- **diodes** for protection against back-EMF,
- and **resistors** for current limiting and speed moderation. :contentReference[oaicite:25]{index=25}

## Navigation Logic
The pseudocode defines:
- `PBL` = left-side pushbutton
- `PBR` = right-side pushbutton
- `PVF` = front photovoltage
- `M1`, `M2` = forward-drive motors
- `M3`, `M4` = lateral-drive motors. :contentReference[oaicite:26]{index=26}

The control idea was:
- if a front wall is detected and neither side button is pressed, move sideways to search for a passage
- if the robot detects a front wall and contact on one side, move away from that blocked side
- if no front obstacle is detected, move forward
- count the number of front-wall sections passed, and terminate once the robot has passed **7 front walls**, which the brief permitted as an assumption for pseudocode design. :contentReference[oaicite:27]{index=27} :contentReference[oaicite:28]{index=28}

This is a reactive robotics strategy: the robot does not need a stored route, but instead makes movement decisions based on real-time sensor inputs.

## Arduino Implementation
The uploaded Arduino file shows an implementation of the sensor-based maze-solving logic using:
- digital inputs for the left and right pushbuttons,
- an analog input for the front photodiode signal,
- motor control pins for forward and lateral movement,
- and a counter variable for tracking progress through the maze. :contentReference[oaicite:29]{index=29}

This aligns with the project structure described in Brief 0, where Part 2 required students to **build the circuits and programme the actual robot** to solve the maze. The same brief also provided preparation material on Arduino programming, digital input/output, analog input, and simulation practice, which formed part of the implementation pathway for the project. :contentReference[oaicite:30]{index=30}

The code reflects the intended control structure:
- read sensor states,
- determine whether a front obstacle is present,
- decide between left, right, or forward movement,
- increment a wall counter,
- and stop once the maze exit condition is reached.

Although the uploaded file appears to be a development-stage implementation rather than a fully polished final software package, it still demonstrates the essential embedded control logic used to connect the robot’s sensing and actuation subsystems into an autonomous navigation task. :contentReference[oaicite:31]{index=31}

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **embedded robotics logic**
- **sensor-based decision making**
- **autonomous navigation in an unknown environment**
- **digital and analog sensor interfacing**
- **motor driver circuit design**
- **H-bridge / bidirectional motor control concepts**
- **Arduino-based control implementation**
- **systems thinking**, linking maze constraints, sensors, actuators, and control logic into one design
- **algorithmic planning**, through structured pseudocode for robot behaviour

## What I Learned
This project developed my understanding of how robotic systems make decisions from local and imperfect sensor information rather than from a complete map of the environment. In particular, it reinforced the importance of designing sensing and actuation together: successful navigation depended not only on writing movement logic, but also on selecting appropriate sensors for different wall types and building the motor-control hardware needed to execute those decisions on a real robot. 

## Repository Contents
- `README.md` – project summary
- `brief/` – scenario briefs and requirements
- `code/` – Arduino implementation
- `planning/` – pseudocode and control logic
- `design/` – motor actuation write-up and circuit-related notes

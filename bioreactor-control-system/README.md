# Connected Bioreactor Control System

## Overview
This project involved the design and development of a **connected small-scale bioreactor control system** capable of monitoring and regulating three critical process variables: **temperature**, **stirring speed**, and **pH**. The aim was to create a system that not only interfaced with the physical bioreactor hardware, but also implemented the sensing, actuation, control logic, and external connectivity required to operate it against a defined engineering specification.

The bioreactor testbed was composed of three core subsystems:
- a **heating subsystem** for temperature regulation,
- a **stirring subsystem** for maintaining homogeneous mixing,
- and a **pH subsystem** for regulating acidity/alkalinity through peristaltic pumps.

The complete system was intended to use an **Arduino Uno** for local sensing and actuation, together with an **ESP32** for connectivity and remote telemetry to an IoT dashboard. The uploaded design specification also required all subsystems to log data and provide a user interface for parameter monitoring and adjustment. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

## Project Context
This was a university interdisciplinary engineering project involving both hardware and software development. The system had to satisfy a formal design specification rather than simply demonstrate that individual components worked in isolation. In other words, the project was not just about making a motor spin or a heater warm the liquid, but about designing a control system capable of maintaining process variables within required limits. :contentReference[oaicite:6]{index=6}

The key system specifications were:
- inlet water temperature assumed in the range **10–20°C**
- temperature setpoint maintained in the range **25–35°C** within **±0.5°C**
- stirring speed maintained in the range **500–1500 RPM** within **±20 RPM**
- pH maintained in the sensing range **3–7**
- data logging and a user-facing interface for monitoring and adjusting setpoints. :contentReference[oaicite:7]{index=7}

## My Contribution
My primary contribution was leading the development of the **stirring subsystem**, which was essential for ensuring that temperature and pH changes were distributed uniformly throughout the entire solution rather than remaining localised near the heater or pumps. This required both hardware interfacing and control design.

In particular, I contributed to:
- the **design and implementation of the stirring subsystem circuitry**
- the **motor drive interface using an NPN transistor and flyback diode**
- the **measurement of rotational speed using a photo-interrupter / reflective sensing approach**
- the **development of motor-speed control logic using PID control**
- the **calibration and testing of RPM against duty cycle using MATLAB**
- the broader integration of the subsystem into the connected bioreactor architecture.

This project strengthened my skills in embedded control, circuit design, sensor interfacing, calibration, and system-level engineering.

## System Architecture
The bioreactor was conceived as a layered control system combining physical subsystems with digital control and network connectivity.

### Core physical subsystems
The design specification identifies three physical subsystems:
- **Heating subsystem**: a **3 Ω, 30 W heating element** and a **10 kΩ thermistor** for temperature sensing
- **Stirring subsystem**: a **propeller**, **motor**, **gearing**, and an **IR LED / phototransistor reflective sensor** that generates **two pulses per revolution**
- **pH subsystem**: a **pH probe** for sensing and **6 V, 1 A peristaltic pumps** to add acid or alkali to the solution. :contentReference[oaicite:8]{index=8}

### Control and connectivity
The uploaded specification makes clear that the bioreactor testbed itself was incomplete without:
- a **microcontroller development board** to act as the control core,
- electronic circuits to interface sensors and actuators,
- an **ESP32** to provide connectivity,
- and two-way communication between the **Arduino Uno**, **ESP32**, and a remote server/dashboard. :contentReference[oaicite:9]{index=9}

The connectivity guide further describes the intended communication chain as:
**Arduino Uno → wired link / I2C → ESP32 → Wi-Fi → ThingsBoard / IoT dashboard**, enabling end-to-end telemetry and remote interaction. :contentReference[oaicite:10]{index=10}

## Stirring Subsystem
The stirring subsystem was critical because heating and pH correction alone are not sufficient unless the solution is mixed effectively. As described in the report, without stirring, the acid/base dosing and heating would mainly affect regions close to the actuators rather than the full liquid volume. The stirring subsystem therefore ensured that temperature and pH regulation applied to the **entire solution**, not just to one local region. :contentReference[oaicite:11]{index=11}

### Hardware design
According to the report, the subsystem used:
- a **3 V DC motor** (maximum current 1 A),
- a **CP2S700HCP photo-interrupter**,
- an **NPN BJT transistor (ZTX450)**,
- a **1N4001 diode**,
- an **Arduino Uno**,
- wiring,
- and a **3 V lead acid battery**. :contentReference[oaicite:12]{index=12}

A transistor-based drive stage was required because the Arduino cannot safely supply the current demanded by the motor directly. The report explains that the transistor was used so the motor could be driven without exceeding the current capability of an Arduino pin, while the diode was placed across the motor to protect the circuit from back-EMF when switching. The use of **PWM on pin 11** allowed the duty cycle applied to the motor to be varied, and therefore allowed the motor speed to be adjusted electronically. :contentReference[oaicite:13]{index=13}

### Speed sensing and RPM measurement
The design specification states that the stirring subsystem uses an optical reflective arrangement with an IR LED and phototransistor, producing **two pulses per revolution** from the output gear. :contentReference[oaicite:14]{index=14}

The uploaded Arduino code shows that the subsystem counted pulses using an interrupt on **digital pin 3**, measured over a fixed interval of **1,000,000 µs**, and then computed speed from the count. In the code, RPM is calculated as `Counter * 30`, which is consistent with a one-second measurement window and two pulses per revolution:
- 1 second count gives pulses per second
- divide by 2 to get revolutions per second
- multiply by 60 to convert to RPM
- giving `RPM = Counter × 30`. 

This is a clean example of using event-driven measurement and timing logic in an embedded system rather than relying on blocking polling. :contentReference[oaicite:15]{index=15}

### PID motor-speed control
The stirring subsystem used **PID control** to maintain motor speed around a target value rather than simply applying a fixed duty cycle. The report explains the design intent clearly:
- the **proportional** term responds to current speed error,
- the **integral** term accumulates previous error and helps reduce steady-state offset,
- the **derivative** term responds to the rate of change of speed and helps damp rapid variation. :contentReference[oaicite:16]{index=16}

The Arduino file confirms the use of PID control through the `ArduPID` library, with:
- setpoint initially set to **550 RPM**
- PWM output on **pin 11**
- feedback input derived from interrupt-based RPM measurement
- and controller gains `Kp = 0.001`, `Ki = 0.000001`, `Kd = 0.01`. :contentReference[oaicite:17]{index=17}

At startup, the motor is driven at an initial PWM value for 5 seconds before the controller loop begins. The report states that the controller then maintains the motor around **550 RPM**, though with some oscillation. :contentReference[oaicite:18]{index=18}

## Calibration and Testing
The report correctly identifies that RPM measurement had to be validated experimentally rather than assumed to be correct. Calibration was performed by comparing the RPM reported by the sensor/Arduino system with expected behaviour and by analysing the relationship between **duty cycle** and **measured RPM**. :contentReference[oaicite:19]{index=19}

The uploaded MATLAB calibration script plots the following measured data:

- duty cycle: `15, 16, 18, 24, 25, 39, 43, 47, 50`
- RPM: `350, 360, 500, 510, 730, 1270, 1300, 1400, 1550`

and generates an `RPM against duty cycle` graph. This provides a practical subsystem characterisation curve and demonstrates that the motor speed increased with duty cycle in a broadly monotonic way, supporting the validity of the sensing and control approach. :contentReference[oaicite:20]{index=20}

This calibration stage was important because it connected:
- low-level sensor behaviour,
- embedded processing,
- and physical motor output

into a verified engineering subsystem rather than an assumed one.

## Connectivity and IoT Integration
A major part of the overall bioreactor concept was external connectivity. The project documentation states that the Arduino Uno was responsible for local sensing and actuation, while the **ESP32** provided Wi-Fi connectivity and communication to a remote platform such as **ThingsBoard**. :contentReference[oaicite:21]{index=21} :contentReference[oaicite:22]{index=22}

The connectivity guide specifies:
- **I2C** as a suitable communication method between Arduino and ESP32,
- the need for **bidirectional logic-level shifting** because the Arduino operates at **5 V** and the ESP32 at **3.3 V**,
- and eventual data transfer to a dashboard server for storage, processing, display, and command return. :contentReference[oaicite:23]{index=23}

The uploaded ESP32 sketch demonstrates the ThingsBoard side of this idea. It:
- connects the ESP32 to Wi-Fi,
- connects to `demo.thingsboard.io`,
- sends telemetry values,
- and subscribes for **RPC callbacks** to support two-way communication. 

Although the example code sends random values rather than final integrated bioreactor data, it clearly demonstrates the connectivity path needed for a remote monitoring and control system. :contentReference[oaicite:24]{index=24}

## pH Measurement Design Considerations
Although my main contribution was the stirring subsystem, the broader bioreactor design also had to account for the characteristics of the pH probe. The reference note you uploaded explains that a pH electrode:
- is a **passive bipolar voltage-output sensor**
- has **very high source impedance**
- and requires attention to **temperature compensation**, **level shifting**, and **high-input-impedance buffering** for accurate measurement. :contentReference[oaicite:25]{index=25}

This is important because it shows that the project was not just mechanical or coding-based; it also involved understanding the analogue limitations of real biochemical sensing hardware.

## Key Engineering Skills Demonstrated
This project demonstrates skills in:
- **embedded systems design**
- **sensor and actuator interfacing**
- **closed-loop control**
- **PID implementation and tuning**
- **PWM motor control**
- **interrupt-based measurement**
- **circuit protection and transistor-based motor driving**
- **calibration and data analysis using MATLAB**
- **IoT system architecture**
- **Arduino–ESP32 communication**
- **remote telemetry and dashboard integration**
- **systems engineering across hardware, software, control, and connectivity**

## Key Outcomes
The strongest outcomes from the project were:
- development of a working **stirring subsystem** that could measure and regulate rotational speed
- implementation of a **PID-based control approach** for maintaining target motor speed
- calibration of **RPM versus duty cycle** using experimental data and MATLAB
- design of a broader connected architecture linking the bioreactor to an **ESP32 + ThingsBoard** telemetry chain
- contribution to a multidisciplinary system addressing **temperature**, **mixing**, **pH**, and **connectivity** in one platform. :contentReference[oaicite:26]{index=26} :contentReference[oaicite:27]{index=27}

## Challenges and Engineering Reflection
The report notes that while the motor could operate in the required range, the initial PID response showed **overshoot** and **ringing**, causing RPM fluctuations and making the reading less stable for the user. This is a realistic and valuable engineering result: it shows that building a controller is not just about selecting PID as a concept, but also about tuning constants to achieve the right transient and steady-state behaviour for the physical plant. The team also created a backup non-PID version for robustness and redundancy. :contentReference[oaicite:28]{index=28}

That is a strong portfolio point because it demonstrates engineering judgment, debugging, and resilience rather than pretending the first implementation was perfect.

## Tools and Technologies
- Arduino Uno
- ESP32 / TTGO
- PWM motor control
- PID control
- IR / photo-interrupter sensing
- DC motor drive circuitry
- NPN transistor switching
- Flyback diode protection
- I2C communication
- Logic-level shifting
- Wi-Fi / ThingsBoard telemetry
- MATLAB calibration and plotting

## What I Learned
This project significantly strengthened my understanding of how to build a real control system from the ground up. In particular, it showed me how sensing, actuation, feedback control, calibration, and connectivity must all work together if a biological process is to be regulated reliably. Leading the stirring subsystem also developed my ability to translate system requirements into practical circuit design, embedded code, and experimental validation.

## Repository Contents
- `README.md` – project summary
- `report/` – report and design write-up
- `brief/` – design specification and connectivity guidance
- `code/` – Arduino, ESP32, and MATLAB files
- `images/` – subsystem diagrams, circuit view, block diagram, and calibration plots

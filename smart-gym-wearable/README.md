# Smart Gym Wearable: Embedded Hardware and PCB Design

## Overview
This project involved the end-to-end hardware design of a **Smart Gym Wearable** intended to monitor workout motion and physiological state during exercise. The device combines:

- **motion sensing** using an ADXL343 3-axis accelerometer
- **heart-rate and pulse oximetry sensing** using the MAX30102
- **wireless communication** through an STM32WB55CEU6 with integrated Bluetooth Low Energy (BLE)
- **external flash memory** for extended data storage
- and a **battery-powered power management system** suitable for wearable use. 

The project covered the full hardware workflow from specification and component selection through schematic design, PCB layout, BOM preparation, and design-rule verification. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

## Project Context
This project was completed for **ELEC0152: Advanced Embedded Design for IoT Systems – Circuit Design and Implementation**. The coursework required an academic-style hardware design report documenting the complete process of designing and implementing an electronic system, including:

- circuit specification
- refined component selection
- system block diagram
- full schematic
- PCB design
- and bill of materials analysis. :contentReference[oaicite:5]{index=5}

The workshop guidance also required:
- at least one sensor using **SPI, I2C, or UART**
- at least one actuator
- at least two protocols among **SPI, I2C, UART**
- **USB power and data**
- and **wireless communication**. :contentReference[oaicite:6]{index=6}

This wearable satisfies those requirements through:
- sensor interfacing over **I2C**
- external memory over **QSPI/SPI**
- USB connectivity
- BLE wireless communication
- and LED-based user feedback. :contentReference[oaicite:7]{index=7}

## My Contribution
This project appears to be an individual hardware design project, and the uploaded report is written in first person around your own design decisions. The work demonstrates my ability to take a product idea from system requirements to a manufacturable PCB implementation.

My contribution included:
- defining the wearable’s hardware objectives
- selecting and justifying the major ICs and support circuitry
- designing the full schematic
- creating the PCB layout in KiCad
- setting design rules and checking manufacturability
- compiling the BOM and supplier-linked part list
- and documenting the design trade-offs in a formal hardware report. :contentReference[oaicite:8]{index=8}

## Product Motivation
The report frames the wearable around a real user problem: while commercial devices such as fitness trackers and smartwatches provide high-level metrics, they often provide limited feedback on **exercise execution quality**, **repetition consistency**, or **training efficiency**. The device was therefore designed to support structured resistance training by monitoring movement and physiological state while transmitting raw data to a smartphone for higher-level analysis. :contentReference[oaicite:9]{index=9}

This gives the project a strong product-engineering angle rather than being only a component-integration exercise.

## System Architecture
The wearable is built around the **STM32WB55CEU6**, which was selected as the central MCU/SoC because it combines:
- microcontroller capability
- low-power operation
- and integrated **Bluetooth Low Energy** support,

making it well suited for a compact wearable design. :contentReference[oaicite:10]{index=10}

The main subsystems shown across the report and schematics are:
- motion sensing
- optical biometric sensing
- mixed-voltage I2C interfacing
- external flash memory
- battery charging and regulation
- USB connection
- and user input/output. :contentReference[oaicite:11]{index=11}

## Motion Sensing: ADXL343 Accelerometer
The design uses the **ADXL343**, a 3-axis digital MEMS accelerometer. According to its datasheet, it supports:
- selectable ranges up to **±16 g**
- digital output over **SPI or I2C**
- motion-related features such as activity, inactivity, tap, double-tap, and free-fall detection
- and low-power operation down to **23 µA**. :contentReference[oaicite:12]{index=12}

This makes it a good fit for workout tracking, where the device needs to capture both static orientation and dynamic motion while remaining power-efficient.

Your accelerometer schematic shows:
- **3.3 V supply**
- local decoupling capacitors
- interrupt lines
- and pull-up resistors for the I2C bus,

which indicates correct attention to practical digital sensor integration rather than just symbolic connection. The uploaded noise-vs-output-data-rate figure also shows awareness of the trade-off between bandwidth and noise in motion sensing, which is particularly relevant in movement analysis for exercise tracking. :contentReference[oaicite:13]{index=13}

## Biometric Sensing: MAX30102 Pulse Oximeter and Heart-Rate Sensor
The wearable uses the **MAX30102** for optical heart-rate and blood-oxygen sensing. The datasheet describes it as an integrated pulse oximeter and heart-rate monitor module designed specifically for **wearable devices**, with:
- internal LEDs
- photodetectors
- ambient-light rejection
- FIFO support
- and low-power operation. It operates with a **1.8 V logic supply** and a separate **3.3 V LED supply**. :contentReference[oaicite:14]{index=14}

That voltage requirement directly explains one of the more interesting design decisions in your schematic: the use of a **voltage-level translator** between the MCU side and the sensor side.

## Mixed-Voltage I2C and Level Translation
Because the MAX30102 uses a lower logic supply than the main 3.3 V MCU domain, the design includes the **PCA9306** dual bidirectional I2C voltage-level translator. According to the datasheet, the PCA9306 is intended for bidirectional translation of I2C/SMBus signals across voltage domains without the need for a direction pin, while requiring pull-up resistors on both sides of the bus. 

Your schematic reflects this correctly by placing the translator between the sensor-side and main I2C-side buses, with supporting pull-ups and enable handling. This is a strong design choice because it shows awareness of:
- logic-level compatibility
- bus integrity
- and safe integration of mixed-voltage peripherals in a wearable system. 

## Memory Expansion: External Flash
The design also includes **external QSPI flash memory** (`W25Q128JVS`) connected through dedicated flash control and IO lines. This is a strong systems decision because it extends local storage for raw sensor data beyond what would be practical using only internal MCU memory. The report explicitly mentions this as part of the design rationale for capturing workout data before or alongside wireless transfer. :contentReference[oaicite:17]{index=17}

Including both BLE transmission and local memory support makes the system much more realistic as a wearable platform.

## Power Management and Battery Charging
A key strength of the project is its complete power subsystem. The design includes:
- a **lithium-ion battery**
- the **MCP73832** charge-management IC
- and the **MIC5365-3.3** LDO regulator. 

The MCP73832 datasheet and your schematic indicate a simple Li-ion charging solution with charge programming through a resistor, while the MIC5365 provides a regulated **3.3 V rail** with:
- low dropout
- low quiescent current
- and strong PSRR,
which is highly suitable for battery-powered portable electronics. :contentReference[oaicite:18]{index=18}

This is particularly important in a mixed-signal wearable, where clean regulation benefits both the MCU and noise-sensitive sensors.

## User Interaction and Feedback
The design includes:
- a **pushbutton** for starting and ending workouts
- and LED indicators for workout state / user feedback. 

This satisfies the actuator requirement from the workshop guidance and also improves usability by giving the user a simple physical interaction point rather than requiring all control through software alone. :contentReference[oaicite:19]{index=19}

## PCB Design
The PCB work is one of the strongest parts of this project. The uploaded board views show:
- a compact rectangular form factor
- routed top and bottom copper
- dense mixed-signal placement
- dedicated sensor areas
- and an RF/antenna-aware layout region. 

The report also states that the PCB design process considered:
- RF constraints for the BLE antenna path
- component placement constraints
- grounding
- routing strategy
- and manufacturability. :contentReference[oaicite:20]{index=20}

The antenna datasheet you uploaded also suggests explicit attention to PCB antenna footprint and layout recommendations, which is an important sign of real embedded-RF design awareness rather than treating BLE as just a software feature. :contentReference[oaicite:21]{index=21}

## BOM and Component Selection
The BOM screenshots and component list show that the project did not stop at schematic completion. It includes:
- actual manufacturer part numbers
- footprints
- supplier / assembly information
- and availability checks.

The report and coursework brief both emphasise performance, availability, and cost trade-offs in component selection, and your uploaded stock screenshots support that this was actively considered for parts such as:
- MAX30102
- MCP73832
- and MIC5365. 

That makes this much closer to a real hardware design project than a purely academic schematic.

## Verification and Manufacturability
The uploaded screenshots show:
- **ERC with zero violations**
- **DRC with zero violations**
- and explicit PCB constraint settings for clearance, track width, annular rings, vias, and board-edge rules.

This is a very important portfolio point because it demonstrates that the PCB was not only drawn, but checked against practical manufacturability and consistency rules. In other words, the project reflects a design flow aimed at real fabrication rather than only conceptual layout.

## Why This Project Matters
What makes this project strong is that it combines several engineering domains in one device:

- embedded hardware design
- mixed-voltage digital interfacing
- low-power wearable sensing
- biometric and motion sensor integration
- battery charging and regulation
- BLE-ready embedded platform design
- memory expansion
- PCB layout and manufacturability

This is the kind of project that shows genuine readiness for embedded hardware, IoT, wearable technology, and PCB/system design roles.

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **embedded hardware architecture**
- **wearable device design**
- **PCB design in KiCad**
- **sensor integration over I2C**
- **mixed-voltage interface design**
- **power management and Li-ion charging**
- **regulator selection and low-power design**
- **external flash integration**
- **BLE-aware PCB design**
- **design-rule verification**
- **BOM preparation and sourcing**
- **technical hardware reporting in academic/professional style**. 

## What I Learned
This project strengthened my understanding of how a complete embedded wearable is developed from the ground up. In particular, it showed me how important it is to think across the full hardware stack: product requirements, component compatibility, supply domains, bus protocols, signal integrity, battery management, PCB layout, and manufacturability all interact. It also reinforced that good hardware design is not only about making a circuit function, but about making it robust, power-efficient, buildable, and appropriate for the real application. 

## Repository Contents
- `README.md` – project summary
- `report/` – final hardware design report
- `pcb/` – KiCad project files
- `schematics/` – key schematic screenshots
- `images/` – PCB views, BOM, ERC/DRC, and component screenshots
- `datasheets/` – supporting technical references

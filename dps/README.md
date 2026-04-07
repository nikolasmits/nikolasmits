# Digital Power Supply for an Antarctic Weather Station

## Overview
This project involved the design and PCB implementation of a **digital power supply subsystem (DPS)** for an Antarctic Weather Station. The goal was to create a compact power-management board capable of producing **two stable regulated DC outputs: 5 V and 12 V**, from a single input supply, while satisfying constraints on efficiency, stability, cost, manufacturability, and physical size.

The project combined:
- **requirements-driven circuit design**
- **power conversion and regulation**
- **simulation-based verification**
- **PCB layout under manufacturing constraints**
- and **cost/performance trade-off analysis**.

## Project Context
This was a team project based on a formal engineering design brief. The brief required the DPS to power several modules in the weather station, including:
- **CPU** at approximately 5 V
- **RAM**
- **flash memory** at approximately 12 V
- and **sensors** at approximately 5 V. :contentReference[oaicite:2]{index=2}

The required output ranges and maximum currents were defined in the brief:
- CPU: **4.7–5.3 V**, max **12 mA**
- RAM: **4.5–5.5 V**, max **3 mA**
- FLASH memory: **11.2–12.8 V**, max **20 mA**
- Sensors: **4.85–5.15 V**, max **5 mA**. :contentReference[oaicite:3]{index=3}

The brief also imposed strict implementation rules:
- **double-sided PCB**
- **components only on the top side**
- **5 cm × 5 cm square board**
- **minimum 0.4 mm track width**
- **minimum 0.4 mm spacing**
- and only a limited set of approved ICs including **MC33063AD**, **UA723CD**, **TL317CD**, and fixed regulators. :contentReference[oaicite:4]{index=4}

## My Contribution
My contribution focused on the **circuit design, simulation, and PCB implementation** of the supply. This included:
- analysing the power requirements from the specification
- selecting an appropriate conversion/regulation strategy
- developing the circuit in simulation
- verifying the expected output voltages
- and translating the design into a PCB layout that met the lab’s physical design constraints.

This project strengthened my ability to work from system requirements rather than starting from a ready-made circuit.

## Design Problem
The key challenge in this project was that the board had to generate **both 5 V and 12 V outputs** from a **single input voltage**, and the input voltage was **not allowed to be close to either output voltage**. The brief defines “close” as within **±10%** of either 5 V or 12 V. :contentReference[oaicite:5]{index=5}

That makes the problem more interesting than a standard regulator design:
- the input cannot simply be 5 V or 12 V
- the board must support both rails from one source
- and the design must balance efficiency, regulation quality, and cost.

## Circuit Design Approach
The uploaded circuit simulation suggests a **multi-stage architecture** built around the **MC33063AD** DC-DC converter and **UA723CD** regulator stages.

This is a sensible engineering approach because:
- the **MC33063AD** is suitable for step-up / switching-based conversion
- while the **UA723** provides a classical analogue regulation stage for stable output setting.

The overall design appears to use:
- one stage to generate or condition the higher-voltage rail
- and regulator sections to refine and stabilise the required outputs.

This is a good solution for a dual-rail system because it separates the problems of **voltage conversion** and **output regulation** rather than trying to do everything in one uncontrolled stage.

## Simulation and Verification
The Multisim screenshot shows simulated output voltages of approximately:
- **11.871 V**
- **4.951 V**

which are both very close to the required nominal targets of **12 V** and **5 V**. These results strongly suggest that the design met the main steady-state voltage objectives in simulation before PCB implementation.

That is an important portfolio point because it shows a proper engineering process:
1. derive the design from requirements
2. simulate and verify behaviour
3. then implement the PCB

rather than laying out a board first and hoping it works.

## PCB Design
The PCB implementation is another strong part of the project. The uploaded board views show a compact routed design with:
- top-side component placement
- routed copper traces on both layers
- plated through-hole style vias
- and a layout that fits within the required small-board format.

This is especially relevant because the project brief required strict PCB rules for fabrication in the teaching lab, including:
- **5 cm × 5 cm board area**
- **top-side components only**
- fixed via and pad sizes
- and minimum routing clearances. :contentReference[oaicite:6]{index=6}

Designing under those constraints is a good demonstration of practical PCB engineering rather than unconstrained schematic-only work.

## Requirements-Driven Engineering
One of the best things about this project is that it was not defined only by the circuit diagram. The brief required a wider systems-engineering workflow including:
- requirements specification
- risk matrix
- gantt chart
- product data sheet
- manufacturing and test procedures
- verification results
- design data
- and costing for manufacture at different scales. :contentReference[oaicite:7]{index=7}

Even if your portfolio repository focuses mostly on the circuit and PCB, this context makes the project sound much more professional because it shows you were working within a full engineering development process.

## Cost and Efficiency Considerations
The brief explicitly rewarded teams for:
- keeping consumable cost low
- maintaining output stability
- and achieving **power efficiency above 60%** under the stated loading conditions. :contentReference[oaicite:8]{index=8}

This is important because it means the project was not only about “making the voltages appear,” but about making technically and economically sensible design choices. That is highly relevant to real electronics design work.

## Why This Project Matters
This project is valuable because it shows several important engineering skills in one place:

- interpreting incomplete requirements and refining them
- selecting a viable conversion/regulation strategy
- designing for dual-output supply generation
- simulating and verifying electrical performance
- laying out a board under strict fabrication constraints
- and thinking about efficiency, cost, and manufacturability together.

That makes it much stronger than a simple linear-regulator exercise.

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **power electronics design**
- **voltage regulation**
- **DC-DC converter design**
- **analogue circuit simulation**
- **requirements-driven engineering**
- **PCB design and routing**
- **design-for-manufacture**
- **performance verification**
- **cost and efficiency trade-off analysis**
- **working to formal engineering specifications**. :contentReference[oaicite:9]{index=9}

## What I Learned
This project strengthened my understanding of how power-supply design is shaped by system requirements rather than only by circuit theory. In particular, it showed me how output tolerance, input constraints, efficiency, cost, and PCB manufacturability all influence topology choice and implementation. It also reinforced the importance of validating a supply in simulation before moving to layout and fabrication. :contentReference[oaicite:10]{index=10}

## Repository Contents
- `README.md` – project summary
- `simulation/` – Multisim circuit design
- `pcb/` – PCB layout images

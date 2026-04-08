# Robotic Surgical Tool for Automated Conformal Bone Resection

## Overview
This project involved the design of an automated robotic system for **conformal bone tumour resection**. The objective was to move beyond traditional straight-cut tumour removal and propose a tool and planning method capable of removing bone tumours in a more shape-conforming way, preserving more healthy bone while still achieving **en-bloc resection**.

The project combined:
- **literature review of surgical bone-cutting technologies**
- **design of a conformal cutting end-effector**
- **mechanical and thermal safety considerations**
- and **algorithmic surgical planning** based on 3D tumour geometry.

The overall goal was to support **limb-sparing surgery** by enabling more precise removal of diseased tissue and better matching of irregular, patient-specific implants. 

## Project Context
This was completed for **ELEC0145 – Robotics in Medicine and Industry**, as **Assignment 1: Automated Bone Resection**. The brief framed the problem around the fact that bone tumours must be removed **en-bloc**, because fragmenting the tumour risks spreading malignant cells into surrounding tissue. It also highlighted the clinical limitation of traditional approaches such as amputation or large straight cuts, both of which remove excessive healthy bone. :contentReference[oaicite:3]{index=3}

The assignment required three major tasks:
1. a **literature survey** on bone cutting tools and technologies
2. a **conformal bone-cutting tool design**
3. a **surgical-planning method** for parameterising cuts from tumour geometry extracted from 3D imaging data. :contentReference[oaicite:4]{index=4}

## My Contribution
This was a team project, and the uploaded report shows a substantial systems-level contribution across both tool design and planning. The project demonstrates work in:
- analysing conventional and advanced bone-cutting technologies
- proposing a new **active hybrid end-effector**
- reasoning about **cooling, sensing, and safety**
- and developing the **mathematical parameterisation** of cutting paths from tumour geometry.

The strongest technical parts of the work are the tool concept itself and the planning workflow based on tumour centroid, principal axes, layer-by-layer circular milling, and safe offsets. :contentReference[oaicite:5]{index=5}

## Clinical Motivation
The central clinical motivation was to enable **conformal removal** of a bone tumour rather than excising a large rectangular block of healthy tissue around it. The brief explicitly states that modern additive manufacturing now makes irregular patient-specific implants possible, which means that surgical cutting no longer needs to be limited to simple geometries. :contentReference[oaicite:6]{index=6}

That makes this project highly relevant to modern orthopaedic oncology and robotic surgery: the cutting tool and motion-planning method must be designed together so that the removed cavity can be matched with a conformal implant.

## Literature Survey and Technology Evaluation
The report begins with a literature review of both **conventional** and **advanced** bone-cutting technologies.

### Conventional tools reviewed
The report analyses:
- **saws**
- **drills**
- **burrs**
- **milling tools**
- and **wire saws**. :contentReference[oaicite:7]{index=7}

The review discusses advantages such as:
- ease of use
- cost-efficiency
- and familiarity in orthopaedic practice,

but also identifies important drawbacks:
- **thermal necrosis**
- **bone debris**
- **microfractures**
- high cutting forces
- and significant bone loss due to tool diameter. :contentReference[oaicite:8]{index=8}

### Advanced technologies reviewed
The report also reviews more advanced options, including:
- **laser-based cutting**
- and **ultrasonic / piezoelectric cutting**. :contentReference[oaicite:9]{index=9}

These are presented as more precise and less mechanically traumatic alternatives, especially for delicate or conformal procedures, although they also have trade-offs such as cost and integration complexity.

A particularly useful part of the report is the comparison table of bone cutting systems by:
- autonomy
- surgical application
- degrees of freedom
- lifespan
- cutting mechanism
- cooling requirement
- precision
- and debris generation. This helps justify the final hybrid-tool choice rather than presenting it as arbitrary. :contentReference[oaicite:10]{index=10}

## Proposed Tool: Active Hybrid Ultrasonic-Laser Dual-Axis Milling System
The main engineering contribution of the project is the proposed **Active Hybrid Ultrasonic-Laser Dual-Axis Milling System**. The report explains that this combines:
- **laser pre-cutting** to define tumour boundaries precisely
- with **ultrasonic-assisted milling** to remove bone while reducing impact on surrounding tissue. :contentReference[oaicite:11]{index=11}

This is a strong concept because it uses the complementary strengths of both technologies:
- laser for accurate boundary definition
- milling for controlled material removal and geometric flexibility.

## Dual-Axis Articulating Burr
A key feature of the tool is the **dual-axis articulating burr**, introduced to avoid repeated repositioning during surgery. The report identifies two motions:
1. **Primary axis** for depth control
2. **Secondary axis** for angular / side-to-side control. :contentReference[oaicite:12]{index=12}

This enables the cutter to perform:
- vertical depth cuts
- angled cuts
- curved / conformal trajectories

without relying entirely on repositioning of the main robot arm. That is an excellent design point, because it improves:
- surgical precision
- efficiency
- and access to irregular tumour geometries. :contentReference[oaicite:13]{index=13}

## Extender for Deep-Seated Tumours
The report also adds an **extender** to increase the effective reach of the tool for deeper tumour locations. This is important because the tool body itself could otherwise obstruct access in confined anatomical spaces. The extender allows the cutting head to reach deeper regions while preserving stability and compatibility with the dual-axis mechanism. :contentReference[oaicite:14]{index=14}

That is a strong practical detail, because it shows the design considered not just kinematics, but also access constraints in real anatomy.

## Milling-Cutter Design
The end-effector uses a **ball-end milling cutter** and the report gives a strong engineering justification for the chosen design.

### Material selection
The cutter material proposed is **M2 High Speed Steel**, selected because of:
- high thermal conductivity relative to bone
- high specific strength and hardness
- and durability under high-speed cutting. :contentReference[oaicite:15]{index=15}

The report explicitly compares the thermal properties of bone and M2 steel, arguing that the cutter can dissipate heat more effectively and therefore reduce local overheating and the risk of thermal necrosis. :contentReference[oaicite:16]{index=16}

### Cutter geometry
The report proposes:
- a **cylindrical cutter with helical grooves**
- and an **8-flute corn-edge / corn-cob tooth design**. :contentReference[oaicite:17]{index=17}

The helical grooves help remove debris efficiently, reducing clogging and friction, while the corn-edge design is justified on the basis that it reduces cutting forces significantly compared with straight-edge mills. The report states that multi-tooth corn-edge milling can reduce cutting forces by roughly **45.60–65.96%** compared with straight-edge mills. :contentReference[oaicite:18]{index=18}

This is one of the strongest parts of the project because it shows detailed mechanical reasoning rather than treating the cutter as a generic spinning tool.

## Degrees of Freedom and Control
The report describes the complete cutting system as:
- **2 DOF** from the active tool head
- plus a **6 DOF robotic arm**
- giving a total of **8 DOF**. :contentReference[oaicite:19]{index=19}

It also explains that:
- **inverse kinematics** can be used to determine the tool-head target angle
- **PID control** is used for angular precision
- and a **strain gauge** provides real-time cutting-force feedback. :contentReference[oaicite:20]{index=20}

That makes the project highly relevant to robotics, because it includes both end-effector mechanics and closed-loop control considerations.

## Surgical Workflow
The report proposes a complete workflow consisting of:
- **Preoperative stage**
- **Planning stage**
- **Intraoperative stage**
- **Postoperative stage**. :contentReference[oaicite:21]{index=21}

This is a major strength, because it shows the project was not limited to the tool alone. It also considered:
- imaging (CT / MRI)
- tumour analysis
- trajectory planning
- intraoperative feedback
- and postoperative verification. :contentReference[oaicite:22]{index=22}

That systems-level thinking makes the project much stronger as a medical-robotics portfolio piece.

## Safety Features
The report pays strong attention to safety, especially **thermal necrosis**, which it notes can occur when bone is exposed to temperatures above **47°C for 1 minute**. :contentReference[oaicite:23]{index=23}

### Cooling
To address this, the design includes:
- an **internal saline cooling system**
- coolant release near the mill tip
- and a **TiO₂-coated internal channel** to improve coolant spreading and heat transfer. :contentReference[oaicite:24]{index=24}

### Temperature feedback
The report also proposes:
- a **high-precision infrared sensor** near the cutter tip
- real-time temperature monitoring
- and a feedback controller that reduces rotational speed and increases coolant flow if the temperature approaches unsafe levels. :contentReference[oaicite:25]{index=25}

### Tissue-boundary sensing
In addition, an **ultrasonic sensor** is proposed to detect tissue-density changes and distinguish tumour from healthy bone, helping the system identify critical boundaries and stop automatically when necessary. The report further discusses the potential use of **quantitative ultrasound (QUS)** and **machine learning** for more detailed tissue classification. :contentReference[oaicite:26]{index=26}

This is excellent portfolio material because it shows awareness that surgical automation must prioritise safety and tissue preservation, not just geometric accuracy.

## Surgical Planning and Parameterisation
The third major part of the project is the **surgical planning algorithm**, which is one of the strongest technical contributions.

The report explains how the tool path can be parameterised from 3D tumour data using:
- **position**
- **orientation**
- **cut shape and size**
- **cut depth**
- and **layer thickness**. 

### PCA for tumour orientation
The report uses **Principal Component Analysis (PCA)** to determine the tumour’s principal axes. The covariance matrix of the tumour points is computed, and the eigenvectors are used to determine:
- the **major axis**
- the second axis
- and the minor axis. :contentReference[oaicite:28]{index=28}

This allows the tool to be aligned with the tumour geometry rather than using a fixed global orientation.

### Centroid and radius calculation
The tumour centroid is computed as the mean of all tumour points, and then, for each cutting layer, the maximum radial distance from the centroid to the tumour boundary is used to define the local cutting radius. A **safe offset** is then added so that the cutter remains outside the tumour margin. :contentReference[oaicite:29]{index=29}

### Entry point and final cut depth
The planning workflow also defines:
- the **entry point** on the bone surface
- the **deepest cut point**
- and the **layer-by-layer depth progression** down to the deepest tumour point. 

### Circular layer-by-layer milling
The report argues that **circular milling layer by layer** is preferable to rectangular block milling for many tumour shapes, because it:
- reduces cutting forces
- reduces heat build-up
- conforms better to irregular tumours
- and is easier to automate without problematic sharp corners. :contentReference[oaicite:31]{index=31}

This is a strong planning concept, because it directly links tool mechanics to tumour geometry and automation feasibility.

## Tumour-Specific Strategies
Another strong element is that the report does not present the tool as one-size-fits-all. It discusses several tumour cases and proposes different cutting strategies for each, such as:
- layered exposure followed by contour and helical cutting
- cylindrical rough cutting followed by helical refinement
- slower cutting near thin bone sections
- and tumour-specific entry strategies. :contentReference[oaicite:32]{index=32}

That is exactly the kind of detail that makes the project feel more realistic and application-driven.

## Why This Project Matters
This project is valuable because it combines three domains that are often separated:
- **surgical tool / end-effector design**
- **medical robotics and control**
- and **algorithmic planning from imaging data**.

Instead of discussing robotic surgery only in general terms, the project shows how a tumour-resection workflow could be designed from literature review through tool concept to geometric planning. That makes it highly relevant to robotic surgery, orthopaedic robotics, medical-device design, and surgical planning.

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **medical robotics system design**
- **literature-based engineering evaluation**
- **end-effector and mechanism design**
- **tool-material and cutter-geometry selection**
- **surgical workflow design**
- **cooling and thermal safety reasoning**
- **sensor-integrated safety design**
- **principal component analysis for geometry alignment**
- **3D geometric path parameterisation**
- **robotic motion-planning concepts**
- **technical report writing for an open-ended engineering problem**. 

## What I Learned
This project strengthened my understanding of how robotic surgery requires the integration of many engineering disciplines at once. In particular, it showed me that designing a useful surgical system is not only about the robot arm, but also about the cutting mechanics, thermal behaviour, safety sensing, tumour geometry, and the mathematical planning of the resection path. It also reinforced the importance of designing tools around the clinical objective — in this case, en-bloc removal with minimal healthy bone sacrifice. 

## Repository Contents
- `README.md` – project summary
- `report/` – final team report
- `data/` – tumour and bone geometry datasets
- `cad/` – CAD models or exported end-effector visuals
- `planning/` – MATLAB / pseudocode / planning material

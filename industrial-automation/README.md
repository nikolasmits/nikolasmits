# Industrial Automation of Wheel Retrieval, Deburring, Polishing and Storage

## Overview
This project involved the design of an automated industrial system for handling sports rims after manufacturing. The objective was to automate the full downstream process from **disorganised storage retrieval** to **deburring**, **polishing**, **flipping**, and **final storage**, while selecting appropriate sensing, robotics, and transport technologies for each stage.

The project combined:
- **image-based rim classification**
- **automation process design**
- **robotic handling**
- **material transport**
- **wheel flipping mechanism design**
- **force-controlled polishing concepts**
- and **cycle-time / bottleneck considerations**

to create a complete industrial automation concept for alloy wheel processing. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

## Project Context
This was completed for **ELEC0145 – Robotics in Medicine and Industry**. The assignment was based on a sports rim producer that manufactured **10 different types of rims**, each with different geometry and dimensions. After casting, the rims were stored in a disorganised way, and the task was to automate the process of:
- retrieving one rim from storage
- identifying its type
- sending it to deburring
- polishing both sides
- flipping it so the second side could be processed
- and sending it to an organised storage facility. :contentReference[oaicite:6]{index=6}

The brief also required:
- comparing multiple technology options
- justifying final selection
- including sensors
- reducing bottlenecks and process time
- and estimating the cost of the final system. :contentReference[oaicite:7]{index=7}

## My Contribution
My contribution focused on the **automation and mechanical systems side** of the project, particularly the process design and robotic handling concepts. This included work on:
- the **wheel flipping concept and its mechanical reasoning**
- the **process flow and automation sequence**
- the **polishing concept**, including force-related considerations
- and the broader integration of handling, transport, and finishing stages into one industrial workflow.

This project strengthened my ability to design automation systems at full-line level rather than thinking only about one isolated robot or mechanism.

## Task 1: Rim Classification
The first part of the assignment required classification of **10 different sports rim types**, using **15 images per class**. The goal was to design and train a CNN model capable of identifying the rim type so that the correct downstream deburring and polishing programme could be selected automatically. :contentReference[oaicite:8]{index=8}

According to the project slides, the dataset was organised as:
- **10 rim types**
- **15 images each**
- split into **70% training**, **20% validation**, and **10% testing**
- with images resized to **224 × 224** and normalised to **[0,1]**. :contentReference[oaicite:9]{index=9}

The proposed CNN architecture in the slides included:
- an image input
- convolution layers with **3 × 3 filters**
- max-pooling
- ReLU and batch normalisation
- a dense layer
- and a 10-class output. :contentReference[oaicite:10]{index=10}

This stage was important because it linked machine vision directly to industrial automation: the system first needed to know **which rim it was handling** before selecting the correct deburring and polishing parameters.

## Automation Process Design
The core of the project was the design of a complete automated process for wheel handling and finishing. The assignment brief defined the required sequence as:
1. retrieve a random rim from disorganised storage
2. identify the rim type
3. send it to deburring
4. send it to polishing
5. process **both sides**
6. and finally place it into proper storage. :contentReference[oaicite:11]{index=11}

Your project material shows that the solution was approached as a **multi-station industrial line**, with a structured floor plan and staged processing rather than a single isolated robot cell. :contentReference[oaicite:12]{index=12}

## Wheel Retrieval and Handling
The brief emphasises that the rims begin in a **disorganised storage area**, so retrieval is not a trivial pick-and-place problem. The system therefore needed:
- a method for identifying rim type
- a handling system that could lift and move rims safely
- and a transport structure to move rims between stations. :contentReference[oaicite:13]{index=13}

The supporting literature also provides useful industrial context:
- alloy wheels are commonly produced by **casting**, followed by **heat treatment**, **machining**, and dimensional quality checks
- which makes post-processing stages such as finishing and inspection highly relevant in production lines. :contentReference[oaicite:14]{index=14}

## Deburring Stage
Deburring was a required stage because rims produced through machining and related manufacturing processes can contain burrs that reduce part quality. The review paper you uploaded explains that burr formation is a common and undesirable consequence of machining and that deburring is a costly but necessary post-processing operation. It also highlights that deburring can easily become a **production bottleneck**, especially when automation is poor. :contentReference[oaicite:15]{index=15}

That aligns very well with the project brief, which required not only a deburring solution but also attention to process time and bottleneck reduction. :contentReference[oaicite:16]{index=16}

Your project therefore has strong industrial relevance: it treats deburring not just as a manufacturing detail, but as a line-design problem requiring automation and throughput awareness.

## Polishing Stage
Polishing was the next major finishing stage after deburring. This required selecting an approach for robotic polishing that could operate on both sides of the rim and maintain controlled contact with the surface. The brief explicitly asks whether deburring and polishing should be done by:
- one shared robot
- or two separate robots,
and whether intermediate transport is needed between these stages. :contentReference[oaicite:17]{index=17}

The polishing literature you uploaded is particularly useful here. The compliant end-effector paper explains that in robotic polishing, the **contact force between the polishing tool and the workpiece is crucial** for surface quality, and that compliant or force-feedback-based designs help avoid damage while improving control accuracy. :contentReference[oaicite:18]{index=18}

Your diagrams also show that the polishing concept was treated through **normal and tangential force components**, a **control block diagram**, and a **force-related process workflow**, which makes this a strong systems-level design rather than a generic polishing idea. :contentReference[oaicite:19]{index=19}

## Flipping Mechanism
One of the most important design constraints in the brief was that **both sides of the rim** had to be deburred and polished. That meant the project required a dedicated solution for flipping the wheel so the second side became accessible. :contentReference[oaicite:20]{index=20}

Your submitted figures make this one of the strongest parts of the project:
- a dedicated **flipping structure**
- a diagram showing **motion along the flipping curve**
- and a **torque analysis** along the flipping path for different wheel mass/radius cases.

This shows that the flipping stage was treated as a real mechanical design problem with load analysis, rather than simply saying “the wheel will be turned over.” That is a strong portfolio point because it demonstrates practical engineering reasoning about gravity, moment loading, and handling robustness.

## Conveyor and Factory Flow
The conveyor-belt reference adds industrial context to the transport part of the system. It highlights that conveyor systems are widely used in industrial material handling because of their simplicity, efficiency, and low power requirements, but also notes that belt systems require good maintenance and proper handling of sticking materials, wear, idlers, and drive components. :contentReference[oaicite:21]{index=21}

This is relevant because your project required multiple stages and transfer between stations, so transport could not be treated as an afterthought. The floor plan and staged process diagrams in your work suggest that conveyor-based or guided transfer was treated as part of the full system architecture, not just a background assumption. :contentReference[oaicite:22]{index=22}

## Systems Engineering Value
What makes this project strong is not only the individual parts, but the fact that it links them together into one industrial system:

- vision identifies the rim
- retrieval brings it from disorganised storage
- transfer sends it to finishing
- deburring removes manufacturing burrs
- polishing improves surface finish
- flipping makes both sides accessible
- and final storage completes the line. 

That kind of full workflow thinking is central to industrial automation engineering.

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **industrial automation system design**
- **process flow and station planning**
- **robotic finishing concepts**
- **CNN-based classification for manufacturing**
- **mechanical handling and flipping mechanism design**
- **torque and load reasoning**
- **sensor-based automation thinking**
- **transport and conveyor integration**
- **force-control concepts for polishing**
- **technology comparison and selection**
- **cycle-time and bottleneck awareness**
- **designing for manufacturing workflows rather than isolated subsystems**. 

## What I Learned
This project strengthened my understanding of how automation systems are built at process level. In particular, it showed me that a successful industrial solution depends on integrating sensing, classification, handling, transport, mechanical fixtures, robotic finishing, and storage into one coherent workflow. It also highlighted that seemingly secondary stages such as flipping, deburring, or transfer can become major engineering challenges if they are not designed properly. 

## Repository Contents
- `README.md` – project summary
- `presentation/` – project presentation
- `images/` – floor plan, flipping mechanism, polishing control, and workflow diagrams
- `references/` – supporting literature used for technology selection
- `code/` – MATLAB / analysis files if included

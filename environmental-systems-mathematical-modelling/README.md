# Environmental Systems Mathematical Model: Pollution Propagation in the Great Lakes

## Overview
This project involved the development of a mathematical model to simulate the **propagation of pollution through the Great Lakes** over time. The aim was to describe how pollutant mass and concentration evolve across an interconnected environmental system when affected by:
- precipitation
- runoff
- evaporation
- connecting inter-lake flows
- and diversions.

The model was implemented in **MATLAB** and used recorded monthly data from **1950 to 2019** to analyse pollutant transport across:
- **Lake Superior**
- **Lake Michigan-Huron**
- **Lake Erie**
- **Lake Ontario**. 

## Project Context
This was a **team mathematical modelling project** focused on environmental systems and water quality. The core environmental motivation was **eutrophication** caused by nutrient pollution, especially phosphorus transported into lakes through agricultural runoff. The reports explain that this process can lead to algal blooms, oxygen depletion, acidification, and severe damage to ecosystems and water resources. 

The Great Lakes were chosen as the system of study because they contain roughly **21% of the planet’s freshwater by volume** and are critically important for water supply, industry, biodiversity, and food production. 

## My Contribution
From the uploaded materials, my contribution clearly included working on the **mathematical modelling and MATLAB implementation** of pollution transport across the Great Lakes. The files show direct work on:
- deriving and explaining the governing equations
- converting the physical lake-network problem into coupled mass-balance equations
- implementing the model numerically in MATLAB
- simulating pollutant propagation under different initial conditions
- and analysing the resulting concentration trends over time. 

## Environmental Problem
The project was motivated by nutrient pollution from fertilizers and runoff. The reports explain that phosphorus-rich runoff from nearby agricultural land can trigger eutrophication, especially in vulnerable lakes such as **Lake Erie**, which is warm, shallow, and highly affected by runoff and sewage input. 

The broader goal of the model was therefore practical: to identify which lakes are most at risk, understand long-term pollutant behaviour, and support decisions on quotas, treatment, and environmental management. 

## Great Lakes Network
The system was modelled as an interconnected lake network consisting of:
1. Superior
2. Michigan-Huron
3. Erie
4. Ontario

with connecting flows between upstream and downstream lakes, plus diversions such as the Ogoki & Long Lac Diversions, Chicago Diversion, and Welland Canal. The Great Lakes network diagram in the report shows the directional flow structure used to build the model equations. :contentReference[oaicite:8]{index=8}

## Mathematical Model

### Water-volume balance
The first stage of the modelling was to express the **change in lake volume** as a balance of inflows and outflows. The report defines the inflow contributions as:
- precipitation \(P_i\)
- runoff \(R_i\)
- upstream connecting flow
- inflow diversions

and outflows as:
- evaporation \(E_i\)
- downstream connecting flow
- outflow diversions. :contentReference[oaicite:9]{index=9}

This gives a set of coupled differential equations for the lake volumes:
- one for **Superior**
- one general form for **Michigan-Huron** and **Erie**
- and one for **Ontario**. :contentReference[oaicite:10]{index=10}

### Pollutant mass balance
The second stage extended the model from water volume to **pollutant mass**. The reports define the change in pollutant mass as:
- pollution added by runoff
- plus pollutant inflow from upstream lakes
- minus pollutant outflow to downstream lakes and diversions. 

This creates a set of coupled lake-by-lake mass-balance equations in which the concentration in one lake directly affects the pollutant load entering the next. That is one of the strongest features of the project, because it turns the Great Lakes into a true **coupled dynamical system** rather than independent compartments.

## Numerical Implementation in MATLAB
The uploaded MATLAB code shows how the system was implemented computationally:
- monthly flow and climate data were loaded from CSV files
- lake surface areas and initial volumes were defined
- flow terms were converted into consistent units
- cumulative water volumes were computed over time
- and pollutant mass was propagated forward using a **for-loop Euler update scheme**. :contentReference[oaicite:12]{index=12}

The code explicitly shows:
- lake surface areas \(A_1\) to \(A_4\)
- initial volumes \(V_{01}\) to \(V_{04}\)
- monthly runoff, precipitation, evaporation, flows, and diversions
- and concentration calculation through  
  \(\rho_i(t) = m_i(t) / V_i(t)\). :contentReference[oaicite:13]{index=13}

This is a strong portfolio point because it demonstrates translation from environmental mathematics into executable simulation code.

## Euler’s Method
The reports explain that pollutant mass was updated month by month using **Euler’s Method**, with:
- one month as the time step
- the pollutant mass at the previous month as the state variable
- and the mass-balance equation as the instantaneous slope. 

That makes the project a good example of using numerical methods to solve a real-world environmental system where exact closed-form solutions would not be practical.

## Unit Consistency and Dimensional Analysis
One of the strongest technical sections of the final report is the **dimensional analysis**. It explains that:
- connecting flows and diversions were recorded in **m³/s**
- runoff was given in **mm over lake area per month**
- and therefore the flow terms had to be converted to compatible units before the mass-balance equations could be solved consistently. :contentReference[oaicite:15]{index=15}

This is a very good engineering and modelling point, because it shows attention to physical consistency rather than only coding formulas directly.

## Scenario Analysis: Initial Pollution in Lake Superior
A major part of the project was the simulation of downstream pollutant propagation when **Lake Superior** starts with an initial pollution mass and runoff pollution is assumed zero. Three cases were considered:
- **75,000 metric tons**
- **50,000 metric tons**
- **25,000 metric tons** of pollution in 1950. 

The results described in the final report show that:
- **Lake Superior** experiences a gradual decrease in pollutant concentration over time
- **Michigan-Huron** increases at a decreasing rate
- **Erie** shows more fluctuation
- **Ontario** rises more slowly and remains the least contaminated of the downstream lakes over the recorded time horizon. :contentReference[oaicite:17]{index=17}

For the **75,000-ton** case, the report states approximate values of:
- Superior decreasing from **6.252 μg/dm³** in 1950 to **4.141 μg/dm³** in 2019
- Michigan-Huron rising to **1.371 μg/dm³**
- Erie rising with fluctuations to around **1.336 μg/dm³**
- Ontario reaching around **0.981 μg/dm³** by 2019. :contentReference[oaicite:18]{index=18}

For the **50,000-ton** case, the report similarly gives:
- Superior decreasing from **4.168 μg/dm³** to **2.761 μg/dm³**
- Michigan-Huron rising to **0.931 μg/dm³**
- Erie reaching about **1.335 μg/dm³**
- Ontario reaching about **0.654 μg/dm³**. :contentReference[oaicite:19]{index=19}

These scenario studies are a strong part of the project because they demonstrate how the same model can be used not only for historical reconstruction but also for hypothetical environmental-risk analysis.

## Interpretation of the Results
The reports conclude that **Lake Superior** can retain high pollutant concentrations for a long time because of its very large volume and long retention time, while **Lake Erie** is especially vulnerable because it is shallow, warm, and strongly influenced by agricultural runoff. 

That interpretation is valuable because it connects the mathematical output back to real environmental geography and lake characteristics rather than leaving the work at the level of numerical curves.

## Why This Project Matters
This project is valuable because it demonstrates how mathematical modelling can be used to analyse a large-scale environmental system with real societal importance. It combines:
- physical reasoning
- mass-balance modelling
- differential-equation thinking
- numerical methods
- MATLAB implementation
- and interpretation of long-term environmental risk.

That makes it relevant not just for mathematics, but also for systems modelling, environmental engineering, and data-driven decision support.

## Engineering and Analytical Skills Demonstrated
This project demonstrates skills in:
- **environmental systems modelling**
- **mass-balance equation derivation**
- **coupled dynamical systems**
- **numerical solution using Euler’s Method**
- **MATLAB programming**
- **handling real time-series data**
- **dimensional analysis and unit conversion**
- **scenario simulation**
- **interpreting model outputs in a physical/environmental context**
- **technical report writing and mathematical explanation**. 

## What I Learned
This project strengthened my understanding of how mathematical models can be used to represent complex environmental systems. In particular, it showed me how interconnected physical processes such as runoff, evaporation, and lake-to-lake flow can be translated into a system of coupled equations and solved numerically over long timescales. It also reinforced the importance of checking units carefully and interpreting model outputs critically rather than treating simulation results as automatically correct. 

## Repository Contents
- `README.md` – project summary
- `report/` – team final report and modelling write-up
- `code/` – MATLAB model implementation
- `data/` – MATLAB model implementated data

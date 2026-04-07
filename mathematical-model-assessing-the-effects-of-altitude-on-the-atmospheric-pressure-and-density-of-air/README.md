# Mathematical Model of the Effects of Altitude on Atmospheric Pressure and Air Density

## Overview
This project developed a mathematical model to assess how **altitude affects atmospheric pressure and the density of air**. The work was motivated by a real-world sports-engineering context: understanding how high-altitude conditions may affect football performance through reduced oxygen availability and altered air properties.

The project progressed through five connected models:
- pressure variation with changing density using the **ideal gas law**
- finite pressure variation in a small control volume of air
- cumulative pressure variation with altitude using **Riemann sums** and integration
- derivation of air-density change with altitude
- and a final model comparing **constant-temperature** and **temperature-dependent** atmospheric pressure behaviour. 

## Project Context
This was completed for **ENGF0003 Coursework 1 (2022–2023)**. The coursework brief framed the problem around the question:

**How does altitude affect the atmospheric pressure and the air that we breathe?** :contentReference[oaicite:3]{index=3}

The engineering motivation was linked to the effect of high altitude on football performance, including reduced aerobic power due to lower oxygen availability and changes in air-density-related behaviour. The brief required five linked models and a MATLAB comparison of the final pressure expressions. :contentReference[oaicite:4]{index=4}

## My Contribution
This appears to be an individual coursework project, and the submitted report is written as your own structured analysis. My contribution included:
- deriving and explaining the mathematical models from first principles
- applying finite differences, derivatives, Riemann sums, and definite integrals
- using dimensional analysis to validate equations
- incorporating temperature as an altitude-dependent variable
- and implementing the final comparison graph in MATLAB. 

## Problem Definition
The core research question was how altitude affects:
- **atmospheric pressure**
- **air density**
- and therefore the physical conditions experienced by people and moving bodies at high altitude. :contentReference[oaicite:6]{index=6}

The project treated this as a modelling exercise in which different assumptions were introduced gradually and then compared. This is an important strength of the work: rather than jumping immediately to one formula, the coursework builds a hierarchy of models, each with clearer physical meaning and increasingly realistic assumptions.

## Model 1: Pressure Variation from the Ideal Gas Law
The first model starts from the **ideal gas law**, relating pressure \(P\), density \(\rho\), gas constant \(R\), and temperature \(T\). The report uses this to study how a small change in air density leads to a corresponding change in pressure and constructs linear approximations for finite density steps. :contentReference[oaicite:7]{index=7}

A key idea here is that, with temperature held constant, pressure is directly proportional to density. This provides the first physical link between the air we breathe and the atmospheric pressure experienced at different conditions.

## Model 2: Pressure Change in a Small Control Volume
The second model uses a small cube of air as a **control volume** and derives an expression for the pressure exerted on its lower face from the weight of the air inside. The report then expands this idea into a finite pressure change with respect to a finite altitude change, using dimensional analysis to confirm consistency. 

This is a good engineering step because it translates abstract gas-law relations into a force-balance picture that is easier to connect to hydrostatics and fluid mechanics.

## Model 3: Hydrostatic Pressure Variation with Altitude
The third model treats the atmosphere as a static fluid and uses the hydrostatic relation:

\[
\frac{dP}{dz} = -\rho g
\]

to study how pressure changes with altitude. The report explains this both through:
- **Riemann-sum reasoning**
- and **definite integration**. 

This is one of the strongest parts of the coursework because it moves from finite differences to cumulative behaviour. Instead of thinking only about a tiny air cube, the model now considers the entire column of air above a reference point and shows that atmospheric pressure decreases with increasing altitude.

The report derives the linear form:

\[
P(z) = P_0 - \rho g z
\]

under the assumption of constant density, and plots it graphically. :contentReference[oaicite:10]{index=10}

## Model 4: Linking Pressure, Density, and Altitude
The fourth model combines:
- the ideal gas law
- and the hydrostatic pressure-altitude relation

to derive an expression for how **air density changes with altitude**. The report uses the **chain rule** to obtain a relation for \(d\rho/dz\), showing that density decreases as altitude increases. 

This is a particularly good modelling step because it removes the oversimplifying assumption that density stays constant. Instead, it shows that pressure and density are coupled, and both vary with height.

## Model 5: Including Altitude-Dependent Temperature
The final and most realistic model recognises that **temperature is not constant with altitude**. The report uses experimental temperature data up to 10 km altitude to define a temperature function \(T(z)\), then substitutes this into the pressure-altitude equations and compares the result with the simpler constant-temperature case. 

The report derives a temperature-dependent pressure function and contrasts it against the constant-temperature exponential-style pressure expression. This is the key modelling contribution of the project, because it shows how changing assumptions changes the predicted atmospheric-pressure profile. :contentReference[oaicite:13]{index=13}

## MATLAB Implementation
The uploaded MATLAB code implements the final comparison by defining:
- `P1` as the **temperature-dependent** pressure model
- `P2` as the **constant-temperature** pressure model
- and plotting both as a function of altitude from **0 to 10 km**. :contentReference[oaicite:14]{index=14}

The resulting graph shows that both pressure models decrease with altitude, but the **constant-temperature model decreases more steeply** than the temperature-dependent one. That matches the conclusion given in the coursework report. 

## Key Result
The most important conclusion from the final model is that **assuming constant atmospheric temperature leads to a faster predicted pressure drop with altitude than the temperature-dependent model**. In other words, ignoring temperature variation can significantly distort the estimate of atmospheric pressure at higher elevations. 

This is a strong engineering result because it highlights a broader modelling lesson: simplifying assumptions are useful, but they must be checked against the physics of the real system.

## Why This Project Matters
This project is valuable because it demonstrates how mathematical modelling develops in stages:
- start with a simple physical law
- build a local force-balance interpretation
- move to differential and integral forms
- then refine the model by including additional variables such as temperature.

That process is central to engineering analysis, where simplified models are often necessary but must be extended carefully when their assumptions become too limiting.

## Engineering and Analytical Skills Demonstrated
This project demonstrates skills in:
- **applied mathematical modelling**
- **ideal-gas-law reasoning**
- **hydrostatic pressure analysis**
- **finite differences and derivatives**
- **Riemann sums and definite integration**
- **chain-rule application**
- **dimensional analysis**
- **model comparison under different assumptions**
- **MATLAB plotting and function evaluation**
- **communicating mathematics in an engineering context**. 

## What I Learned
This project strengthened my understanding of how physical assumptions shape mathematical models. In particular, it showed me that pressure, density, altitude, and temperature are not independent quantities, and that the realism of a model depends strongly on which relationships are included or neglected. It also reinforced the value of validating formulas with units, graphs, and comparison between simpler and more detailed models. 

## Repository Contents
- `README.md` – project summary
- `report/` – full coursework write-up
- `code/` – MATLAB implementation of the final pressure models

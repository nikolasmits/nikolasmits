# Enhancement of Optical Absorption in Silicon Photovoltaics

## Overview
This project investigated how metallic nanostructures can be used to enhance light absorption in thin-film silicon photovoltaic cells. The work focused on a **hydrogenated amorphous silicon (a-Si:H) photovoltaic structure** incorporating a **periodic gold nanowire grating** above the active layer and a **gold back reflector** beneath it.

The aim was to determine whether the introduction of a periodic metallic grating could increase optical absorption through the excitation of **surface plasmon resonances** and **waveguide modes**, thereby improving the light-trapping performance of the device. The project combined photonic theory, nanostructure design, numerical simulation, and MATLAB-based post-processing to identify the key resonant mechanisms and optimise the cell geometry. :contentReference[oaicite:2]{index=2}

## Project Context
This was my **3rd Year Project Final Report** in the UCL Department of Electronic and Electrical Engineering. The project was carried out under the supervision of **Prof. Nicolae-Coriolan Panoiu** and focused on simulation-based enhancement of thin-film photovoltaic performance rather than fabrication. The report title, declared scope, and methods make clear that this was an individual research project centred on **electromagnetic modelling of nanostructured photovoltaics**. :contentReference[oaicite:3]{index=3}

## My Contribution
This was an individual research project, so I completed the full technical workflow myself. My contribution included:
- defining the photovoltaic cell geometry and research objective
- studying the theory of **surface plasmon resonance** and **waveguide-mode coupling**
- building the simulated structure in **RSoft DiffractMOD**
- performing **RCWA-based wavelength sweeps** and parameter scans
- comparing the nanostructured cell against a non-grating control design
- analysing electric and magnetic field distributions
- using MATLAB to process absorption maps, field data, and enhancement plots
- and interpreting how geometry and angle of incidence affected absorption performance. :contentReference[oaicite:4]{index=4}

## Research Objective
The report states that the aim of the project was to simulate, analyse, and explain whether **surface plasmon and waveguide modes induced by a metallic periodic grating** in the active layer improve light absorption and therefore enhance PV-cell efficiency. The project goals included:
- understanding the theoretical basis of plasmonic and waveguide effects
- optimising structural parameters such as grating period and width
- and using numerical simulation to evaluate absorption spectra and field intensity distributions with and without the metallic grating. :contentReference[oaicite:5]{index=5}

## Why Amorphous Silicon?
The report gives a strong device-level motivation for choosing **hydrogenated amorphous silicon (a-Si:H)**:
- it is cheaper than crystalline silicon
- it has stronger absorption in the visible range
- it can operate effectively in much thinner layers
- and it is suitable for flexible, thin-film photovoltaic applications. :contentReference[oaicite:6]{index=6}

At the same time, the report also identifies the key limitation of a-Si:H: although its optical absorption is favourable, its efficiency is reduced by short carrier diffusion lengths and defect-related recombination. This makes optical path enhancement especially important, which is why introducing metallic nanostructures is such a relevant design strategy. :contentReference[oaicite:7]{index=7}

## Device Structure
The final photovoltaic structure consisted of:
- an **a-Si:H active layer** of thickness **90 nm**
- a **gold substrate** of thickness **250 nm**
- and a **periodic gold nanowire grating** with width **120 nm**, height **20 nm**, and period **350 nm**. :contentReference[oaicite:8]{index=8}

The report explains the role of each layer clearly:
- the **a-Si:H layer** generates electron-hole pairs
- the **gold substrate** acts as a back reflector, increasing the effective optical path
- and the **gold nanowire grating** acts as a momentum-matching structure that enables coupling into resonant plasmonic and waveguide modes. :contentReference[oaicite:9]{index=9}

## Physical Mechanism
A key strength of the project is that it does not stop at reporting absorption peaks. It develops the underlying theory of **surface plasmon resonance (SPR)** and explains why a flat interface alone cannot always provide the momentum needed for coupling between incident photons and plasmonic modes. The report shows that introducing a periodic grating supplies additional in-plane momentum, allowing the incident light to satisfy the resonance condition for plasmon excitation. :contentReference[oaicite:10]{index=10}

The project also explains how the grating folds the dispersion relation into the first Brillouin zone, enabling coupling into modes with propagation constants larger than those of free-space light. This is what makes the grating so important for enhancing absorption at targeted wavelengths. :contentReference[oaicite:11]{index=11}

## Simulation Method
The simulations were performed using **Synopsys RSoft DiffractMOD**, which the report describes as a frequency-domain electromagnetic simulation tool based on **Rigorous Coupled Wave Analysis (RCWA)**. The structure was treated as periodic along the x-axis, and wavelength sweeps were performed using RSoft’s **MOST** tool across the range **0.2–1.6 µm**, covering ultraviolet, visible, and near-infrared light. :contentReference[oaicite:12]{index=12}

The report also explains several important simulation decisions:
- **TM-polarised plane-wave illumination** was used for the main analysis
- the incident direction was set along **−z**
- harmonic truncation was considered carefully, with **12 harmonics** chosen after trial-and-error as sufficient for convergence
- and both total reflection / absorption and field profiles were extracted. :contentReference[oaicite:13]{index=13}

This is a strong portfolio point because it shows that the simulation setup was not treated as a black box; it was justified in physical and numerical terms.

## Control Structure and Parameter Scans
To isolate the effect of the nanograting, the report explicitly compares the final design with a **control PV cell without the grating**. The non-grating case was simulated using the same general structure but with **zero harmonics**, since there is no periodicity in the x-direction and only the zeroth diffraction order is meaningful. :contentReference[oaicite:14]{index=14}

The project then used parameter scans to explore how absorption changed with:
- **grating period**
- **grating width**
- and, more selectively, other geometrical dimensions. :contentReference[oaicite:15]{index=15}

This is important because it moves the work beyond “one design example” into genuine design-space exploration.

## Key Results
The report states that introducing the periodic gold grating significantly enhanced the optical response of the device. In particular:
- absorption at certain wavelengths could be **more than doubled** compared to the control structure without a grating
- the strongest performance was obtained for **width = 120 nm**, **height = 20 nm**, **period = 350 nm**, and **a-Si:H thickness = 90 nm**
- and strong resonance features were observed at wavelengths around **1.05 µm** and **1.3 µm**, associated with tightly confined field distributions. :contentReference[oaicite:16]{index=16}

The report also identifies a distinct peak near **0.66 µm** that is independent of grating period and appears in both grating and non-grating structures, distinguishing it from the grating-induced plasmonic features. This is a very strong analytical point because it shows that the resonances were classified carefully rather than all peaks being grouped together simplistically. :contentReference[oaicite:17]{index=17}

## Field Analysis
The report makes especially good use of field-intensity contour plots. It explains that the relevant field components under TM illumination are:
- magnetic field **H\(_y\)**
- electric fields **E\(_x\)** and **E\(_z\)**. :contentReference[oaicite:18]{index=18}

The field maps were then used to confirm resonant modal excitation, with sharply confined electric and magnetic field distributions supporting the interpretation that absorption enhancement arose from **plasmonic and waveguide-mode coupling**, not just from generic scattering or increased path length alone. :contentReference[oaicite:19]{index=19}

That combination of spectral and field-level interpretation makes the project much stronger scientifically.

## Angle of Incidence
The report also extended the study beyond normal incidence. It found that absorption enhancement remains present for **oblique angles up to 45°**, although the resonance features broaden and shift. This is a strong practical result because solar illumination in real applications is rarely perfectly normal to the surface. :contentReference[oaicite:20]{index=20}

Including this angle study makes the project sound much more complete and application-aware.

## Why This Project Matters
This project is valuable because it sits at the intersection of:
- **electromagnetics**
- **nanophotonics**
- **materials / photovoltaic physics**
- and **computational simulation**.

Rather than treating photovoltaic performance only in terms of semiconductor device equations, it investigates how carefully designed optical nanostructures can alter the local electromagnetic field and increase the probability of photon absorption. That makes it especially relevant to advanced solar-cell design, plasmonics, and photonic engineering.

## Engineering and Research Skills Demonstrated
This project demonstrates skills in:
- **computational electromagnetics**
- **RCWA / frequency-domain optical simulation**
- **nanophotonic structure design**
- **surface plasmon resonance theory**
- **waveguide-mode analysis**
- **parameter optimisation**
- **field-distribution interpretation**
- **MATLAB post-processing**
- **scientific report writing**
- **linking physical theory to numerical simulation results**. :contentReference[oaicite:21]{index=21}

## What I Learned
This project strengthened my understanding of how strongly optical absorption can be shaped by nanostructure geometry. In particular, it showed me that photovoltaic performance is not only limited by the semiconductor material itself, but can also be enhanced through controlled electromagnetic coupling and light trapping. It also improved my ability to interpret simulation outputs critically, distinguishing between intrinsic material effects, waveguide behaviour, and truly grating-induced plasmonic resonances. :contentReference[oaicite:22]{index=22}

## Repository Contents
- `README.md` – project summary
- `report/` – final report
- `simulation/` – MATLAB live scripts for absorption maps, field analysis, and enhancement studies
- `images/` – PV schematics, absorption maps, field plots, and parameter-sweep outputs

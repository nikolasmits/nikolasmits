# Surface EMG Human-Machine Interface (sEMG HMI)

## Overview
This project involved the design of a **surface electromyography (sEMG) based human-machine interface** that converted muscle activity into a processed control signal suitable for machine interaction. The core aim was to acquire a weak bio-signal from the skin surface, condition it through analogue circuitry, extract an estimate of muscle activation level, and use that as the basis for a correlated output.

The project focused on the full analogue signal-processing chain:
- **electrode-based sEMG acquisition**
- **pre-amplification**
- **filtering**
- **active rectification**
- **mean absolute value (MAV) extraction using an integrator**
- and preparation of the signal for downstream control / HMI output. :contentReference[oaicite:3]{index=3}

## Project Context
This project was completed for **Scenario W: Bio-signal based human-machine interface (HMI)** in the UCL Department of Electronic and Electrical Engineering. The brief required the design of a prototype in which a bio-signal produced an audio-visual output or actuated some form of movement correlated with the measured signal. The recommended starting point was a **single-channel sEMG-based system**. :contentReference[oaicite:4]{index=4}

The scenario brief also provided the expected system architecture:
- **Electrodes**
- **Pre-amplification**
- **Analogue signal conditioning**
- **ADC**
- **Control**
- **Correlated output**. :contentReference[oaicite:5]{index=5}

This gives the project a strong systems-engineering structure rather than being only an isolated circuit exercise.

## My Contribution
My contribution focused on the **analogue signal conditioning chain**, particularly the circuitry needed to turn raw sEMG into a more stable and interpretable amplitude estimate. This included work on:
- the **pre-amplification / front-end signal path**
- **active rectification**
- **MAV extraction using an integrator**
- and selecting component values so the processed signal matched the expected muscle activation dynamics.

In particular, the integrator was designed around a target corner frequency of approximately **2 Hz**, aligning with the intended rate of muscle flexion and relaxation rather than the much higher raw EMG carrier frequencies. 

## Background: Why sEMG?
The project is based on **surface electromyography (sEMG)**, which the briefing describes as a signal correlated with muscle activity and caused by the electrical activity of muscle fibres. Because these signals can be recorded on the skin surface, they are suitable for wearable or non-invasive human-machine interfaces. :contentReference[oaicite:7]{index=7}

The reference thesis you uploaded reinforces the practical importance of this idea. It describes how EMG can be used to interpret muscle activation and drive assistive robotic or orthotic systems, and explains the need for correct electrode placement, amplification, filtering, rectification, and feature extraction before useful control decisions can be made. :contentReference[oaicite:8]{index=8}

## System Architecture
The overall system followed the signal chain recommended in the briefing:

1. **surface electrodes** capture the differential muscle signal  
2. **pre-amplification** boosts the weak biopotential  
3. **analogue conditioning** removes unwanted noise and converts the signal into a more useful form  
4. **ADC and control** can then map the processed signal to a meaningful output. :contentReference[oaicite:9]{index=9}

This is a strong portfolio point because it shows understanding of how a weak, noisy biological signal must be progressively transformed before it can become a usable HMI input.

## Electrode Placement and Signal Acquisition
The thesis reference explains that EMG signals are low-amplitude, millivolt-level signals and are very sensitive to:
- motion artefacts
- electromagnetic interference
- and poor electrode placement. It also notes that correct muscle selection and electrode positioning are essential if the acquired signal is to be meaningful. :contentReference[oaicite:10]{index=10}

This is directly relevant to your project, because any success in later analogue stages depends heavily on the quality of the initial differential acquisition.

## Pre-Amplification
The Scenario W briefing recommends an **instrumentation amplifier** style front end with:
- **differential input**
- **high input impedance**
- and experimentally determined gain. :contentReference[oaicite:11]{index=11}

That is exactly the right design philosophy for sEMG, because the signal is weak and should be amplified without excessively loading the electrodes. The pre-amplification stage is therefore one of the most critical blocks in the signal chain.

## Analogue Filtering
The briefing states that sEMG is band-limited to roughly **10 Hz to 500 Hz**, and notes that filtering is needed to reject out-of-band content and residual interference such as **50 Hz mains contamination**, which may remain even with differential recording. :contentReference[oaicite:12]{index=12}

The thesis reference supports this by describing common EMG processing using:
- high-pass filtering
- low-pass filtering
- and notch filtering,

with the goal of reducing motion artefacts, line noise, and equipment noise before classification or control. :contentReference[oaicite:13]{index=13}

This makes filtering a central engineering part of the project, not just an optional refinement.

## Active Rectification
A key step in extracting the amplitude envelope of EMG is taking the absolute value of the signal. The Scenario W briefing explicitly recommends using a **rectifier** before the integrator when computing **MAV**. :contentReference[oaicite:14]{index=14}

The “Active Rectifiers” reference you uploaded is highly relevant here. It explains:
- ideal diode concepts using op-amps
- faster half-wave rectifiers
- two-stage rectifiers
- and active full-wave rectifiers,

all of which avoid the limitations of a simple passive diode rectifier, especially the approximately **0.6 V diode drop** that would be unacceptable for small bio-signals. :contentReference[oaicite:15]{index=15}

This is an excellent portfolio point because it shows proper analogue reasoning: for low-level EMG, a standard diode rectifier is not enough, so an **active rectifier** is the correct design choice.

## MAV Extraction Using an Integrator
One of the most important design decisions in this project is the integrator used to estimate the **mean absolute value (MAV)** of the rectified EMG signal. The Scenario W brief explains that MAV is a good analogue estimate of muscle activation level, and that the integrator corner frequency should be based on the speed of muscle activation and relaxation, approximately **1–2 Hz**, rather than the raw EMG frequency band. :contentReference[oaicite:16]{index=16}

Your uploaded integrator design shows:
- **R1 = 80 kΩ**
- **C = 1 µF**
- **R2 = 80.429 kΩ**

with a calculated cutoff near **2 Hz**. :contentReference[oaicite:17]{index=17}

This is a strong design choice because it demonstrates that the circuit was tuned to the **envelope dynamics** of muscle activity rather than to the raw carrier-like EMG waveform itself.

## Relation to Real EMG Systems
The uploaded thesis gives a useful reference point for how these ideas are used in more complete systems. It describes a practical EMG-controlled orthotic robotic arm in which:
- raw EMG is amplified
- filtered
- rectified
- and then features such as **MAV**, **RMS**, **variance**, and **standard deviation** are calculated to classify motion states. :contentReference[oaicite:18]{index=18}

It also reports that rectified and averaged signals were clearer than raw EMG for distinguishing movement states, which supports the logic of your own analogue conditioning approach. :contentReference[oaicite:19]{index=19}

## Why This Project Matters
This project is valuable because it demonstrates the difficult middle ground between electronics and bioengineering:

- the signal is real, weak, and noisy
- the front-end must respect biological measurement constraints
- analogue processing must be designed around both circuit theory and physiology
- and the final signal must be stable enough to drive a control decision.

That combination makes this much stronger than a standard op-amp lab exercise.

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **bio-signal acquisition concepts**
- **differential measurement for low-level analogue signals**
- **instrumentation-style pre-amplification**
- **analogue filtering**
- **active rectifier design**
- **envelope / MAV extraction**
- **frequency-response-based component selection**
- **op-amp analogue design**
- **signal-chain thinking for human-machine interfaces**
- **linking physiological signal properties to circuit behaviour**. 

## What I Learned
This project significantly strengthened my understanding of how difficult real biological signals are to work with compared with ideal textbook inputs. In particular, it showed me that useful sEMG control depends on the entire signal chain being designed carefully: weak differential acquisition, noise rejection, rectification, smoothing, and time-constant selection all matter. It also reinforced the importance of matching the circuit dynamics to the behaviour of the human body, not just to the frequency content of the raw signal. 

## Repository Contents
- `README.md` – project summary
- `references/` – background papers
- `design/` – integrator design and analogue stage screenshots
- `simulations/` – Multisim / circuit simulation files
- `planning/` – gantt chart and project planning material

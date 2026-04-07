# Real-Time Audio Descrambler Using FPGA

## Overview
This project involved the design and implementation of a **real-time digital audio descrambler** using an **FPGA**. The aim was to recover the contents of a scrambled voice message by analysing the scrambling method in MATLAB and then implementing the corresponding descrambling chain in hardware.

The final system combined:
- **time- and frequency-domain signal analysis**
- **digital filtering**
- **frequency translation through modulation**
- **FPGA-based signal processing**
- **digital-to-analogue conversion**
- and **analogue low-pass filtering**

to reconstruct the original intelligible audio signal from a scrambled recording. 

## Project Context
This project was completed as **Scenario X: Real-Time Audio Descrambler using FPGA**. The scenario required students to analyse provided `original.wav` and `scrambled.wav` files, determine how the scrambling had been performed, and then implement a real-time hardware descrambler using the **DE0 Nano FPGA** and supporting external circuitry. :contentReference[oaicite:3]{index=3}

The briefing also required:
- examination of the signals in both **time** and **frequency** domains
- design of appropriate **digital filters**
- and implementation of supporting **analogue circuitry**, including a DAC output stage and analogue filtering. :contentReference[oaicite:4]{index=4}

## My Contribution
This was a group project, and the uploaded presentation identifies the team members. My contribution focused on the **signal-processing strategy and system implementation reasoning**, including the descrambling chain, filtering concept, and hardware flow from ADC through FPGA processing to DAC and analogue reconstruction.

The project demonstrates my ability to combine DSP reasoning with real hardware constraints, especially when translating a MATLAB signal-processing idea into an FPGA-compatible real-time design. :contentReference[oaicite:5]{index=5}

## The Scrambling Method
The uploaded “How to descramble” notes explain the scrambling process clearly:
- the original audio spectrum was **flipped around 3.5 kHz**
- and an additional **8 kHz sine tone** was added.  
The flipped spectrum itself was produced using **single-sideband modulation** with a **7 kHz sine wave**, followed by selection of the **lower sideband**. :contentReference[oaicite:6]{index=6}

This is what made the message unintelligible: the useful speech spectrum was inverted, and a strong narrowband tone was also inserted.

## Descrambling Strategy
The same notes define the correct recovery process:

1. **Remove the 8 kHz tone** using a digital **band-stop / notch filter**
2. **Multiply the filtered signal by a 7 kHz sine wave**
3. Use a **low-pass filter** to reject the unwanted upper sideband and keep the desired lower-frequency output, which corresponds to the original message. :contentReference[oaicite:7]{index=7}

This is a strong engineering point because it shows a clear understanding of the relationship between:
- time-domain multiplication
- frequency-domain translation
- and sideband generation/removal.

## MATLAB Analysis and Algorithm Development
The uploaded MATLAB script shows the workflow used to analyse and reconstruct the signal. It:
- reads the original and scrambled WAV files
- plots the signals in the **time domain**
- computes **FFT-based frequency spectra**
- designs an **8 kHz band-stop filter**
- generates a **7 kHz sine wave**
- multiplies the filtered signal by that sine wave
- applies a **low-pass filter**
- and then compares the scrambled and descrambled spectra. :contentReference[oaicite:8]{index=8}

That is a particularly strong part of the project because it demonstrates a full DSP prototyping pipeline:
- analyse first in software
- validate the recovery method
- then move towards real-time hardware implementation.

## Digital Band-Stop Filter
The group presentation states that the scrambled signal had its highest power at **8 kHz**, and that an **8 kHz digital band-stop filter** was therefore designed in MATLAB using `filterDesigner`. The team chose an **FIR band-stop filter** because of its stability, even though it uses more FPGA resources than an IIR design. :contentReference[oaicite:9]{index=9}

That is a good design trade-off for FPGA work:
- FIR filters are typically easier to reason about
- have guaranteed stability
- and are often preferred when predictability matters more than minimal resource usage.

## 7 kHz Sine-Wave Modulation
After tone removal, the descrambling process required multiplication by a **7 kHz sine wave**. The group presentation explains this correctly in terms of time- and frequency-domain behaviour:
- in the time domain, the signal is amplitude-modulated by the carrier
- in the frequency domain, this creates shifted components / sidebands
- and the low-pass filter then selects the desired portion. :contentReference[oaicite:10]{index=10}

The uploaded Verilog module `SineWaveGenerator` also shows how a **12-bit sine wave** was generated in hardware using:
- a **phase accumulator**
- and a **lookup table** with 1024 entries. :contentReference[oaicite:11]{index=11}

This is a very good portfolio point because it shows that the design was not only conceptual — the carrier-generation block itself was implemented in HDL form.

## DAC and Mixed-Signal Output
The Scenario X notes explain that after digital processing, the signal must be converted back to analogue form, and recommend an **R-2R ladder DAC**. They also discuss two DAC topologies with an op-amp, noting that one is safer because it avoids feeding a potentially harmful op-amp output back into FPGA pins. :contentReference[oaicite:12]{index=12}

The group presentation confirms that the design used an **R-2R ladder DAC** and emphasises the importance of the safer buffered configuration. That is another strong practical engineering detail: it shows awareness of protecting the FPGA as well as simply obtaining an output signal. :contentReference[oaicite:13]{index=13}

## Analogue Low-Pass Filter
After modulation and DAC conversion, an external **low-pass filter** was required to:
- remove the unwanted upper sideband
- keep the lower-frequency descrambled output
- and also serve as an **anti-aliasing / smoothing stage** after the DAC. :contentReference[oaicite:14]{index=14}

The group presentation states that the low-pass filter was designed with a cutoff of approximately **5 kHz**, using an online active-filter design tool, and notes the practical trade-off that improving attenuation by increasing slope would require more cascaded stages and more breadboard space. :contentReference[oaicite:15]{index=15}

That is a very good design reflection because it shows awareness of implementation constraints, not just ideal filter theory.

## FPGA System Design
The briefing explains that the DE0 Nano board is digital-only, so the system needed:
- an **ADC interface** for capturing analogue audio
- internal digital processing in Verilog / FPGA logic
- and a **DAC** to return to analogue output. It also mentions example FPGA projects for DAC ramp generation and ADC digitisation, including SPI-based ADC communication. :contentReference[oaicite:16]{index=16}

Your project therefore sits at the boundary of:
- FPGA design
- DSP
- and real-world mixed-signal interfacing.

That combination is especially strong for embedded and digital-hardware roles.

## Why This Project Matters
This project is valuable because it demonstrates a full signal-processing workflow from theory to hardware:

- identifying the scrambling method from spectral analysis
- deriving the inverse processing chain
- implementing filtering and modulation digitally
- generating a carrier in hardware
- interfacing digital logic with external ADC/DAC hardware
- and reconstructing a usable analogue audio output.

That is much stronger than a project that only simulates DSP in MATLAB.

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **digital signal processing**
- **FFT-based frequency-domain analysis**
- **MATLAB audio analysis**
- **filter design**
- **FIR band-stop filtering**
- **modulation and frequency translation**
- **Verilog / FPGA design**
- **lookup-table sine generation**
- **mixed-signal interfacing**
- **R-2R DAC design**
- **analogue active-filter design**
- **translating software signal-processing ideas into real-time hardware**. 

## What I Learned
This project significantly strengthened my understanding of how DSP concepts behave in real systems. In particular, it showed me that recovering a signal is not only about identifying the correct maths, but also about implementing that strategy within hardware constraints such as sampling rate, FPGA resources, DAC reconstruction, and analogue filtering. It also reinforced the importance of analysing a system in both time and frequency domains before committing to a hardware architecture. 

## Repository Contents
- `README.md` – project summary
- `matlab/` – MATLAB scripts for analysis and prototyping
- `presentation/` – project presentation

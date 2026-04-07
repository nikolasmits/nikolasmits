# Communication Systems Lab: Baseband Digital Transmission in MATLAB

## Overview
This project focused on the implementation and simulation of the basic building blocks of a **baseband digital communication system** in MATLAB. The laboratory was centred on understanding how information bits are converted into symbols, how symbols are represented in different signalling schemes, and how communication performance is affected by noise in an additive white Gaussian noise (AWGN) channel.

The work was based on three signalling schemes:
- **binary unipolar**
- **binary polar**
- **quaternary**

and explored how their different alphabets influence symbol mapping, constellation spacing, and error performance. :contentReference[oaicite:2]{index=2}

## Project Context
This was completed for **ELEC0020 – Photonics and Communication Systems**, in the **Communication Systems Laboratory**. The lab learning objectives were to:
- implement key functions in a **digital transmitter**, especially the **mapper**
- implement key functions in a **digital receiver**, especially the **demodulator**
- and simulate the behaviour of different signalling schemes in a noisy communication channel. :contentReference[oaicite:3]{index=3}

The communication system model described in the lab brief consisted of three main blocks:
1. a **digital transmitter** with mapper and modulator
2. an **AWGN channel**
3. a **digital receiver** with demodulator and demapper. :contentReference[oaicite:4]{index=4}

## My Contribution
This project appears to be an individual MATLAB laboratory exercise. From the uploaded files, my contribution clearly included implementing the **mapping stage** of the transmitter and testing the conversion of random bit streams into symbol streams for multiple signalling alphabets.

The uploaded MATLAB scripts show work on:
- defining signal alphabets
- generating random bit streams
- reshaping bits into symbol groups
- converting grouped bits into decimal symbol indices
- and mapping them onto the corresponding amplitudes for binary unipolar, binary polar, and quaternary signalling. 

## Communication System Model
The laboratory brief defines the communication model using MATLAB simulation parameters such as:
- sampling period `Tsampling`
- sampling frequency `fsampling`
- bit period `Tb`
- symbol period `Ts`
- number of bits and symbols
- and the one-sided noise spectral density `N0`. :contentReference[oaicite:6]{index=6}

The overall process described in the brief is:
- generate transmitted bits
- map them to symbols
- modulate them into a waveform
- add AWGN
- demodulate the received waveform
- and demap the resulting symbols back into bits. :contentReference[oaicite:7]{index=7}

This makes the lab a good introduction to the full digital communication chain rather than a standalone coding exercise.

## Signalling Schemes Studied
The lab brief defines the three signalling alphabets as:
- **Binary unipolar:** \(A = \{0,1\}\)
- **Binary polar:** \(A = \{-1,1\}\)
- **Quaternary:** \(A = \{-3,-1,1,3\}\). :contentReference[oaicite:8]{index=8}

These schemes differ in how many bits are represented per symbol and in how much separation there is between symbol amplitudes. That makes them ideal for comparing trade-offs between spectral efficiency and noise robustness.

## Mapper Implementation
The strongest evidence from the uploaded files is the MATLAB implementation of the **mapper**. The scripts:
- define the three alphabets
- generate a random bit stream
- reshape the bit stream into groups of size \(\log_2(M)\)
- convert each bit group into a decimal index using `bi2de`
- and assign the corresponding symbol from the chosen alphabet. 

This is a key communications concept because the mapper forms the interface between raw binary data and the symbol-level representation used for transmission.

The use of `reshape` is especially relevant for quaternary signalling, where two bits must be grouped into one symbol. That reflects an important communications idea: the number of bits per symbol depends on the size of the alphabet.

## Relation to the Lab Specification
The mapper implementation closely follows the algorithm given in the lab brief, which specifies that the function should:
- accept `tx_bits` and `alphabet`
- initialise `tx_symbols`
- reshape the bit stream into a matrix of size  
  **number of symbols × bits per symbol**
- and use the decimal value of each bit group to select the correct symbol from the alphabet. :contentReference[oaicite:10]{index=10}

That makes this a good example of converting an algorithmic specification into functioning MATLAB code.

## Digital Modulation and Receiver Context
Although the uploaded MATLAB files mainly show the mapper stage, the laboratory itself also covered:
- **baseband modulation** using rectangular pulses
- **demodulation** using a matched rectangular pulse structure
- **demapping**
- constellation diagrams
- and bit-error probability versus \(E_b/N_0\). :contentReference[oaicite:11]{index=11}

This broader context is important because it shows the mapper was not an isolated function; it was intended as one part of a full end-to-end communication model.

## Comparison of Signalling Schemes
A central theme of the lab was comparing binary unipolar, binary polar, and quaternary transmission under the same \(E_b/N_0\). The brief explicitly notes that comparisons should be made on equal grounds and gives the expressions for the average energy per bit for each scheme. :contentReference[oaicite:12]{index=12}

This is a strong conceptual point because it highlights a real communications engineering issue: different alphabets may look superficially better or worse, but fair comparison requires normalising the energy per bit.

## Why This Project Matters
This project is valuable because it shows understanding of the most fundamental layer of digital communication:
- how binary information is grouped
- how it is mapped into symbol alphabets
- how signalling choices affect system behaviour
- and how a communication system can be represented and tested computationally.

Even though the uploaded code is focused on the mapper, that stage is one of the essential building blocks in any digital transmitter.

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **MATLAB programming**
- **digital communications modelling**
- **bit-to-symbol mapping**
- **binary and M-ary signalling concepts**
- **baseband transmission understanding**
- **communication-system block modelling**
- **algorithm implementation from lab specification**
- **interpreting signalling alphabets and symbol structure**
- **relating mathematical communication concepts to simulation code**. 

## What I Learned
This project strengthened my understanding of the relationship between bits, symbols, and signalling schemes in digital communication systems. In particular, it showed me that even the mapper stage requires careful treatment of alphabet size, bit grouping, and symbol indexing. It also reinforced how communication theory is implemented in practice through simulation, where transmitter, channel, and receiver blocks can be modelled explicitly and compared under noise. :contentReference[oaicite:14]{index=14}

## Repository Contents
- `README.md` – project summary
- `code/` – MATLAB scripts for mapper implementation and signalling exploration

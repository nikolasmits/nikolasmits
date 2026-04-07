# Single-Cycle RISC-V CPU in SystemVerilog

## Overview
This project involved the design, completion, and simulation of a **single-cycle RISC-V central processing unit (CPU)** in **SystemVerilog**. The processor was based on a simplified **RV32I subset**, and the work included both digital hardware design and low-level assembly programming.

The project covered:
- completion of key processor submodules in SystemVerilog
- simulation and verification of individual blocks using testbenches
- integration of the full top-level CPU
- execution of machine-code programs through instruction memory
- and development of RISC-V assembly programs to test processor functionality.

This project demonstrates practical understanding of computer architecture, HDL-based hardware design, instruction decoding, ALU control, program flow, and processor verification. 

## Project Context
This was completed for **ELEC0028 Advanced Digital Design**. The coursework required students to implement and simulate a **single-cycle-per-instruction RISC-V CPU**, based on the provided microarchitecture and ALU diagrams. The supported instructions were a subset of **RV32I**, including:

- arithmetic and logic operations such as `add`, `sub`, `or`, `and`, `sll`, `srl`, `slt`
- immediate versions such as `addi`, `ori`, `andi`, `slli`, `srli`, `slti`
- memory operations `lw` and `sw`
- branch instructions `beq`, `bne`, `blt`, `bge`
- and jump / upper-immediate instructions `jal`, `jalr`, `lui`. :contentReference[oaicite:3]{index=3}

The brief also required sub-block implementation, testbench-based simulation, full CPU integration, and assembly programming tasks such as:
- counting the number of 1s in an input byte
- and multiplying two bytes using shift-and-add. :contentReference[oaicite:4]{index=4}

## My Contribution
This project appears to be an individual coursework submission, and the uploaded report presents the work as your own implementation. My contribution included:
- completing the missing SystemVerilog modules for the processor
- defining and validating control signals
- implementing the immediate extension logic
- implementing the ALU behaviour
- integrating the top-level `risc_v` CPU
- writing and running testbenches
- and writing RISC-V assembly test programs to verify correct processor operation. :contentReference[oaicite:5]{index=5}

## CPU Architecture
The provided coursework architecture is a **single-cycle RISC-V microarchitecture**, meaning each instruction is executed in one clock cycle rather than being pipelined. The processor datapath includes:
- program counter logic
- instruction memory
- control unit
- register file
- immediate extension unit
- ALU
- and data memory with memory-mapped I/O. :contentReference[oaicite:6]{index=6}

The coursework brief explicitly maps the required sub-blocks to SystemVerilog module names:
- `program_counter`
- `instruction_memory`
- `control_unit`
- `reg_file`
- `extend`
- `alu`
- `data_memory_and_io`. :contentReference[oaicite:7]{index=7}

This is a strong project because it required understanding how all these modules interact at system level, not just how each works individually.

## Control Logic and Instruction Decoding
One of the core parts of the CPU was the **control unit**, which generates control signals such as:
- `PCSrc`
- `ResultSrc`
- `MemWrite`
- `ALUSrc`
- `RegWrite`
- `ALUControl`
- and `ImmSrc`. :contentReference[oaicite:8]{index=8}

The report includes a completed control-signal table for all supported instructions, showing how the CPU distinguishes between R-type, I-type, memory, branch, and jump operations. That is a particularly strong part of the project because it reflects a real understanding of how instruction format, opcode, `funct3`, and `funct7` fields map into hardware control behaviour. :contentReference[oaicite:9]{index=9}

## Immediate Extension Unit
The `extend` module sign-extends or constructs immediates for different instruction formats:
- I-type
- S-type
- B-type
- U-type
- J-type. 

The report explains and tests how immediate bits are assembled from instruction fields for each format. This is a good portfolio point because immediate handling is one of the areas where ISA understanding and hardware implementation meet directly.

## ALU Design
The ALU implementation supports:
- addition and subtraction
- logical operations
- shifts
- and set-less-than behaviour.

The uploaded report shows that the ALU uses a compact control structure where bits of `ALUControl` determine:
- arithmetic mode
- logic mode
- shift direction
- and the final operation selection. The ALU testbench then verifies each class of operation with specific inputs and expected outputs. :contentReference[oaicite:11]{index=11}

This is a strong example of translating an architectural block diagram into real HDL logic and then validating it properly.

## Program Counter and Program Flow
The `program_counter` module handles:
- normal sequential execution via `PC + 4`
- branch targets
- and jump behaviour. :contentReference[oaicite:12]{index=12}

The coursework brief also explains that:
- the PC resets to `0x00000000`
- instruction memory is byte-addressable
- data memory is byte-addressable
- and memory-mapped I/O is used for interaction between CPU and external input/output. :contentReference[oaicite:13]{index=13}

This memory-mapped I/O feature is important because it lets the CPU communicate with `CPUIn` and `CPUOut` through specific addresses, making the processor testable in simulation.

## Top-Level CPU Integration
After completing the submodules, the full `risc_v` top-level module was built by interconnecting:
- instruction fetch
- register-file reads
- immediate generation
- ALU execution
- data memory / I/O access
- write-back selection
- and PC update logic. :contentReference[oaicite:14]{index=14}

The report shows that:
- branch targets and jump targets were computed
- `ResultSrc` selected between immediate, ALU result, data memory, and `PC + 4`
- and the full CPU was exercised in simulation through a dedicated `risc_v_tb`. :contentReference[oaicite:15]{index=15}

That full integration step is one of the strongest parts of the project, because it turns separate modules into a functioning processor.

## Verification with Testbenches
A major strength of this project is the use of **testbenches** to verify individual blocks and the full CPU. The report includes dedicated simulation sections for:
- program counter
- extend
- control unit
- ALU
- and the complete `risc_v` processor. :contentReference[oaicite:16]{index=16}

The simulations were evaluated in:
- terminal text output
- and waveform form using **GTKWave**. 

This is a strong portfolio point because it shows structured verification, not just coding.

## Running a CPU Test Program
The coursework required running a machine-code test program that exercised the supported instruction set. The uploaded test-program file includes operations to test:
- `addi`
- `add`
- `sub`
- `or`
- `sll`
- `slt`
- `andi`
- `srli`
- `slti`
- `lw`
- `beq`
- `bne`
- `blt`
- `bge`
- `jal`
- and `jalr`. :contentReference[oaicite:18]{index=18}

The report’s simulation results show that the processor stepped through these instructions and updated `CPUOut` via memory-mapped I/O at the correct stages, confirming functional operation of the implemented CPU. :contentReference[oaicite:19]{index=19}

## Assembly Programming Tasks
The project also included writing RISC-V assembly programs, which is a major strength because it links ISA-level software with the custom hardware.

### Program 1: Count the number of 1s in an input byte
The coursework required an assembly program that:
- reads `CPUIn`
- counts the number of 1 bits in the least significant byte
- and writes the result to `CPUOut`. :contentReference[oaicite:20]{index=20}

You uploaded the machine-code listing for this program, showing that the task was implemented and prepared for processor simulation. :contentReference[oaicite:21]{index=21}

### Program 2: Multiply two bytes using shift-and-add
The second assembly task required implementing multiplication in software using the shift-and-add algorithm, since the chosen RV32I subset does not include a dedicated multiply instruction. :contentReference[oaicite:22]{index=22}

You also uploaded the machine-code listing for this multiplication program, which shows the shift, test, and accumulate structure expected from the algorithm. :contentReference[oaicite:23]{index=23}

This is particularly strong for your portfolio because it shows understanding of both:
- hardware datapath constraints
- and low-level algorithm implementation on a simple processor.

## Why This Project Matters
This project is valuable because it demonstrates real digital systems thinking at multiple levels:

- **ISA level**: understanding instruction formats and assembly behaviour
- **microarchitecture level**: building datapath and control
- **HDL level**: writing SystemVerilog modules
- **verification level**: designing testbenches and checking waveforms
- **software/hardware interaction**: running assembly code on your own CPU design

That combination is exactly what makes it relevant for digital design, FPGA, processor, and computer architecture roles.

## Engineering Skills Demonstrated
This project demonstrates skills in:
- **SystemVerilog hardware design**
- **digital logic and computer architecture**
- **RISC-V instruction set understanding**
- **control-unit design**
- **ALU implementation**
- **immediate decoding and instruction-format handling**
- **processor integration**
- **testbench development**
- **waveform-based verification**
- **assembly programming**
- **hardware/software co-design thinking**. 

## What I Learned
This project significantly strengthened my understanding of how a processor actually works beyond the textbook block diagram. In particular, it showed me how instruction formats, control signals, register transfers, ALU behaviour, and program flow all have to align precisely for correct execution. It also reinforced the importance of verification: even relatively small HDL modules need structured testbenches and careful simulation before they can be trusted as part of a working CPU. 

## Repository Contents
- `README.md` – project summary
- `report/` – final coursework write-up
- `rtl/` – SystemVerilog modules
- `tb/` – testbenches
- `programs/` – assembly / machine-code test programs

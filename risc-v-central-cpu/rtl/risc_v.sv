`include "instruction_memory.sv"
`include "reg_file.sv"
`include "extend.sv"
`include "alu.sv"
`include "data_memory_and_io.sv"
`include "program_counter.sv"
`include "control_unit.sv"

module risc_v(output logic [31:0] CPUOut,
                input logic [31:0] CPUIn,
                input logic Reset, CLK);

    logic [31:0] Instr, WD3, RD1, RD2, SrcA, SrcB, ALUResult, WD, RD, A, Result, ImmExt, PCTarget, PCNext, PC, PCPlus4;
    logic [31:0] BranchTarget, JalTarget, JalrTarget;
    logic [4:0] A1, A2, A3;
    logic MemWrite, ALUSrc, RegWrite;
    logic Zero, Negative;
    logic [4:0] ALUControl;
    logic [2:0] ImmSrc;
    logic [1:0] ResultSrc;
    logic [1:0] PCSrc;
    logic WE3, WE;

    assign BranchTarget = PC + ImmExt;
    assign JalTarget = PC + ImmExt;
    assign JalrTarget = ALUResult;

    assign PCTarget = (PCSrc == 2'b01) ? BranchTarget :
                      (PCSrc == 2'b10) ?
                      ((Instr[6:0] == 7'b1101111) ? JalTarget : 
                       (Instr[6:0] == 7'b1100111) ? JalrTarget : 32'hXXXXXXXX)
                  : 32'hXXXXXXXX;

    program_counter PC_module(PC, PCPlus4, PCTarget, ALUResult, PCSrc, Reset, CLK);

    instruction_memory IM_module(Instr, PC);

    control_unit CU_module(PCSrc, ResultSrc, MemWrite, ALUSrc, RegWrite, ALUControl, ImmSrc, Instr, Zero, Negative);

    assign A1 = Instr[19:15];
    assign A2 = Instr[24:20];
    assign A3 = Instr[11:7];

    assign WE3 = RegWrite;

    reg_file RF_module(RD1, RD2, WD3, A1, A2, A3, WE3, CLK);

    extend EXT_module(ImmExt, Instr, ImmSrc);

    assign SrcA = RD1;
    assign SrcB = (ALUSrc) ? ImmExt : RD2;

    alu ALU_module(ALUResult, Zero, Negative, SrcA, SrcB, ALUControl);

    assign A = ALUResult;
    assign WD = RD2;
    assign WE = MemWrite;

    data_memory_and_io DM_module(RD, CPUOut, A, WD, CPUIn, WE, CLK);

    assign Result = (ResultSrc == 2'b00) ? ImmExt :
                    (ResultSrc == 2'b01) ? ALUResult :
                    (ResultSrc == 2'b10) ? RD :
                    PCPlus4;

    assign WD3 = Result;

endmodule
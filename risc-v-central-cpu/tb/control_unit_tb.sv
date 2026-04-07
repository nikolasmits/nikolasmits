`timescale 1ns/1ps
`include "control_unit.sv"

module control_unit_tb;
    logic [1:0] PCSrc;
    logic [1:0] ResultSrc;
    logic MemWrite, ALUSrc, RegWrite;
    logic [4:0] ALUControl;
    logic [2:0] ImmSrc;
    logic [31:0] Instr;
    logic Zero, Negative;

    control_unit dut(PCSrc, ResultSrc, MemWrite, ALUSrc, RegWrite, ALUControl, ImmSrc, Instr, Zero, Negative);

    initial begin
        $dumpfile("control_unit_tb.vcd");
        $dumpvars(0, control_unit_tb);

        Zero = 0;
        Negative = 0;

        Instr = 32'b000000000100_00000_111_00001_0010011;
        #10;

        Instr = 32'b0000000_00011_00010_010_00101_0100011;
        #10;

        Instr = 32'b0000000_00000_00001_000_01000_0110011;
        Zero = 1;
        Negative = 0;
        #10;

        Instr = 32'b1111111_00000_00000_000_1111_1_1100011;
        Zero = 0;
        Negative = 1;
        #10;

        Instr = 32'b11111111111111111111_00000_0110111;
        Zero = 0;
        Negative = 0;
        #10;

        Instr = 32'b0_0000000001_0_00000000_00101_1101111;
        Zero = 0;
        Negative = 0;
        #100;
        $finish;
    end

    initial begin
        $monitor("Time = %3d | Instr = %h | PCSrc = %b | ResultSrc = %b | MemWrite = %b | ALUSrc = %b | RegWrite = %b | ALUControl = %b | ImmSrc = %b", $time, Instr, PCSrc, ResultSrc, MemWrite, ALUSrc, RegWrite, ALUControl, ImmSrc);
    end
endmodule
        
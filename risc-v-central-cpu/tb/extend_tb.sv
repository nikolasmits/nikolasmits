`timescale 1ns/1ps
`include "extend.sv"

module extend_tb;
    logic [31:0] ImmExt;
    logic [31:0] Instr;
    logic [2:0] ImmSrc;

    extend dut(ImmExt, Instr, ImmSrc);

    initial begin
        $dumpfile("extend_tb.vcd");
        $dumpvars(0, extend_tb);

        Instr = 32'h00400093;
        ImmSrc = 3'b000;
        #10;

        Instr = 32'h005FA223;
        ImmSrc = 3'b001;
        #10;

        Instr = 32'h01C30463;
        ImmSrc = 3'b010;
        #10;

        Instr = 32'h80000FB7;
        ImmSrc = 3'b011;
        #10;

        Instr = 32'h0080006F;
        ImmSrc = 32'b100;
        #40;
        $finish;
    end

    initial begin
        $monitor("Time = %3d | Instr = %h | ImmSrc = %b | ImmExt = %h", $time, Instr, ImmSrc, ImmExt);
    end

endmodule
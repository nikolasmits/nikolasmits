`timescale 1ns/1ps
`include "program_counter.sv"

module program_counter_tb;

    logic [31:0] PC, PCPlus4;
    logic [31:0] PCTarget, ALUResult;
    logic [1:0] PCSrc;
    logic Reset, CLK;

    program_counter dut( PC, PCPlus4, PCTarget, ALUResult, PCSrc, Reset, CLK);

    always #5 CLK = ~CLK;

    initial begin
        $dumpfile("program_counter_tb.vcd");
        $dumpvars(0, program_counter_tb);

        CLK = 0;
        Reset = 1;
        PCSrc = 2'b00;
        PCTarget = 32'h00000020;

        #10 Reset = 0;

        #10 PCSrc = 2'b00;

        #10 PCSrc = 2'b01;

        #10 PCSrc = 2'b11;

        #10 PCSrc = 2'b10;
    end

    initial begin
        $monitor("Time = %3d | Reset = %b | PCSrc = %b | PCTarget = %h | PC = %h \n", $time, Reset, PCSrc, PCTarget, PC);
    end

endmodule
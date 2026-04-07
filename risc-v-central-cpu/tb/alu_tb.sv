`timescale 1ns/1ps
`include "alu.sv"

module alu_tb;
    logic signed [31:0] ALUResult;
    logic Zero, Negative;
    logic signed [31:0] SrcA, SrcB;
    logic [4:0] ALUControl;

    alu dut (ALUResult, Zero, Negative, SrcA, SrcB, ALUControl);

    initial begin
        $dumpfile("alu_tb.vcd");
        $dumpvars(0, alu_tb);

        SrcA = 32'd5;
        SrcB = 32'd5;
        ALUControl = 5'b00010;
        #10;

        SrcA = 32'd5;
        SrcB = 32'd5;
        ALUControl = 5'b01010;
        #10;

        SrcA = 32'hF0F0F0F0;
        SrcB = 32'h0F0F0F0F;
        ALUControl = 5'b00011;
        #10;

        SrcA = 32'hF0F0F0F0;
        SrcB = 32'h0F0F0F0F;
        ALUControl = 5'b00111;
        #10;

        SrcA = 32'd4;
        SrcB = 32'd2;
        ALUControl = 5'b00000;
        #10;

        SrcA = 32'd4;
        SrcB = 32'd2;
        ALUControl = 5'b10000;
        #10;

        SrcA = 32'd5;
        SrcB = 32'd10;
        ALUControl = 5'b01001;
        #40;
        $finish;
    end

    initial begin
        $monitor("Time = %3d | SrcA = %h | SrcB = %h | Zero = %b | Negative = %b | ALUControl = %h | ALUResult = %h \n", $time, SrcA, SrcB, Zero, Negative, ALUControl, ALUResult);
    end
endmodule
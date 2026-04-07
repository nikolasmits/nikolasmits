`timescale 1ns/1ps
`include "risc_v.sv"

module risc_v_tb;
    logic [31:0] CPUOut, CPUIn;
    logic Reset, CLK;

    risc_v dut(CPUOut, CPUIn, Reset, CLK);

    initial begin // Generate clock signal with 20 ns period
        CLK = 0;
        forever #10 CLK = ~CLK;
    end

    initial begin // Apply stimulus
        $dumpfile("risc_v_tb.vcd");
        $dumpvars(0, risc_v_tb);

        Reset = 1;    // Initial reset
        CPUIn = 32'd0; // Default CPUIn value
        
        #20; 
        Reset = 0;    // Deassert reset to begin execution
        
        // Simulate the external input changing (CPUIn changes when address 0x7FFFFFFC is read)
        #20 CPUIn = 32'h000000FF;
        
        #1500;
        $finish;
    end

    always @ (negedge CLK)
        $display ("t = %3d | CPUIn = %h | CPUOut = %h | Reset = %b | PCSrc = %b | PC = %h | PCTarget = %h | ImmExt = %h | Instr = %h | ALUResult = %h", $time, CPUIn, CPUOut, Reset, dut.PCSrc, dut.PC, dut.PCTarget, dut.ImmExt, dut.Instr, dut.ALUResult);

endmodule
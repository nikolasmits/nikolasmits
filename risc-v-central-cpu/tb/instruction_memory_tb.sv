`timescale 1ns/1ps
`include "instruction_memory.sv"

module instruction_memory_tb;
    logic [31:0] Instr;
    logic [31:0] Addr;

    // Instantiate the instruction memory module
    instruction_memory dut(Instr, Addr);

    initial begin
        // Apply some example addresses to read the first few words
        $dumpfile("instruction_memory_tb.vcd");
        $dumpvars(0, instruction_memory_tb);

        $display("Testing instruction memory loading...");

        // Loop over first few addresses
        for (int i = 0; i < 5; i++) begin
            Addr = i * 4;  // Byte address, increment by 4
            #5;  // Small delay
            $display("Addr = %h | Instr = %h", Addr, Instr);
        end

        $finish;
    end
endmodule

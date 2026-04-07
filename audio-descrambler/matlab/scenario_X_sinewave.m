module SineWaveGenerator (
    input wire clk,               // Clock input
    output reg signed [11:0] sine_output // Output sine wave (12-bit resolution)
);

reg signed [9:0] phase = 0;       // Phase accumulator
reg signed [11:0] sine_wave [0:1023]; // Sine wave lookup table (adjust size for accuracy)

// Initialize sine wave lookup table (one period)
initial begin
    integer i;
    for (i = 0; i < 1024; i = i + 1) begin
        sine_wave[i] = $rtoi(2047.0 * sin(2.0 * $itor(i) * 3.14159 / 1024.0)); // 12-bit resolution
    end
end

always @(posedge clk) begin
    phase <= phase + 1;         // Increment phase on each clock cycle

    // Output sine value based on phase
    sine_output <= sine_wave[phase[9:0]];
end

endmodule

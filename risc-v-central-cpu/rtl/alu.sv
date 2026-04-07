module alu (output logic signed [31:0] ALUResult,
            output logic Zero, Negative,
            input logic signed [31:0] SrcA, SrcB,
            input logic [4:0] ALUControl);

    logic signed [31:0] ArithResult;
    logic signed [31:0] LogicResult;
    logic signed [31:0] ShiftResult;
    logic signed [31:0] SLTResult;
    logic [1:0] ALUOp;

    assign ALUOp = ALUControl[1:0];

    assign ArithResult = (ALUControl[3]) ?  SrcA - SrcB : SrcA + SrcB;

    assign LogicResult = (ALUControl[2]) ? SrcA | SrcB : SrcA & SrcB;

    assign ShiftResult = (ALUControl[4]) ? SrcA >> SrcB[4:0] : SrcA << SrcB[4:0];

    assign SLTResult = (SrcA < SrcB) ? 32'b1 : 32'b0;

    always_comb begin
        case (ALUOp) 
            2'b00: ALUResult = ShiftResult;
            2'b01: ALUResult = SLTResult;
            2'b10: ALUResult = ArithResult;
            2'b11: ALUResult = LogicResult;
            default: ALUResult = 32'b0;
        endcase
    end

    assign Zero = (ALUResult == 0);

    assign Negative = (ALUOp == 2'b01) ? ALUResult[0] : 1'b0;

endmodule
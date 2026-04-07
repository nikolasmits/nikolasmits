module control_unit (output logic [1:0] PCSrc, 
                    output logic [1:0] ResultSrc,
                    output logic MemWrite, ALUSrc, RegWrite,
                    output logic [4:0] ALUControl,
                    output logic [2:0] ImmSrc,
                    input logic [31:0] Instr,
                    input logic Zero, Negative);

logic [6:0] opcode;
logic [2:0] funct3;
logic [6:0] funct7;

assign opcode = Instr[6:0];
assign funct3 = Instr[14:12];
assign funct7 = Instr[31:25];

always_comb begin
    case (opcode)
        7'b0110011: begin
            RegWrite = 1;
            ImmSrc = 3'b???;
            ALUSrc = 0;
            MemWrite = 0;
            ResultSrc = 2'b01;
            PCSrc = 2'b00;

            case (funct3)
                3'b000: ALUControl = (funct7 == 7'b0100000) ? 5'b?1?10 : 5'b?0?10;
                3'b110: ALUControl = 5'b??111;
                3'b111: ALUControl = 5'b??011;
                3'b001: ALUControl = 5'b0??00;
                3'b101: ALUControl = 5'b1??00;
                3'b010: ALUControl = 5'b?1?01;
            endcase
        end

        7'b0010011: begin
            RegWrite = 1;
            ImmSrc = 3'b000;
            ALUSrc = 1;
            MemWrite = 0;
            ResultSrc = 2'b01;
            PCSrc = 2'b00;

            case (funct3)
                3'b000: ALUControl = 5'b?0?10;
                3'b110: ALUControl = 5'b??111;
                3'b111: ALUControl = 5'b??011;
                3'b001: ALUControl = 5'b0??00;
                3'b101: ALUControl = 5'b1??00;
                3'b010: ALUControl = 5'b?1?01;
            endcase
        end

        7'b0000011: begin
            RegWrite = 1;
            ImmSrc = 3'b000;
            ALUSrc = 1;
            MemWrite = 0;
            ResultSrc = 2'b10;
            PCSrc = 2'b00;
            ALUControl = 5'b?0?10;
        end

        7'b0100011: begin
            RegWrite = 0;
            ImmSrc = 3'b001;
            ALUSrc = 1;
            MemWrite = 1;
            ResultSrc = 2'b01;
            PCSrc = 2'b00;
            ALUControl = 5'b?0?10;
        end

        7'b1100011: begin
            RegWrite = 0;
            ImmSrc = 3'b010;
            ALUSrc = 0;
            MemWrite = 0;
            ResultSrc = 2'b??;
            ALUControl = 5'b?1?10;

            case (funct3)
                3'b000: PCSrc = (Zero) ? 2'b01 : 2'b00;
                3'b001: PCSrc = (Zero) ? 2'b00 : 2'b01;
                3'b100: PCSrc = (Negative) ? 2'b01 : 2'b00;
                3'b101: PCSrc = (Negative) ? 2'b00 : 2'b01;
            
            endcase
        end

        7'b1101111: begin
            RegWrite = 1;
            ImmSrc = 3'b100;
            ALUSrc = 0;
            ALUControl = 5'b?????;
            MemWrite = 0;
            ResultSrc = 2'b11;
            PCSrc = 2'b01;
        end

        7'b1100111: begin
            RegWrite = 1;
            ImmSrc = 3'b000;
            ALUSrc = 1;
            ALUControl = 5'bX0X10;
            MemWrite = 0;
            ResultSrc = 2'b11;
            PCSrc = 2'b10;
        end

        7'b0110111: begin
            RegWrite = 1;
            ImmSrc = 3'b011;
            ALUSrc = 0;
            ALUControl = 5'b?????;
            MemWrite = 0;
            ResultSrc = 2'b00;
            PCSrc = 2'b00;
        end

    endcase

end

endmodule
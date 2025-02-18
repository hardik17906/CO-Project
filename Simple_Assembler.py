// We are making a Simple Assembler
// This will be a 32-bit Assembler
// We will use RISC-V
# We are making a Assembler 
# This will be 32-bit Assembler
# We made this using RISC V ISA

import sys   # importing sys for taking input file and name of output file as arguments from stdin

if len(sys.argv) !=3:
    print("The Format of the input should be : python <File_name>.py <input.txt> <output.bin> ")
    sys.exit( 1 )  # To exit out of the this sys

input_file=sys.argv[1]   # loading name of input txt file in input_file
output_file=sys.argv[2]  # loading name of the ouput txt file in outut_file
# Making a Dictionary having Keys as the name of the register and Values as their binary conversion
Register_map_with_their_binary_values= {"x0":"00000" }
Register_map_with_their_binary_values = { "x0": "00000", "x1": "00001", "x2": "00010", "x3": "00011", "x4": "00100", 
    "x5": "00101", "x6": "00110", "x7": "00111", "x8": "01000", "x9": "01001", 
    "x10": "01010", "x11": "01011", "x12": "01100", "x13": "01101", "x14": "01110", 
    "x15": "01111", "x16": "10000", "x17": "10001", "x18": "10010", "x19": "10011", 
    "x20": "10100", "x21": "10101", "x22": "10110", "x23": "10111", "x24": "11000", 
    "x25": "11001", "x26": "11010", "x27": "11011", "x28": "11100", "x29": "11101", 
    "x30": "11110", "x31": "11111"  }

# #  Making dictionary for Diferrent types of instructions of R types

# #  Mkaing dictionary for opcodes of different opeartions 
# Operations_map_with_their_opcode={"add":"00000"}

#  Making a list of all the given instructions in the input file 

with open(input_file,"r") as Input_file_taken:
    List_of_lines_of_input_file=Input_file_taken.readlines()

with open(output_file,"w") as Output_file_taken:

    for i in range(len(List_of_lines_of_input_file)):
        if List_of_lines_of_input_file[i].strip()=="" :
            continue
        # print(List_of_lines_of_input_file[i],end="")

        List_after_space_separated=(List_of_lines_of_input_file[i].strip()).split(" ")
        List_after_comma_separated=List_after_space_separated[1].split(",")
        List_after_comma_separated=[i.strip() for i in List_after_comma_separated]
        # print(List_after_space_separated)
        # print(List_after_comma_separated)
#  for R -TYPE INSTRUCTIONS
        if List_after_space_separated[0]=="add":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_add="0110011"
            funct7_for_add="0000000"
            funct3_for_add="000"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")


        elif List_after_space_separated[0]=="sub":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_sub="0110011"
            funct7_for_sub="0100000"
            funct3_for_sub="000"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_sub}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_sub}{Register_map_with_their_binary_values[rd]}{opcode_for_sub}\n")


        elif List_after_space_separated[0]=="and":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_and="0110011"
            funct7_for_and="0000000"
            funct3_for_and="111"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_and}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_and}{Register_map_with_their_binary_values[rd]}{opcode_for_and}\n")


        elif List_after_space_separated[0]=="or":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_or="0110011"
            funct7_for_or="0000000"
            funct3_for_or="110"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_or}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_or}{Register_map_with_their_binary_values[rd]}{opcode_for_or}\n")


        elif List_after_space_separated[0]=="xor":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_xor="0110011"
            funct7_for_xor="0000000"
            funct3_for_xor="100"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_xor}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_xor}{Register_map_with_their_binary_values[rd]}{opcode_for_xor}\n")


        elif List_after_space_separated[0]=="sll":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_sll="0110011"
            funct7_for_sll="0000000"
            funct3_for_sll="001"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_sll}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_sll}{Register_map_with_their_binary_values[rd]}{opcode_for_sll}\n")


        elif List_after_space_separated[0]=="srl":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_srl="0110011"
            funct7_for_srl="0000000"
            funct3_for_srl="101"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_srl}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_srl}{Register_map_with_their_binary_values[rd]}{opcode_for_srl}\n")


        elif List_after_space_separated[0]=="sra":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_sra="0110011"
            funct7_for_sra="0100000"
            funct3_for_sra="101"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_sra}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_sra}{Register_map_with_their_binary_values[rd]}{opcode_for_sra}\n")

        elif List_after_space_separated[0]=="slt":
            if len(List_after_comma_separated)!=3 :
                print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                break
            rd=List_after_comma_separated[0]
            rx1=List_after_comma_separated[1]
            rx2=List_after_comma_separated[2]
            opcode_for_slt="0110011"
            funct7_for_slt="0000000"
            funct3_for_slt="010"
            # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
            Output_file_taken.write(f"{funct7_for_slt}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_slt}{Register_map_with_their_binary_values[rd]}{opcode_for_slt}\n")


        elif List_after_space_separated[0]=="div":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    rx2=List_after_comma_separated[2]
                    opcode_for_div="0110011"
                    funct7_for_div="0000001"
                    funct3_for_div="100"
                    # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
                    Output_file_taken.write(f"{funct7_for_div}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_div}{Register_map_with_their_binary_values[rd]}{opcode_for_div}\n")

        elif List_after_space_separated[0]=="mul":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    rx2=List_after_comma_separated[2]
                    opcode_for_mul="0110011"
                    funct7_for_mul="0000001"
                    funct3_for_mul="000"
                    # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
                    Output_file_taken.write(f"{funct7_for_mul}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_mul}{Register_map_with_their_binary_values[rd]}{opcode_for_mul}\n")


        elif List_after_space_separated[0]=="sltu":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    rx2=List_after_comma_separated[2]
                    opcode_for_sltu="0110011"
                    funct7_for_sltu="0000000"
                    funct3_for_sltu="011"
                    # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
                    Output_file_taken.write(f"{funct7_for_sltu}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_sltu}{Register_map_with_their_binary_values[rd]}{opcode_for_sltu}\n")

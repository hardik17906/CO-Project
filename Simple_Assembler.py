# We are making a Assembler 
# This will be 32-bit Assembler
# We made this using RISC V ISA

import sys   # importing sys for taking input file and name of output file as arguments from stdin

def converter_to_12bit_binary(n):
    if n<0:
        return format((1<<12) + n, '012b')
    else:
        return format(n,'012b')

def converter_to_20bit_binary(n):
    if n<0:
        return format((1<<20) + n, '020b')
    else:
        return format(n, '020b')

if len(sys.argv) !=3:
    print("The Format of the input should be : python <File_name>.py <input.txt> <output.bin> ")
    sys.exit( 1 )  # To exit out of the this sys

input_file=sys.argv[1]   # loading name of input txt file in input_file
output_file=sys.argv[2]  # loading name of the ouput txt file in outut_file


# Making a Dictionary having Keys as the name of the register and Values as their binary conversion
Register_map_with_their_binary_values = { "zero":"00000" ,
    "x0": "00000", "x1": "00001", "ra": "00001", "x2": "00010", "sp": "00010", 
    "x3": "00011", "gp": "00011", "x4": "00100", "tp": "00100", "x5": "00101", 
    "t0": "00101", "x6": "00110", "t1": "00110", "x7": "00111", "t2": "00111", 
    "x8": "01000", "s0": "01000", "x9": "01001", "s1": "01001", "x10": "01010", 
    "a0": "01010", "x11": "01011", "a1": "01011", "x12": "01100", "a2": "01100", 
    "x13": "01101", "a3": "01101", "x14": "01110", "a4": "01110", "x15": "01111", 
    "a5": "01111", "x16": "10000", "a6": "10000", "x17": "10001", "a7": "10001", 
    "x18": "10010", "s2": "10010", "x19": "10011", "s3": "10011", "x20": "10100", 
    "s4": "10100", "x21": "10101", "s5": "10101", "x22": "10110", "s6": "10110", 
    "x23": "10111", "s7": "10111", "x24": "11000", "s8": "11000", "x25": "11001", 
    "s9": "11001", "x26": "11010", "s10": "11010", "x27": "11011", "s11": "11011", 
    "x28": "11100", "t3": "11100", "x29": "11101", "t4": "11101", "x30": "11110", 
    "t5": "11110", "x31": "11111", "t6": "11111"
}

dictionary_fro_line_number_of_label={}
#  Making a list of all the given instructions in the input file 
with open(input_file,"r") as Input_file_taken:
    List_of_lines_of_input_file=Input_file_taken.readlines()

Temp_for_virtual_error_checker=List_of_lines_of_input_file[-1].split(":")
# print(Temp_for_virtual_error_checker)
if len(Temp_for_virtual_error_checker)==2:
    if f"beq zero,zero,{Temp_for_virtual_error_checker[0].strip()}" not in Temp_for_virtual_error_checker[1].strip() and "beq zero,zero,0" not in Temp_for_virtual_error_checker[1].strip() and "beq zero,zero,-0" not in Temp_for_virtual_error_checker[1].strip() :
        print("ERROR : Virtual Hault Instruction missing ")
        sys.exit(1)
elif len(Temp_for_virtual_error_checker)==1:
    if "beq zero,zero,0" not in Temp_for_virtual_error_checker[0].strip() and "beq zero,zero,-0" not in Temp_for_virtual_error_checker[0].strip():
        print("ERROR : Virtual Hault Instruction missing ")
        sys.exit(1)
            
        
# if "beq zero,zero" not in List_of_lines_of_input_file[-1].strip()  :
#       print("ERROR : Virtual Hault Instruction missing ")
#       sys.exit(1)
stop=0
for i in range(len(List_of_lines_of_input_file)):
        if List_of_lines_of_input_file[i].strip()=="" :
            continue     
        List_after_colon_separated=List_of_lines_of_input_file[i].split(":")
        if len(List_after_colon_separated)==2 :
              if List_after_colon_separated[0] in dictionary_fro_line_number_of_label:
                    print(f"There is a labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}\nThe label '{List_after_colon_separated[0]}' was also present in the line number {dictionary_fro_line_number_of_label[List_after_colon_separated[0]]+1} --> {List_of_lines_of_input_file[dictionary_fro_line_number_of_label[List_after_colon_separated[0]]]}")
                    stop=1
                    break
              else :
                  dictionary_fro_line_number_of_label[List_after_colon_separated[0].strip()]=i
# print(dictionary_fro_line_number_of_label)

if stop==1:
      sys.exit(1)
with open(output_file,"w") as Output_file_taken:
    Done=0

    for i in range(len(List_of_lines_of_input_file)):

        if List_of_lines_of_input_file[i].strip()=="" :
            continue
        # print(List_of_lines_of_input_file[i],end="")
        
        
        List_after_colon_separated=List_of_lines_of_input_file[i].split(":")
        # print(List_after_colon_separated)
        # continue
        List_after_colon_separated_for_further=List_after_colon_separated[len(List_after_colon_separated)-1].strip(" ")
        # print(List_after_colon_separated_for_further)
        List_after_space_separated=(List_after_colon_separated_for_further.strip()).split(" ")
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
            if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                  print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                  break
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
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
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
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
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
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values or rx2 not in Register_map_with_their_binary_values:
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    opcode_for_sltu="0110011"
                    funct7_for_sltu="0000000"
                    funct3_for_sltu="011"
                    # print(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")
                    Output_file_taken.write(f"{funct7_for_sltu}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_sltu}{Register_map_with_their_binary_values[rd]}{opcode_for_sltu}\n")
       


# FOR I -TYPE INSTRUCTIONS
        elif List_after_space_separated[0]=="addi":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_addi="0010011"
                    funct3_for_addi="000"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary}{Register_map_with_their_binary_values[rx1]}{funct3_for_addi}{Register_map_with_their_binary_values[rd]}{opcode_for_addi}\n")


        elif List_after_space_separated[0]=="andi":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_andi="0010011"
                    funct3_for_andi="111"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary}{Register_map_with_their_binary_values[rx1]}{funct3_for_andi}{Register_map_with_their_binary_values[rd]}{opcode_for_andi}\n")
             

        elif List_after_space_separated[0]=="ori":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_ori="0010011"
                    funct3_for_ori="110"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary}{Register_map_with_their_binary_values[rx1]}{funct3_for_ori}{Register_map_with_their_binary_values[rd]}{opcode_for_ori}\n")

        elif List_after_space_separated[0]=="xori":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_xori="0010011"
                    funct3_for_xori="100"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary}{Register_map_with_their_binary_values[rx1]}{funct3_for_xori}{Register_map_with_their_binary_values[rd]}{opcode_for_xori}\n")


        elif List_after_space_separated[0]=="lb":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_lb="0000011"
                    funct3_for_lb="000"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary}{Register_map_with_their_binary_values[rx1]}{funct3_for_lb}{Register_map_with_their_binary_values[rd]}{opcode_for_lb}\n")

        elif List_after_space_separated[0]=="lh":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_lh="0000011"
                    funct3_for_lh="001"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary}{Register_map_with_their_binary_values[rx1]}{funct3_for_lh}{Register_map_with_their_binary_values[rd]}{opcode_for_lh}\n")


        elif List_after_space_separated[0]=="lw":
                    if len(List_after_comma_separated)!=2 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    immi,rx1=List_after_comma_separated[1].split("(")
                    rx1=rx1.strip(")")
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_lw="0000011"
                    funct3_for_lw="010"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary}{Register_map_with_their_binary_values[rx1]}{funct3_for_lw}{Register_map_with_their_binary_values[rd]}{opcode_for_lw}\n")
            
        
        elif List_after_space_separated[0]=="jalr":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd=List_after_comma_separated[0]
                    rx1=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rd not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_jalr="1100111"
                    funct3_for_jalr="000"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary}{Register_map_with_their_binary_values[rx1]}{funct3_for_jalr}{Register_map_with_their_binary_values[rd]}{opcode_for_jalr}\n")
        
# FOR S -TYPE INSTRUCTIONS

        elif List_after_space_separated[0]=="sw":
                    if len(List_after_comma_separated)!=2 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rx2=List_after_comma_separated[0]
                    immi,rx1=List_after_comma_separated[1].split("(")
                    rx1=rx1.strip(")")
                    if (rx2 not in Register_map_with_their_binary_values) or (rx1 not in Register_map_with_their_binary_values) :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_sw="0100011"
                    funct3_for_sw="010"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary[0:7]}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_sw}{imm_in_binary[7:]}{opcode_for_sw}\n")


        elif List_after_space_separated[0]=="sh":
                    if len(List_after_comma_separated)!=2 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rx2=List_after_comma_separated[0]
                    immi,rx1=List_after_comma_separated[1].split("(")
                    rx1=rx1.strip(")")
                    if rx2 not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    opcode_for_sh="0100011" 
                    funct3_for_sh="001"  
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    Output_file_taken.write(f"{imm_in_binary[0:7]}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_sh}{imm_in_binary[7:]}{opcode_for_sh}\n")




# FOR B -TYPE INSTRUCTIONS
        

        elif List_after_space_separated[0]=="beq":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rx1=List_after_comma_separated[0]
                    rx2=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rx2 not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    opcode_for_beq="1100011" 
                    funct3_for_beq="000" 
                    Output_file_taken.write(f"{imm_in_binary[0]}{imm_in_binary[1:7]}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_beq}{imm_in_binary[7:11]}{imm_in_binary[1]}{opcode_for_beq}\n")

        elif List_after_space_separated[0]=="bge":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rx1=List_after_comma_separated[0]
                    rx2=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rx2 not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    opcode_for_bge="1100011" 
                    funct3_for_bge="101" 
                    Output_file_taken.write(f"{imm_in_binary[0]}{imm_in_binary[1:7]}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_bge}{imm_in_binary[7:11]}{imm_in_binary[1]}{opcode_for_bge}\n")
              
        elif List_after_space_separated[0]=="bne":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rx1=List_after_comma_separated[0]
                    rx2=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rx2 not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    opcode_for_bne="1100011" 
                    funct3_for_bne="001" 
                    Output_file_taken.write(f"{imm_in_binary[0]}{imm_in_binary[1:7]}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_bne}{imm_in_binary[7:11]}{imm_in_binary[1]}{opcode_for_bne}\n")



        elif List_after_space_separated[0]=="blt":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rx1=List_after_comma_separated[0]
                    rx2=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rx2 not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    opcode_for_blt="1100011" 
                    funct3_for_blt="100" 
                    Output_file_taken.write(f"{imm_in_binary[0]}{imm_in_binary[1:7]}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_blt}{imm_in_binary[7:11]}{imm_in_binary[1]}{opcode_for_blt}\n")

        elif List_after_space_separated[0]=="bltu":
                    if len(List_after_comma_separated)!=3 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rx1=List_after_comma_separated[0]
                    rx2=List_after_comma_separated[1]
                    immi=(List_after_comma_separated[2])
                    if rx2 not in Register_map_with_their_binary_values or rx1 not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    imm_in_binary=str(converter_to_12bit_binary(immi))
                    opcode_for_bltu="1100011" 
                    funct3_for_bltu="110" 
                    Output_file_taken.write(f"{imm_in_binary[0]}{imm_in_binary[1:7]}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_bltu}{imm_in_binary[7:11]}{imm_in_binary[1]}{opcode_for_bltu}\n")

# FOR J -TYPE INSTRUCTIONS 
        elif List_after_space_separated[0]=="jal":
                    if len(List_after_comma_separated)!=2 :
                        print(f"Error in line number {i+1} : {List_of_lines_of_input_file[i]}")
                        break
                    rd= List_after_comma_separated[0]
                    if rd not in Register_map_with_their_binary_values :
                        print(f"ERROR : INVALID INSTRUCTION in line number {i+1} --> {List_of_lines_of_input_file[i]}")
                        break
                    immi=List_after_comma_separated[1]
                    if immi.isdigit() or (immi[0]=="-" and immi[1:].isdigit()) :
                          immi=int(immi)
                          pass
                    else:
                        if immi in dictionary_fro_line_number_of_label:
                              offset=dictionary_fro_line_number_of_label[immi]
                              immi=(offset-i)*4
                        else :
                              print(f"There is labelling error in the line number {i+1} --> {List_of_lines_of_input_file[i]}The label '{immi}' is not defined anywhere in the instruction set")
                              break
                    imm_in_binary=str(converter_to_20bit_binary(immi))
                    # print(imm_in_binary)
                    opcode_for_jal="1101111" 
                    Output_file_taken.write(f"{imm_in_binary[0]}{imm_in_binary[9:19]}{imm_in_binary[8]}{imm_in_binary[1:9]}{Register_map_with_their_binary_values[rd]}{opcode_for_jal}\n")

#  NOT A VALID INSTRUCTION

        else:
              print(f"There is an Error in the line number {i+1} --> {List_of_lines_of_input_file[i]}\nGiven operation '{List_after_space_separated[0]}' is not a valid operation.")
              break
        
        if i==len(List_of_lines_of_input_file)-1:
              Done=1



if Done ==1 :
      print(f"Encoding For all the given instructions have been done and has been written to {output_file}.\nThanks BYE !")
      
#done
print("hello")
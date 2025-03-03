# We are making a Simulator for RISC v architecture
import sys

if len(sys.argv)!=3 :
    print("The Format of the input should be: python <Simulator_File_Name> <Input_file_name> <Output_file_name>")
    sys.exit(1)    # To exit out of the this sys

input_file=sys.argv[1]   # loading name of input txt file in input_file
output_file=sys.argv[2]  # loading name of the ouput txt file in outut_file

# As said in the instructions that we have to initialize all the registers to zero
# so making a dictionary for the value of the regsiters
Dict_for_the_values_of_the_registers=registers = {
    "zero": 0, "x0": 0, "x1": 0, "ra": 0, "x2": 0, "sp": 0, "x3": 0, "gp": 0, "x4": 0, "tp": 0, 
    "x5": 0, "t0": 0, "x6": 0, "t1": 0, "x7": 0, "t2": 0, "x8": 0, "s0": 0, "x9": 0, "s1": 0, 
    "x10": 0, "a0": 0, "x11": 0, "a1": 0, "x12": 0, "a2": 0, "x13": 0, "a3": 0, "x14": 0, "a4": 0, 
    "x15": 0, "a5": 0, "x16": 0, "a6": 0, "x17": 0, "a7": 0, "x18": 0, "s2": 0, "x19": 0, "s3": 0, 
    "x20": 0, "s4": 0, "x21": 0, "s5": 0, "x22": 0, "s6": 0, "x23": 0, "s7": 0, "x24": 0, "s8": 0, 
    "x25": 0, "s9": 0, "x26": 0, "s10": 0, "x27": 0, "s11": 0, "x28": 0, "t3": 0, "x29": 0, "t4": 0, 
    "x30": 0, "t5": 0, "x31": 0, "t6": 0
}


# making dictionary for opcodes for different operations

dictionary_for_opcode_for_operations = {"0110011":"R-TYPE","0010011":"I-TYPE","0100011":"S-TYPE","1100011":"B-TYPE","1101111":"J-TYPE"}
dictionary_for_funct_3_for_operations={"R-TYPE":{""}}
with open(input_file,"r") as Input_file_taken:
    List_of_lines_of_the_input_file=Input_file_taken.readlines()


List_of_lines_of_the_input_file=[i.strip() for i in List_of_lines_of_the_input_file]

# print(List_of_lines_of_the_input_file)
# print(len(List_of_lines_of_the_input_file[0]))

for i in range(len(List_of_lines_of_the_input_file)):
    if len(i)!=32:
        print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Instruction is not 32 bit.")
        sys.exit(1)
    binary_for_the_opcode=List_of_lines_of_the_input_file[i][25:]
    if binary_for_the_opcode not in dictionary_for_opcode_for_operations:
        print(f"There is an error in the line number {i+1} :{List_of_lines_of_the_input_file[i]}.\nError: Opcode given for this line is invald.")
        sys.exit(1)
    Instruction_type=dictionary_for_opcode_for_operations[binary_for_the_opcode] # TAKING OUT OPCODE FROM 32 BIT INFO

#  for R -TYPE INSTRUCTIONS
    if Instruction_type=="R-TYPE":
        funct7_for_this=List_of_lines_of_the_input_file[i][0:7]
        source_register_2=List_of_lines_of_the_input_file[i][7:12]
        source_register_1=List_of_lines_of_the_input_file[i][12:17]
        funct3_for_this=List_of_lines_of_the_input_file[i][17:20]
        destination_register=List_of_lines_of_the_input_file[i][20:25]
 
        # For add instruction




                    # Output_file_taken.write(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")



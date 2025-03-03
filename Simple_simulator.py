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


# Dictionary for binary to register
Dict_for_binary_to_register = {
    "00000": "x0", "00001": "x1", "00010": "x2", "00011": "x3", "00100": "x4", "00101": "x5", 
    "00110": "x6", "00111": "x7", "01000": "x8", "01001": "x9", "01010": "x10", "01011": "x11", 
    "01100": "x12", "01101": "x13", "01110": "x14", "01111": "x15", "10000": "x16", "10001": "x17", 
    "10010": "x18", "10011": "x19", "10100": "x20", "10101": "x21", "10110": "x22", "10111": "x23", 
    "11000": "x24", "11001": "x25", "11010": "x26", "11011": "x27", "11100": "x28", "11101": "x29", 
    "11110": "x30", "11111": "x31"
}

#  making dict for same registers
Dict_for_same_registers = {
    "x0": "x0", "zero": "x0", "x1": "x1", "ra": "x1", "x2": "x2", "sp": "x2", "x3": "x3", "gp": "x3", 
    "x4": "x4", "tp": "x4", "x5": "x5", "t0": "x5", "x6": "x6", "t1": "x6", "x7": "x7", "t2": "x7", 
    "x8": "x8", "s0": "x8", "fp": "x8", "x9": "x9", "s1": "x9", "x10": "x10", "a0": "x10", 
    "x11": "x11", "a1": "x11", "x12": "x12", "a2": "x12", "x13": "x13", "a3": "x13", "x14": "x14", "a4": "x14", 
    "x15": "x15", "a5": "x15", "x16": "x16", "a6": "x16", "x17": "x17", "a7": "x17", "x18": "x18", "s2": "x18", 
    "x19": "x19", "s3": "x19", "x20": "x20", "s4": "x20", "x21": "x21", "s5": "x21", "x22": "x22", "s6": "x22", 
    "x23": "x23", "s7": "x23", "x24": "x24", "s8": "x24", "x25": "x25", "s9": "x25", "x26": "x26", "s10": "x26", 
    "x27": "x27", "s11": "x27", "x28": "x28", "t3": "x28", "x29": "x29", "t4": "x29", "x30": "x30", "t5": "x30", 
    "x31": "x31", "t6": "x31"
}



# making dictionary for opcodes for different operations
dictionary_for_opcode_for_operations = {"0110011":"R-TYPE","0010011":"I-TYPE","0100011":"S-TYPE","1100011":"B-TYPE","1101111":"J-TYPE"}


dictionary_for_funct_3_for_operations={"R-TYPE":{"000":"ADD_SUB_MUL","111":"AND","110":"OR","100":"XOR","001":"SLL","101":"SRL","010":"SLT","100":"DIV","011":"SLTU"}}


dictionary_for_funct_7_for_operations={"R-TYPE":{"0000000":"ADD","0100000":"SUB","0000001":"MUL"}}
with open(input_file,"r") as Input_file_taken:
    List_of_lines_of_the_input_file=Input_file_taken.readlines()


List_of_lines_of_the_input_file=[i.strip() for i in List_of_lines_of_the_input_file]

# print(List_of_lines_of_the_input_file)
# print(len(List_of_lines_of_the_input_file[0]))
i=0
while i<len(List_of_lines_of_the_input_file):
    if List_of_lines_of_the_input_file[i]=="":
        i=i+1
        continue
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
 
        if funct3_for_this not in dictionary_for_funct_3_for_operations["R-TYPE"]:
            print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Funct3 is not matching with any of the R-TYPE instructions.")
            sys.exit(1)
        if funct7_for_this not in dictionary_for_funct_7_for_operations["R-TYPE"]:
            print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Funct7 is not matching with any of the R-TYPE instructions.")
            sys.exit(1)
        if source_register_1 not in Dict_for_binary_to_register:
            print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for source register 1 is not valid.")
            sys.exit(1)          
        if source_register_2 not in Dict_for_binary_to_register:
            print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for source register 2 is not valid.")
            sys.exit(1)          
        if destination_register not in Dict_for_binary_to_register:
            print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for destination register is not valid.")
            sys.exit(1)          
        operation=dictionary_for_funct_3_for_operations["R-TYPE"][funct3_for_this]
        if operation=="ADD_SUB_MUL":
            operation=dictionary_for_funct_7_for_operations["R-TYPE"][funct7_for_this]
        source_register_1=Dict_for_binary_to_register[source_register_1]
        source_register_2=Dict_for_binary_to_register[source_register_2]
        destination_register=Dict_for_binary_to_register[destination_register]

        # For ADD instruction
        if operation=="ADD":
            Dict_for_the_values_of_the_registers[destination_register]=

            

        # For ADD instruction






                    # Output_file_taken.write(f"{funct7_for_add}{Register_map_with_their_binary_values[rx2]}{Register_map_with_their_binary_values[rx1]}{funct3_for_add}{Register_map_with_their_binary_values[rd]}{opcode_for_add}\n")


































































































































































































































































































































































































































































































































































































































































































































































































































































# B AN S TYPE


# We are making a Simulator for RISC v architecture
import sys

if len(sys.argv)!=3 :
    print("The Format of the input should be: python <Simulator_File_Name> <Input_file_name> <Output_file_name>")
    sys.exit(1)    # To exit out of the this sys

input_file=sys.argv[1]   # loading name of input txt file in input_file
output_file=sys.argv[2]  # loading name of the ouput txt file in outut_file


# Function for conversion  of decimal to binary
def decimal_to_32bit_binary(value):
    value=int(value)
    if value < -2**31 or value >= 2**31:
        return "Error"
    return format(value & 0xFFFFFFFF, '032b')


# Function for converison of binary to decimal
def twos_complement_to_decimal(value_in_binary_form):
    value_in_binary_form = str(value_in_binary_form)
    bit_length = len(value_in_binary_form)
    
    if value_in_binary_form[0] == '0':  
        return int(value_in_binary_form, 2)
    else:
        return int(value_in_binary_form, 2) - (1 << bit_length)
    
def and_for_two_registers(source_1,source_2):
    final_answer=""
    for i in range(0,32):
        if source_1[i]=="0" and source_2[i]=="1":
            final_answer+="0"
        elif source_1[i]=="1" and source_2[i]=="1":
            final_answer+="1"
        elif source_1[i]=="1" and source_2[i]=="0":
            final_answer+="0"
        else:
            final_answer+="0"
    return final_answer


def or_for_two_registers(source_1,source_2):
    final_answer=""
    for i in range(0,32):
        if source_1[i]=="0" and source_2[i]=="1":
            final_answer+="1"
        elif source_1[i]=="1" and source_2[i]=="1":
            final_answer+="1"
        elif source_1[i]=="1" and source_2[i]=="0":
            final_answer+="1"
        else:
            final_answer+="0"
    return final_answer


def xor_for_two_registers(source_1,source_2):
    final_answer=""
    for i in range(0,32):
        if source_1[i]=="0" and source_2[i]=="1":
            final_answer+="1"
        elif source_1[i]=="1" and source_2[i]=="1":
            final_answer+="0"
        elif source_1[i]=="1" and source_2[i]=="0":
            final_answer+="1"
        else:
            final_answer+="0"
    return final_answer


def decimal_to_8bit_hex(value):
    if value < 0:
        value = (1 << 32) + value  
    return f'0x{value:08X}'  

# As said in the instructions that we have to initialize all the registers to zero
# so making a dictionary for the value of the regsiters
Dict_for_the_values_of_the_registers = {
    "x0": 0, "x1": 0, "x2": 380, "x3": 0, "x4": 0, "x5": 0, "x6": 0, "x7": 0, 
    "x8": 0, "x9": 0, "x10": 0, "x11": 0, "x12": 0, "x13": 0, "x14": 0, "x15": 0, 
    "x16": 0, "x17": 0, "x18": 0, "x19": 0, "x20": 0, "x21": 0, "x22": 0, "x23": 0, 
    "x24": 0, "x25": 0, "x26": 0, "x27": 0, "x28": 0, "x29": 0, "x30": 0, "x31": 0
}
# stack memory
stack_memory = {
    "0x00000100": 0, "0x00000104": 0, "0x00000108": 0, "0x0000010C": 0,
    "0x00000110": 0, "0x00000114": 0, "0x00000118": 0, "0x0000011C": 0,
    "0x00000120": 0, "0x00000124": 0, "0x00000128": 0, "0x0000012C": 0,
    "0x00000130": 0, "0x00000134": 0, "0x00000138": 0, "0x0000013C": 0,
    "0x00000140": 0, "0x00000144": 0, "0x00000148": 0, "0x0000014C": 0,
    "0x00000150": 0, "0x00000154": 0, "0x00000158": 0, "0x0000015C": 0,
    "0x00000160": 0, "0x00000164": 0, "0x00000168": 0, "0x0000016C": 0,
    "0x00000170": 0, "0x00000174": 0, "0x00000178": 0, "0x0000017C": 0
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
dictionary_for_opcode_for_operations = {"0110011":"R-TYPE","0010011":"ADDI","0000011":"LW","1100111":"JALR","0100011":"S-TYPE","1100011":"B-TYPE","1101111":"J-TYPE"}

#dictionary for the funct3 
dictionary_for_funct_3_for_operations={
    "R-TYPE":{
        "000":"ADD_SUB_MUL",
        "111":"AND",
        "110":"OR",
        "100":"XOR",
        "001":"SLL",
        "101":"SRL",
        "010":"SLT",
        "011":"SLTU",
        "100":"DIV"
    },
    "S-TYPE":{
        "001":"SH",
        "010":"SW"
    },
    "B-TYPE":{
        "000":"BEQ",
        "001":"BNE",
        "100":"BLT",
        "101":"BGE",
        "110":"BLTU",
        
    },
    "I-TYPE":{
        "000":"ADDI",
        "010":"SLTI",
        "011":"SLTIU",
        "100":"XORI",
        "110":"ORI",
        "111":"ANDI",
        "001":"SLLI",
        "101":"SRLI_SRAI",
        "000":"LB",
        "001":"LH",
        "010":"LW",
        "100":"LBU",
        "101":"LHU"
    },
    "J-TYPE":{
        "000":"JAL"
    }
}


#dictionary for the funct7
dictionary_for_funct_7_for_operations={"R-TYPE":{"0000000":"ADD","0100000":"SUB","0000001":"MUL"}}

#dictionary for the values stored in the memory locations
dict_for_values_stored_in_memory_locations = {
    "0x00010000": 0, "0x00010004": 0, "0x00010008": 0, "0x0001000C": 0, "0x00010010": 0, "0x00010014": 0,
    "0x00010018": 0, "0x0001001C": 0, "0x00010020": 0, "0x00010024": 0, "0x00010028": 0, "0x0001002C": 0,
    "0x00010030": 0, "0x00010034": 0, "0x00010038": 0, "0x0001003C": 0, "0x00010040": 0, "0x00010044": 0,
    "0x00010048": 0, "0x0001004C": 0, "0x00010050": 0, "0x00010054": 0, "0x00010058": 0, "0x0001005C": 0,
    "0x00010060": 0, "0x00010064": 0, "0x00010068": 0, "0x0001006C": 0, "0x00010070": 0, "0x00010074": 0,
    "0x00010078": 0, "0x0001007C": 0
}



with open(input_file,"r") as Input_file_taken:
    List_of_lines_of_the_input_file=Input_file_taken.readlines()


List_of_lines_of_the_input_file=[i.strip() for i in List_of_lines_of_the_input_file]

# print(List_of_lines_of_the_input_file)
# print(len(List_of_lines_of_the_input_file[0]))
i=0
program_counter=0
with open(output_file,"w") as Output_file_taken:
    while i<len(List_of_lines_of_the_input_file):
        if List_of_lines_of_the_input_file[i]=="":
            i=i+1
            continue
        if len(List_of_lines_of_the_input_file[i])!=32:
            print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Instruction is not 32 bit.")
            sys.exit(1)
        for value in List_of_lines_of_the_input_file[i]:
            if value =="0" or value =="1":
                pass
            else:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Instruction is incorrect. Bits can only be either 0 or 1.")
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
            source_register_1_=Dict_for_binary_to_register[source_register_1]
            source_register_2_=Dict_for_binary_to_register[source_register_2]
            destination_register_=Dict_for_binary_to_register[destination_register]
            print(operation)

            # For ADD instruction
            if operation=="ADD":
                value_to_be_stored=Dict_for_the_values_of_the_registers[source_register_1_]+Dict_for_the_values_of_the_registers[source_register_2_]
                if value_to_be_stored < -2**31 or value_to_be_stored >= 2**31:
                    print(f"Line number {i} : {List_of_lines_of_the_input_file[i]}.\nWe can't proceed further because the value to be stored in the destination register cannot be converted into 32 bit.")
                    sys.exit(1)
                Dict_for_the_values_of_the_registers[destination_register_]=value_to_be_stored

            #  for Sub instruction
            elif operation=="SUB":
                value_to_be_stored=Dict_for_the_values_of_the_registers[source_register_1_]-Dict_for_the_values_of_the_registers[source_register_2_]
                if value_to_be_stored < -2**31 or value_to_be_stored >= 2**31:
                    print(f"Line number {i} : {List_of_lines_of_the_input_file[i]}.\nWe can't proceed further because the value to be stored in the destination register cannot be converted into 32 bit.")
                    sys.exit(1)
                Dict_for_the_values_of_the_registers[destination_register_]=value_to_be_stored

            elif operation=="MUL":
                value_to_be_stored=Dict_for_the_values_of_the_registers[source_register_1_]*Dict_for_the_values_of_the_registers[source_register_2_]
                if value_to_be_stored < -2**31 or value_to_be_stored >= 2**31:
                    print(f"Line number {i} : {List_of_lines_of_the_input_file[i]}.\nWe can't proceed further because the value to be stored in the destination register cannot be converted into 32 bit.")
                    sys.exit(1)
                Dict_for_the_values_of_the_registers[destination_register_]=value_to_be_stored

            elif operation=="AND":
                Dict_for_the_values_of_the_registers[destination_register_]=twos_complement_to_decimal(and_for_two_registers(decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[source_register_1_]),decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[source_register_2_])))
            elif operation=="OR":
                Dict_for_the_values_of_the_registers[destination_register_]=twos_complement_to_decimal(or_for_two_registers(decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[source_register_1_]),decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[source_register_2_])))
            elif operation=="XOR":
                # print(xor_for_two_registers(decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[source_register_1_]),decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[source_register_2_])))
                Dict_for_the_values_of_the_registers[destination_register_]=twos_complement_to_decimal(xor_for_two_registers(decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[source_register_1_]),decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[source_register_2_])))
            elif operation=="SLL":
                value_of_rs2=Dict_for_the_values_of_the_registers[source_register_2_]
                value_of_rs2=value_of_rs2%32
                value_to_be_stored=((Dict_for_the_values_of_the_registers[source_register_1_]) << value_of_rs2) & 0xFFFFFFFF
                Dict_for_the_values_of_the_registers[destination_register_]=value_to_be_stored

            elif operation=="SRL":
                value_of_rs2=Dict_for_the_values_of_the_registers[source_register_2_]
                value_of_rs2=value_of_rs2%32
                value_to_be_stored = ((Dict_for_the_values_of_the_registers[source_register_1_]) >> value_of_rs2) & 0xFFFFFFFF
                Dict_for_the_values_of_the_registers[destination_register_]=value_to_be_stored
            elif operation=="SLT":
                if Dict_for_the_values_of_the_registers[source_register_1_]<Dict_for_the_values_of_the_registers[source_register_2_]:
                    Dict_for_the_values_of_the_registers[destination_register_]=1
                else:
                    Dict_for_the_values_of_the_registers[destination_register_]=0
            i+=1
            program_counter+=4
            # print(Dict_for_the_values_of_the_registers)
            # print("\n\n\n\n\n")


            # Output_file_taken.write(str(program_counter)+" ")

            # for registers in Dict_for_the_values_of_the_registers:
            #     Output_file_taken.write(f"{Dict_for_the_values_of_the_registers[registers]} ")
            # Output_file_taken.write("\n")

            Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

            for registers in Dict_for_the_values_of_the_registers:
                Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
            Output_file_taken.write("\n")


    #    I-TYPE INSTRUCTION
   
        elif Instruction_type=="ADDI":
            print(Instruction_type)
            immediate_value=List_of_lines_of_the_input_file[i][0:12]  
            source_register_1=List_of_lines_of_the_input_file[i][12:17]  
            funct3_for_this=List_of_lines_of_the_input_file[i][17:20]  
            destination_register=List_of_lines_of_the_input_file[i][20:25] 
            if source_register_1 not in Dict_for_binary_to_register:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for source register 1 is not valid.")
                sys.exit(1) 
            if funct3_for_this not in dictionary_for_funct_3_for_operations["I-TYPE"]:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Funct3 is not matching with any of the R-TYPE instructions.")
                sys.exit(1)
            if destination_register not in Dict_for_binary_to_register:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for destination register is not valid.")
                sys.exit(1)
            source_register_1_=Dict_for_binary_to_register[source_register_1]
            destination_register_=Dict_for_binary_to_register[destination_register] 
            # print(immediate_value)                
            Decimal_Value_of_immediate=twos_complement_to_decimal(immediate_value)
            value_to_be_stored=Dict_for_the_values_of_the_registers[source_register_1_]+Decimal_Value_of_immediate
            # print(Decimal_Value_of_immediate)
            # print(Dict_for_the_values_of_the_registers[source_register_1_])
            # print(value_to_be_stored)
            if value_to_be_stored < -2**31 or value_to_be_stored >= 2**31:
                print(f"Line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nWe can't proceed further because the value to be stored in the destination register cannot be converted into 32 bit.")
                sys.exit(1)
            Dict_for_the_values_of_the_registers[destination_register_]=value_to_be_stored
            i+=1
            program_counter+=4
            # Output_file_taken.write(str(program_counter)+" ")

            # for registers in Dict_for_the_values_of_the_registers:
            #     Output_file_taken.write(f"{Dict_for_the_values_of_the_registers[registers]} ")
            # Output_file_taken.write("\n")

            Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

            for registers in Dict_for_the_values_of_the_registers:
                Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
            Output_file_taken.write("\n")

        elif Instruction_type=="JALR":
            print(Instruction_type)
            immediate_value=List_of_lines_of_the_input_file[i][0:12]  
            source_register_1=List_of_lines_of_the_input_file[i][12:17]  
            funct3_for_this=List_of_lines_of_the_input_file[i][17:20]  
            destination_register=List_of_lines_of_the_input_file[i][20:25] 
            if source_register_1 not in Dict_for_binary_to_register:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for source register 1 is not valid.")
                sys.exit(1) 
            if funct3_for_this not in dictionary_for_funct_3_for_operations["I-TYPE"]:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Funct3 is not matching with any of the R-TYPE instructions.")
                sys.exit(1)
            if destination_register not in Dict_for_binary_to_register:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for destination register is not valid.")
                sys.exit(1)
            # print(program_counter)

            source_register_1_=Dict_for_binary_to_register[source_register_1]
            destination_register_=Dict_for_binary_to_register[destination_register]                 
            Decimal_Value_of_immediate=twos_complement_to_decimal(immediate_value)
            # print(Decimal_Value_of_immediate)
            value_to_be_stored_inside_the_destination_regsiter=program_counter+4
            if (source_register_1_!="x0"):
                Dict_for_the_values_of_the_registers[destination_register_]=value_to_be_stored_inside_the_destination_regsiter
            # print(Dict_for_the_values_of_the_registers[source_register_1_])
            new_value_for_program_counter=Dict_for_the_values_of_the_registers[source_register_1_]+Decimal_Value_of_immediate
            # print(new_value_for_program_counter)
            if (new_value_for_program_counter)%4!=0:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError : PC is no more a multiple of 4.So this is an error.")
                sys.exit(1)
            program_counter=new_value_for_program_counter
            i=program_counter//4
            # Output_file_taken.write(str(program_counter)+" ")

            # for registers in Dict_for_the_values_of_the_registers:
            #     Output_file_taken.write(f"{Dict_for_the_values_of_the_registers[registers]} ")
            # Output_file_taken.write("\n")

            Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

            for registers in Dict_for_the_values_of_the_registers:
                Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
            Output_file_taken.write("\n")




        elif Instruction_type=="LW":
            print(Instruction_type)
            immediate_value=List_of_lines_of_the_input_file[i][0:12]  
            source_register_1=List_of_lines_of_the_input_file[i][12:17]  
            funct3_for_this=List_of_lines_of_the_input_file[i][17:20]  
            destination_register=List_of_lines_of_the_input_file[i][20:25] 
            if source_register_1 not in Dict_for_binary_to_register:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for source register 1 is not valid.")
                sys.exit(1) 
            if funct3_for_this not in dictionary_for_funct_3_for_operations["I-TYPE"]:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Funct3 is not matching with any of the R-TYPE instructions.")
                sys.exit(1)
            if destination_register not in Dict_for_binary_to_register:
                print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError: Given binary for destination register is not valid.")
                sys.exit(1)
            source_register_1_=Dict_for_binary_to_register[source_register_1]
            destination_register_=Dict_for_binary_to_register[destination_register]                 
            Decimal_Value_of_immediate=twos_complement_to_decimal(immediate_value)
            # print(decimal_to_8bit_hex(Dict_for_the_values_of_the_registers[source_register_1_]+Decimal_Value_of_immediate))
            memory_location_for_lw=decimal_to_8bit_hex(Dict_for_the_values_of_the_registers[source_register_1_]+Decimal_Value_of_immediate)
            if memory_location_for_lw in dict_for_values_stored_in_memory_locations:        
                value_to_be_stored=dict_for_values_stored_in_memory_locations[memory_location_for_lw]
            else:
                value_to_be_stored=0
            
            if value_to_be_stored < -2**31 or value_to_be_stored >= 2**31:
                print(f"Line number {i} : {List_of_lines_of_the_input_file[i]}.\nWe can't proceed further because the value to be stored in the destination register cannot be converted into 32 bit.")
                sys.exit(1)
            Dict_for_the_values_of_the_registers[destination_register_]=value_to_be_stored
            i+=1
            program_counter+=4
            # Output_file_taken.write(str(program_counter)+" ")

            # for registers in Dict_for_the_values_of_the_registers:
            #     Output_file_taken.write(f"{Dict_for_the_values_of_the_registers[registers]} ")
            # Output_file_taken.write("\n")

            Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

            for registers in Dict_for_the_values_of_the_registers:
                Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
            Output_file_taken.write("\n")





        # B-TYPE INSTRUCTION
        elif Instruction_type=="B-TYPE":
            imm_1_6 = List_of_lines_of_the_input_file[i][1:7]
            rx2 = List_of_lines_of_the_input_file[i][7:12]
            rx1 = List_of_lines_of_the_input_file[i][12:17]
            funct3 = List_of_lines_of_the_input_file[i][17:20]
            imm_7_10 = List_of_lines_of_the_input_file[i][20:24]
            imm_0 = List_of_lines_of_the_input_file[i][24]
        
            final_imm = imm_0+imm_1_6+imm_7_10+"0"
            # print(final_imm)
            Decimal_Value_of_immediate = twos_complement_to_decimal(final_imm)
        
            operation = dictionary_for_funct_3_for_operations["B-TYPE"][funct3]
            print(operation)
            rx1_ = Dict_for_binary_to_register[rx1]
            rx2_ = Dict_for_binary_to_register[rx2]
            # print(Decimal_Value_of_immediate)
            if operation == "BEQ":
                if Dict_for_the_values_of_the_registers[rx1_] == Dict_for_the_values_of_the_registers[rx2_]:
                    if Decimal_Value_of_immediate==0:
                        print("done")
                        program_counter+=4
                        Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

                        for registers in Dict_for_the_values_of_the_registers:
                            Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
                        Output_file_taken.write("\n")
                        break
                    else:
                        program_counter += Decimal_Value_of_immediate
                        i = program_counter // 4
                else:
                    i+=1
                    program_counter+=4
        
            elif operation == "BNE":
                if Dict_for_the_values_of_the_registers[rx1_] != Dict_for_the_values_of_the_registers[rx2_]:
                    if Decimal_Value_of_immediate==0:
                        print("done")
                        program_counter+=4

                        Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

                        for registers in Dict_for_the_values_of_the_registers:
                            Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
                        Output_file_taken.write("\n")
                        break
                    else:
                        program_counter += Decimal_Value_of_immediate
                        i = program_counter // 4
                else:
                    i+=1
                    program_counter+=4

            elif operation == "BLT":
                if Dict_for_the_values_of_the_registers[rx1_] < Dict_for_the_values_of_the_registers[rx2_]:
                    if Decimal_Value_of_immediate==0:
                        print("done")
                        program_counter+=4

                        Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

                        for registers in Dict_for_the_values_of_the_registers:
                            Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
                        Output_file_taken.write("\n")
                        break
                    else:
                        program_counter += Decimal_Value_of_immediate
                        i = program_counter // 4
                else:
                    i+=1
                    program_counter+=4


            elif operation == "BGE":
                if Dict_for_the_values_of_the_registers[rx1_] >= Dict_for_the_values_of_the_registers[rx2_]:
                    if Decimal_Value_of_immediate==0:
                        print("done")
                        program_counter+=4

                        Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

                        for registers in Dict_for_the_values_of_the_registers:
                            Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
                        Output_file_taken.write("\n")
                        break
                    else:
                        program_counter += Decimal_Value_of_immediate
                        i = program_counter // 4
                else:
                    i+=1
                    program_counter+=4

            elif operation == "BLTU":
                    continue
            # Output_file_taken.write(str(program_counter)+" ")

            # for registers in Dict_for_the_values_of_the_registers:
            #     Output_file_taken.write(f"{Dict_for_the_values_of_the_registers[registers]} ")
            # Output_file_taken.write("\n")

            Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

            for registers in Dict_for_the_values_of_the_registers:
                Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
            Output_file_taken.write("\n")
            




        # S-TYPE INSTRUCTION
        elif Instruction_type=="S-TYPE":
            imm_0_6 = List_of_lines_of_the_input_file[i][0:7]
            rx2 = List_of_lines_of_the_input_file[i][7:12]
            rx1 = List_of_lines_of_the_input_file[i][12:17]
            funct3 = List_of_lines_of_the_input_file[i][17:20]
            imm_7_11 = List_of_lines_of_the_input_file[i][20:25]
        
            final_imm = imm_0_6 + imm_7_11
            Decimal_Value_of_immediate = twos_complement_to_decimal(final_imm)
            operation = dictionary_for_funct_3_for_operations["S-TYPE"][funct3]
            print(operation)
            rx1_ = Dict_for_binary_to_register[rx1]
            rx2_ = Dict_for_binary_to_register[rx2]

            
            if operation=="SW":
                value_to_be_stored_in_the_memory_location=Dict_for_the_values_of_the_registers[rx2_]
                memory_location_for_sw=decimal_to_8bit_hex(Dict_for_the_values_of_the_registers[rx1_]+Decimal_Value_of_immediate)
                if memory_location_for_sw in dict_for_values_stored_in_memory_locations:        
                    dict_for_values_stored_in_memory_locations[memory_location_for_sw]=value_to_be_stored_in_the_memory_location
            i+=1
            program_counter+=4
            # Output_file_taken.write(str(program_counter)+" ")

            # for registers in Dict_for_the_values_of_the_registers:
            #     Output_file_taken.write(f"{Dict_for_the_values_of_the_registers[registers]} ")
            # Output_file_taken.write("\n")

            Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

            for registers in Dict_for_the_values_of_the_registers:
                Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
            Output_file_taken.write("\n")
          

        

#   J -TYPE INSTRUCTIONS
        elif Instruction_type=="J-TYPE":
            operation="JAL"
            print(operation)
            # imm_0=List_of_lines_of_the_input_file[i][0]
            imm_10_19=List_of_lines_of_the_input_file[i][1:11]
            imm_9=List_of_lines_of_the_input_file[i][11]
            imm_1_8=List_of_lines_of_the_input_file[i][12:20]
            destination_register=List_of_lines_of_the_input_file[i][20:25]
            destination_register_=Dict_for_binary_to_register[destination_register]
            final_imm=imm_1_8+imm_9+imm_10_19+"0"
            Decimal_Value_of_immediate=twos_complement_to_decimal(final_imm)
            memory_to_be_stored_inside_the_destination_regsiter=program_counter+4
            if destination_register_!="x0":
                Dict_for_the_values_of_the_registers[destination_register_]=memory_to_be_stored_inside_the_destination_regsiter
            new_value_for_program_counter=Decimal_Value_of_immediate
            if (new_value_for_program_counter)%4!=0:
                # print(f"There is an error in the line number {i+1} : {List_of_lines_of_the_input_file[i]}.\nError : PC is no more a multiple of 4.So this is an error.")
                # sys.exit(1)
                program_counter+=4
                i+=1
            else:
                program_counter=new_value_for_program_counter
                i=program_counter//4 
            # Output_file_taken.write(str(program_counter)+" ")

            # for registers in Dict_for_the_values_of_the_registers:
            #     Output_file_taken.write(f"{Dict_for_the_values_of_the_registers[registers]} ")
            # Output_file_taken.write("\n")

            Output_file_taken.write(f"0b{decimal_to_32bit_binary(program_counter)} ")

            for registers in Dict_for_the_values_of_the_registers:
                Output_file_taken.write(f"0b{decimal_to_32bit_binary(Dict_for_the_values_of_the_registers[registers])} ")
            Output_file_taken.write("\n")  


        # print(program_counter)

        # print(i)
    for i in dict_for_values_stored_in_memory_locations:
        Output_file_taken.write(f"{i}:0b{decimal_to_32bit_binary(dict_for_values_stored_in_memory_locations[i])}\n")   

            

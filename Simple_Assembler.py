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

#  Making a list of all the given instructions in the input file 
with open(input_file,"r") as Input_file_taken:
    List_of_lines_of_input_file=Input_file_taken.readlines()

# for i in List_of_lines_of_input_file:
#     if !(i=="") :
#         print(i,end="")

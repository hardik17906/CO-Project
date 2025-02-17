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

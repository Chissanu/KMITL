# PROGRAM: Hello, World!
.data # Data declaration section
out_string: .asciiz "\nHello, Worldsss!\n"
.text # Assembly language instructions
main: # Start of code section
    li $v0, 4 # system call code for printing string = 4
    la $a0, out_string # load address of string to be printed into $a0
    syscall
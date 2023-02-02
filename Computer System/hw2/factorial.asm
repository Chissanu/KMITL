.data
    msg: .asciiz "Enter a number: "
    chosen: .asciiz "You chose: "
    complete: .asciiz "The answer is: "
    space: .asciiz "\n"

.text

main:
    li $v0, 4
    la $a0, msg
    syscall

    li $v0, 5
    syscall

    # Store n times to t0
    move $t0, $v0

    li $v0, 4
    la $a0, chosen
    syscall

    li $v0, 1
    move $a0, $t0
    syscall

    beq $t0, $zero, zero
    syscall

    li $v0,4
    la $a0, space
    syscall

    # Total Values
    li $t1, 1

    # For Looping
    li $t2, 0

loop:
    addi $t2, $t2, 1
    mul $t3, $t2, 1

    mul $t1, $t1, $t3
    beq $t2, $t0, end
    j loop

end:
    li $v0, 4
    la $a0, space
    syscall

    li $v0, 4
    la $a0, complete
    syscall

    li $v0, 1
    move $a0, $t1
    syscall

    li $v0, 10  
    syscall

# Case
zero:
    li $v0, 4
    la $a0, space
    syscall

    li $v0, 4
    la $a0, complete
    syscall

    li $t1, 1

    li $v0, 1
    move $a0, $t1
    syscall

    li $v0, 10  
    syscall

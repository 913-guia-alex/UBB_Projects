bits 32
global start

extern exit
import exit msvcrt.dll

; 4. A byte string s is given. Build the byte string d such that every byte d[i] is equal to the count of ones in the corresponding byte s[i] of s.
; Example:
; s: 5, 25, 55, 127
; in binary:
; 101, 11001, 110111, 1111111
; d: 2, 3, 5, 7

segment data use32 class=data
    s db 5, 25, 55, 127
    len equ $-s
    d resb len

segment code use32 class=code
start:
    mov ecx, len ; loop len times
    jecxz end_program ; jump to the end if ecx is 0

    mov esi, 0 ; initialize string address index for s and d
    loop_string:
        mov al, [s+esi] ; put the current value into al
        xor ebx, ebx ; clear the ebx register because we will count with it
        ; xor ebx, ebx  is faster than  mov ebx, 0
        
        
        shr al, 1 ; move rightmost bit to carry flag
        
        count_ones:
        adc bl, 0 ; add with carry
        shr al, 1 ; move rightmost bit to carry flag
        jnz count_ones ; loop while ZF=1
        
        adc bl, 0 ; count last bit
        
        
        mov [d+esi], bl ; add the count of 1's into d at the index i
        
        inc esi ; increment esi to the next index
    loop loop_string
    
    end_program: ; program end label
    
    ; exit(0)
    push    dword 0      ; push the parameter for exit onto the stack
    call    [exit]       ; call exit to terminate the program

bits 32
global start

extern exit
import exit msvcrt.dll

; 19.  Being given two strings of bytes, compute all positions where the second string appears as a substring in the first string. 

segment data use32 class=data
    a db 1, 2, 3, 1, 2, 4, 1, 3, 1, 2, 5
       ; 0  1  2  3  4  5  6  7  8  9  10
    lenA equ $-a
    
    b db 1, 2
    lenB equ $-b
    
    d resb lenA
    ; 0, 3, 8

segment code use32 class=code
start:
    mov ecx, lenA ; loop lenA times
    jecxz program_end ; jump to the end if ecx is 0
    
    xor ebx, ebx ; index for the current value in d
    ; xor ebx, ebx  is faster than  mov ebx, 0
    
    mov esi, 0 ; the index for the current value in a
    mov edi, 0 ; the index for the current value in b
    loop_string:
        mov al, [a+esi] ; move the current value from a to al
        
        count_appearance: ; count the number of values from the substring that appear in the main string from index esi onwards and stop when we reach a value from a that is not in b
            mov dl, [b+edi] ; move the current value from b to dl
            cmp al, dl ; compare the two values
            jne check_length ; if the values are NOT equal we stop the loop
            
            inc edi ; if the values ARE equal we increment edi (index for b) to check the next value from the substring
        je count_appearance ; we keep looping until we reach a value from the main string that is not in the substring
        
        
        check_length: ; we check if the count from above is equal to the length of the substring
        cmp edi, lenB ; compare the current index for b to the length of b
        jne end_loop ; if they are NOT equal we jump to the next index of a
        
        mov eax, esi ; if they ARE equal we compute the starting position of the subtring appearance by substracting the length of b from esi (esi=ending position from the count_appearance loop)
        inc eax
        sub eax, lenB
        
        mov [d+ebx], al ; if they ARE equal we save the starting index of the substring appearance in d
        inc ebx ; if they ARE equal we increment the current index for d
        mov edi, 0 ; if they ARE equal we reset the current index of b
        
        end_loop:
        inc esi ; increment esi to the next index
    loop loop_string
    
    program_end: ; program end label
    
    ; exit(0)
    push    dword 0      ; push the parameter for exit onto the stack
    call    [exit]       ; call exit to terminate the program

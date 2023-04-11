import paramiko
import time, webbrowser
x=[]
host = "192.168.0.200"
port = 22
username = "pi"
password = "raspberry"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
print("connected")
stdin, stdout, stderr = ssh.exec_command('python try.py')
print("exe")
lines = stdout.readlines()
o=0
for i in (lines):
    x.append(i)
    o=o+1

print(x)
for i in range(int(len(x)/2)):
    webbrowser.open("https://www.google.com/maps/place/"+x[i]+","+x[i+1])
    time.sleep(10)

#import pxssh package used in setup ssh connection
import pxssh
s = pxssh.pxssh()

#get hostnames, username and command from user. Password not required is this is passwrod less authentication
hostnames = raw_input('hostname: ').split(",")
username = raw_input('username: ')
command = raw_input('Enter command: ')

#run loop for all hostnames
for hostname in hostnames
if not s.login (hostname, 'username'):
    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful"
    #run command on each server
    s.sendline (command)
    s.logout()

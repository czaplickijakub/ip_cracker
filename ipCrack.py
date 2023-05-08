#Jakub Czaplicki
#Tool to crack IP hashes
#5/8/23

#Import Tools
import hashlib
import itertools
import datetime
import re

while True:

    #Enter the IP hash to crack 
    hashed_ip = input("Enter the hashed IP address and press enter: ")

    # Check if the input is a valid MD5 hash
    if not re.match(r'^[a-fA-F0-9]{32}$', hashed_ip):
        print("Invalid input: not an MD5 hash.")
        continue

    #Check time to provide metric later
    start_time = datetime.datetime.now()

    #Generate tuples from 0.0.0.0 to 255.255.255.255, hash, then compare to input
    for ip_tuple in itertools.product(range(256), repeat=4):
        ip_address = ".".join(str(i) for i in ip_tuple)

        hashed = hashlib.md5(ip_address.encode('utf-8')).hexdigest()
        
        print(f"Trying {ip_address}")
        if hashed == hashed_ip:
            print("Hashed IP address cracked successfully! The original IP address is:", ip_address)
            print("Please take a moment and write the IP down.")
            break
    else:
        print("Unable to crack the hashed IP address: hash input error.")

    end_time = datetime.datetime.now()

    total_time = end_time - start_time
    hours, remainder = divmod(total_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Total time taken: {hours} hours, {minutes} minutes, {seconds} seconds")

    answer = input("Would you like to run another hash? Press y for yes and n for no and press enter\n")
    if answer.lower() == 'n':
        break
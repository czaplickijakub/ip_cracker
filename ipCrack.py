import hashlib
import itertools
import datetime

while True:

    hashed_ip = input("Enter the hashed IP address and press enter: ")

    start_time = datetime.datetime.now()

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
    if answer.lower() != 'y':
        break
import hashlib
import itertools
import datetime

hashed_ip = input("Enter the hashed IP address: ")

start_time = datetime.datetime.now()

for ip_tuple in itertools.product(range(256), repeat=4):
    ip_address = ".".join(str(i) for i in ip_tuple)
    hashed = hashlib.sha256(ip_address.encode('utf-8')).hexdigest()
    print(f"Trying {ip_address}")
    if hashed == hashed_ip:
        print("Hashed IP address cracked successfully! The original IP address is:", ip_address)
        break
else:
    print("Unable to crack the hashed IP address using every possible IP address combination.")

end_time = datetime.datetime.now()

total_time = end_time - start_time
print(total_time)
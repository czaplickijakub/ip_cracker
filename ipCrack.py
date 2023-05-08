import hashlib
import itertools
import datetime
import pandas as pd

hash_table = pd.DataFrame(columns=['IP', 'SHA1', 'SHA224', 'SHA256', 'MD5'])

start_time = datetime.datetime.now()

for ip_tuple in itertools.product(range(256), repeat=4):
    ip_address = ".".join(str(i) for i in ip_tuple)

    hashed_SHA1 = hashlib.sha1(ip_address.encode('utf-8')).hexdigest()
    hashed_SHA224 = hashlib.sha224 (ip_address.encode('utf-8')).hexdigest()
    hashed_SHA256 = hashlib.sha256(ip_address.encode('utf-8')).hexdigest()
    hashed_MD5 = hashlib.md5(ip_address.encode('utf-8')).hexdigest()

    hash_table.loc[len(hash_table)] = [ip_address, hashed_SHA1, hashed_SHA224, hashed_SHA256, hashed_MD5]
    print(f"Hashing {ip_address}")

hash_table.to_excel('ip_hash_table.xlsx', index=TRUE)

end_time = datetime.datetime.now()

total_time = end_time - start_time
hours, remainder = divmod(total_time.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Total time: {hours} hours, {minutes} minutes, {seconds} seconds")
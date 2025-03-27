import json
import hashlib


json_data = '''
{
    "student": {
        "first_name": "aksha",
        "last_name": "Smith",
        "roll_number": "240350000046"
    }
}
'''

data = json.loads(json_data)


first_name = data['student']['first_name']
roll_number = data['student']['roll_number']


concatenated_string = (first_name + roll_number).lower()


md5_hash = hashlib.md5(concatenated_string.encode()).hexdigest()


with open('output.txt', 'w') as f:
    f.write(md5_hash)

print(f'MD5 Hash: {md5_hash}')
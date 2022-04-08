import re

verify_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")    # Verify email syntax
verify_password = re.compile(r"[A-Za-z0-9!@#$%]{8,}")                          # Verify password criteria
email = 'testaccount7@gmail.com'                                                  # 8 digits, special character
password = 'TestpasW0rd!234'

a = re.fullmatch(verify_email, email)
b = re.fullmatch(verify_password, password)
print(a)
print(b)

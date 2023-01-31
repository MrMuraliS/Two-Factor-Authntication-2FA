import pyotp
import qrcode

# Generate a random secret key
# secret = pyotp.random_base32()
Name = input('Enter Your Name without spaces or Any special characters: ').upper()
while not Name.isalpha():
    Name = input('I said, Enter Your Name without spaces or Any special characters: ')
secret = f"JBSWY3DPEHPK3PXP{Name}"
# print(secret)

# Create a TOTP object
totp = pyotp.TOTP(secret)

uri = totp.provisioning_uri(name=Name, issuer_name="ClearPyCode")
# print(uri)

qrcode.make(uri).save("qrcode.png")

# Print the OTP
print(totp.now())
user_input = int(input('Enter the OTP: '))
# Verify the OTP
print(totp.verify(user_input))

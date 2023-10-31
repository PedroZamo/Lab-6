#encode method
def encode(password):
	new_password = ''
	for char in password:
		new_digit = str((int(char) + 3) % 10)
		new_password += new_digit
	return new_password


#decode method
def decode(encoded_password):
	orig_password = ''
	for char in encoded_password:
		orig_digit = str((int(digit) - 3 + 10) % 10)
		orig_password += orig_digit
	return orig_password


def main():
	print('Please select an option')
	print('1. Encode password')
	print('2. Decode password')
	choice = int(input())
	if choice == 1:
		print('Please enter an 8 digit password to be encoded')
		password = input()
		encoded_pw = encode(password)
		print(f'Encoded password: {encoded_pw}')
	if choice == 2:
		print('Please enter an 8 digit password to be decoded')
		password = input()
		decoded_pw = decode(password)
		print(f'Decoded password: {decoded_pw}')


if __name__ == '__main__'

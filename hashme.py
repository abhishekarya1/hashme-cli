import argparse
import hashlib
import os

#Constants
SHA256 = 'sha256'
MD5 = 'md5'
UTF8 = 'utf-8'

#Util Methods
def generate_hash_md5(file):
	md5_hash = hashlib.md5() 
	content = open(file, "rb").read()
	md5_hash.update(content)
	md5_digest = md5_hash.hexdigest()
	return md5_digest

def generate_hash_sha256(file):
	sha256_hash = hashlib.sha256() 
	content = open(file, "rb").read()
	sha256_hash.update(content)
	sha256_digest = sha256_hash.hexdigest()
	return sha256_digest

def verify_hash(file, algorithm, hash_value):
	if algorithm == MD5:
		if generate_hash_md5(file) == hash_value:
			return "File matches the MD5 hash value provided - VERIFIED."
		else:
			return "File doesn't match the MD5 hash value provided - UNVERIFIED."
	elif algorithm == SHA256:
		if generate_hash_sha256(file) == hash_value:
			return "File matches the SHA256 hash value provided - VERIFIED."
		else:
			return "File doesn't match the SHA256 hash value provided - UNVERIFIED."

def generate_verifile(file):
	with open(f"{os.path.splitext(file)[0]}.verifile",'w', encoding = 'utf-8') as f:
		md5_hash = generate_hash_md5(file)
		sha256_hash = generate_hash_sha256(file)
		f.write(f"MD5: {md5_hash}\nSHA256: {sha256_hash}")

def verify_file(file):
	with open(f"{os.path.splitext(file)[0]}.verifile",'r', encoding = 'utf-8') as f:
		data = f.read().split('\n')
		for i in range(0, 2):
			line = data[i].split(': ')
			algo = line[0]
			hash_val = line[1]
			print(f"{verify_hash(file, algo.lower(), hash_val)}")

def main():
	parser = argparse.ArgumentParser(description='HASH ME CLI: Verify files against hashes to detect tampering.')
	subparser = parser.add_subparsers(dest='command')
  
	cli = subparser.add_parser('cli')
	verifile = subparser.add_parser('verifile')

	cli.add_argument('file', help="file to generate hash for or verify")
	cli.add_argument('-a', '--algo',
			choices=[MD5, SHA256],
			help="specifies hashing algorithm, default is MD5",
			default=MD5)
	cli.add_argument('-v', '--hash',
			help="provide hash value for specified algorithm")

  
	verifile.add_argument('file', help="file to generate verifile for")
	verifile.add_argument('-v', '--verify',
			action='store_true',
			help="toggle verify mode")

	args = parser.parse_args()

	if args.command == 'cli':
		if args.hash:   #hash value is present; md5 is default
			print(verify_hash(args.file, args.algo, args.hash))
		elif args.algo:   #algo is specified but no hash value
			print(f"MD5: {generate_hash_md5(args.file)}") if args.algo == MD5 else print(f"SHA256: {generate_hash_sha256(args.file)}")
		else:       #file will always be there
			md5_hash = generate_hash_md5(args.file)
			sha256_hash = generate_hash_sha256(args.file)
			print(f"MD5: {md5_hash}\nSHA256: {sha256_hash}")

	elif args.command == 'verifile':
		if args.verify:
			try:
				verify_file(args.file)
			except FileNotFoundError as e:
				print(e)
		else:
			generate_verifile(args.file)


#main
if __name__ == '__main__':
	main()
import argparse
import hashlib

#Constants
SHA256 = 'sha256'
MD5 = 'md5'

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
			return "File matches the hash value provided - VERIFIED."
		else:
			return "File doesn't match the hash value provided - UNVERIFIED."
	elif algorithm == SHA256:
		if generate_hash_sha256(file) == hash_value:
			return "File matches the hash value provided - VERIFIED."
		else:
			return "File doesn't match the hash value provided - UNVERIFIED."

def main():
	parser = argparse.ArgumentParser(description='HASH ME CLI: Verify files against hashes to detect tampering.')
	parser.add_argument('file', help="file to generate hash for or verify")
	parser.add_argument('-a', '--algo',
						choices=[MD5, SHA256],
						help="specifies hashing algorithm, default is MD5",
						default=MD5)
	parser.add_argument('-v', '--hash',
						help="provide hash value for specified algorithm")

	args = parser.parse_args()

	if args.hash:		#hash value is present; md5 is default
		print(verify_hash(args.file, args.algo, args.hash))
	elif args.algo:		#algo is specified but no hash value
		print(f"MD5: {generate_hash_md5(args.file)}") if args.algo == MD5 else print(f"SHA256: {generate_hash_sha256(args.file)}")
	else:				#file will always be there
		md5_hash = generate_hash_md5(args.file)
		sha256_hash = generate_hash_sha256(args.file)
		print(f"MD5: {md5_hash}\nSHA256: {sha256_hash}")

#main
if __name__ == '__main__':
	main()
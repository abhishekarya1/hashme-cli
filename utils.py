import os
import hashlib

from constants import MD5, SHA256, UTF8

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
	else:
		return "Invalid algorithm specified."		

def file_gen(file):
	with open(f"{file}.verifile", 'w', encoding='utf-8') as f:
		md5_hash = generate_hash_md5(file)
		sha256_hash = generate_hash_sha256(file)
		f.write(f"MD5={md5_hash}\nSHA256={sha256_hash}")
	print('Verifile generated successfully.')

def generate_verifile(file):
	if(os.path.splitext(file)[1] == '.verifile'):
		print("Are you sure you want to create verifile for an existing verifile? (y/n):")	
		while(True):
			inp = str(input())
			if inp.lower() == 'n':
				print("No verifile generated.")
				break
			elif inp.lower() == 'y':
				file_gen(file)
				break
			else:
				print('Invalid option. Please choose from (y/n):')
				continue
	else: 
		file_gen(file)

def verify_file(file):
	with open(f"{file}.verifile", 'r', encoding='utf-8') as f:
		data = f.read().split('\n')
		for i in range(len(data)):
			line = data[i].split('=')
			algo = line[0]
			hash_val = line[1]
			print(f"{verify_hash(file, algo.lower(), hash_val)}")
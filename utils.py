import os
import hashlib

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
    with open(f"{os.path.splitext(file)[0]}.verifile", 'w',
              encoding='utf-8') as f:
        md5_hash = generate_hash_md5(file)
        sha256_hash = generate_hash_sha256(file)
        f.write(f"MD5: {md5_hash}\nSHA256: {sha256_hash}")


def verify_file(file):
    with open(f"{os.path.splitext(file)[0]}.verifile", 'r',
              encoding='utf-8') as f:
        data = f.read().split('\n')
        for i in range(0, 2):
            line = data[i].split(': ')
            algo = line[0]
            hash_val = line[1]
            print(f"{verify_hash(file, algo.lower(), hash_val)}")


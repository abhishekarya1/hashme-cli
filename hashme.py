import argparse
import hashlib


def generate_hash(file):
    md5_hash = hashlib.md5()
    a_file = open(file, "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest


def verify_hash(file, hash):
    if generate_hash(file) == hash:
        return "File matches the hash value provided - VERIFIED."
    else:
        return "File doesn't match the hash value provided - UNVERIFIED."


def main():
    parser = argparse.ArgumentParser(description='HASH ME CLI')
    parser.add_argument('file', help="generates MD5 hash")
    parser.add_argument('-v',
                        '--verify',
                        dest='hash',
                        help="verify file against MD5 hash")
    args = parser.parse_args()

    if args.hash:
        print(verify_hash(args.file, args.hash))
    else:
        print(f"MD5: {generate_hash(args.file)}")


if __name__ == '__main__':
    main()
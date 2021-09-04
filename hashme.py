import argparse

import pyfiglet
import pyperclip

from utils import generate_hash_sha256, verify_hash, generate_verifile, verify_file
from constants import MD5, SHA256, UTF8


def main():
	desc_str = pyfiglet.figlet_format("Hash Me", font="Slant")
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description=desc_str,
		epilog="Simple utility to generate hashes and verify files with them.")
	subparser = parser.add_subparsers(dest='command')

	cli = subparser.add_parser('cli')
	verifile = subparser.add_parser('verifile')

	cli.add_argument('file', help="file to generate hash for or verify")
	cli.add_argument('-a',
					 '--algo',
					 choices=[MD5, SHA256],
					 help="specifies hashing algorithm, default is MD5")
	cli.add_argument('-v',
					 '--hash',
					 help="provide hash value for specified algorithm")
	cli.add_argument('-c',
					 '--clipboard',
					 action='store_true',
					 help="copies hash value(s)to clipboard")

	verifile.add_argument('file', help="file to generate verifile for")
	verifile.add_argument('-v',
						  '--verify',
						  action='store_true',
						  help="toggle verify mode")

	args = parser.parse_args()

	if args.command == 'cli':
		if args.hash:  #hash value is present; md5 is default
			print(verify_hash(args.file, MD5, args.hash))
		elif args.algo:  #algo is specified but no hash value
			print(f"MD5: {generate_hash_md5(args.file)}") if args.algo == MD5 else print(f"SHA256: {generate_hash_sha256(args.file)}")
			if args.clipboard:
				clip_str =  f"{generate_hash_md5(args.file)}" if args.algo == MD5 else f"{generate_hash_sha256(args.file)}"
				pyperclip.copy(clip_str)
				pyperclip.paste()
				print("Hash copied to clipboard.")
		else:  #file will always be there
			md5_hash = generate_hash_md5(args.file)
			sha256_hash = generate_hash_sha256(args.file)
			print(f"MD5: {md5_hash}\nSHA256: {sha256_hash}")
			if args.clipboard:
				pyperclip.copy(f"MD5: {md5_hash}\nSHA256: {sha256_hash}")
				pyperclip.paste()
				print("Hashes copied to clipboard.")

	elif args.command == 'verifile':
		if args.verify:
			try:
				verify_file(args.file)
			except FileNotFoundError as e:
				print(e)
		else:
			try:
				generate_verifile(args.file)
			except BaseException as e:
				print(e)


#main
if __name__ == '__main__':
	main()
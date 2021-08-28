# hashme-cli ✔️
A simple command line utility to generate hashes and verify if your files have been tampered with.

## Installation
Hashme uses `argparse` and `hashlib`, both of which are included already in Python standard library. No need to install anything.

## Modes
- **CLI Mode**: 
	- generates hash and display to console
	- takes all inputs from command line
	- ouptuts verification result to command line

- **Verifile Mode**: 
	- generates hash using _both_ (`md5` and `sha256`) algorithms and saves to `<filename>.verifile` in the current directory
	- takes input from `<filename>.verifile` that should exist in the current directory
	- verify against _both_ (`md5` and `sha256`) algorithms and ouptut results to console

## Usage/Examples
- File(s) need to be in the same directory as the utility.
- Two hashing algorithms are available: faster `MD5` and robust `SHA256`.

```sh
$ hashme [-h] {cli,verifile} ...
$ hashme cli [-h] [-a {md5,sha256}] [-v HASH] file 			#cli mode
$ hashme verifile [-h] [-v] file 					#verifile mode
```

```sh
#generation
$ py hashme.py file				#to generate hash, MD5 is default
$ py hashme.py cli -a algorithm file

# verification
$ py hashme.py cli -v hash file		#to verify file against hash (assumed to be MD5 by default)
$ py hashme.py cli --hash hash file

$ py hashme.py cli -a algorithm -v hash file		#explicitly specifying algorithm
$ py hashme.py cli --algo algorithm --hash hash file

# file mode
$ py hashme.py verifile file
$ py hashme.py verifile -v file
```

## Executable
Executable is generated with `pyinstaller`.

```sh
$ pyinstaller --onefile "hashme.py"
```

Checkout latest release (`.exe`) [here](https://github.com/abhishekarya1/hashme-cli/releases).

## Further
- Hashing entire folder recursively and generate hash file to be verified with later (like QuickSFV)
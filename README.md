# hashme-cli ✔️
A simple command line utility to generate hashes and verify if your files have been tampered with.

## Installation
```sh
$ pip install -r requirements.txt
```
- Hashme uses `argparse` and `hashlib`, both of which are included already in Python3 standard library
- `pyfiglet` is used for stylized description text on help
- `pyperclip` is used to copy text to clipboard

## Modes
- **CLI Mode**: 
	- generates hash and display to console
	- takes all inputs from command line
	- ouptuts verification result to command line
	- copies hash to clipboard if `-c` flag is present

![cli_mode](https://i.imgur.com/4XgegXW.png)

- **Verifile Mode**: 
	- generates hash using _both_ (`md5` and `sha256`) algorithms and saves to `<filename>.verifile` in the current directory
	- takes input from `<filename>.verifile` that should exist in the current directory
	- verify against _both_ (`md5` and `sha256`) algorithms and ouptut results to console

![verifile_mode](https://i.imgur.com/5g79qng.png)

## Usage/Examples
- File(s) need to be in the same directory as the utility.
- Two hashing algorithms are available: faster `MD5` and robust `SHA256`.

```sh
$ hashme [-h] {cli,verifile} ...
$ hashme cli [-h] [-a {md5,sha256}] [-v HASH] [-c] file 		#cli mode
$ hashme verifile [-h] [-v] file 			                #verifile mode
```

```sh
#generation
$ py hashme.py cli file				#to generate hash, MD5 is default
$ py hashme.py cli -a algorithm file

$ py hashme.py cli -c file 	                #generate hash and copy to clipboard
$ py hashme.py cli --clipboard file

# verification
$ py hashme.py cli -v hash file		        #to verify file against hash (assumed to be MD5 by default)
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

#after pyfigment addition (fix for font not found issue)
$ pyinstaller --onefile --add-data "venv\Lib\site-packages\pyfiglet;./pyfiglet" hashme.py
```

Checkout latest release (`.exe`) [here](https://github.com/abhishekarya1/hashme-cli/releases).

## Further
- Hashing entire folder recursively and generate hash file to be verified with later (like QuickSFV)

## References
- [Argparse Tutorial = YouTube](https://youtu.be/Y2Vatkp4Y6M)
- https://docs.python.org/3/library/argparse.html
- https://docs.python.org/3/howto/argparse.html
- [A Simple Guide To Command Line Arguments With ArgParse - towards data science](https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3)
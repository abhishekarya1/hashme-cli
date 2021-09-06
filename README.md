# hashme-cli ✔️
A simple command line utility to generate hashes and verify if your files have been tampered with.

![help](https://i.imgur.com/nEuAHbi.png)

## Installation
```sh
$ pip install -r requirements.txt
```
- Hashme mainly uses `argparse` and `hashlib`, both of which are included already in Python3 standard library
- [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) is used for stylized description text on help
- [pyperclip](https://pypi.org/project/pyperclip/) is used to copy text to clipboard

## Modes
- **CLI Mode**: 
	- generates hash and display to console
	- takes all inputs from command line; ouptuts verification result to command line
	- copies hash to clipboard if `-c` flag is present

![cli_mode](https://i.imgur.com/fSTY6cA.png)

- **Verifile Mode**: 
	- generates hash using _both_ (`md5` and `sha256`) algorithms and saves to `<filename>.verifile` in the current directory
	- takes input from `<filename>.verifile` that should exist in the current directory
	- verify against _both_ (`md5` and `sha256`) algorithms and outputs results to console

![verifile_mode](https://i.imgur.com/jcHODqn.png)

- **Verifolder Mode**: 
	- generates hash for all files in a folder using `md5` algorithm and saves to `<path>/verifolder/verifile.md5` (no folders)
	- uses well-known [SFV](https://en.wikipedia.org/wiki/Simple_file_verification) file format compatible with most popular sfv tools
	- takes `path` input from cli, it should be a valid path on filesystem
	- verifies all specified files and outputs results (`OK`, `BAD`, `MISSING`) to console for each file

![verifolder_mode](https://i.imgur.com/GHlZqK9.png)

## Usage/Examples
- File(s) need to be in the same directory as the utility for cli and verifile modes.
- In folder mode, a folder named (`/verifolder`) is created inside target directory that will have `verifile.md5` for all _files_ (not folders) in directory pointed to by `path`. 
- Two hashing algorithms are available: faster `MD5` and robust `SHA256`.

```sh
$ hashme [-h] {cli,verifile,verifolder} ...
$ hashme cli [-h] [-a {md5,sha256}] [-v HASH] [-c] file 		#cli mode
$ hashme verifile [-h] [-v] file 			                #verifile mode
$ hashme verifolder [-h] [-p PATH | -v]					#verifolder mode
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

# folder mode
$ py hashme.py verifile "path"
$ py hashme.py verifile -v
```

## Executable (.exe)
Executable is generated with `pyinstaller`.

```sh
$ pyinstaller --onefile "hashme.py"

#after pyfigment addition (fix for font not found issue)
$ pyinstaller --onefile --add-data "venv\Lib\site-packages\pyfiglet;./pyfiglet" hashme.py
```

Checkout latest release (`.exe`) [here](https://github.com/abhishekarya1/hashme-cli/releases).

## Further
- Hashing entire folder recursively

## References
- [Argparse Tutorial - YouTube](https://youtu.be/Y2Vatkp4Y6M)
- https://docs.python.org/3/library/argparse.html
- https://docs.python.org/3/howto/argparse.html
- [A Simple Guide To Command Line Arguments With ArgParse - towards data science](https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3)
- http://pure-sfv.sourceforge.net/faqsfv.html#4.a
- [Why not CRC32? -> can detect change; but not secure as making files having same hash is easier](https://stackoverflow.com/a/16122368)

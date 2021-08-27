# hashme-cli ✔️
A simple command line utility to generate hashes and verify if your files have been tampered with.

## Installation
Hashme uses `argparse` and `hashlib`, both of which are included already in Python standard library. No need to install anything.

## Usage/Examples
- File needs to be in the same directory as the utility.
- Two hashing algorithms are available: faster `MD5` and robust `SHA256`.

```sh
$ hashme [-h] [-a {md5,sha256}] [-v HASH] file
```

```sh
$ py hashme.py file					#to generate hash, MD5 is default

$ py hashme.py -a algorithm -v hash file 		#to verify file against hash (assumed to be MD5 by default)
$ py hashme.py --algo algorithm --hash hash file
```

## Executable
Executable is generated with `pyinstaller`.

```sh
$ pyinstaller --onefile "hashme.py"
```

Checkout latest release (`.exe`) [here](https://github.com/abhishekarya1/hashme-cli/releases).

## Further
- Support for other hashing algorithms (`MD2` `MD4` `MD5` `SHA1` `SHA256` `SHA384` `SHA512`)
- Exporting hash to file (`filename.verifile`)
- Hashing entire folder recursively and generate hash file to be verified with later (like QuickSFV)
- "Swag-ify" and `--help` documentation
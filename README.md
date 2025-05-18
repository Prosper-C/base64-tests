# Base64 Encoder/Decoder Tests

This project contains unit tests for validating the functionality of a Base64 encoder and decoder using Python's built-in `base64` module.

## ✅ Features

- ✔️ Tests random binary data encoding/decoding using `os.urandom`
- ✔️ Ensures invalid Base64 strings result in a non-zero exit code
- ✔️ All tests written using `unittest`
- ✔️ CI pipeline using GitHub Actions to automatically test on every push

## 🔬 How to Run the Tests

Run the following in terminal:

```bash
python -m unittest discover -s . -p "test_*.py"

import unittest
import base64
import os
import sys
import subprocess

class TestBase64EncoderDecoder(unittest.TestCase):

    def test_base64_encoding_random(self):

        for _ in range(5):
            data = os.urandom(16)
            encoded = base64.b64encode(data)
            decoded = base64.b64decode(encoded)
            self.assertEqual(decoded, data)

    def test_base64_decoding_invalid_data(self):

        script = """
import base64
import sys
try:
    base64.b64decode(b'!!!notbase64!!!', validate=True)
except Exception:
    sys.exit(1)
sys.exit(0)
"""
        result = subprocess.run([sys.executable, "-c", script])
        self.assertNotEqual(result.returncode, 0)

if __name__ == "__main__":
    unittest.main()

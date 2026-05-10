import os
import sys
import subprocess

# Install requirements
subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    "-q",
    "-r",
    "requirements.txt"
])

# Download features nếu chưa có
if not os.path.exists("features/"):
    subprocess.check_call([
        sys.executable,
        "download.py"
    ])
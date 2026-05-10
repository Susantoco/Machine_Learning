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

# Download data nếu chưa có
if not os.path.exists("features/raw"):
    subprocess.check_call([
        sys.executable,
        "download.py"
    ])

print("Setup completed.")
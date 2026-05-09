import os

os.system("pip install -q -r requirements.txt")

if not os.path.exists("features/raw"):
    os.system("python download.py")
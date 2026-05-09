import os

if not os.path.exists("/content/Machine_Learning"):
    os.system(
        "git clone https://github.com/Susantoco/Machine_Learning.git"
    )

os.chdir("/content/Machine_Learning")

os.system("pip install -q -r requirements.txt")

if not os.path.exists("features/raw"):
    os.system("python download.py")
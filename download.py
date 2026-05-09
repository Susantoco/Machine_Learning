import os
import gdown

os.makedirs("features", exist_ok=True)

url = "https://drive.google.com/drive/folders/1-8VtHC916P6kavmyP72kjjJlF_cSepsj"

gdown.download_folder(
    url=url,
    output="features",
    quiet=False,
    use_cookies=False
)
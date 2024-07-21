import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


packages = ["requests", "colorama"]

for package in packages:
    install(package)

print("Gerekli paketler yüklendi.")

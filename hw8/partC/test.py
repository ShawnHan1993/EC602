import subprocess
import os

T = subprocess.run(['dir'])
Files = T.stdout.decode().splitlines()

OSfiles = os.listdir('.')

print(Files)
print(OSfiles)
assert sorted(Files) == OSfiles
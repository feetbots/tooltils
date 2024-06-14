from subprocess import CalledProcessError, run
from shutil import copyfileobj, rmtree
from tarfile import open as topen
from gzip import open as gopen
from time import sleep
from os import remove
import sys

if sys.platform.startswith("win"):
    split: str = '\\'
else:
    split: str = '/'

sys.path.insert(0, split.join(__file__.split(split)[:-2]))

from tooltils.requests import verifiable
from tooltils.info import version


basic: bool = not verifiable()

if basic:
    print("\nUnable to verify, falling back on basic setup.py build method\n")
    sleep(0.5)

def call(cmd: list, shell: bool=False) -> int:
    try:
        return run(cmd, check=True, shell=shell).returncode
    except CalledProcessError:
        exit(1)


try:
    rmtree("dist", True)
    rmtree("tooltils.egg-info", True)
    rmtree("build", True)
except Exception:
    pass

if basic:
    call([sys.executable, "setup.py", "sdist", "bdist_wheel"])

    rmtree("build", True)
else:
    call([sys.executable, "-m", "build"])

try:
    input("\n\u001b[31;1mopen built file directory...\u001b[0;0m")
except KeyboardInterrupt:
    print("")
    sys.exit(0)

with gopen(f"dist{split}tooltils-{version}.tar.gz", "rb") as _f, \
     open(f"dist{split}tooltils-{version}.tar", "wb") as _f2:
    copyfileobj(_f, _f2)

with topen(f"dist{split}tooltils-{version}.tar") as _f:
    _f.extractall(f"dist{split}tooltils-{version}", filter="data")

remove(f"dist{split}tooltils-{version}.tar")

call([("open" if split == '/' else "start"), f"dist{split}tooltils-{version}{split}tooltils-{version}"])

# pip install dist/tooltils-{version}.tar.gz --break-system-packages
# pip uninstall tooltils --break-system-packages

from subprocess import CalledProcessError, run
from ssl import SSLCertVerificationError
from http.client import HTTPSConnection
from shutil import copyfileobj, rmtree
from tarfile import open as topen
from gzip import open as gopen
from sys import exit, platform
from socket import gaierror
from typing import Union
from time import sleep
from os import remove


if platform.startswith('win'):
    split: str = '\\'
else:
    split: str = '/'

version: str = '1.6.0'
basic:  bool = False

try:
    HTTPSConnection('httpbin.org', timeout=3).request('HEAD', '/get')
except (SSLCertVerificationError, gaierror, TimeoutError):
    basic: bool = True

    print('\nUnable to verify, falling back on basic setup.py build method\n')
    sleep(0.75)

def call(cmd: Union[str, list], shell: bool=False) -> int:
    try:
        return run(cmd, check=True, shell=shell).returncode
    except CalledProcessError:
        exit(1)

try:
    rmtree('dist', True)
    rmtree('tooltils.egg-info', True)
    rmtree('build', True)
except:
    pass

if basic:
    call(['python3.12' if split == '/' else 'py', 'setup.py', 'sdist', 'bdist_wheel'])

    rmtree('build', True)
else:
    call(['python3.12' if split == '/' else 'py', '-m', 'build'])

try:
    input('\nopen built file directory...')
except KeyboardInterrupt:
    exit(0)

with gopen(f'dist{split}tooltils-{version}.tar.gz', 'rb') as _f, open(
     f'dist{split}tooltils-{version}.tar', 'wb') as _f2:
    copyfileobj(_f, _f2)

with topen(f'dist{split}tooltils-{version}.tar') as _f:
    _f.extractall(f'dist{split}tooltils-{version}')

remove(f'dist{split}tooltils-{version}.tar')
call('open' if split == '/' else 'start' + f' dist{split}tooltils-{version}{split}tooltils-{version}', True)

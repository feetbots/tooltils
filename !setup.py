from setuptools import setup

from .src.info import version


with open('README.md') as _f:
    desc: str = _f.read()

setup(
    name='tooltils',
    description='A lightweight python utility package built on the standard library',
    long_description=desc,
    version=version,
    license='MIT',
    author='feetbots',
    author_email='pheetbots@gmail.com',
    packages=['tooltils',],
    ext_modules=[],
    package_dir={'': "src"},
)

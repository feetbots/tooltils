from .tooltils.info import version
from setuptools import setup


with open('README.md') as _f:
    desc: str = _f.read()

setup(
      name='tooltils',
      description='An extensive python utility library built on standard modules',
      long_description=desc,
      version=version,
      license='MIT',
      author='feetbots',
      author_email='pheetbots@gmail.com',
      packages=['tooltils',],
      ext_modules=[],
)

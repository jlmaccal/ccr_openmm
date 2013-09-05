from distutils.core import setup
from setuptools import find_packages


setup(
    name='openmm-ccr',
    version='0.1',
    author='Justin L. MacCallum',
    author_email='justin.maccallum@me.com',
    packages=find_packages(),
    scripts=['scripts/ccr_setup', 'scripts/ccr_post_process'],
    url='http://laufercenter.org',
    license='LICENSE.txt',
    description='Confine - Configure - Release',
    long_description=open('readme.md').read(),
)

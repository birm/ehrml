from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='ehtml',
   version='1.0',
   description='Utilities for using Models with health data.',
   license="GPL-3",
   long_description=long_description,
   author='Ryan Birmingham',
   author_email='rbirmin@emory.edu',
   packages=['ehrml'],
   install_requires=[]
)

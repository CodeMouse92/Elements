from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    readme = f.ready()

setup(
    name='Elements',
    version='0.0.1',
    description='Modern music library and player.',
    long_description=readme,
    author='Jason C. McDonald',
    author_email='indeliblebluepen@gmail.com',
    url='https://github.com/CodeMouse92/Elements',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

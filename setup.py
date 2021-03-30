#!/usr/bin/env python3
from setuptools import find_packages, setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='elements-app',
    version='0.1.0',
    description='Modern music curation.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jason C. McDonald',
    author_email='codemouse92@outlook.com',
    url='https://github.com/codemouse92/elements',
    project_urls={
        'Bug Reports': 'https://github.com/codemouse92/elements/issues',
        'Funding': 'https://github.com/sponsors/CodeMouse92',
        'Source': 'https://github.com/codemouse92/elements',
    },
    keywords='music, audio',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: X11 Applications :: Qt',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        ],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),

    include_package_data=True,

    python_requires='>=3.6, <4',
    install_requires=[
        'appdirs >= 1.4.4',
        'PySide2 >= 5.15.2',
        'mutagen >= 1.45.1',
        'musicbrainzngs >= 0.7.1'
    ],

    extras_require={
        'test': ['ward'],
    },

    entry_points={
          'gui_scripts': [
              'elements-app = elements.__main__:main'
          ]
      }
)

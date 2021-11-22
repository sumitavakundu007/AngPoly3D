"""A setuptools based setup module."""

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
        name='AngPoly3D',
        version='0.0.1',
        description='A Python package to calculate the angle between the oreintation of a particle and a global reference orientation considering the particle\'s point group symmetry',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/sumitavakundu007/AngPoly3D',
        author='Sumitava Kundu',
        author_email='kundusumitava@gmail.com',
        classifiers=[
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            ],
        keywords='sample, setuptools, development', 
        packages=['AngPoly3D'],
        python_requires='>=3.6',
        install_requires=['rowan'],
        
        entry_points={
                'console_scripts': [
                'AngPoly3D=AngPoly3D.ang_poly3d:ang_poly3d_func',
            ],
        },
        
        project_urls={  # Optional
            'Bug Reports': 'https://github.com/sumitavakundu007/AngPoly3D/issues',
            'Say Thanks!': 'http://saythanks.io/to/example',
            'Source': 'https://github.com/sumitavakundu007/AngPoly3D/',
            },
        )

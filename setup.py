# -*- coding: utf-8 -*-
from io import open
from setuptools import setup

"""
:authors: drygdryg
:license: MIT
:copyright: (c) 2020 drygdryg
"""

version = '0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wpspin',
    version=version,
    description='WPS PIN generator written in Python 3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',

    author='drygdryg',
    author_email='drygdryg2014@yandex.com',
    url='https://github.com/drygdryg/wpspin',
    download_url='https://github.com/drygdryg/wpspin/archive/v{}.zip'.format(version),

    keywords='wireless wifi wpa wps generator pin code',

    packages=['wpspin'],
    python_requires='>=3.4',
    entry_points={
        'console_scripts': [
            'wpspin = wpspin.wpspin:main'
        ]
    },

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Topic :: Security',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)

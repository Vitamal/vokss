import json
import os
from setuptools import setup, find_packages



setup(
    name='vokss',
    description='The vokss django project.',
    version=1,
    author='Vitamal',
    packages=find_packages(exclude=['manage']),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)

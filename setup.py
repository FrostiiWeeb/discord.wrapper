from setuptools import setup
import re

with open('discord/wrapper/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open("README.md", "r") as f:
	long_desc = f.read()

setup(
name="discord.wrapper",
author="Alex Hutz",
author_email="frostiiweeb@gmail.com",
keywords=["discord"],
version=version,
packages=['discord.wrapper'],
license='MIT',
long_description=long_desc,
long_description_content_type="text/markdown",
description="An API wrapper for discord.",
install_requires=['aiohttp>=3.7.3'],
python_requires='>=3.7.1',
url="https://discordwrapper.readthedocs.io/en/latest",
classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
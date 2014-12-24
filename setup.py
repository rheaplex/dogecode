import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dogecode",
    version = "0.0.1",
    author = "Rob Myers",
    author_email = "rob@robmyers.org",
    description = ("Representing and running programs as Dogeparty tokens."),
    license = "GPLv3+",
    keywords = "dogeparty",
    url = "http://robmyers.org/dogecode",
    packages=['dogecode'],
    scripts=['bin/dcc', 'bin/dcsend', 'bin/dcrun'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Development",
        "License :: OSI Approved :: GPL License",
    ],
)

from __future__ import unicode_literals
from setuptools import setup, find_packages


def parse_requirements(requirements):
    # load from requirements.txt
    with open(requirements) as f:
        return [l.strip() for l in f if not l.startswith('#')]


PACKAGE_NAME = "PyDejavu"
PACKAGE_VERSION = "0.1.3"
SUMMARY = 'Dejavu: Audio Fingerprinting in Python'
DESCRIPTION = """
Audio fingerprinting and recognition algorithm implemented in Python

See the explanation here:

`http://willdrevo.com/fingerprinting-and-audio-recognition-with-python/`__

Dejavu can memorize recorded audio by listening to it once and fingerprinting
 it. Then by playing a song and recording microphone input or on disk file,
 Dejavu attempts to match the audio against the fingerprints held in the
 database, returning the song or recording being played.

__ http://willdrevo.com/fingerprinting-and-audio-recognition-with-python/
"""
REQUIREMENTS = parse_requirements("requirements.txt")

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=SUMMARY,
    long_description=DESCRIPTION,
    author='Will Drevo',
    author_email='will.drevo@gmail.com',
    maintainer="Will Drevo",
    maintainer_email="will.drevo@gmail.com",
    url='http://github.com/tuxdna/dejavu',
    license='MIT License',
    include_package_data=True,
    packages=find_packages(),
    platforms=['Unix'],
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords="python, audio, fingerprinting, music, numpy, landmark",
)

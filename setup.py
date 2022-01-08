from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A Speech Recognition tool for MySQL Database Management'
LONG_DESCRIPTION = 'This library is built to convert user voice commands into sql commands by catching keywords spoken by the user using Artificial Intelligence of speech recognition.'

# Setting up
setup(
    name="MySQLvoice",
    version=VERSION,
    author="Hari Om, Abhisekh Kumar Jha, Rajsekhor Saikia",
    author_email="hari_202000004@smit.smu.edu.in"
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    packages=find_packages(),
    install_requires=['SpeechRecognition', 'pyaudio', 'mysql-connector-python' ],
    keywords=["mycursor","tablename1","tablename2","t1c1","t1c2","t1c3","t2c1","t2c2"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Data Scientist/Analyst",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
        "Operating System :: Microsoft :: Windows",
    ]
)
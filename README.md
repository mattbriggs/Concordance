# Concordance
Written in 2016 by Matt Briggs

This program will count all of the words in the file and export a CSV named Indexof_<inputfilename>.csv. You can use this repository to create a command-line utility for the Mac and PC with Pyinstaller.

## Operation of the application
The command-line application will ask for a filename. It will take a text only file (UTF-8). The application will then parse the file and count each word. A word is defined by any string between spaces. The app will produce a comma delimited file (CSV) with the each string in alpha order and the count in the source file.

## Application Set Up
The application requires:
Python 3+
CMD (Lib/cmd.py) For more information see: https://docs.python.org/3.6/library/cmd.html

**Optionally**: You can use Pyinstaller with the two stubbed out scripts to create command-line utilities for the Mac or PC. There is a small shell script for the PC (build.cmd) and a bash script for the Mac (Build.sh). Make sure both scripts point to the directory that contains these python files.

For more information about Pyinstaller and steps on installing Pyinstaller see:
http://www.pyinstaller.org
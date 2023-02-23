# Chrome-Extension-Check
Analyze Google Chrome extensions for dangerous permissions and keylogger code

The argparse, os, re, and json packages are included in the standard library of Python, which means they are available by default and do not require any additional installation. Therefore, no additional packages need to be installed to run this script.


usage: 


python3 ChrmExAna.py -h
usage: ChrmExAna.py [-h] [-p PATH]

Analyze Google Chrome extensions for dangerous permissions and keylogger code

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the directory containing the extensions 
                        For Windows, the path is C:\Users\<username>\AppData\Local\Google\Chrome\UserData\Default\Extensions 
                        For macOS, the path is /Users/<username>/Library/ApplicationSupport/Google/Chrome/Default/Extensions/ 
                        For Linux, the path is ~/.config/google-chrome/Default/Extensions/

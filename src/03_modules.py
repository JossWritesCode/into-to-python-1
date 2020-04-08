"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
print(sys.argv[0])
# Print out the command line arguments in sys.argv, one per line:

for x in sys.argv:
    print("Argument: ", x)

# Print out the OS platform you're using:

print(sys.platform, "sys.platform")

# Print out the version of Python you're using:

print(sys.version)
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID

print(os.getpid(), "os.getpid()")
# Print the current working directory (cwd):

print(os.getcwd(), "os.getcwd()")
# Print out your machine's login name

print(os.getlogin(), "os.getlogin()")

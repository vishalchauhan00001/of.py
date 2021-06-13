Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> filename = input("Input the Filename:abc.py")
Input the Filename:abc.py
>>> f_extns = filename.split(".")
>>> print ("The extension of the file is :python " + repr(f_extns[-1]))
The extension of the file is :python ''
>>> 
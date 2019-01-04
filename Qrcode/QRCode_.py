from qrtools import QR
import os


bookmark=u"EBKM:TITLE:My Blog;URL:https://ralgozino.wordpress.com/;;"
myCode = QR(data=bookmark)
myCode.encode()
os.system("mv " + myCode.filename + " ~/Desktop")
print myCode
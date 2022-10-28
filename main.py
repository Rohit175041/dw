# importing the module
import pywhatkit
i = 1
while i < 10:
    pywhatkit.sendwhatmsg("+91-8799743125", "Hello sir", 20, 9 + i)
    i = i+1
print("Successfully Sent!")
# install
# pip install pywhatkit
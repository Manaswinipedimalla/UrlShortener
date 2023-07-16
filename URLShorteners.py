import pyshorteners as s

Copied_Url=input("please paste Your URL HERE : ")
Shorten_Url=s.Shortener().tinyurl.short(Copied_Url)
print("Shorten URL: ",Shorten_Url)
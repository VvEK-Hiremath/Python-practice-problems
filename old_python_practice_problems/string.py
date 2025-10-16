str1 = "Hello,World,hi,how,are,u"
stripped = str1.split(",")
str2 = "\t".join(stripped)
print(str1)
print(stripped)
print(str2)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)
    print(thisdict[x])
for x in thisdict.values():
    print(x)
for x in thisdict.items():
    print(x)

# copy
abc=thisdict.copy()
print(abc)
newdis= dict(thisdict)
print(newdis)
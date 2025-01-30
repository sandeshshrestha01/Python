thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)
# print(thisdict["model"])
x= thisdict.keys()
y=thisdict.values()
z= thisdict.items()
print(y)
print(z)
print(x)
thisdict["color"]= "red"
print(x)
thisdict.update({"year": 2024})
thisdict.update({"price": 2000000})
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.pop("model")
print(thisdict)
del thisdict["color"]
print(thisdict)
thisdict.clear()
print(thisdict)
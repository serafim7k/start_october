thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

print(len(thisdict))

print(type(thisdict))

x = thisdict["model"]

x = thisdict.get("model")

x = thisdict.keys()

thisdict["year"] = 2018

thisdict.update({"year": 2020})

thisdict["color"] = "red"
print(thisdict)

thisdict.update({"color": "red"})

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)

a = {b: b**2 for b in range(5)}
print(a)

a = dict.fromkeys(range(5), True)
print(a)

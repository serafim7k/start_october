newDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(newDict)

print(newDict["brand"])

newDict["year"] = 2018

print(newDict)

newDict["color"] = "red"
print(newDict)

newDict.pop("model")
print(newDict)

otherDict = {}

otherDict = {i: i for i in range(10)}

print(otherDict)
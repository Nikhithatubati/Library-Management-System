
a = {
  "Index": 1,
  "Model": "2019",
  1: 2,
  2:1
}
import json
with open('file.txt', 'w') as file:    # Writing to file here
    file.write(json.dumps(a))
file.close()

with open('file.txt') as file:         # Reading the file here
    data = json.load(file)
    print (data)
file.close()

data["type"] = "dictionary"            # Adding item to dictionary
print(data)

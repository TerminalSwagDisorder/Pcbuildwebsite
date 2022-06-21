from pcpartpicker import API
import json
import os

fPath = os.path.abspath(os.path.realpath(__file__))
dPath = os.path.dirname(fPath)
path = dPath + "\\json"
api = API()
api = API("de")

if not os.path.exists(path):
    os.makedirs(path)

cpu_data = api.retrieve("cpu")
#print(cpu_data.to_json)
#print(json.dumps(cpu_data.to_json(), sort_keys=True, indent=4))

with open(path + "\\cpu.json", "w", encoding='utf-8') as wf:
    json.dump(cpu_data.to_json(), wf, indent=4)

with open(path + "\\cpu.json", "r") as of:
    json_file = json.load(of)
print(json_file)
print(type(json_file))


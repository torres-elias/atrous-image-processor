import json

def read_parameters(path):
    with open(path, "r") as p:
        parameters = json.load(p)
    return parameters
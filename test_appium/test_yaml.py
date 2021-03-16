import yaml

with open("test.yaml", "r") as f:
    data = yaml.safe_load(f)

print(data)
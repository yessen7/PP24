import json

with open('sample-data.json') as file:
    data = json.load(file)


interfaces = data.get("imdata", [])

print("Interface status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("dot1", "Description", "autoNeg", "bw"))
print("-" * 80)

for interface in interfaces:
    attributes = interface.get('l1PhysIf', {}).get('attributes', {})
    dot1 = attributes.get('dot1qEtherType')
    description = attributes.get('descr', '')
    autoNeg = attributes.get('autoNeg')
    bw = attributes.get('bw')

    print("{:<50} {:<20} {:<10} {:<6}".format(dot1, description, autoNeg, bw))



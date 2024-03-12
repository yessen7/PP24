import json

with open('sample-data.json') as file:
    data = json.load(file)


interfaces = data.get("imdata", [])

print("Interface status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    dn = interface.get('l1PhysIf', {}).get('attributes', {}).get('dn', '')
    description = interface.get('l1PhysIf', {}).get('attributes', {}).get('descr', '')
    speed = interface.get('l1PhysIf', {}).get('attributes', {}).get('speed', 'inherit')
    mtu = interface.get('l1PhysIf', {}).get('attributes', {}).get('mtu', '9150')

    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))



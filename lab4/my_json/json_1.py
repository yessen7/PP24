import json

# Load the JSON data from the file
with open('sample-data.json') as file:
    data = json.load(file)

# Extract relevant information
interfaces = data.get('imdata', [])

# Print header
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print interface information
for interface in interfaces:
    attributes = interface.get('l1PhysIf', {}).get('attributes', {})
    dn = attributes.get('dn', '')
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')

    print("{:<50} {:<20} {:<10} {:<6}".format(dn, description, speed, mtu))

    
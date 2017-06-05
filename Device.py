import bluetooth

print("Searching for bluetooth-enabled client devices...\n")

while True:
    devices = bluetooth.discover_devices(duration=10, lookup_names=True)

    if devices.__len__() != 0:
        break;
    print("No devices found, retrying...")

if devices.__len__() == 1:
    print(str(devices.__len__()) + " device discovered")
else:
    print(str(devices.__len__()) + " devices discovered")

i = 0
for addr, name in devices:
    print(str(i) + " - " + name + '(' + addr + ')')
    i += 1

client_index = input("Please enter the number (shown above) of the device you would like to connect to:")
client_addr = devices[client_index][0]

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((client_addr, 21997))

sock.send("Back to the future")

sock.close()

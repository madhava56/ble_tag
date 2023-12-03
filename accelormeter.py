from bluepy.btle import Scanner, DefaultDelegate

class BLEScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev and dev.addr == "0x009078563412":
            print("Discovered BLE Tag:", dev.addr)
            for (adtype, desc, value) in dev.getScanData():
                if desc == "Manufacturer":
                    # Check if it's an accelerometer beacon
                    if value.startswith("1a18"):
                        parse_accelerometer_data(value[4:])
                        break

def parse_accelerometer_data(data):
    frame_type = int(data[0:2], 16)
    
    if frame_type == 0xA1:
        version = int(data[2:4], 16)
        battery_level = int(data[4:6], 16)
        x_axis = int(data[6:10], 16) / 256.0
        y_axis = int(data[10:14], 16) / 256.0
        z_axis = int(data[14:18], 16) / 256.0

        print("Version:", version)
        print("Battery Level:", battery_level)
        print("X-Axis:", x_axis)
        print("Y-Axis:", y_axis)
        print("Z-Axis:", z_axis)

def main():
    scanner = Scanner().withDelegate(BLEScanDelegate())
    devices = scanner.scan(10)  # Scan for 10 seconds

if __name__ == "__main__":
    main()

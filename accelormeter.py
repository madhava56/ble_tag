#include <stdio.h>
#include <stdint.h>
#include <math.h>

// Define the structure for Accelerometer data
typedef struct {
    uint16_t x_axis;
    uint16_t y_axis;
    uint16_t z_axis;
} AccelerometerData;

// Parse Accelerometer data from the given packet
AccelerometerData parseAccelerometerData(uint8_t *data) {
    AccelerometerData accelData;
    accelData.x_axis = (uint16_t)data[11] << 8 | data[10];
    accelData.y_axis = (uint16_t)data[13] << 8 | data[12];
    accelData.z_axis = (uint16_t)data[15] << 8 | data[14];
    return accelData;
}

// Process Accelerometer data packet
void processAccelerometerPacket(uint8_t *data) {
    // Assuming the packet structure based on provided definitions
    uint8_t frameType = data[9];

    if (frameType == 0xA1) {
        // Accelerometer frame
        AccelerometerData accelData = parseAccelerometerData(data);

        // Calculate the magnitude of the acceleration vector
        double accelerationMagnitude = sqrt(pow(accelData.x_axis, 2) + pow(accelData.y_axis, 2) + pow(accelData.z_axis, 2));

        // Set a threshold value for movement detection
        double threshold = 100.0;  // Adjust this value based on your requirements

        // Check if the magnitude exceeds the threshold
        if (accelerationMagnitude > threshold) {
            printf("Tag is moving\n");
        } else {
            printf("Tag is stationary\n");
        }
    } else {
        //  Unsupported frame type
        printf("Unsupported frame type: 0x%02X\n", frameType);
    }
}

int main() {
    // Example BLE packet for Accelerometer data
    uint8_t accelerometerDataPacket[] = {
        0x02, 0x01, 0x06, 0x03, 0x03, 0xE1, 0xFF, 0x03, 0x18, 0xE1, 0xFF, 0xA1, 0x03, 0x64, 0x00, 0x80, 0xFF, 0x38, 0x38, 0x01, 0x00, 0x90, 0x78, 0x56, 0x34, 0x12};

    // Process Accelerometer data packet
    processAccelerometerPacket(accelerometerDataPacket);

    return 0;
}


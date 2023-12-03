# ble_tagStep 1: Install Required Libraries
Make sure you have Python installed on your system. You also need to install the bluepy library, which is used for Bluetooth Low Energy communication. Open your terminal or command prompt and run the following command:

bash
Copy code
pip install bluepy
Step 2: Modify Code
Open the code in a text editor and replace "MAC_ADDRESS_OF_BLE_TAG" with the actual MAC address of your BLE Tag. Save the changes.

Step 3: Run the Code
Now, open your terminal or command prompt and navigate to the directory where you saved the Python script. Run the script using the following command:

bash
Copy code
python script_name.py
Replace script_name.py with the actual name of your Python script. This command initiates the Bluetooth scanning process for 10 seconds.

Step 4: Observe Output
During the scanning process, the script will print information about discovered BLE devices. If the specified BLE Tag is found, the script will attempt to parse accelerometer data based on the provided frame definition.

Note:
Ensure that your Bluetooth adapter is enabled.
Make sure the BLE Tag is in the range and actively broadcasting data.
Verify that your system supports Bluetooth Low Energy and that you have the necessary permissions to access Bluetooth devices.

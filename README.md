
# SDM120 Modbus Reader
This project is designed to interface with an SDM120 energy meter using Modbus RTU over RS485. It reads voltage, current, and power values from the meter and prints them out continuously.

## Prerequisites
### Hardware:

- Raspberry Pi with RS485 communication setup
- SDM120 energy meter
### Software:

- Python 3
- pymodbus and pyserial Python libraries
### Installation
To set up the environment and install the necessary dependencies, follow these steps:

Clone the repository to your Raspberry Pi:
```
git clone https://github.com/itbdelaboprogramming/SDM120CT_RS485CANHAT
cd <your-repo-directory>
```
Run the setup script to configure the Raspberry Pi and install dependencies:

```
bash install.sh
```
The install.sh script will:
- Configure the Raspberry Pi's serial interface for RS485 communication.
- Update the system packages.
- Install Python 3 and set up a virtual environment.
- Install required Python packages: pymodbus and pyserial.
Usage
After the setup, activate the virtual environment and run the main script:

```
bash main.sh
```

This will start reading the voltage, current, and power data from the SDM120 energy meter and output the results continuously.

## Script Details
SDM120.py:

The core script that communicates with the SDM120 energy meter.
It reads the registers for voltage, current, and power using Modbus.
The values are printed every second.
install.sh:
Sets up the Raspberry Pi's hardware and installs necessary software dependencies.

main.sh:
Activates the virtual environment and runs the SDM120.py script.
Troubleshooting

## Troubleshooting
If you encounter any issues with Modbus communication, ensure that:

- The RS485 connection is properly wired.
- The correct port (/dev/ttyS0) is being used.
- The SDM120 energy meter is correctly configured with the expected Modbus address.
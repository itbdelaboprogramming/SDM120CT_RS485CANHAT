from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder as decoder
import time

#setup RS485 serial comn
devicePort = "/dev/ttyS0"
baudrate = 9600
parity = 'N'
client= ModbusClient(port=devicePort, parity =parity, baudrate= baudrate)

#adress and count
SDM120 = 1
volt_addr = [ 0x00 ,2]
watt_addr = [ 0x0C ,2]
curr_addr = [ 0x06 ,2]

#Connect to the serial modbus server
connection = client.connect()
print(connection)


while 1:
    #Starting add, num of reg to read, slave unit.
    try:
        voltReg = decoder(client.read_input_registers(volt_addr[0],volt_addr[1],slave= SDM120).registers)
        volt = voltReg.decode_32bit_float()
        currReg = decoder(client.read_input_registers(curr_addr[0],curr_addr[1],slave= SDM120).registers)
        curr = currReg.decode_32bit_float()
        wattReg = decoder(client.read_input_registers(watt_addr[0],watt_addr[1],slave= SDM120).registers)
        watt = wattReg.decode_32bit_float()
    except ModbusIOException as e:
        print(f"Modbus communication error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    print("-"*30)
    print("volt : %0.2f v \ncurrent : %0.2f A\nwatt : %0.2f w" % (volt,curr,watt))
    time.sleep(1)

#Closes the underlying socket connection
client.close()
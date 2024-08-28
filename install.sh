echo "setting up hardware for RS485"
sudo raspi-config nonint do_serial_cons 1
echo "disable shell logging over serial"
sudo raspi-config nonint do_serial_hw 0
echo "enable serial hardware port"

if grep -Fxqw "enable_uart=1" /boot/firmware/config.txt
then
    echo -e "config.txt file configured"
else
    echo "enable_uart=1" | sudo tee -a /boot/firmware/config.txt
    echo -e "config.txt file configured"
fi

sudo apt update
sudo apt upgrade

if ! command -v python3 &> /dev/null
then
    sudo apt install -y python3 python3-venv python3-pip
fi

python3 -m venv env
source env/bin/activate

pip install pymodbus
pip install pyserial

deactivate

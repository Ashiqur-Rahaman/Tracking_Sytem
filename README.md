Pet Tracking System

This project uses a Raspberry Pi and GPS module to track the location of a pet and display it on a map. The GPS data is sent to a server using a GSM module, but for demo purposes, we are using a Wi-Fi module to send the data to the host device.
Getting Started

To run this project, you will need to turn on the Raspberry Pi and connect it to Wi-Fi. The IP address is fixed at 192.168.0.200, and the SSH password is "raspberry". The GPS module should be connected to the Raspberry Pi through the serial port.

The host machine will connect to the Raspberry Pi remotely and execute the "try.py" script, which will generate GPS data. The latitude and longitude will then be used to open a browser tab and show the pet's location on Google Maps.
Running the Program

To run the program, execute the pet_tracking.py script on the host machine. This will remotely execute the try.py script on the Raspberry Pi, which will generate GPS data. The latitude and longitude will be used to display the pet's location on Google Maps.
License

This project is licensed under the MIT License. See the LICENSE file for more information.

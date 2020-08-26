# Serial Frecuency Count

This program tries to estimate how many lines can be sent to the computer through serial port, per second (Frecuency).

## How to use:
- on line that contains ' ser = serial.Serial('COM4', 115200) ' replace COM4 for the port used and replace 115200 for the baudrate used.

- This program will count 3 times the frecuency, since the first read could not be so accurate, since sometimes the buffer is full can cause some problems counting.

- The 2nd and 3rd results should be more accurate, ideally the same result.

## Explanation, why you did this?

This program answer to some questions that I had in the past, like:
What is the real frecuency allowed by a Arduino to send a line of Serial to the computer?
Is the Arduino really capable to send such data to the PC?


## TODO:

- Upload a code to test this code with arduino.
- Upload images as example and instruction.


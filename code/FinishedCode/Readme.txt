To run the script go into this folder in the terminal and the type sudo ./script
or you can open three terminals and run DeviceLogic.py using sudo python3 and then run 
Monitor1 and Monitor2 after.

I recommend rewriting a lot of the DeviceLogic code since I work on it with a single pulse in mind.

I'd recommend making a class for the pulse and then just keep track of them within an array using a function like updatestrips I had in playground.py in Localtest. 

The monitor code should be fine if you can figure out how to reuse the ports.

Probably something in this git post could solve that problem.

https://stackoverflow.com/questions/6380057/python-binding-socket-address-already-in-use

If the program crashes and stop running afterwards then it is likely the port numbers need to be 
updated within the code or the connections on the raspi are loose.
# Author - Samuel Ambler

# Fail command for bebop
from pyparrot.Bebop import Bebop

bebop = Bebop(drone_type="Bebop2")

print("connecting")
success = bebop.connect(10)
print(success)

if(success):
	bebop.safe_land(10)
	print("DONE - disconnecting")
	bebop.smart_sleep(5)
	print(bebop.sensors.battery)
	print("\032[1;37;41m BEBOP DOWN \033[1;37;40m");
	bebop.disconnect()

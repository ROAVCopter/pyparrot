# Bebop Hover example
# - STA -

from pyparrot.Bebop import Bebop

bebop = Bebop(drone_type="Bebop2")

print("connecting")
success = bebop.connect(10)
print(success)

if (success):
	bebop.ask_for_state_update()
	bebop.safe_takeoff(10)
	bebop.set_max_tilt(5)
	bebop.set_max_vertical_speed(1)
	bebop.set_max_altitude(2)

	print("sleep 25")
	bebop.smart_sleep(25)

	print("Landing")
	bebop.safe_land(10)

	print("DONE - disconnecting")
	bebop.smart_sleep(5)
	print(bebop.sensors.battery)
	bebop.disconnect()

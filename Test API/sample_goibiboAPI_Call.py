## Sample program to test goibiboAPI

from goibiboAPI import goibiboAPI

GO = goibiboAPI("653332e6", "7c2191040b1d951516221290d893741a")

print GO.FlightSearch("CCJ", "HYD", 20170920)
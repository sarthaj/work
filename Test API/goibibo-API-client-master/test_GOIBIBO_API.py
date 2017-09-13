import requests,json

#def sample_GOIBIBO_API_Call():

	#headrs = {"app_id": '653332e6', "app_key": '7c2191040b1d951516221290d893741a'}



'''def FlightSearch(source, destination, dateofdeparture, dateofarrival=None, seatingclass="E", adults=1, children=0, infants=0):

	BASE = "http://developer.goibibo.com/api/"

	auth = {"app_id" : '653332e6', "app_key" : '7c2191040b1d951516221290d893741a'}

	response = requests.get(BASE + "search/" + "?format=json" + "&source=%s" % source + "&destination=%s" % destination + "&dateofdeparture=%d" % dateofdeparture + "&seatingclass=%s" % seatingclass + "&adults=%d" % adults + "&children=%d" % children + "&infants=%d" % infants,	params=auth)
	print(response.status_code)
	data = response.json()
	print(data)'''


from goibibo import goibiboAPI

GO = goibiboAPI('653332e6', '7c2191040b1d951516221290d893741a')

print GO.FlightSearch("CCJ", "HYD", 20170910)
#print GO.MinimumFare("BLR", "HYD", 20141028)
#print GO.BusSearch("bangalore", "hyderabad", 20141028)
#print GO.BusSeatMap("vJ52KC0ymd0635qTD9bDDy9GHBkGl5FJMJje0aFX\
#                    _GQTyev_4N9Y62TTfrmS-Re3dCHl0-UxLq4AsoQ%3D")
#print GO.SearchHotelsByCity(6771549831164675055)
#print GO.GetHotelData([1017089108070373346, 6085103403340214927])
#print GO.GetHotelPriceByCity(6771549831164675055, 20141101, 20141102)
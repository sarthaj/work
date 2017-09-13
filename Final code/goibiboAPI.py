import requests,json

class goibiboAPI(object):

	base = "http://developer.goibibo.com/api/search/"

	def __init__(self, app_id, app_key):
		# App_id and App_key provided by GOIBIBO for authentication
		self.auth = {"app_id": app_id, "app_key": app_key}


	def FlightSearch(self, source, destination, dateofdeparture, dateofarrival=None, seatingclass="E", adults=1, children=0, infants=0, counter=100):
		''' Search flights based on specific parameters.

		Parameters
		----------
		source: Origin Airport code. (Should be a valid IATA code)
		destination: Destination Airport code. (Should be a valid IATA code)
		dateofdeparture: Departure Date (onward flights only). Format (YYYYMMDD)
		dateofarrival: Arrival Date (onward & return Flights). Format (YYYYMMDD)
		seatingclass: Travel Class/Cabin Type. E(Economy) or B(Business). Default is E
		adults: No of Adults. Integer value between 1-9. Minimum of one adult is required. Default = 1
		children: No of children. Integer value between 0-9. Default = 0
		infants: No of infants. Integer value between 0-9. Default = 0
		counter: 100 for domestic,0 for international. Default = 100
		'''

		if dateofarrival:
			dateda = "&dateofdeparture=%d&dateofarrival%d" % (dateofdeparture, dateofarrival)
		else:
			dateda = "&dateofdeparture=%d" % dateofdeparture

		# formatting the url for API Call
		full_req = self.base + "?app_id=%s" %self.auth["app_id"] + "&app_key=%s" %self.auth["app_key"] + "&format=json" + "&source=%s" % source + "&destination=%s" % destination + dateda + "&seatingclass=%s" % seatingclass + "&adults=%d" % adults + "&children=%d" % children + "&infants=%d" % infants + "&counter=%d" % counter
		response = requests.get(full_req, params = self.auth)
		flight_data = response.json()

		# Contains all the flight details between source and destination for all flights
		flights = flight_data['data']['onwardflights']
		
		with open('sample_flights.json', 'w') as fp: # temporarily dumping into a file sample_flights.json. To be Changed as per the requirement
			json.dump(flights, fp, indent=4)

		return flights



		### Need to format the data returned.

		'''
		# Fetch only the required parameters from the whole flight details result
		sample_dict = {}
		count = 0
		for i in flights:
			stops = len(i['onwardflights']) ###Another approach to calculate NUMBER OF STOPS instaed of using 'stops' slot

			count += 1

			origin = i['origin']
			deptime = i["deptime"]
			duration = i["duration"]
			flightno = i["flightno"]
			destination = i["destination"]
			total_amount = i["fare"]["grossamount"]

			# If the flight is not a direct one, fetch the layover flight details.			
			onward_dic = {}
			onward_list = []
			if stops > 0:
				for j in range(stops):
					new_from = i["onwardflights"][j]['origin']
					dep_time = i["onwardflights"][j]["deptime"]
					flight_no = i["onwardflights"][j]["flightno"]
					desti = i["onwardflights"][j]["destination"]

					onward_dic = {'new_from': new_from, 'dep_time': dep_time, 'flight_no': flight_no, 'desti': desti}
					onward_list.append(onward_dic.copy())

			seatingclass = i["seatingclass"]
			split_duration = i["splitduration"]
			airline = i["airline"]
			depdate = i["depdate"]
			arrivaltime = i["arrtime"]
			arrivaldate = i["arrdate"]

			s = {'origin': origin, 'deptime': deptime, 'duration': duration, 'flightno': flightno, 'destination': destination, \
					'total_amount': total_amount, 'stops': stops, 'onward_flight_list': onward_list, \
					'seatingclass': seatingclass, 'split_duration': split_duration, 'airline': airline, \
					'depdate': depdate, 'arrivaltime': arrivaltime, 'arrivaldate': arrivaldate}

			sample_dict[count] = s

		#return sample_dict[1]
		return flights'''
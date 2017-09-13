import requests,json




base = "http://developer.goibibo.com/api/search/?app_id=653332e6&app_key=7c2191040b1d951516221290d893741a"
app_id = "653332e6"
app_key = "7c2191040b1d951516221290d893741a"
format = "json"
source = "CCU"
destination = "BLR"
dateofdeparture=20170910
seatingclass='E'
adults=1
children=0
infants=0
counter=100

#full_request = base+"app_id="+app_id+"&app_key="+app_key+"&format="+format+"&source="+source+"&destination="+destination+"&dateofdeparture="+dateofdeparture+"&seatingclass="+seatingclass+"&adults="+adults+"&children="+children+"&infants="+infants+"&counter="+counter

full_req = base + "&format=json" + "&source=%s" % source + "&destination=%s" % destination + "&dateofdeparture=%d" % dateofdeparture + "&seatingclass=%s" % seatingclass + "&adults=%d" % adults + "&children=%d" % children + "&infants=%d" % infants + "&counter=%d" % counter
#print full_req
response = requests.get(full_req)
data = response.json()

'''d = data['data']['onwardflights'][0]['onwardflights'] #['onwardflights'][0]['stops'] ###Gives the total stops the flight makes
print d
print len(d)'''

flights = data['data']['onwardflights'] # Contains all the flight details between source and destination for all flights

#print flights
sample_dict = {}
count = 0
for i in flights:

	#s = {'origin': i['origin'], 'deptime': i["deptime"], 'duration': i["duration"], 'flightno': i["flightno"], 'phone': phone, 'pricerange': pricerange, 'postcode': postcode, 'signature': signature, 'id': id1, 'name': name}

	#stops = abs(int(i["stops"]))
	stops = len(i['onwardflights']) ###Another approach to calculate NUMBER OF STOPS instaed of using 'stops' value

	print "PRINTING ", count," FLIGHT"
	count += 1
	#print i
	print "Origin: ",i['origin']
	print "Dep. Time: ",i["deptime"]
	print "Duration: ",i["duration"]
	print "Flight No: ",i["flightno"]
	print "Destination: ",i["destination"]
	print "Total Amount: ",i["fare"]["grossamount"]
	#stops = abs(int(i["stops"]))
	print "No of Stops: ",stops
	if stops > 0:
		print " Onward flights "
		for j in range(stops):
			print "From: ",i["onwardflights"][j]['origin']
			print "Dep. Time: ",i["onwardflights"][j]["deptime"]
			print "Flight No.: ",i["onwardflights"][j]["flightno"]
			print "Destination: ", i["onwardflights"][j]["destination"]
	print "Class :",i["seatingclass"]
	print "Split duration :",i["splitduration"]
	print "Airline: ",i["airline"]
	print "Dep Date: ",i["depdate"]
	print "Arr time: ",i["arrtime"]
	print "Arr Date: ",i["arrdate"]
	print " "
	print " "


#name 
#price

#data{onwardflights}

#print requests.get("http://developer.goibibo.com/api/search/?app_id=653332e6&app_key=7c2191040b1d951516221290d893741a&format=json&source=PNQ&destination=CCJ&dateofdeparture=20170910").json()

#print "http://developer.goibibo.com/api/search/?app_id=653332e6&app_key=7c2191040b1d951516221290d893741a&format=json&source=PNQ&destination=CCJ&dateofdeparture=20170910&seatingclass=E&adults=1&children=0&infants=0&counter=100"
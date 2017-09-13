import requests,json

def sample_API_Call(city):

	headrs = {"user-key": '690cad7bc32ea5507ab1f6bb146f2db8'}

	parameters = {"q": city}
	city_id_response = requests.get("https://developers.zomato.com/api/v2.1/cities", headers=headrs, params=parameters)

	data = city_id_response.json()
	city_id = data['location_suggestions'][0]['id']
	state_name = data['location_suggestions'][0]['state_name']

	parameters2 = {"entity_id": city_id, "entity_type": 'city'}
	response = requests.get("https://developers.zomato.com/api/v2.1/search", headers=headrs, params=parameters2)

	res_data = response.json()
	sample_dict = []
	count = 0
	#print(response.content)
	for restaurant in res_data["restaurants"]:
		count += 1
		#print restaurant
		addr = restaurant["restaurant"]["location"]["address"]
		area = restaurant["restaurant"]["location"]["city"]
		food = restaurant["restaurant"]["cuisines"]
		description = restaurant["restaurant"]["url"]

		if 'phone_numbers' in response.content:
			phone = restaurant["restaurant"]["phone_numbers"]
		else:
			phone = "not available"
		pricerange = restaurant["restaurant"]["price_range"]
		postcode = restaurant["restaurant"]["location"]["zipcode"]
		signature = "not available"
		id1 = restaurant["restaurant"]["id"]
		name = restaurant["restaurant"]["name"]
		

		s = {'addr': addr, 'area': area, 'food': food, 'description': description, 'phone': phone, 'pricerange': pricerange, 'postcode': postcode, 'signature': signature, 'id': id1, 'name': name}
		#print s

		sample_dict.append(s)

	print sample_dict


	#return sample_dict
	#print(response.content)
	
sample_API_Call('Birmingham')
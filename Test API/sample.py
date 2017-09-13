import requests,json

headrs = {"user-key": '690cad7bc32ea5507ab1f6bb146f2db8'}

parameters = {"q": 'birmingham'}
city_id_response = requests.get("https://developers.zomato.com/api/v2.1/cities", headers=headrs, params=parameters)

data = city_id_response.json()
city_id = data['location_suggestions'][0]['id']
state_name = data['location_suggestions'][0]['state_name']

parameters2 = {"entity_id": city_id, "entity_type": 'city'}
response = requests.get("https://developers.zomato.com/api/v2.1/search", headers=headrs, params=parameters2)

#print(response.status_code)

res_data = response.json()

sample_dict = {}
count = 0
for restaurant in res_data["restaurants"]:
	count += 1
	#print restaurant
	City = restaurant["restaurant"]["location"]["city"]
	Theater = restaurant["restaurant"]["name"]
	Zip = restaurant["restaurant"]["location"]["zipcode"]
	Critic = restaurant["restaurant"]["user_rating"]["rating_text"]
	Genre = restaurant["restaurant"]["cuisines"]
	State = state_name
	Start = "9:30"
	Date = "day after tomorrow"
	Movie = "Zomato"

	s = {'city': City, 'theater': Theater, 'zip': Zip, 'critic_rating': Critic, 'genre': Genre, 'state': State, 'starttime': Start, 'date': Date, 'moviename': Movie}
	print s

	sample_dict[count] = s

print sample_dict

	#print res_data["restaurants"][id]["restaurant"]["location"]["city"]

#for key, value in data.items() :
#    print (key, value)

#print(response.content)
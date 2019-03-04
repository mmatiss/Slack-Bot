import urllib.request
import json
def weather(text):
	if (len(text.split()) != 1):
		return "/weather takes in only 1 arguement"
	try:
		int(text)
	except:
		return text + " is not a valid zipcode"
	if (len(text) != 5):
		return text + " is not a valid zipcode"
	i = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?zip=" + str(text) + ",us&mode=json&APPID=16a8c8024c22df04565602e331df934d")
	i_string = i.read().decode('utf-8')
	info = json.loads(i_string)
	temp = info["main"]["temp"]
	temp = (temp - 273) * 1.8 + 32
	location = info["name"]
	weather = info["weather"][0]["main"]
	temp = str(round(temp))
	return {"response_type": "in_channel",
    "text": "The current weather in " + location + " is " + weather.lower() + " with a temperature of " + str(temp) + " Fahrenheit."}

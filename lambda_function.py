import json
from tasker import tasker
from weather import weather
from shortenUrl import shortenUrl

functions = {"/tasker": tasker, "/weather": weather, "/shorturl": shortenUrl}

def lambda_handler(event, context):
	command = event["command"]
	text = event["text"]
	return functions[command](text)
import json
from tasker import tasker
from weather import weather
from shortenUrl import shortenUrl

functions = {"/tasker": tasker, "/weather": weather, "/shorturl": shortenUrl}

def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))
	command = event["command"]
	text = event["text"]
	print(command, text)
	return functions[command](text)
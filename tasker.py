import boto3
from boto3.dynamodb.conditions import Key

def makeTask(text, table):
	if (len(text) < 2):
		return "Making a task requires a task argument."
	s = ' '.join(text[1:])
	table.put_item(
	Item={'Task': s.lower(), "Completed": 0}
	)
	return "Task added: " + s
	
def todo(_, table):
	fe = Key('Completed').eq(0)
	pe = "Task"
	uncompleted = table.scan(
		ProjectionExpression = pe,
		FilterExpression = fe
		)
	s = ''
	counter = 0
	for i in uncompleted['Items']:
		s += i['Task'] + ', '
		counter += 1
	s = s[:-2]
	if not counter:
		return "No tasks are incomplete"
	if counter == 1:
		return s + " has yet to be completed"
	return s + " have all yet to be completed"

def complete(_, table):
	fe = Key('Completed').eq(1)
	pe = "Task"
	completed = table.scan(
		ProjectionExpression = pe,
		FilterExpression = fe
		)
	s = ''
	counter = 0
	for i in completed['Items']:
		s += i['Task'] + ', '
		counter += 1
	s = s[:-2]
	if not counter:
		return "No tasks have been completed"
	if counter == 1:
		return s + " has been completed"
	return s + " have all been completed"

def checkoff(text, table):
	if (len(text) < 2):
		return "Checking a task requires a task argument."
	s = ' '.join(text[1:])
	response = table.update_item(
		Key = {'Task': s.lower()},
		UpdateExpression = "set Completed = :d",
		ExpressionAttributeValues = {':d': 1},
		ReturnValues = "UPDATED_NEW"
	)
	return "Task completed!"
	
def deleteTask(text, table):
	if (len(text) < 2):
		return "Deleting a task requires a task argument."
	s = ' '.join(text[1:])
	table.delete_item(
		Key={'Task' : s.lower()}
	)
	return "Task deleted"

def help(_, __):
	s = "Possible commands: make [task] (creates new task), todo (show all uncompleted tasks), completed (show completed tasks), "
	s += "check-off [task] (mark a task as completed), and delete [task] (remove a task from the list)"
	return s
	

valid_commands = {"-h": help, "make": makeTask, "check-off": checkoff, "delete": deleteTask, "completed": complete, "todo": todo}

def tasker(text):
	db = boto3.resource('dynamodb')
	table = db.Table('Task')
	text_array = text.split()
	if text_array[0].lower() in valid_commands:
		return valid_commands[text_array[0].lower()](text_array, table)
	else:
		return text_array[0] + " is not a valid command! Try -h to see a list of valid commands."
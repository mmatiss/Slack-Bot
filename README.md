# Coding Challenge
For the Ping coding challenge, the three slack commands I chose to implement were a URL shortener, a basic task manager, and a location based weather app.

The slack  with these apps is located at ping-challenge.slack.com
The Account email to get in is: mmatiss42@gmail.com and the password is Ping-Account

## My implementations
To run my slack commands, I chose to use AWS Lambda for running my commands as they were called and Amazon API Gateway to run idly until an http request is sent to it. Upon recieving the request, it is mapped to a JSON file and sent to the lambda, which then executes the command. I additionally used DynamoDB as a simple way of storing information between calls to the server. 

Two of my commands (/weather and /shorturl) used existing APIs, found at https://openweathermap.org/api and 
http://www.tiny-url.info/open_api.html respectively. The third (/tasker) exclusively uses my code and DynamoDB to keep track of the status of an array of tasks. For the full list of tasker capabilities, try /tasker -h on the slack.

### Sources
Two sources of help in configuring both slack and AWS were the Boto3 API (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) and an article providing the basics on slack slash commands (https://medium.com/@cu_tech/create-a-slack-slash-command-with-aws-lambda-83fb172f9a74).

### Running the Server and Tests
The server is currently being run indefinitely, through the help of the free-tier of the AWS platform. For more information on this, please email me at mickeymatiss@gmail.com.
For testing, I only worked on local tests. This is because the server structure is both out of my control, and can be assumed to work correctly. 

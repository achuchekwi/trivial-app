# trivial-app
Environment: Production
Purpose: test
Statement:
 • GET /
 ·  Returns plain-text “Hello world” and HTTP status code 200
 • GET /status/alive
 ·  Returns an empty body and HTTP status code 200
 • GET /status/ready
 ·  If the app has been running for less than 10 seconds
 o Returns JSON content {“ready”: false} and HTTP status code 500
 ·  If the app has been running at least 10 seconds
 o Returns JSON content {“ready”: true} and HTTP status code 200
 Include some aspect of DevOps/Platform work, which may include any of the following...
 • Dockerize your application
 • Use a SaaS service to perform some automated step (of your choosing) whenever you push to your code repository for this application.   For example...
  ·  Travis-CI
  ·  CircleCI
  ·  DockerHub
  ·  Heroku

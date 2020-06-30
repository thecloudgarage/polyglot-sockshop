# Load / Integration Tests

These tests simulate actual end user usage of the application. They are used to validate the overall functionality and can also be used to put simulated load on the system. The tests are written using [locust.io](http://locust.io)

## Running in Docker Container
* Edit the locustfile.py in the sub-directory "scripts" to do any changes to your tests
* Run the command "docker-compose up"
* Visit the IP address of your host with 8089 port number (in this case, the locust is listening on all ports, so if your host has a public IP, you can also browse from Internet)
* You can start running the tests providing the total number of users & hatch rate (users added per second)

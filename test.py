Steps to setup Jenkins hosted in Docker containers:

Pull the Latest Jenkins image from the Hub:
docker pull jenkins/jenkins:latest

Build  the Image:
docker build -t img_name[my_jenkins]:tag[latest] .

Create a jenkins network, so that we can access it within network:
docker network create jenkins

Run the container:
docker run --network jenkins -p 8080:8080 -p 50000:50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins:latest

Since Jenkins is running as a container it is unable to reach docker host, so we need to run a container that can mediate between Doc host & jenkins. By running below cmd it will help proxy connection between docker & jenkins.

docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v //var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock

docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock


cd Ewauf && pip3 install -r requirements.txt
export PYTHONPATH=$(pwd)
robot -t TC_5.2 Tests/ewauf.robot


************************
Test Statement
***********************

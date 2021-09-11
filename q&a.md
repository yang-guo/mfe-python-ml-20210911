what will happen when you search www.google.com in your web browser
- some one will map `google.com` -> IP address (4.4.4.4)
- establish a TCP connection between your local machine and that IP address
- ask for data from the main page
- google serviec will return the data



Q: how to bring my local service online
- figure out which cloud provider to use (AWS/Azure/GCP/Alibaba/...)
- these cloud provide will have a vanilla machine to host your application
	- most of the time, these serivcer (whatever brand) are running linux operating system
	- this means we need to make sure our application is compatible with linux OS
	- its extremely hard to guarantee that whatever works on your local machine works remotely
	- solution -- containernization
		- docker


Q: continus deployment
- first time of deploy a serivce
	- write up the code
	- define a dockerfile
	- buil the docker image (1231231232.pricing/master-latest)
	- ask AWS host that image
- what if I found a bug in my code, and I want to update my serivce
	- fix the bug locally
	- building a new docker image (using the same dockerfile)
	- ask AWS to update the image it's using
- what can i do when i am making some changes to my model so that it's incompatible with the model I trained
	- retain the model
	- label the type of a code change
	- hard code the pickle version into the docker file
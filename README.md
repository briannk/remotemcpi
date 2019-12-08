# remotemcpi

remotemcpi is a web application powered by the Flask framework to allow a user to play Minecraft: Pi Edition through a smartphone with gyroscope and accelerometer functionality. A user can connect to a local development server provided by Flask and interact with a web interface to play Minecraft through their smartphone. The aim of the application is to provide an alternate, accessible way to play the most popular video game in history.

## Before you start
In order to use remotemcpi, you should consider setting up a virtual environment to contain dependencies exclusively for this application. To install virtualenv, do

```sudo pip install virtualenv```

and create a virtual environment with

```virtualenv [environment name]```

and activate it with 

```. [environment name]/bin/activate```

You can deactivate the virtual environment with

```deactivate```

Once the virtual environment is activated, dependencies can be installed using 

```pip install -r requirements.txt```

## Running the server
To run the server, do

```export FLASK_APP="test.py"
flask run --host=0.0.0.0
```
the ```--host=0.0.0.0``` argument is required so that the server is visible to other devices on the network
 
## Connecting with a mobile device
You must first identify the ip address of the device hosting the Flask server which can be found with
 
```ip address```
 
following an inet.
 
From a mobile device, you can connect to the server via [ip address]:5000 (Flask defaults to port 5000)

You should now be able to input through the mobile device to send keystrokes to the active window on the device running the Flask server!
 
 

 
 

# Milton: Scan Art for Info. A Platform for Artist.

Brief description of the project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API] (#api docs)

## Installation

To install this project, make sure you have Python 3.11+ and pip installed on your system. Clone the repository then install the dependencies using the following command in the root directory of this repository:
```bash
$ pip install -r requirements.txt
```

## Usage

To start the server execute the following in the root directory:
```bash
$ python server/manage.py runserver
```

Make the server available to your network with forward tunneling:

### Forward Tunneling with Ngrok

Download Ngrok (https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip)

Add your authtoken to the config file
```sh
$ ngrok config add-authtoken <your-ngrok-authtoken>
```

Deploy the server in your network (Default port is 8000)
```sh
$ ngrok http http://localhost:<port>
```

## API

Access the API Documentation at [https://documenter.getpostman.com/view/30898740/2sA2r3Yk8w](https://documenter.getpostman.com/view/30898740/2sA2r3Yk8w)

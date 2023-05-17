# Secure File Transfer Project

This project demonstrates secure file transfer with RSA key's using the `paramiko` library in Python.

## Setup

Follow the steps below to set up the project and create a virtual environment (on Windows):

### Prerequisites

- Python 3.x installed on your system (Download Python: https://www.python.org/downloads/)

### Clone the repository

1. Open a command prompt or terminal.

2. Clone the repository using the following command:

   git clone <repository_url>

### Create a virtual environment

1. Change your current directory to the project folder:

   cd secure-file-transfer-project

2. Create a virtual environment using the `venv` module:

   python -m venv venv

3. Activate the virtual environment:

   venv\Scripts\activate

### Install dependencies

1. Install the required dependencies using `pip`:

   pip install -r requirements.txt

   This will install the necessary dependencies, including `paramiko`.

### Create .env file

1. Create new file in root directory called .env:

    Add these variables:
        HOSTNAME=
        
        USERNAME=
        
        PASSWORD=
        
        PUBLIC_KEY_PATH=
        
        PRIVATE_KEY_PATH=

    HOSTNAME: This refers to the hostname or IP address of the remote server you want to connect to for secure file transfer. For example, it could be something like example.com or 192.168.1.100.

    USERNAME: This represents the username or account name associated with the remote server. It is the credentials used to authenticate and access the server.

    PASSWORD: This refers to the password associated with the username provided above. It is the corresponding password for the given username to establish the secure connection.

    PUBLIC_KEY_PATH: The path to the file storing your public key
    
    PRIVATE_KEY_PATH: The path to the file storing your private key

### Run the project

1. Create your public and private keys.

    Enter the path to where you want to store the keys

    run the key_gen file: python key_gen.py

2. You can now run the project using the following command:

   python main.py

   This will execute the main Python script and demonstrate the secure file transfer functionality.

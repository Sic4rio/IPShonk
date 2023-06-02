
# SICARIOS IP Grabber
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

SICARIOS IP Grabber is a Python script that retrieves the IP addresses of websites listed in a file. It uses the `socket` module to perform DNS resolution and retrieve the IP address of each domain.

## Usage

1. Make sure you have Python 3 installed on your system.

2. Install the required dependencies using the following command:
pip install colorama termcolor


3. Create a file containing the list of URLs (one URL per line) that you want to retrieve IP addresses for.

4. Run the script using the following command:
```
python ip_grabber.py
```

5. When prompted, enter the name of the file containing the URLs.

6. The script will start retrieving the IP addresses for each URL and display the results on the console.

7. The retrieved IP addresses will be saved to a file named `ips.txt` in the same directory.



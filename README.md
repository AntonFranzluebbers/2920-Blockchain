# 2920 Blockchain demo
## An Array of Solar Powered Soil Monitoring Stations
_Anton Franzluebbers_

## To Use My Self-Hosted Web Portal

http://2920proj.ddns.net/  
http://2920proj.ddns.net/display_all/ shows the data with hash and nonce. This page would be removed in production.  
If it doesn't work, it is because my Raspberry Pi isn't plugged in. Contact me if you want me to turn it on.  
Go to http://2920proj.ddns.net/ or http://2920proj.ddns.net/display_all just like above.  
To add data, modify the url in `tester.py` from `http://localhost:8000/` to `http://2920proj.ddns.net/` and run it locally.  
`tester.py` first gets a correct nonce and hash from the server, then sends back the data with the nonce and hash to be added to the database.

## To Use Locally

### To start the server
`make start`

### To stop the server
`make stop`  
Uses pkill - take a look first

### To add data
`python3 tester.py` adds random data using POST requests. This kind of script would be on each sensor station.  
`python3 node.py` actually logs data from the sensor station prototype I built.  

### To view data
Go to `localhost:8000/` for the data.  
Go to `localhost:8000/display` for the data.  
Go to `localhost:8000/display_all` for data including the nonce and hash.

## Video
https://youtu.be/Kgwnvgy4lSY - old video  
https://youtu.be/V62epPNxirA - overview of project

## References
https://github.com/adamchinkc/blockchain_database/  
https://medium.com/programmers-blockchain/create-simple-blockchain-java-tutorial-from-scratch-6eeed3cb03fa


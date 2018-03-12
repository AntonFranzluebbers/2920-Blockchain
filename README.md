# 2920 Blockchain demo
## An Array of Solar Powered Soil Monitoring Stations
_Anton Franzluebbers_

## To Use Locally

### To start the server
`make start`

### To stop the server
`make stop`  
Uses pkill - take a look first

### To add data
`python3 tester.py`  
This adds random data using POST requests. This kind of script would be on each sensor station.

### To view data
Go to `localhost:8000/display` for the data.  
Go to `localhost:8000/display_all` for data including the nonce and hash.

## To use on my hosted server
If it doesn't work, it is because my Raspberry Pi isn't plugged in. Contact me if you want me to turn it on.  
Go to `http://2920proj.ddns.net/display` or `http://2920proj.ddns.net/display_all` just like above.


## References
https://github.com/adamchinkc/blockchain_database/  
https://medium.com/programmers-blockchain/create-simple-blockchain-java-tutorial-from-scratch-6eeed3cb03fa


start:
	python3 hash.py &
	python3 nonce.py &
	python3 main.py &

stop:
	pkill -f hash.py
	pkill -f nonce.py
	pkill -f main.py


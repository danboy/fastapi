.PHONY: server start test

server:start

start:
	fastapi dev main.py --port 3040

test:
	pytest

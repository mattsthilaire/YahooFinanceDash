install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py
	
lint:
	pylint --disable=R,C application.py
	
test:
	python -m pytest -vv --cov=hello application.py
	
all: install lint test
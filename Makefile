export CURRENT_DIR=$(shell pwd)
export PYTHONPATH=${CURRENT_DIR}
export PYTHONWARNINGS=ignore::UserWarning
export DJANGO_SETTINGS_MODULE=base.settings.base

dev-setup:
	docker-compose up -d postgres redis
	pip install -U -r requirements.txt

dev-setup-down:
	docker-compose down

lint-check:
	ruff check simple_graphql --fix

format:
	ruff format simple_graphql

run-makemigrations:
	python3 simple_graphql/manage.py makemigrations

run-migrations:
	python3 simple_graphql/manage.py migrate

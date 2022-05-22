.PHONY: build start test migrate

build:
	docker-compose build

start:
	docker-compose up

test:
	docker-compose run --rm app sh -c "pytest ."

migrate:
	docker-compose run --rm app sh -c "python src/manage.py run_migrations"

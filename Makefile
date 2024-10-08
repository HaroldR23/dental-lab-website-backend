override AUTOFLAKE_FORMAT=echo Run autoflake...; autoflake \
		--remove-all-unused-imports \
		--remove-unused-variables \
		--recursive \
		--in-place . \
		--exclude=__init__.py;
COVERAGE_THRESHOLD = 95

create_dev_env:
	python3 -m venv .venv

install_requirements:
	pip install -r requirements.txt

test:
	pytest

start:
	uvicorn main:app --reload --port 8000

format:
	${AUTOFLAKE_FORMAT}
	echo Run black...; black .;
	echo Run isort...; isort .;
	echo Run flake8...; flake8 .;
	echo Run mypy...; mypy .;

test_coverage:
	coverage run -m pytest
	coverage xml -o coverage.xml
	coverage report -m --fail-under=$(COVERAGE_THRESHOLD)

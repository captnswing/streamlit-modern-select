SHELL := /bin/bash
.DEFAULT_GOAL := test

all: test

poetry.lock: pyproject.toml
	poetry lock
	@# not all changes to pyproject.toml lead to a change of the poetry.lock file
	@# so let's update poetry.lock file modification date in any case
	@touch poetry.lock

.PHONY:
install: poetry.lock
	poetry install --sync

.PHONY:
format: install
	poetry run ruff format streamlit_modern_select

.PHONY:
lint: format
	poetry run ruff check --fix streamlit_modern_select

.PHONY:
test: lint
	poetry run pytest -v .

.PHONY:
streamlit: install
	poetry run streamlit run streamlit_modern_select/__init__.py

.PHONY:
bump-version: lint
	poetry version prerelease

.PHONY:
build: bump-version
	@grep -q "_RELEASE = True" "streamlit_modern_select/__init__.py" || (echo "Please set _RELEASE = True in __init__.py" && exit 1)
	poetry build

.PHONY:
pypi-test: build
	poetry publish -r test-pypi
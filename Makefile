SHELL := /bin/bash
.DEFAULT_GOAL := test

all: test

uv.lock: pyproject.toml
	uv lock
	@# not all changes to pyproject.toml lead to a change of the poetry.lock file
	@# so let's update poetry.lock file modification date in any case
	@touch uv.lock

.PHONY:
install: uv.lock
	uv sync

.PHONY:
format: install
	uv run ruff format streamlit_modern_select

.PHONY:
lint: format
	uv run ruff check --fix streamlit_modern_select

.PHONY:
test: lint
	uv run pytest -v .

.PHONY:
streamlit: install
	uv run streamlit run streamlit_modern_select/__init__.py

.PHONY:
build: lint
	@grep -q "_RELEASE = True" "streamlit_modern_select/__init__.py" || (echo "Please set _RELEASE = True in __init__.py" && exit 1)
	uv build

.PHONY:
publish-test: build
	uv publish
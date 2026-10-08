.PHONY: lint format type-check install-local-package test start-doc-server deploy-documentation build clean publish

lint:
	uv run ruff check --exclude src/unittest_extensions/tests

format:
	uv run ruff format ./

type-check:
	uv run ty check

install-local-package:
	uv pip install -e .

test:
	uv run python -m unittest discover -v src/unittest_extensions/tests/

start-doc-server:
	uv run python -m mkdocs serve

deploy-documentation:
	uv run python -m mkdocs gh-deploy --config-file mkdocs.yml

build:
	uv build

clean:
	rm -rf dist src/unittest_extensions.egg-info

publish:
	uv publish

install-documentation-builder:
	$(PIP) install mkdocs

start-documentation-server:
	$(INTERPRETER) -m mkdocs serve

deploy-documentation:
	$(INTERPRETER) -m mkdocs gh-deploy --config-file mkdocs.yml

install-package-builder:
	$(PIP) install --upgrade build

install-package-uploader:
	$(PIP) install --upgrade twine

install-local-package:
	$(PIP) install -e .

test-package:
	$(INTERPRETER) -m unittest discover -v src/unittest_extensions/tests/

build-package:
	$(INTERPRETER) -m build

upload-package:
	$(INTERPRETER) -m twine upload --verbose -u '__token__' dist/*

clean:
	rm -rf dist src/unittest_extensions.egg-info
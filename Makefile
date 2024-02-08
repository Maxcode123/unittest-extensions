install-package-builder:
	$(PIP) install --upgrade build

install-package-uploader:
	$(PIP) install --upgrade twine

install-local-package:
	$(PIP) install -e .

test-package: install-local-package
	$(INTERPRETER) -m unittest discover -v src/unittest_extensions/tests/

build-package: test-package install-package-builder
	$(INTERPRETER) -m build

upload-package: build-package install-package-uploader
	$(INTERPRETER) -m twine upload --verbose -u '__token__' dist/*

clean:
	rm -rf dist src/unittest_extensions.egg-info
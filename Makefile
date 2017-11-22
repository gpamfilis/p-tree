test:
	nosetests

run:
	python ./p_tree/run.py

dbox:
	python ./p_tree/dbox.py

pypi:
	rm -rf dist
	rm -rf build
	python setup.py bdist_wheel
	twine upload dist/*

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf dist/
	@rm -rf *.egg
	@rm -rf *.egg-info

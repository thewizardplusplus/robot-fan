PROJECT_FILES = \
	robot_fan/configuration.py \
	robot_fan/interval.py \
	robot_fan/toggling_value.py \
	robot_fan/running.py \
	robot_fan/__main__.py

.PHONY: help test build

help:
	@echo "Usage:"
	@echo "  make [options] <target>"
	@echo
	@echo "Options: see for the details \"man make\"."
	@echo
	@echo "Targets:"
	@echo "  help   Show this help message."
	@echo "  test   Run the unit tests."
	@echo "  build  Run the building."

test:
	python3 -m unittest discover --pattern '*_test.py'

build:
	mkdir --parents builds
	cat $(PROJECT_FILES) \
		| sed --regexp-extended 's/\s{4}/\t/g' \
		| sed --regexp-extended 's/^\s*#.*$$//' \
		| grep --invert-match 'from robot_fan' \
		| grep --invert-match '^\s*$$' \
		> builds/robot_fan.py

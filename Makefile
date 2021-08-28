PROJECT_FILES = \
	robot_fan/configuration.py \
	robot_fan/interval.py \
	robot_fan/toggling_value.py \
	robot_fan/running.py \
	robot_fan/__main__.py

.PHONY: build

build:
	mkdir --parents builds
	cat $(PROJECT_FILES) \
		| sed --regexp-extended 's/\s{4}/\t/g' \
		| sed --regexp-extended 's/^\s*#.*$$//' \
		| grep --invert-match 'from robot_fan' \
		| grep --invert-match '^\s*$$' \
		> builds/robot_fan.py

none: help

help:
	@echo "Elements: A modern music library."
	@echo
	@echo "demo_deploy    Run Elements from /tmp on Ubuntu."
	@echo "demo_clean     Clean up the demo."
	@echo "run            Run Elements directly from this repository."
	@echo "lint           Run pylint3 on the Elements package."
	@echo "test           Run pytests for Elements."

demo_deploy: demo_clean
	@mkdir -p /tmp/bin
	@cp -rf elements /tmp/bin/elements
	@cp -f deploy/elements_tmp.desktop ~/.local/share/applications/
	@gtk-launch elements_tmp
	@rm -f ~/.local/share/applications/elements_tmp.desktop

demo_clean:
	@rm -rf /tmp/bin/elements
	@rm -f ~/.local/share/applications/elements_tmp.desktop

lint:
	pylint3 --rcfile=pylintrc elements

run:
	python3 elements/elements.py

test:
	python3 -m pytest elements

.PHONY: demo_clean demo_deploy lint run test

none: help

help:
	@echo "Elements: A modern music library."
	@echo
	@echo "run            Run Elements."
	@echo "lint           Run pylint3 on the Elements package."
	@echo "test           Run pytests for Elements."

demo_deploy: demo_clean
	# Above, we're first cleaning up from any prior runs.
	# Create a folder in /tmp for our application.
	@mkdir -p /tmp/bin
	# Copy our application to the /tmp directory.
	@cp -rf elements /tmp/bin/elements
	# Install our .desktop file.
	@cp -f deploy/elements_tmp.desktop ~/.local/share/applications/
	# Start the application using the .desktop file, thus showing the icon.
	@gtk-launch elements_tmp.desktop
	# Once we start the application, we can delete the .desktop file.
	@rm -f ~/.local/share/applications/elements_tmp.desktop
	# NOTE: We don't want our .desktop file to stay after execution, because
	# it will be broken if we restart our computer (which clears /tmp)

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

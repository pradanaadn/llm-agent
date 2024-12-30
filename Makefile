.PHONY: clean-pycache

clean-pycache:
	@if find . -type d -name "__pycache__" | grep -q __pycache__; then \
        find . -type d -name "__pycache__" -exec rm -r {} +; \
        echo "Cleared __pycache__ directories."; \
	else \
        echo "No __pycache__ directories to clear."; \
	fi
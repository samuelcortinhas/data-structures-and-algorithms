.PHONY: check
check:
	black . --check
	isort . --check

.PHONY: diff
diff:
	black . --diff
	isort . --diff

.PHONY: format
format:
	black .
	isort .

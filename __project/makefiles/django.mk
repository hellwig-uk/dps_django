# Check if there are packages that require updating.
manage:
	@$(VENV)/bin/python manage.py $(ARGS)

runserver:
	@$(VENV)/bin/python manage.py runserver 0.0.0.0:8080

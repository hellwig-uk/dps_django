DC=docker compose -f __project/docker/docker-compose.yml --project-directory ./

# Building docker images with compose.
build:
	$(DC) build

# Same as build but adds --progress-plain to it, handy for troubleshooting.
build-plain:
	$(DC) build --progress=plain

# Start the compose defined docker environment(s).
up:
	$(DC) up -d --force-recreate

# Stop the compose defined docker environment(s).
down:
	$(DC) down

# Create a user shell on work.
shell:
	@$(DC) exec -it -u $(UID) work /bin/bash

# Create a root shell on work.
root:
	@$(DC) exec -it work /bin/bash

# Spin up a base image and create a shell.
base:
	@$(DC) run -it --rm base /bin/bash


DC=docker compose\
 --env-file .env \
 -f __project/docker/docker-compose.yml --project-directory ./

# Building docker images with compose.
build:
	@$(DC) build

# Same as build but adds --progress-plain to it, handy for troubleshooting.
build-plain:
	@$(DC) build --progress=plain

# Start the compose defined docker environment(s).
up:
	@$(DC) up -d --force-recreate

# Stop the compose defined docker environment(s).
down:
	@$(DC) down

# Spin up a base image and run command.
base:
	@$(DC) run -it --rm base $(ARGS)

# Run on work using user.
work:
	@$(DC) exec -it -u $(UID) work $(ARGS)

# Run on work using root
work-root:
	@$(DC) exec -it work $(ARGS)



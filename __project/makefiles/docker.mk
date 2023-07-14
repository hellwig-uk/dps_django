# Building docker images with compose.
build:
	@$(DC) build

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

# Run on db using root
db:
	@$(DC) exec -it db $(ARGS)

psql:
	@$(DC) exec -it -u postgres db /usr/bin/psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

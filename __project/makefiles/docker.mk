DC=docker compose -f __project/docker/docker-compose.yml --project-directory ./

# Building docker images with compose.
build:
	$(DC) build

# Start the compose defined docker environment(s).
up:
	$(DC) up -d --force-recreate

down:
	$(DC) down

shell:
	@$(DC) exec work /application/__project/scripts/add_passwd_line.sh
	@$(DC) exec -it -u $(UID) work /bin/bash

root:
	@$(DC) exec -it work /bin/bash


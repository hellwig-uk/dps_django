ifeq ($(shell test -e .env && echo yes),)
    $(error '.env' file is missing)
endif

CHECK:=$(shell  __project/scripts/check.sh)

ifneq ($(CHECK), )
    $(error $(CHECK))
endif

include .env

ARGS?=
NAME?=
NARG=$(words $(MAKECMDGOALS))

ifeq ($(NARG),1)
	include __project/makefiles/*.mk
else ifeq ($(NARG), 0)
    include __project/makefiles/help.mk
    .DEFAULT_GOAL = help
else
	ARGS=$(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
	NAME=$(firstword  $(MAKECMDGOALS))
endif

$(NAME):
	@ARGS="$(ARGS)" make --no-print-directory $(NAME)

%:
	@if test $(NARG) -eq 1; then \
		echo Target \'$(MAKECMDGOALS)\' invalid, type \`make help\` for a list \
		of valid commands. && exit 1\
	; fi
# This is the master makefile, it changes the behaviour of make so that given
# multiple targets only the first one is executed and the others are given as
# ARGS. For this to work the actual make commands need to be defined in a 
# seperate makefile which are imported when there is only a single target.
# in other cases the first target is used to call make again with only that
# target and the other targets are passed as ARGS. However make does still call
# the other targets, but they have no effect as % will capture them and they
# silently do nothing, unless the target doesn't exist, hence why the actual
# targets need to be in a different sub makefile so that they don't exist.

include __project/environment.txt

ifeq ($(shell test -e $(DOT_ENV) && echo yes),)
    $(error '.env' file is missing)
endif

CHECK:=$(shell  $(DOT_ENV_CHECK_SH))

ifneq ($(CHECK), )
    $(error $(CHECK))
endif

include .env

ARGS?=
NAME?=
NARG=$(words $(MAKECMDGOALS))

ifeq ($(NARG),1)
	include $(MAKEFILES)/*.mk
else ifeq ($(NARG), 0)
    include $(MAKEFILES)/help.mk
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
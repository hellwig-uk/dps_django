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

__ARGS?=
__NAME?=
__NARG=$(words $(MAKECMDGOALS))

ifeq ($(__NARG),1)
	__ARGS:=$(__ARGS)
	include $(MAKEDIR)/*.mk
else ifeq ($(__NARG), 0)
    include $(MAKEDIR)/help.mk
    .DEFAULT_GOAL = help
else
	__ARGS=$(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
	__NAME=$(firstword  $(MAKECMDGOALS))
endif

.PHONE: $(MAKECMDGOALS)

$(__NAME):
	@__ARGS="$(__ARGS)" make --no-print-directory $(__NAME)

$(__ARGS): .FORCE
	@if test $(__NARG) -eq 1; then \
		echo Target \'$(MAKECMDGOALS)\' invalid, type \`make help\` for a list \
		of valid commands. && exit 1\
	; fi

.FORCE:
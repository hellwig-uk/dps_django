# This is the master makefile, it changes the behaviour of make so that given
# multiple targets only the first one is executed and the others are given as
# ARGS. For this to work the actual make targets need to be defined in seperate
# makefile(s) which are imported when there is no target. In other cases the
# first target is used to call make again given the target and the other goals
# as variables (so no target).

include __project/makefiles/__environment._mk

ARGS?=
__TARGET?=help
__NARG=$(words $(MAKECMDGOALS))

ifeq ($(__NARG), 0)
    undefine CALL_MAKE
    include $(MAKEDIR)/*.mk
	ARGS:=$(ARGS)
	.DEFAULT_GOAL = $(__TARGET)
else
    CALL_MAKE=true
	__TARGET=$(firstword  $(MAKECMDGOALS))
    __OTHERS=$(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
	__IGNORE=$(shell echo $(__OTHERS) | tr ' ' '\n' | sort -u | grep -vwxE "$(__TARGET)")
	__VALID_TARGETS=$(shell $(SCRIPTS)/list_targets.sh)
	ifneq ($(filter $(__TARGET), $(__VALID_TARGETS)), $(__TARGET))
        $(error '$(__TARGET)' is not a valid target must be one of:$(__VALID_TARGETS))
	endif
endif

.EXPORT_ALL_VARIABLES:
.PHONY: $(__TARGET) $(__OTHERS)
.SILENT:
.FORCE:

ifdef CALL_MAKE

$(__TARGET): .FORCE
	@ARGS="$(__OTHERS)" __TARGET=$(__TARGET) make --no-print-directory

$(__IGNORE): .FORCE
	@true

endif
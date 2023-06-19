UID?=$(shell id -u)
GID?=$(shell id -g)
USER?=$(shell id -un)
PWDLINE?=$(USER):x:$(UID):$(GID):$(USER):$(HOME):/bin/bash
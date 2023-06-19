# Devdocker

This repository is a template for using docker in a development environment.
It is driven by Make and modifies its behaviour by having multiple targets
become one target (the first) and the other targets become variables.
It does so by checking upon first invocation if there are multiple targets,
if so rebuild the make command to be one target with variables and call itself.
The other targets will go to a no-op target.




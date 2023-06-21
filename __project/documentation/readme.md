Dunder Project
==============

This layout is to prevent cluttering of the repository root. It uses makefiles
to drive most of the project administrative functionality.
The reason for using makefiles is because this is the lowest common denominator,
which is by default installed in almost all unix like environments.

For setting up the environment we use Docker, again driven by Make.
This makes it straight forward to setup the various environments in a
predictable and automated way. Please refer to [environments](environments.md)
for more information about this.

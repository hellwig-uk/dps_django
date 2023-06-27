Django Extended Dunder Project Structure
========================================

This layout is used for `Python` based projects with a focus on preventing as
much as possible of cluttering of the repository root. It uses `Make` to drive
most of the project administrative functionality. The reason for using `Make` is
because this is the lowest common denominator, which is by default installed in
almost all unix like environments.

For setting up the environment we use Docker, again driven by `Make`. This makes
it straight forward to setup the various environments in a predictable and
automated way. Please refer to [Branches & Environments](branch_envs.md) for
more information about this.

You will need to have an `.env` file set in the root of the project, which sets
things up like the environment and user/passwords for services. A copy of what
is expected can be found in `__project/dependencies/dot_env_file.txt`.

Other more static project specific variables can be set in
`__project/environment.txt`.

VSCode
------
The docker environment is meant to be run outside any other applications, this
can make it more difficult for IDE's that have high integration such as VScode.
What you would probably want to do is open the container using  dev container
extension, then follow the 
[guide](https://code.visualstudio.com/docs/devcontainers/attach-container) to
create a `Named Configuration File`, subsequently add in the configuration:
`"remoteUser": "<your-local-user-name>"` .
Upon next vscode attachment you should now use the local user and have your
home directory mapped.

You probably also want to install the Python extension and select the
interpreter path which is in /opt/venv/$PROJECT/bin/python


Dunder Project Structure
========================

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

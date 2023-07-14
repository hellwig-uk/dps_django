"""
This will return the makefile environment as a dictionary.
"""
from subprocess import PIPE, run


def _get_make_environment():
    show = run(
        ["make show_environment"],
        check=True,
        shell=True,
        stdout=PIPE,
    ).stdout.decode("utf-8")

    values = {}
    key = ""
    value = ""
    for line in show.split("\n"):
        if "=" in line:
            key, value = line.split("=", 1)
            values[key] = value
        else:
            value = value + "\n" + line
            values[key] = value

    for key in list(values.keys()):
        values[key] = values[key][1:-1]

    return values


MAKE = _get_make_environment()

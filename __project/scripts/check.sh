#! /usr/bin/env sh

EXPECTED=`mktemp`
PROVIDED=`mktemp`

cut -f1 -d# < __project/dependencies/dot_env_file.txt | \
cut -f1 -d= | \
sort | grep "\S" > $EXPECTED

cut -f1 -d# < .env | \
cut -f1 -d= | \
sort | grep "\S" > $PROVIDED

DIFFERENCE=`diff $EXPECTED $PROVIDED`

if test -n "$DIFFERENCE"
then
    echo "'.env' file is not valid, difference is:"
    echo $DIFFERENCE
fi

rm $EXPECTED $PROVIDED
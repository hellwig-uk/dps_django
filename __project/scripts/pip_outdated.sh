#! /usr/bin/env sh
EXCLUDE=$(awk '!/^#/ { printf "--exclude %s ", $0 }' $PIPRDIR/_pip_outdated_check_exclude.txt)
OUTDATED=`"$VENV"/bin/pip list --outdated --not-required $EXCLUDE`
if [ -z "$OUTDATED" ]
then
    exit 0
else
    echo "----------------------------"
    echo "! Outdated packages detected"
    echo "----------------------------"
    echo "$OUTDATED"
    exit 1
fi
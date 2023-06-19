#! /usr/bin/env sh

if grep :$UID:$GID: < /etc/passwd
then
   :
else
   echo $PWDLINE >> /etc/passwd
fi
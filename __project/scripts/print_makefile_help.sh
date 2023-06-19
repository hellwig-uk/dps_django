#! /usr/bin/env sh
printf "%s\n" "The following commands are available:"

beginswith() { case $2 in "$1"*) true;; *) false;; esac; }
endswith() { case $2 in *"$1") true;; *) false;; esac; }

FILES=`ls __project/makefiles/*.mk`
DOC=""

for file in $FILES; do
    while IFS= read -r line; do
		if beginswith "#" $line; then
			line=`echo $line | cut -f2 -d#`
			DOC="$DOC\n\t$line"
		else
			if endswith ":" $line; then
				line=`echo $line | cut -f1 -d:`
				printf "%s" "- $line"
				echo $DOC
			fi
			DOC=""			
		fi
    done < "$file"
done
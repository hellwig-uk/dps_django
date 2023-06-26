#! /usr/bin/env sh
endswith() { case $2 in *"$1") true;; *) false;; esac; }

FILES=`ls __project/makefiles/*.mk`

for file in $FILES; do
    while IFS= read -r line; do
			if endswith ":" $line; then
				line=`echo $line | cut -f1 -d:`
				printf "%s" " $line"
			fi
    done < "$file"
done

#!/usr/bin/env zsh

strings | tr '.' ' ' | sed "s/[^A-Za-z'][^A-Za-z']*/\n/g" | grep . | sort | uniq -c | sort -n | sed 's/^ *[0-9]* //' | while read x; do 
	torify w3m -dump "http://en.m.wiktionary.org/wiki/$x"
	torify w3m -dump "https://www.urbandictionary.com/define.php?term=$x"
	torify w3m -dump "https://www.etymonline.com/search?q=$x"
	torify w3m -dump "https://en.m.wikipedia.org/wiki/$x"
	torify w3m -dump "http://simple.m.wikipedia.org/wiki/$x" 
	torify w3m -dump "https://everything2.com/?node=$x"
	torify w3m -dump "https://www.gematrix.org/?word=$x&view_rude=on"
  grep -i "$x" ~/stories/ebooks/gutenberg/*
	sleep 23
done

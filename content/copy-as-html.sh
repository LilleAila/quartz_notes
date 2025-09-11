#!/usr/bin/env bash

# wl-paste | perl -pe 's/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/"[" . (defined $2 ? $2 : $1) . "](" . $1 . ")"/ge' | pandoc -f markdown -t html5 --lua-filter=resolve-images.lua | wl-copy --type text/html

wl-paste | pandoc -f markdown+wikilinks_title_after_pipe -t html5 --lua-filter=resolve-images.lua | wl-copy --type text/html

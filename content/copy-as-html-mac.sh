#!/usr/bin/env bash

pbpaste | pandoc -f markdown+wikilinks_title_after_pipe+task_lists+yaml_metadata_block+tex_math_dollars+raw_html+markdown_in_html_blocks+mark+hard_line_breaks -t html5 --lua-filter=resolve-images.lua --mathjax | pbcopy

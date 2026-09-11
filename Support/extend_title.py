#!/usr/bin/env python3
"""
	Extends the reST title. Cursor needs to be on the title line or the
	title markup line. Must add one reST title markup character to extend.
"""

import os
import re
import sys

lines = [line.rstrip() for line in sys.stdin.readlines()]

# current line should be the markup line
currentLine = int(os.environ['TM_LINE_NUMBER']) - 1
match = re.search(r'^(=|-|~|`|#|"|\^|\+|\*)+', lines[currentLine])
if not match:
	# Oops, there needs to be text to match. Don't change anything.
	print('Cursor is not on a line with a section adornment')
	print('i.e. one of: = - ~ ` # " ^ + *')
	sys.exit(206)
lineLen = len(lines[(currentLine - 1)].expandtabs(int(os.environ['TM_TAB_SIZE'])))
# escape snippet characters
lines = [re.sub(r'([$`\\])', r'\\\1', line) for line in lines]
lines[currentLine] = lineLen * lines[currentLine][0] + '$0'
print('\n'.join(lines))

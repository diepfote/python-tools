#!/usr/bin/env python3

# BSD 2-Clause License

# Copyright (c) 2019, Florian Begusch
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice, this
  # list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright notice,
  # this list of conditions and the following disclaimer in the documentation
  # and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from sys import argv
import re

def get_snippets(content):
    regexp = re.compile(u'snippet.*?(?=snippet)', re.S)
    return regexp.findall(content)

def generate_gedit_snippet (parsed_snippet):
    tab_completion = parsed_snippet[0]
    description = parsed_snippet[1]
    snippet_content = parsed_snippet[2]

    snippet  = '  <snippet>\n'
    snippet += '    <tag>' + tab_completion + '</tag>\n'
    snippet += '    <text><![CDATA['
    snippet += snippet_content.replace('\\', '\\\\')
    snippet += ']]></text>\n'

    return snippet + '  </snippet>\n'

def parse_gummi_snippet (snippet):
    snippet_content = ''
    for index, line in enumerate(snippet.splitlines()):
        if not index:
            tab_completion = line.split(',')[0].split(' ')[1]
            description = line.split(',')[2]

        else:
            snippet_content += line[1:] + '\n'
    
    snippet_content = snippet_content[:len(snippet_content)-1]
    
    return (tab_completion, description, snippet_content)


gummi_snippet_file = argv[1]
matches = []
empty   = ''
content = empty

with open(gummi_snippet_file, 'r') as f:
    content = ''
    for line in f.readlines():
        # skip comments
        if not line.startswith('#'):
            content += line
    
snippets = get_snippets(content)

parsed_snippets = []
for snippet in snippets:
    parsed_snippets.append(parse_gummi_snippet(snippet))

gedit_snippets = []
for parsed_snippet in parsed_snippets:
    gedit_snippets.append(generate_gedit_snippet(parsed_snippet))

# Debug
# print(parsed_snippets[0])

print('<snippets>')
for gedit_snippet in gedit_snippets:
    print(gedit_snippet)
print('</snippets>')


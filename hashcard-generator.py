#!/usr/bin/env python3

# generator for https://github.com/eudoxia0/hashcards

# example:
# $ hashcard-generator 100R.txt > "$t"/test.md
# $ head -n 20 $t/test.md
# Q: sodium percarbonate
# A: Natriumpercarbonat (2 Na2CO3 · 3 H2O2) ist eine Anlagerungsverbindung (Addukt) von Wasserstoffperoxid H2O2 an Natriumcarbonat (Soda, Na2CO3).
#
# ---
#
# Q: bubble wrap
# A: Luftpolsterfolie
#
# ---

# Q: glaze
# A: overlay or cover (food, fabric, etc.) with a smooth, shiny coating or finish: new potatoes which had been glazed in mint-flavoured butter.
#
# ---
#
# Q: lines
# A: a length of cord, rope, wire, or other material serving a particular purpose: wring the clothes and hang them on the line | a telephone line
#
# ---


import sys

with open(sys.argv[1]) as f:
    for line in f:
        if line.isspace() or '--' in line:
            continue
        try:
            q, a = line.split('...', 1)
            print(f'Q: {q.strip()}\nA: {a.strip()}\n\n---\n')
        except:
            print(f'[.] no card for {line[:10].strip()}', file=sys.stderr)


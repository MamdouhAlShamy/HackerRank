inp = "He is a very very good boy, isn't he?"
inp = "[a\\\\b]"

# inp = raw_input()
import re

inp = inp.rstrip()
inp = re.sub("[\[\]!,?._'@+\\\\]", ' ', inp)
inp = inp.split()

print len(inp)

for s in inp:
	print s

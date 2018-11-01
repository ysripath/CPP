'Scan a log file from a NASA server'

import collections
import glob
import re
import pprint

visited = collections.Counter()
for filename in glob.glob('notes/*.log'):
    with open(filename) as f:
        for line in f:
            mo = re.search(r'GET\s+(\S+)\s+200', line)
            if mo is not None:
                url = mo.group(1)
                visited[url] += 1

pprint.pprint(visited.most_common(20))


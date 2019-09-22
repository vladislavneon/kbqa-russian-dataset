import json

with open('properties_forms.txt', 'r') as inf:
    res = {}
    pid = None
    aliases = []
    for line in inf:
        line = line.strip('\n')
        if line.startswith('Count') or \
           line.startswith('Description') or \
           line.startswith('Aliases') or \
           line.startswith('Question') or \
           line.startswith('Label') or \
           line.startswith('# ') or \
           not line:
                continue
        elif line.startswith('####'):
            res[pid] = aliases
            pid = None
            aliases = []
        elif line.startswith('PID'):
            pid = line.replace('PID: ', '')
        else:
            aliases.append(line)

with open('properties_aliases.json', 'w') as ouf:
    json.dump(res, ouf, ensure_ascii=False, indent=4)

def finder_substr(q, prop):
    if re.search(prop, q) is not None:
        return True
    return False

def apply_properties_finder(q, finder, prop):
    f = partial(finder, prop=prop)
    return list(filter(f, q))

def find_property(aliases):
    qs = []
    for alias in aliases:
        cur_qs = apply_properties_finder(filtered_q, finder_substr, alias)
        qs.extend(cur_qs)
    return qs

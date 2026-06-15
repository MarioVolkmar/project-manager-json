def normalize_text(text):
    text = text.strip().lower().split()
    text = " ".join(text)
    return text



def next_id(ls, id_name):
    if len(ls) == 0:
        return 1
    next_value = ls[0][id_name]
    for l in ls:
        if l[id_name] >=  id:
            next_value = l[id_name] + 1
    return next_value



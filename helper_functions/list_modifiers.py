def unique_list(list_in):
    list_out = []

    for x in list_in:
        if x not in list_out:
            list_out.append(x)
    return list_out

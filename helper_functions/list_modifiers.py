from flask import jsonify


def unique_list(list_in):
    list_out = []

    for x in list_in:
        if x not in list_out:
            list_out.append(x)
    return list_out


def as_dict(data_list):
    return [element.as_dict() for element in data_list]


def jsonify_dict(data_list):
    return jsonify(as_dict(data_list))

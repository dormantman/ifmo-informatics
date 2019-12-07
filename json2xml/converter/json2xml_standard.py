# -*- coding: utf-8 -*-
import json


def json2xml(content):
    data = json.loads(content)
    return '<XML>%s</XML>' % _json2xml(data)


def _json2xml(content):
    data = ""

    query = content.keys() if isinstance(content, dict) else range(len(content))

    for key in query:
        value = content[key]
        next_content = _json2xml(value) if isinstance(value, (dict, list)) else value
        data += '<{key}>{content}</{key}>'.format(key=key, content=next_content)

    return data

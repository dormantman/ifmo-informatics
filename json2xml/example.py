import json

from json2xml.converter.json2xml import Json2Xml

json_content = {
    "id":               17047,
    "label_translated": "Pub \"hotel",
    "index_name":       "pub_hotel",
    "label":            {
        "en-GB": "Pub hotel"
    },
    "category":         74,
    "arrays":           {
        "1": [
            1,
            2,
            3
        ],
        "2": [
            {},
            {
                "abs": True,
                "aaa": None
            },
            {}
        ]
    }
}

json_content = json.dumps(json_content)

converter = Json2Xml()
data = converter.convert_json_to_xml(json_content)

print(data)

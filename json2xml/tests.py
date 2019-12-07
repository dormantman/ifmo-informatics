import os

from json2xml.converter.json2xml import Json2Xml

DEBUG = False
ITEM_NAME = 'item'

TESTS_FOLDER = os.path.join('.', 'tests')
OUTPUT_FOLDER = os.path.join('.', 'output')

if not os.path.exists(TESTS_FOLDER):
    os.mkdir(TESTS_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

converter = Json2Xml(item_name=ITEM_NAME, debug_output=DEBUG)

for filename in os.listdir(TESTS_FOLDER):
    name, extension = os.path.splitext(filename)

    if extension == '.json':
        file_path = os.path.join(TESTS_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, name + '.xml')

        content = converter.read_file(file_path)
        data = converter.convert_json_to_xml(content)
        converter.write_file(output_path, data)

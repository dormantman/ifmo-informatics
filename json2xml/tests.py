import json
import os
import time

from json2xml.converter.json2xml import Json2Xml
from json2xml.converter.json2xml_standard import json2xml

DEBUG = False
ZIPPED = False

ITEM_NAME = 'item'

TESTS_FOLDER = os.path.join('.', 'tests')
OUTPUT_FOLDER = os.path.join('.', 'output')

if not os.path.exists(TESTS_FOLDER):
    os.mkdir(TESTS_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

print('Start tests..', end='\n\n')

converter = Json2Xml(item_name=ITEM_NAME, debug_output=DEBUG, zipped=ZIPPED)

for filename in os.listdir(TESTS_FOLDER):
    name, extension = os.path.splitext(filename)

    if extension == '.json':
        time_for = time.time()

        file_path = os.path.join(TESTS_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, name + '.xml')

        print('Convert %s to %s ...' % (filename, name + '.xml'))

        content = converter.read_file(file_path)
        data = converter.convert_json_to_xml(content)
        converter.write_file(output_path, data)

        time_diff = round(time.time() - time_for, 5)
        print('Successfully converted %s to %s for %s seconds' % (
            filename, name + '.xml', time_diff
        ))

        time_for = time.time()
        json2xml(content)
        time_diff = round(time.time() - time_for, 5)
        print('Standard solution for %s seconds' % time_diff, end='\n\n')

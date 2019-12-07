# -*- coding: utf-8 -*-


class Types:
    Key = 'key'
    Element = 'element'
    Structure = 'structure'


class Symbols:
    ObjectOpen = '{'
    ObjectClose = '}'
    ArrayOpen = '['
    ArrayClose = ']'
    StringOpen = '"'
    StringClose = '"'
    Space = ' '
    NELL = '\n'
    Colon = ':'
    Comma = ','
    Slash = '\\'
    Passed = (Space, NELL)
    Split = (Colon, Comma, StringOpen)
    ElementSides = (ObjectOpen, ObjectClose, ArrayOpen, ArrayClose)


class Json2Xml:
    def __init__(self, item_name='item', debug_output=False):
        self._write_data = None
        self._on_string = False
        self._virtual_structure = None
        self._keys = []
        self._indexes = []
        self._open_keys = []

        self.item_name = item_name
        self.debug_output = debug_output

    @staticmethod
    def read_file(filename: str) -> str:
        with open(filename, mode='r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def write_file(filename: str, data: str):
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(data)

    def _write(self, data: str):
        self._write_data += data

    @staticmethod
    def _get_symbol_type(symbol: str or None):
        if symbol in (',', ''):
            return Types.Element

        elif symbol == ':':
            return Types.Key

        return Types.Structure

    def _get_current_object(self):
        current_object = self._virtual_structure

        for index, key in enumerate(self._keys):
            try:
                if isinstance(current_object[key], (list, dict)):
                    current_object = current_object[key]

            except (KeyError, TypeError):
                continue

        return current_object

    def _virtual_add(self, object):
        if self._virtual_structure is None:
            self._virtual_structure = object
            return

        current_object = self._get_current_object()

        if isinstance(current_object, list):
            self._keys.append(len(current_object))
            current_object.append(object)

            item_name = self.item_name.format(index=len(current_object) - 1)

            if isinstance(object, str):
                self._write('<{item}>{obj}</{item}>\n'.format(item=item_name, obj=object))
            else:
                self._write('<{item}>\n'.format(item=item_name))

        else:
            key = self._keys[-1]

            current_object[key] = object

            if isinstance(object, str):
                self._write('<{key}>{obj}</{key}>\n'.format(key=key, obj=object))

            else:
                if key.isdigit():
                    key = '_%s_' % key

                self._write('<%s>\n' % key)
                self._open_keys.append(key)

    def _add_index(self):
        self._indexes.append(len(self._keys) - 1)

    def _get_index(self):
        return self._indexes.pop()

    def _close_object(self):
        index = self._get_index()

        self._keys = self._keys[:index]
        new_object = self._get_current_object()

        if isinstance(new_object, list):
            item_name = self.item_name.format(index=len(new_object) - 1)
            self._write('</{item}>\n'.format(item=item_name))

    def _get_current_with_close(self):
        index = self._get_index()

        copy_keys = self._keys
        self._keys = self._keys[:index]
        closed_object = self._get_current_object()
        self._keys = copy_keys

        self._indexes.append(index)

        return closed_object

    def _processing_word(self, word: str, symbol: str or None = None):
        if not word:
            return

        word = word.strip(Symbols.StringOpen)
        types = self._get_symbol_type(symbol)

        if self.debug_output:
            print(word.center(20), types.center(14))

        if types == Types.Structure:
            if word == Symbols.ArrayOpen:
                self._virtual_add([])
                self._add_index()
                self._write('<array>\n')

            elif word == Symbols.ArrayClose:
                self._write('</array>\n')
                self._close_object()

                if isinstance(self._get_current_object(), dict) and self._open_keys:
                    key = self._open_keys.pop()
                    self._write('</%s>\n' % key)

            elif word == Symbols.ObjectOpen:
                self._virtual_add({})
                self._add_index()

            elif word == Symbols.ObjectClose:
                if self._open_keys:
                    current_object = self._get_current_with_close()

                    if isinstance(current_object, dict) and self._open_keys:
                        key = self._open_keys.pop()
                        self._write('</%s>\n' % key)

                self._close_object()

        elif types == Types.Key:
            self._keys.append(word)

        elif types == Types.Element:
            self._virtual_add(word)

    def _put_spaces(self):
        level = 0
        write_data = ''

        for line in self._write_data.split('\n'):
            tags = line.split('</')
            length_tags = len(tags)

            if length_tags == 2:
                first, second = tags

                first = first.split('>')[0].lstrip('<')
                second = second.rstrip('>')

                if first == second:
                    write_data += '%s%s\n' % (' ' * ((level + 1) * 4), line)

                else:
                    write_data += '%s%s\n' % (' ' * (level * 4), line)
                    level -= 1

            else:
                level += 1
                write_data += '%s%s\n' % (' ' * (level * 4), line)

        self._write_data = write_data.rstrip()

    def convert_json_to_xml(self, content: str):
        self._write_data = ''
        self._virtual_structure = None
        self._keys = []
        self._indexes = []
        self._open_keys = []

        word = ''
        for symbol in content:
            if self._on_string:
                if symbol == Symbols.StringClose and word[-1] != Symbols.Slash:
                    self._on_string = not self._on_string
                    word += symbol

                else:
                    word += symbol

            elif symbol in Symbols.ElementSides:
                self._processing_word(word, '')
                self._processing_word(symbol)
                word = ''

            elif symbol not in Symbols.Passed and symbol not in Symbols.Split:
                word += symbol

            elif symbol == Symbols.StringOpen:
                self._on_string = not self._on_string

                self._processing_word(word)
                word = symbol

            elif word:
                self._processing_word(word, symbol.strip())
                word = ''

        self._put_spaces()

        self._write_data = '<?xml version="1.0" encoding="utf-8"?>\n' \
                           '<XML>\n%s\n</XML>' % self._write_data

        return self._write_data

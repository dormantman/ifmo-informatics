import json
from heapq import heapify
from heapq import heappop
from heapq import heappush

import numpy as np


def encodeHuffman(fileIn, fileOut):
    try:
        file = open(fileIn, "r")
        i = 0
        str = ""
        for line in file:  # итерация по строкам файла
            str += line.replace("\n", "")
            i += 1
        file.close()

        tree = makeTree(str)
        # print(tree)
        result = ""
        for char in list(str):
            for i, sublist in enumerate(tree):
                if char in sublist:
                    result += tree[i][1]

        f = open(fileOut, "w")
        f.write(json.dumps(tree) + "\n")
        f.write(result)
        f.close()
        return True
    except:
        return False


def makeTree(str):
    data = getCharFrequency(str)
    heap = [[weigh, [char, ""]] for char, weigh in data.items()]
    heapify(heap)
    while len(heap) > 1:
        left_node = heappop(heap)
        right_node = heappop(heap)
        for pair in left_node[1:]:
            pair[1] = '0' + pair[1]
        for pair in right_node[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [left_node[0] + right_node[0]] + left_node[1:] + right_node[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def decodeHuffman(fileIn, fileOut):
    try:
        with open(fileIn, "r") as read_file:
            line = read_file.readline()
            tree = np.array(json.loads(line))

            content = read_file.readline()

            key = ""
            result = ""
            while len(content):
                key += content[0]
                content = content[1:]
                for i, sublist in enumerate(tree):
                    if key in sublist:
                        result += tree[i][0]
                        key = ""

            f = open(fileOut, "w")
            f.write(result)
            f.close()
            return True
    except:
        return False


def getCharFrequency(str):
    letters_list = list(str)
    unique_letters = set(letters_list)

    result = dict()
    for chars in unique_letters:
        result[chars] = letters_list.count(chars)
    return result


def encodeLZ(fileIn, fileOut):
    try:
        file = open(fileIn, "r")
        i = 0
        input_str = ""
        for line in file:  # итерация по строкам файла
            input_str += line.replace("\n", "")
            i += 1
        file.close()

        keys_dict = {}

        result = ""

        start = 0
        offset = 1
        isWritten = False
        sub_str = ""
        while True:
            if not (len(input_str) >= start + offset):
                if not isWritten:
                    result += sub_str
                break
            sub_str = input_str[start:start + offset]
            # print (sub_str, start, offset)
            if sub_str in keys_dict:
                offset += 1
                isWritten = False
            else:
                keys_dict[sub_str] = "{:03d}".format(len(keys_dict))
                start += offset
                offset = 1
                if len(sub_str) > 1:
                    result += str(keys_dict[sub_str[:-1]]) + sub_str[-1]
                else:
                    result += sub_str
                isWritten = True
                # print ('Adding %s' %sub_str)
        # print (result)
        # print(keys_dict)
        f = open(fileOut, "w")
        f.write(result)
        f.close()
        return True
    except:
        return False


def decodeLZ(fileIn, fileOut):
    try:
        with open(fileIn, "r") as read_file:
            content = read_file.readline()

            result = ""

            keys_dict = {}
            keys_dict['000'] = content[:1]
            result += keys_dict['000']
            content = content[1:]

            while len(content):
                # print('dict = '+str(keys_dict))
                # print('content[:1] = '+str(content[:1]))
                if content[:3].isdigit():
                    if not content[3:4].isdigit():
                        newKey = keys_dict[content[:3]] + content[3:4]
                        keys_dict[str("{:03d}".format(len(keys_dict)))] = newKey
                        result += newKey
                        content = content[4:]
                    else:
                        newKey = keys_dict[content[:3]]
                        keys_dict[str("{:03d}".format(len(keys_dict)))] = newKey
                        result += newKey
                        content = content[3:]
                else:
                    newKey = content[:1]
                    keys_dict[str("{:03d}".format(len(keys_dict)))] = newKey
                    result += newKey
                    content = content[1:]

            # print(keys_dict)
            f = open(fileOut, "w")
            f.write(result)
            f.close()
            return True
    except:
        return False


def file_size(filePath):
    with open(filePath, 'r') as file:
        filename = file.read()
        len_chars = sum(len(word) for word in filename)
        return len_chars


fileNameIn1 = "./files/textIn.txt"
fileNameOut1 = "./files/textOut.txt"
print(encodeHuffman(fileNameIn1, fileNameOut1))
print(decodeHuffman(fileNameOut1, fileNameIn1))

print("Huffman data compression coefficient = " + str(file_size(fileNameOut1) / file_size(fileNameIn1)))

fileNameIn2 = "./files/textIn2.txt"
fileNameOut2 = "./files/textOut2.txt"
print(encodeLZ(fileNameIn2, fileNameOut2))
print(decodeLZ(fileNameOut2, fileNameIn2))

print("ZVW data compression coefficient = " + str(file_size(fileNameOut2) / file_size(fileNameIn2)))

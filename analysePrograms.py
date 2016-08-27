import os
import re
from collections import Counter
from math import floor


def readProgramList(filename):
    programs = []

    with open(filename, 'r') as f:
        keys = f.readline().strip().split('\t')

        for line in f:
            data = line.strip().split('\t')
            programs.append(dict(zip(keys, data)))

        return programs


def readProgram(filepath):
    """ Strip out comments and blank lines"""

    code = ""

    with open(filepath, 'r') as f:
        multiline = False

        for line in f:
            txt = ""

            if not multiline:
                index = line.find('/*')
                if index != -1:
                    txt = line[:index]
                    multiline = True
                else:
                    txt = line

            if multiline:
                index = line.find('*/')
                if index != -1:
                    txt += line[index + 2:]
                    multiline = False
                else:
                    continue

            if not multiline:
                index = txt.find('//')
                if index != -1:
                    txt = txt[:index]

            txt = txt.strip()
            if txt:
                code += txt + '\n'

    return code


def getAllCode(folder):
    code = ""
    files = os.listdir(folder)

    for f in files:
        code += readProgram(os.path.join(folder, f))

    return code


def getAllCodeLengths(folder):
    codeLength = []

    for f in os.listdir(folder):
        c = readProgram(os.path.join(folder, f))
        codeLength.append(len(c.split('\n')))

    print sum(codeLength) / len(codeLength)
    print codeLength[int(floor(len(codeLength) / 2))]


def countWords(code, n):
    split_re = re.compile("[\s+,;\.\(\)\{\}\[\]]")
    digit_re = re.compile("\d+")

    re_number = re.compile("(?:-?\d+(?:\.\d+)?)")
    re_operator = re.compile("([\+\-=<>\!\*\/&\|]+)")
    re_word = re.compile("(\w[\w\d_]*)")
    re_function = re.compile("var\s*(\w[\w\d_]*)\s*=\s*function")
    re_function = re.compile("prototype\.(\w[\w\d_]*)\s*=\s*function")

    #words = re_number.findall(code)
    #words = re_word.findall(code, re.IGNORECASE)
    words = re_function.findall(code, re.IGNORECASE)

    #words = split_re.split(code)
    #words = [word for word in words if word and not digit_re.match(word)]

    #for word in split_re.split(code):
    #    word_count[word] += 1

    print Counter(words).most_common(n)


#code = readProgram('testComments.txt')
#countWords(code)

all_code = getAllCode('code')
countWords(all_code, 100)

#getAllCodeLengths('code')

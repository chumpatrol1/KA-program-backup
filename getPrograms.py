import urllib2
import json
import os

# Keys from JSON that we want to save
data_keys = ['id', 'title', 'created', 'sumVotesIncremented', 'spinoffCount']


def getJSONFromURL(url):
    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read()
        return

    html = response.read()
    return json.loads(html)


def getProgramList(max_programs, username='peterwcollingridge'):
    """ Get the JSON data for a given number of my programs. """

    data = getJSONFromURL('https://www.khanacademy.org/api/internal/user/scratchpads?username=%s&sort=1&limit=%s&page=0' % (username, max_programs))

    # Add a program ID, based on its URL
    for program in data["scratchpads"]:
        program['id'] = program['url'].split('/')[-1]

    return data["scratchpads"]


def writeProgramList(program_data, filename, data_keys):
    """Write a list of specific keys from each program in the program data to a file. """

    with file(filename, 'w') as f:
        f.write('\t'.join(data_keys) + '\n')

        for program in program_data:
            f.write('\t'.join(("%s" % program[key]).encode('utf8') for key in data_keys) + '\n')


def readProgramList(filename):
    programs = []

    with open(filename, 'r') as f:
        keys = f.readline().strip().split('\t')

        for line in f:
            data = line.strip().split('\t')
            programs.append(dict(zip(keys, data)))

        return programs


def getCodeFromProgram(id):
    """ Get the JSON data for a given number of my programs. """

    data = getJSONFromURL('https://www.khanacademy.org/api/internal/show_scratchpad?scratchpad_id=%s' % id)

    if not data:
        return

    scratchpad = data["scratchpad"]
    revision = scratchpad["revision"]
    return revision['code']


def writeCode(id):
    code = getCodeFromProgram(id)

    if code:
        with open(os.path.join('code', '%s' % id), 'w') as f:
            f.write(code.encode('utf8'))


def getExistingPrograms(filepath):
    return os.listdir(filepath)


def writePrograms(list, start, stop, existing_programs):
    """ Find programs within two bounds in the program list and write its code. """

    count = 0

    for program in list[start:]:
        if (program['id'] not in existing_programs):
            writeCode(program['id'])
            count += 1
            if count >= stop:
                break

    print "%d programs added" % count


#program_data = getProgramList(1000)
#print len(program_data)
#writeProgramList(program_data, 'program_list.txt', data_keys)

existing_programs = getExistingPrograms('code')
program_data = readProgramList('program_list.txt')
writePrograms(program_data, 0, 50, existing_programs)

import urllib.request
import json
import os
import datetime
# Keys from JSON that we want to save
data_keys = ['id', 'title', 'created', 'sumVotesIncremented', 'spinoffCount', 'url']


def getJSONFromURL(url):
    try:
        response = urllib.request.urlopen(url)
    except Exception as e:
        print(e)
        return

    html = response.read()
    #print(html)
    return json.loads(html)


def getProgramList(max_programs, username='peterwcollingridge', kaid=None):
    """ Get the JSON data for a given number of my programs. """
    if(kaid):
        if('kaid_' not in kaid):
            kaid = 'kaid_' + kaid
        url = 'https://www.khanacademy.org/api/internal/user/scratchpads?kaid=%s&sort=1&limit=%s&page=0' % (kaid, max_programs)
        #print(url)
        data = getJSONFromURL(url)
    else:
        data = getJSONFromURL('https://www.khanacademy.org/api/internal/user/scratchpads?username=%s&sort=1&limit=%s&page=0' % (username, max_programs))
    # Add a program ID, based on its URL
    for program in data["scratchpads"]:
        program['id'] = program['url'].split('/')[-1]

    return data["scratchpads"]


def writeProgramList(program_data, filename, data_keys):
    """Write a list of specific keys from each program in the program data to a file. """
    print(filename)
    with open("profiles/"+filename, 'w', encoding='utf-8') as f:
        f.write('\t'.join(data_keys) + '\n')

        for program in program_data:
            f.write('\t'.join(("%s" % program[key]) for key in data_keys) + '\n')


def readProgramList(filename):
    programs = []

    with open(filename, 'r', encoding='utf-8') as f:
        keys = f.readline().strip().split('\t')

        for line in f:
            data = line.strip().split('\t')
            programs.append(dict(zip(keys, data)))

        return programs


def getCodeFromProgram(id):
    """ Get the JSON data for a given number of my programs. """
    url = f"https://www.khanacademy.org/api/labs/scratchpads/{id}"
    #print(url)
    data = getJSONFromURL(url)

    if not data:
        return
    
    new_data = {
        'spinoffCount': data['spinoffCount'],
        'height': data['height'],
        'date': data['date'],
        'originSimilarity': data['originSimilarity'],
        'title': data['title'],
        'slug': data['slug'],
        'width': data['width'],
        'revision': data['revision'],
        'imageUrl': data['imageUrl'],
        'url': data['url'],
        'created': data['created'],
        'kaid': data['kaid'],
        'sumVotesIncremented': data['sumVotesIncremented'],
        'originScratchpadId': data['originScratchpadId'],
        'retrievalDate': datetime.datetime.now(tz=None).strftime("%d-%b-%Y (%H:%M:%S.%f)"),
    }

    #print(new_data)

    #revision = data["revision"]
    return new_data

def writeCode(id, author = "David Elijah de Siqueira Campos McLaughlin", kaid = "kaid_976851263300560061760577"):

    code = getCodeFromProgram(id)
    #print(code['spinoffCount'])
    #print(code)
    script = f"/**{str(code['title'])} by {str(author)}\\n" +\
        f"Original size({code['width']}, {code['height']});\\n" +\
        f"Originally Created on {code['created']} by {code['kaid']}\\n" +\
        f"Last Edited: {code['created']}\\n" +\
        f"Votes/Spinoffs: {code['sumVotesIncremented']}/{code['spinoffCount']}\\n" +\
        f"Originally Created: {code['date']} from origin {code['originScratchpadId']} with similarity of {code['originSimilarity']}\\n" +\
        f"Original Link: {code['url']}\\n" +\
        f"Retrieved On: {code['retrievalDate']}**/\\\n"
    #if(id == "2508346688"):
    #    print(repr(code['revision']['code']))
    real_code = repr(code['revision']['code']).replace("\n", "\\n")[1:-1]
    real_code = real_code.replace('\"', '\\"')

    if code:
        with open(os.path.join('code', '%s' % kaid, '%s-%s.html' % (code['slug'], id)), 'w', encoding = 'utf-8') as f:
            f.write(f"<html>\n\
<head>\n\
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n\
    <title>{code['title']}</title>\n\
    <link rel=\"stylesheet\" href=\"../../build/css/live-editor.core_deps.css\"/>\n\
    <link rel=\"stylesheet\" href=\"../../build/css/live-editor.audio.css\"/>\n\
    <link rel=\"stylesheet\" href=\"../../build/css/live-editor.tooltips.css\"/>\n\
    <link rel=\"stylesheet\" href=\"../../build/css/live-editor.ui.css\"/>\n")
            f.write("<style>\n\
        body {\n\
            padding: 20px;\n\
        }\n\
        h1 {\n\
            padding: 0;\n\
            margin: 0 0 20px 0;\n\
        }\n\
        #sample-live-editor {\n\
            padding: 0;\n\
        }\n\
    </style>\n")
            f.write(f"</head>\n\
<body>\n\
    <h1>{code['title']}</h1>\n\
    <div id=\"sample-live-editor\"></div>\n\
    <script src=\"../../build/js/live-editor.core_deps.js\"></script>\n\
    <script src=\"../../build/js/live-editor.editor_ace_deps.js\"></script>\n\
    <script src=\"../../build/js/live-editor.audio.js\"></script>\n\
    <script src=\"../../build/js/live-editor.shared.js\"></script>\n\
    <script src=\"../../build/js/live-editor.tooltips.js\"></script>\n\
    <script src=\"../../build/js/live-editor.ui.js\"></script>\n\
    <script src=\"../../build/js/live-editor.editor_ace.js\"></script>\n\
    <script>\n\
    var outputUrl = \"../output.html\";\n")
            f.write(f"var code = \"{script}\";\n\n")
            f.write(f"code = code + \"\\n{real_code}\";\n")
            f.write("window.liveEditor = new LiveEditor({\n\
                el: $(\"#sample-live-editor\"),\n\
                code: code,\n\
                width: 400,\n\
                height: 400,\n\
                editorHeight: \"80%\",\n\
                autoFocus: true,\n\
                workersDir: \"../../build/workers/\",\n\
                externalsDir: \"../../build/external/\",\n\
                imagesDir: \"../../build/images/\",\n\
                soundsDir: \"../../sounds/\",\n\
                execFile: outputUrl,\n\
                jshintFile: \"../../build/external/jshint/jshint.js\",\n\
                newErrorExperience: true,\n\
            });\n\
            liveEditor.editor.on(\"change\", function() {\n\
                window.localStorage[\"test-code\"] = liveEditor.editor.text();\n\
            });\n\
            ScratchpadAutosuggest.init(liveEditor.editor.editor);\n\
            </script>\n\
        </body>\n\
        </html>\n\
        ")

def getExistingPrograms(filepath):
    return os.listdir(filepath)


def writePrograms(list, kaid):
    """ Find programs within two bounds in the program list and write its code. """

    count = 0

    for program in list:
        #print(program['id'])
        writeCode(program['id'], author = program['authorNickname'], kaid = kaid)
        count += 1

    print(f"{count} programs added")


#program_data = getProgramList(1000)
#print len(program_data)
#writeProgramList(program_data, 'program_list.txt', data_keys)

kaids = ['kaid_976851263300560061760577']
usernames = []
for kaid in kaids:
    program_data = getProgramList(1000, 'E.McLaughlin', kaid)
    #print(program_data[0])
    writeProgramList(program_data, kaid+'.txt', data_keys)
    writePrograms(program_data, kaid)
    
for username in usernames:
    program_data = getProgramList(1000, username)
    print(len(program_data))
    writeProgramList(program_data, username+'.txt', data_keys)

'''
existing_programs = getExistingPrograms('code')
program_data = readProgramList('program_list.txt')
writePrograms(program_data, 0, 50, existing_programs)
'''
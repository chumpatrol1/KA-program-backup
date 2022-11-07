import urllib.request
import json
import os

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
    print(url)
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
        'originScratchpadId': data['originScratchpadId']
    }

    #print(new_data)

    #revision = data["revision"]
    return new_data

def writeCode(id):

    code = getCodeFromProgram(id)
    #print(code['spinoffCount'])
    #print(code)
    script = code['revision']['code'].replace('mouseIsPressed', 'mousePressed')
    script = script.replace('keyIsPressed', 'keyPressed')
    script = script.replace('getImage', 'loadImage')
    if code:
        with open(os.path.join('code', '%s-%s.html' % (code['slug'], id)), 'w', encoding = 'utf-8') as f:
            f.write('<!DOCTYPE html>\n\
            <!-- Webpage with JavaScript Processing code embedded in the HTML -->\n\
<html>\n\
\n\
\t<head>\n\
\t\t<title>')
            f.write(code['title'])
            f.write('</title>\n\
</head>\n\
 <body>\n\
    <p align="center">\n\
	<!--This draws the Procesing Canvas on the webpage -->\n\
      <canvas id="mycanvas"></canvas> \n\
    </p>\n\
 </body>\n\
 \n\
 <!-- Run all the JavaScript stuff -->\n\
 <!-- Include the processing.js library -->\n\
 <script src="processing-1.4.8.min.js"></script>\n\
\n\
\n\
 <script>')
            f.write('var sketchProc=function(processingInstance){ with (processingInstance){\n')
            f.write(f"size({code['width']}, {code['height']});\n")
            f.write(script)
            f.write('}};')
            f.write('// Get the canvas that Processing-js will use\n\
    var canvas = document.getElementById("mycanvas"); \n\
    // Pass the function sketchProc (defined in myCode.js) to Processing\'s constructor.\n\
    var processingInstance = new Processing(canvas, sketchProc); \n\
 </script>\n\n')
            #print(code.keys())
            f.write(f"<p>Originally Created on {code['created']} by {code['kaid']}</p>")
            f.write(f"<p>Last Edited: {code['date']}</p>")
            f.write(f"<p>Votes/Spinoffs: {code['sumVotesIncremented']}/{code['spinoffCount']}</p>")
            f.write(f"<p>Originally Created: {code['created']} from origin {code['originScratchpadId']} with similarity of {code['originSimilarity']}</p>")
            f.write(f"<a href={code['url']}>Original Link: {code['url']}</a>\n")
            f.write(f"Has Image? {'Yes' if 'loadImage' in script else 'No'}. Has Sound? {'Yes' if 'getSound' in script else 'No'}. Has Rotate? {'Yes' if 'rotate' in script else 'No'}")
            f.write('</html>')



def getExistingPrograms(filepath):
    return os.listdir(filepath)


def writePrograms(list):
    """ Find programs within two bounds in the program list and write its code. """

    count = 0

    for program in list:
        print(program['id'])
        writeCode(program['id'])

    print(f"{count} programs added")


#program_data = getProgramList(1000)
#print len(program_data)
#writeProgramList(program_data, 'program_list.txt', data_keys)

kaids = ['kaid_976851263300560061760577']
usernames = []
for kaid in kaids:
    program_data = getProgramList(1000, 'E.McLaughlin', kaid)
    print(program_data)
    writeProgramList(program_data, kaid+'.txt', data_keys)
    writePrograms(program_data)
    
for username in usernames:
    program_data = getProgramList(1000, username)
    print(len(program_data))
    writeProgramList(program_data, username+'.txt', data_keys)

'''
existing_programs = getExistingPrograms('code')
program_data = readProgramList('program_list.txt')
writePrograms(program_data, 0, 50, existing_programs)
'''
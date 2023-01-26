## Before You Start
WARNING: Archived programs may potentially trigger seizures for people with photosensitive epilepsy. Viewer discretion is advised.

## Running Salvaged Programs

In order to run `live-editor` locally you'll have run a local web server.  If you have python installed this can be accomplished by running the following command from the `live-editor` folder:

    python -m SimpleHTTPServer
Alternatively:
    python -m http.server 8000

You should see the following console output:

    Serving HTTP on 0.0.0.0 port 8000 ...

Open up a browser and navigate to http://0.0.0.0:8000/code.
Each folder present contains a list of program, and each folder represents an individual user.


## Preserving Programs

In getPrograms.py, update the kaids line (193) and include the Khan Academy ID's found in every profile. The program will extract user data and every program and place it into a neat folder in code.

## Credits
David Elijah "chumpatrol1" de Siqueira Campos McLaughlin for pulling this together
Peter Collingridge for the base getPrograms code
The Team @ https://github.com/Khan/live-editor for the Live Editor I am currently using
Dillinger "musicalglass" Lee for producing an alternative viewing method "KA Offline"
Sunken, GDA-G and Unsung for onboarding me onto archival projects
and all the programmers whose works have been archived
#!/usr/bin/python
import sys;
import json;
from datetime import time;
from datetime import datetime;
from colors import bcolors;

with open("db.json") as dbfile:
    db = json.loads(dbfile.read());

args = sys.argv;
argLength = len(args);

def main():
    def method(m):
        return {
            'start': start,
            'stop': stop,
            'list': loglist,
            'help': printhelp
        }[m];

    if( argLength > 1 ):
        method( args[1] )();
    else:
        printhelp();

def start():
    def last_id():
        max_id = 0;
        for entry in db:
            if (entry['i'] > max_id):
                max_id = entry[i]
        return max_id;

    if( argLength != 5 ):
        print "Not enough arguments";
        return;
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
    entry = {
            'i': last_id() + 1,
            's': args[2],
            'p': args[3],
            'd': args[4],
            'b': current_time,
            'e': "",
            }

    db.append(entry);
    print json.dumps(db);

    return_message = """\
    Starting a log:
        id: {0}
        sector: {1}
        project: {2}
        description: {3}
        start_time: {4}"""
    print return_message.format( 
            entry['i'],
            entry['s'],
            entry['p'],
            entry['d'],
            entry['b']
            )

def stop():
    print "Stopping the job";

def loglist():
    print "Here's the list";

def printhelp():
    help_string = """{0}\
    Available methods:{1}
        start stop list time"""

    print help_string.format(bcolors.BOLD, bcolors.NORMAL)

main();

# Don't forget to read over JSON stuff

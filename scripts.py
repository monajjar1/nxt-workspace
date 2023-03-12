#!/usr/bin/env python3

import os, getopt, sys;
from  subprocess import Popen,PIPE, run;
from logging import info, basicConfig, INFO;
from threading import Thread;

currentDir = os.getcwd();


def nuke_dir(dir, name):
    info("cleaning {0}".format(name))
    os.system('cd {0}; rm -rf ./node_modules package-lock.json yarn.lock dist build'.format(dir));


def update_dir(dir, name):
    if(os.path.isdir(dir) == False):
        return;
    if(nuke):
       nuke_dir(dir,name)
    # if(update):
    #     os.system('cd {0}; git pull'.format(dir))
    # if(setup):
    #     os.system('cd {0}; rm -rf ./node_modules package-lock.json yarn.lock;'.format(dir))
    # if(publish):
    #     publishPackage(dir);




def main(argv):
    global nuke, setup, update;
    nuke=setup=update=False
    basicConfig(level=INFO, format='%(message)s')
    opts, args =  getopt.getopt(argv,"nsu",["nuke","setup", "update"]);
    for opt,arg in opts:
        if opt in ("-s", "--setup"):
            setup=True;
        elif opt in ("-n", "--nuke"):
            nuke=True;
        elif opt in ("-u", "--update"):
            update=True;
    
    threads = list()
    packages = os.path.join(currentDir, "packages");
    
    for dir in os.listdir(packages):
        thread = Thread(target=update_dir, args=(os.path.join(packages, dir), dir))
        thread.start();
        threads.append(thread);
        if(len(threads) > 3):
            for x in threads:
                x.join()
            threads = list();
    update_dir(currentDir, "workspace")

if __name__ == "__main__":
    main(sys.argv[1:])



    



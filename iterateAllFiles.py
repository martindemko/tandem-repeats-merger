# Copyright (C) 2019 by Zdenka Sedenka <zdenka@sedenka.cz>

import glob
import os
import argparse

parser = argparse.ArgumentParser(description='For all files in directory, runs paresRes.py - scripts that extracts only rows with more than N repetitions with period of length P.')
parser.add_argument('-i', '--inFolder',
                       help='insert filename', required = True)

parser.add_argument('-r', '--res',
                   help='insert res folder', required = True)   

parser.add_argument('-n', '--minNumOfRepeats',                   
                   help='insert min number of repeats', required = True)   

parser.add_argument('-p', '--minLengthOfPeriod',
                   help='insert min length of repeat', required = True)   

args = vars(parser.parse_args())
    
inFolder = args['inFolder']
resFolder = args['res']
minNumOfRepeats = args['minNumOfRepeats']
minLengthOfPeriod = args['minLengthOfPeriod']

os.mkdir(resFolder)

for file in glob.glob(inFolder + "/*.out"):
    print (file, '\n')
    os.system("python parseRes.py -f " + file + " -r " + resFolder + " -n " + minNumOfRepeats + " -p " + minLengthOfPeriod)

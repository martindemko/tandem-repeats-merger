import os.path
from itertools import groupby
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='extracts only rows with more than N repetitions with period of length P.')
    parser.add_argument('-f', '--filename',
                       help='insert filename', required = True)
    parser.add_argument('-r', '--res',
                   help='insert res folder', required = True)   
    parser.add_argument('-n', '--minNumOfRepeats', type=int, 
			help='insert min number of repeats allowed', required = True)
    parser.add_argument('-p', '--minLengthOfPeriod', type=int,
			help='insert min length of period', required = True)	
                   
    args = vars(parser.parse_args())
    
    inname = args['filename']
    resFolder = args['res']
    minNumOfRepeats = args['minNumOfRepeats']
    minLengthOfPeriod = args['minLengthOfPeriod']
    
    inname = os.path.normpath(inname)
    pathList = inname.split(os.sep)
    fileName = pathList[len(pathList) - 1]
    fileNameSplit = fileName.split('.')
    infix = fileNameSplit[0]
    suffix = fileNameSplit[1]
    
    resultsName = resFolder + '/' + infix + '_ppr.txt'
    
    ishead = lambda x: x.startswith('@')
    seqDict = {}
    numOfLine = 0
    with open(inname) as handle:
        head = None
        for h, lines in groupby(handle, ishead):
            numOfLine += 1
            if h:
                head = next(lines)
            else:
                seqLine = next(lines) 
                seqLine = seqLine.strip()
                seq = seqLine.split()[13]
                if int(seqLine.split()[2]) >= int(minLengthOfPeriod) and float(seqLine.split()[3]) >= int(minNumOfRepeats):
                  perms = [seq]
                  for i in range(1,len(seq)):
                    perms.append(seq[i:len(seq)] + seq[0:i])  
                  found = False
                  for perm in perms:
                    if perm in seqDict:
                      seqDict[perm] += 1
                      found = True
                      break
                  if not found: 
                    seqDict[seq] = 1
                              
    with open(resultsName, 'w') as resFile:
        keys = reversed(sorted(seqDict, key=seqDict.get))
        for key in keys:
            resFile.write('%s %s\n' % (seqDict[key], key))
    
    
    
    

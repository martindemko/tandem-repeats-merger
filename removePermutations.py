# Copyright (C) 2019 by Zdenka Sedenka <zdenka@sedenka.cz>

import argparse
import sys
import os

def sumLines(line1, line2):  #sequence from line1 is kept
    line1Split = line1.split()
    line2Split = line2.split()
    resLine = line1Split[0]
    for i in range(1, len(line1Split)):
       resLine = resLine + ' ' + str(int(line1Split[i]) + int(line2Split[i]))
    return resLine 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Removes cyclic permutations from joined.txt.')
    parser.add_argument('-f', '--filename',
                       help='insert filename', required = True)

                   
    args = vars(parser.parse_args())
    
    inname = args['filename']
    
    inname = os.path.normpath(inname)
    pathList =  inname.split(os.sep)
    innameSplit = inname.rsplit('.', 1)
    infix = innameSplit[0]
    suffix = innameSplit[1]
    
    resultsName  = infix + '_fixed.txt' 
    seqDict = {}
    with open(inname, 'r') as handle:
        firstLine = handle.readline()
        for line in handle:
            line = line.strip()
            seq = line.split()[0]
            seqDict[seq] = line
    newDict = {}
    doneArray = []
    for seq in seqDict: 
      if seq in doneArray: #done already as a permutation
          continue
      doneArray.append(seq)
      newDict[seq] = seqDict[seq]
      perms = [] 
      for i in range(1,len(seq)):
        perms.append(seq[i:len(seq)] + seq[0:i])  
      for perm in perms:
        if perm in seqDict:
          doneArray.append(perm)
          newDict[seq] = sumLines(newDict[seq], seqDict[perm])  #keep seq from first
          
    with open(resultsName, 'w') as resFile:
      resFile.write('%s' % (firstLine))
      for key in sorted(newDict): 
          resFile.write('%s\n' % (newDict[key]))
    
            
    
    
    
    

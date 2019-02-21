# Copyright (C) 2016 by Zdenka Sedenka <zdenka@sedenka.cz>

import os 
import argparse

def reverseComplement(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G', '-':'-'}
    return "".join([seq_dict[base] for base in reversed(seq)])

def sumLines(line1, line2):
    line1Split = line1.split()
    line2Split = line2.split()
    newLine = 'sum'
    for i in range(1, len(line1Split)):
        newLine = newLine + ' ' + str(int(line1Split[i]) + int(line2Split[i]))
    return newLine

def sumOneLine(line):
    lineSplit = line.split()
    sum = 0
    for i in range(1, len(lineSplit)):
        sum = sum + int(lineSplit[i])
    return sum
        
    
parser = argparse.ArgumentParser(description='Groups reverse complements.')
parser.add_argument('-f', '--filename',
                   help='insert filename', required = True) 
args = vars(parser.parse_args())

inname = args['filename']

inname = os.path.normpath(inname)
pathList =  inname.split(os.sep)
innameSplit = inname.rsplit('.', 1)
infix = innameSplit[0]
suffix = innameSplit[1]

resultsName  = infix + '_pairedReverseComplement.txt'
resultsNameWithout = infix + '_without_pairedReverseComplement.txt'
resFile = open(resultsName, 'w')
resFileWithout = open(resultsNameWithout, 'w')

seqDict1 = {}
seqDict2 = {}
reverseSeqDict = {}
with open(inname) as handle:
  firstLine = handle.readline()
  for line in handle:
      line = line.strip()
      seq = line.split()[0]
      perms = [seq]
      for i in range(1,len(seq)):
        perms.append(seq[i:len(seq)] + seq[0:i])  
      found = False
      foundSeq = ''
      for perm in perms:
        if perm != seq and perm in seqDict1:
            print ('very weird\n')
        elif reverseComplement(perm) in seqDict1: 
            #print ('reverseComplFound\n')          
            found = True
            foundSeq = reverseComplement(perm) 
            break
        elif reverseComplement(perm) == seq:
            found = True
            foundSeq = 'this'
            break
      if found == True and foundSeq == 'this':
        seqDict1[seq] = line + ' ' + str(sumOneLine(line))
        reverseSeqDict[seq] = 'this'
      elif found == True:
        seqDict2[seq] = line + ' ' + str(sumOneLine(line))
        reverseSeqDict[foundSeq] = seq
      else:
        seqDict1[seq] = line + ' ' + str(sumOneLine(line))
resFile.write(firstLine.strip() + ' sum\n')
resFileWithout.write(firstLine.strip() + ' sum\n')
for seq in sorted(seqDict1):
    if seq in reverseSeqDict:
      if reverseSeqDict[seq] == 'this':#reverse complement itself
        print('exception:', seq, '\n')
        resFile.write(seqDict1[seq] + '\nsum')
        lineSplit = seqDict1[seq].split()
        for i in range(1, len(lineSplit)):
            resFile.write(' ' + lineSplit[i])
        resFile.write('\n\n')
      else:    #has reverse complement
        reverseComplSeq = reverseSeqDict[seq]
        resFile.write(seqDict1[seq] + '\n' + seqDict2[reverseComplSeq] + '\n' + sumLines(seqDict1[seq], seqDict2[reverseComplSeq]) + '\n' +'\n')
    else:   #does not have reverse complement
      resFileWithout.write(seqDict1[seq] + '\n')
          
 
          
    
  
          

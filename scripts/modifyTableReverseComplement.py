import os
import argparse

def reverseComplement(seq):
    seq_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G', '-':'-', 'a':'t', 't':'a', 'c':'g', 'g':'c'}
    return "".join([seq_dict[base] for base in reversed(seq)])

def sumLines(line1, line2, sumCol = True):
    line1Split = line1.split()
    line2Split = line2.split()
    if sumCol:
      newLine = 'sum'
    else:
      newLine = ''
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
merged_resultsName  = infix + '_pairedReverseComplement_merged.txt'
resultsNameWithout = infix + '_without_pairedReverseComplement.txt'
resFile = open(resultsName, 'w')
merged_resFile = open(merged_resultsName, 'w')
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
firstLineSplit = firstLine.split()
merged_resFile.write('Sequence_forw ')
for ind in range(1, len(firstLineSplit)):
    merged_resFile.write(firstLineSplit[ind]+'_forw ')
merged_resFile.write('sum_forw Sequence_rev ')
for ind in range(1, len(firstLineSplit)):
    merged_resFile.write(firstLineSplit[ind]+'_rev ')
merged_resFile.write('sum_rev ')
for ind in range(1, len(firstLineSplit)):
    merged_resFile.write(firstLineSplit[ind]+'_both ')
merged_resFile.write('sum_both\n')
for seq in sorted(seqDict1):
    if seq in reverseSeqDict:
      if reverseSeqDict[seq] == 'this':#reverse complement itself
        print('exception:', seq, '\n')
        lineSplit = seqDict1[seq].split()
        resFile.write(seqDict1[seq] + '\n' + lineSplit[0])
        for i in range(1, len(lineSplit)):
            resFile.write(' 0')
        resFile.write('\nsum')
        for i in range(1, len(lineSplit)):
            resFile.write(' ' + lineSplit[i])
        resFile.write('\n\n')
        merged_resFile.write(seqDict1[seq] + ' ' + lineSplit[0])
        for i in range(1, len(lineSplit)):
            merged_resFile.write(' 0')
        for i in range(1, len(lineSplit)):
            merged_resFile.write(' ' + lineSplit[i])
        merged_resFile.write('\n')
      else:    #has reverse complement
        reverseComplSeq = reverseSeqDict[seq]
        resFile.write(seqDict1[seq] + '\n' + seqDict2[reverseComplSeq] + '\n' + sumLines(seqDict1[seq], seqDict2[reverseComplSeq]) + '\n' +'\n')
        merged_resFile.write(seqDict1[seq] + ' ' + seqDict2[reverseComplSeq] + sumLines(seqDict1[seq], seqDict2[reverseComplSeq], False) + '\n')
    else:   #does not have reverse complement
      resFileWithout.write(seqDict1[seq] + '\n')

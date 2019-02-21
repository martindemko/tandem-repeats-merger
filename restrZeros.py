# Copyright (C) 2016 by Zdenka Sedenka <zdenka@sedenka.cz>

import argparse
import sys
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Removes lines with more than allowed number of zeros per linesss.')
    parser.add_argument('-f', '--filename',
                       help='insert filename', required = True)
    parser.add_argument('-z', '--allowedZeros',
                   help='allowed number of zeros per line', required = True)
    parser.add_argument('-s', '--isSimple',
                   help=' 1 for simple file format, 0 for reverse complements ', required = True)  
    parser.add_argument('-b', '--allowedBal',
                   help='how many times bal can be greater than non-bal', required = True)                  
    parser.add_argument('-r', '--relativize',
                   help='should the values be relativized to the size of the dataset', required = True)                  
    args = vars(parser.parse_args())
    
    inname = args['filename']
    allowedZeros = int(args['allowedZeros'])
    allowedBal = int(args['allowedBal'])
    isSimple = int(args['isSimple'])
    relativize = int(args['relativize'])
    
    inname = os.path.normpath(inname)
    pathList =  inname.split(os.sep)
    innameSplit = inname.rsplit('.', 1)
    infix = innameSplit[0]
    suffix = innameSplit[1]

    numberOfReads = [14970820,10885988,15797160,15814626,9470406,56974950,11623050,10304624,10196784,11609754,11381892,7158556,8604606,9145284,7742944,12816646,10614178,13694252,33587370,32821404,6656904,14209658]
    readLength = 90

    resultsName  = infix + '_allowedZeros_' + str(allowedZeros) + '_allowedBal_' + str(allowedBal) + '_rel' + str(relativize) + '.txt' 
    resFile = open(resultsName, 'w')
    rememberedLines = []
    with open(inname) as handle:
        firstLine = handle.readline()
        resFile.write(firstLine)
        for line in handle:
            line = line.strip()
            lineSplit = line.split()
            if not isSimple and (not lineSplit or lineSplit[0] != 'sum'):
                #print('first if')
                rememberedLines.append(line)
                continue
            zeroCounter = 0
            nonBal = -1
            balCounter = 0
	    if relativize:
		relativeLine = 'relative'
		percentLine = 'percent'
            for i in range(1, len(lineSplit)-1): #first one is name of sequence, last one is the sum 
		if relativize:
			if i%2 == 1: #first: non-bal
				nonBalSize = numberOfReads[i-1]
				current = float(lineSplit[i])
			else: #second: bal
				balSize = numberOfReads[i-1]
				current = (float(lineSplit[i])/balSize)*nonBalSize
			percent = float(lineSplit[i])/(nonBalSize*readLength) 
			relativeLine = relativeLine + ' ' + str(current)
			percentLine = percentLine + ' ' + ('%.25f' % (percent)) 	
		else:	
			current = float(lineSplit[i])
		if i%2 == 1:
                    nonBal = current
                    if current == 0:
                        zeroCounter += 1
                else:
                    if nonBal < current:
                          balCounter += 1
            if zeroCounter <= allowedZeros and balCounter <= allowedBal:
                if not isSimple:
                  for remLine in rememberedLines:
                      resFile.write('%s\n' % (remLine))
                resFile.write('%s\n' % (line))
		if relativize:
			resFile.write(relativeLine + '\n' + percentLine + '\n')
            if not isSimple:
                rememberedLines = []
    resFile.close()
    
    
    
    

import os
from CreatingPreferenceList import CreatingPrefList
import time
import matplotlib.pyplot as plt
import copy
import sys
import ast

class MainController:
    def __init__(self):
        self.homeDir = os.path.abspath('.')
        self.outputPath = os.path.abspath(self.homeDir + '/outputFiles')
        self.objCreatingPreferenceList = CreatingPrefList()
        self.totalTime = list()
        self.Xaxis = list()
        count = 0
        for root, subFolder, files in os.walk(self.homeDir + '\inputPreferenceFiles'):
            for file in files:
                count = count + 1
                self.Xaxis.append(count)
                self.time_start = time.time()
                print('start_time', self.time_start)
                fileNew = open(self.homeDir + '\inputPreferenceFiles/' + str(file))
                outputFile = open(self.outputPath + '/' + 'output_' + str(count) + '.txt', 'w')
                fileContents = fileNew.readlines()
                self.menDict = dict()
                self.womenDict = dict()
                for i in range(2, 2 + self.objCreatingPreferenceList.valueOfN):
                    key, value = fileContents[i].split(':'.strip(" "))
                    self.menDict[key] = ast.literal_eval(value)
                for j in range(2 + self.objCreatingPreferenceList.valueOfN, len(fileContents)):
                    key, value = fileContents[j].split(':'.strip(" "))
                    self.womenDict[key] = ast.literal_eval(value)
                self.checkEngagements(self.menDict, self.womenDict, outputFile)

        self.plotGraph(self.totalTime, self.Xaxis)

    def checkEngagements(self, menDict, womenDict, outputFile):
        guys = sorted(menDict.keys())
        gals = sorted(womenDict.keys())
        guysfree = guys[:]
        engaged = {}
        guyprefers2 = copy.deepcopy(menDict)
        galprefers2 = copy.deepcopy(womenDict)
        while guysfree:
            guy = guysfree.pop(0)
            guyslist = guyprefers2[guy]
            gal = guyslist.pop(0)
            fiance = engaged.get(gal)
            if not fiance:
                # She's free
                engaged[gal] = guy
                print("  %s and %s" % (guy, gal))
                outputFile.write("  %s and %s\n" % (guy, gal))
            else:
                # The bounder proposes to an engaged lass!
                galslist = galprefers2[gal]
                if galslist.index(fiance) > galslist.index(guy):
                    # She prefers new guy
                    engaged[gal] = guy
                    print("  %s dumped %s for %s" % (gal, fiance, guy))
                    outputFile.write("  %s dumped %s for %s\n" % (gal, fiance, guy))
                    if guyprefers2[fiance]:
                        # Ex has more girls to try
                        guysfree.append(fiance)
                else:
                    # She is faithful to old fiance
                    if guyslist:
                        # Look again
                        guysfree.append(guy)
        print('engagements')
        print(engaged)
        outputFile.write('Engagements\n')
        outputFile.write(str(engaged))
        end_time = time.time() - self.time_start
        self.totalTime.append(end_time)
        print('End_time is ', end_time)
        outputFile.write('\nEnd_time is %s' %str(end_time))

    def plotGraph(self, yaxis, xaxis):
        plt.plot(yaxis)
        plt.xlabel('Instance Number')
        plt.xticks(xaxis)
        plt.ylabel('Time for each execution')
        plt.savefig(self.outputPath + '/outputGraph_' + str(self.objCreatingPreferenceList.valueOfN) +'.png')
        plt.show()


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Usage <script name> <number of subjects>')
        print('For example : python MainController.py 5')
        sys.exit()
    elif (sys.argv[1].isdigit()):
        objController = MainController()
    else:
        print('Entered number of subjects value is not integer. Please enter INTEGER value.')
        sys.exit()
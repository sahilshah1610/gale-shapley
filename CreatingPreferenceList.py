
from collections import defaultdict
import os
import random
import sys
import shutil

class CreatingPrefList():
    def __init__(self):

        self.valueOfN = int(sys.argv[1])
        self.currentPath = os.path.abspath('.')

        if os.path.exists(self.currentPath + ('\inputPreferenceFiles')):
            shutil.rmtree(self.currentPath + ('\inputPreferenceFiles'))
        if os.path.exists(self.currentPath + ('\outputFiles')):
            shutil.rmtree(self.currentPath + ('\outputFiles'))
        os.mkdir(self.currentPath + ('/outputFiles'))
        os.mkdir(self.currentPath + ('\inputPreferenceFiles'))
        self.preferenceListDict = defaultdict(dict)
        self.womenDict = dict()
        self.menDict = dict()
        self.createNumberList()

    def createNumberList(self):
        noofppl = self.valueOfN
        menNumberList = list()
        womenNumberList = list()
        for i in range(noofppl*2):
            if (i % 2) == 0:
                menNumberList.append(str(i))
            else:
                womenNumberList.append(str(i))


        for i in range(self.valueOfN):
            print(os.path.abspath('inputPreferenceFiles/input_' + str(i+1) + '.txt'))
            filePreference = open(os.path.abspath('inputPreferenceFiles/input_' + str(i+1) + '.txt'), 'w')
            filePreference.write('\t\t' + str(noofppl) + '\n')
            filePreference.write('Even number are mens and Odd number are women\n')
            self.womenPrefList(womenNumberList, menNumberList, 1, noofppl, filePreference)
            self.womenPrefList(menNumberList, womenNumberList, 0, noofppl, filePreference)
        #print('Finished')

    def womenPrefList(self, NumberList, womenNumberList, tag, noofPpl, inputFile):

        womenListDict = dict()
        for x in range(len(womenNumberList)):
            womenListDictNew = {womenNumberList[x]: []}
            count = 0
            while count < len(NumberList):
                value = random.choice(NumberList)
                if (value in womenListDictNew[womenNumberList[x]]):
                    continue
                elif (value not in womenListDictNew[womenNumberList[x]]):
                    womenListDictNew[womenNumberList[x]].append(value)
                    count = count + 1
            womenListDict.update(womenListDictNew)

        #new code start
        if tag == 1:
            for key, value in womenListDict.items():
                 inputFile.write(str(key) + ':' + str(value) + '\n')

        elif tag == 0:
            for key, value in womenListDict.items():
                inputFile.write(str(key) + ':' + str(value) + '\n')
    # new code ends

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print('Usage <script name> <number of subjects>')
        print('For example : python CreatingPrefList.py 5')
        sys.exit()
    elif (sys.argv[1].isdigit()):
        objCreatePrefList = CreatingPrefList()
    else:
        print('Entered number of subjects value is not integer. Please enter INTEGER value.')
        sys.exit()

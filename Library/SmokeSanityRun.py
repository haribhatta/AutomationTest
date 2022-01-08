import shortcut as sc
import Library.ApplicationConfiguration as AC
print("A")
from LocalShareVariables import LSV
print("B")
import pathlib
import os
import Library.GlobalShareVariables as GSV

smokesanityresult = "SmokeSanity_ExecutionResult_"
scheduletype = input("Enter 'A' to schedule new run and 'B' to restart previous run")
appVersion = input("Please entry (name+veresion) for Test Summary Report")
#AppName = input("Please entry (Application Name) for Test Summary Report")
AppName = GSV.appName
print("app name test", AppName)
if scheduletype == 'A':
    if AppName == 'LPH':
        Originalfile = "SmokeSanityTestCases_LPH.xlsx"
    elif AppName == 'SNCH':
        Originalfile = "SmokeSanityTestCases_SNCH.xlsx"
else:
    Originalfile = smokesanityresult + appVersion + AppName + ".xlsx"
    print("Originalfile:", Originalfile)
    Originalfile = smokesanityresult + appVersion + AppName + ".xlsx"
    print("Originalfile:", Originalfile)

duplicatefile = smokesanityresult + appVersion + AppName + ".xlsx"
print("This is test", duplicatefile)
print("This is original file", Originalfile)
rows = sc.getTotalrows(Originalfile, 'test')

def files(file, file1, rows, *args):
    global runEnv
    #print("runEnv2:", runEnv)
    if not args:
        sc.copyoriginal(file, file1)
        #AC.applicationSelection()

    for r in range(2, rows + 1):
        Testcase = str(sc.readData(file1, 'test', r, 1))
        Status = sc.readData(file1, 'test', r, 2)
        runEnv = sc.readData(file1, 'test', r, 8)
        print("runEnv3:", runEnv)
        RunNoR = (sc.readData(file1, 'test', r, 4))
        if Status == 'Norun' or Status == 'UnderAnalysis':
            print("Executing Norun and UnderAnalysis test scripts.")
            base_dir = str(pathlib.PureWindowsPath(LSV.SystemTestPath))
            Pythonfilepath = os.path.join(base_dir, Testcase)
            print(Pythonfilepath)
            try:
                exec(open(Pythonfilepath).read())
                sc.writeData(file1, 'test', r, 2, 'Passed')
            except:
                sc.writeData(file1, 'test', r, 2, 'UnderAnalysis')
                sc.writeData(file1, 'test', r, 4, RunNoR + 1)

files(Originalfile, duplicatefile, rows)





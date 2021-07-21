from SystemTest import shortcut as sc
from TestActionLibrary import A
from LocalShareVariables import LSV
import pathlib
import os

def files(file,file1,rows,*args):
    if not args:
        sc.copyoriginal(file, file1)
        A.applicationSelection()
    for r in range(2, rows + 1):
        Testcase = str(sc.readData(file1, 'test', r, 1))
        Status = sc.readData(file1, 'test', r, 2)
        RunNoR = (sc.readData(file1, 'test', r, 4))
        if Status != 'Passed':
            print(" Status is Norun or Failed")
            base_dir = str(pathlib.PureWindowsPath(LSV.SystemTestPath))
            Pythonfilepath = os.path.join(base_dir, Testcase)
            print(Pythonfilepath)

            try:
                exec(open(Pythonfilepath).read())
                sc.writeData(file1, 'test', r, 2, 'Passed')
            except:
                sc.writeData(file1, 'test', r, 2, 'Failed')
                sc.writeData(file1, 'test', r, 4, RunNoR + 1)

smokesanityresult = "SmokeSanity_ExecutionResult_"
scheduletype = input("Enter 'A' to schedule new run and 'B' to restart previous run")
appVersion = input("Please entry (name+veresion) for Test Summary Report")

if scheduletype == 'A':
    Originalfile = "SmokeSanityTestCases.xlsx"

else:
    Originalfile = smokesanityresult + appVersion + ".xlsx"

duplicatefile = smokesanityresult + appVersion + ".xlsx"
print("This is test", duplicatefile)
print("This is original file", Originalfile)
rows = sc.getTotalrows(Originalfile, 'test')
files(Originalfile, duplicatefile, rows)
#files(Originalfile, duplicatefile, rows,2) #if you don't want to do test twice then you should comment this





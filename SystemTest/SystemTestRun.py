from SystemTest import shortcut as sc
import pathlib
import os

def files(file,file1,rows,*args):
    if not args:
        sc.copyoriginal(file,file1)
    for r in range(2, rows + 1):
        Testcase = str(sc.readData(file1, 'Sheet1', r, 1))
        Status = sc.readData(file1, 'Sheet1', r, 2)
        RunNoR = (sc.readData(file1, 'Sheet1', r, 4))
        if Status != 'Passed':
            base_dir = str(pathlib.PureWindowsPath(r'E:\QA\AutomationTest\SystemTest'))
            Pythonfilepath = os.path.join(base_dir, Testcase)
            print(Pythonfilepath)


            try:
                exec(open(Pythonfilepath).read())
                sc.writeData(file1, 'Sheet1', r, 2, 'Passed')
            except:
                sc.writeData(file1, 'Sheet1', r, 2, 'Failed')
                sc.writeData(file1, 'Sheet1', r, 4, RunNoR + 1)

systemtestresult = "SystemTestExecutionResult_LPH_V"
userinput = input("Please entry current version number")
scheduletype = input("Enter 'A' to schedule new run and 'B' to restart previous run")

if scheduletype == 'A':
    Originalfile = "SystemTestCases.xlsx"

else:
    Originalfile = systemtestresult + userinput + ".xlsx"

print(userinput)
duplicatefile = systemtestresult + userinput + ".xlsx"
print("This is test", duplicatefile)
print("This is original file", Originalfile)
rows = sc.getTotalrows(Originalfile, 'Sheet1')
files(Originalfile, duplicatefile, rows)
files(Originalfile, duplicatefile, rows,2) #if you don't want to do test twice then you should comment this





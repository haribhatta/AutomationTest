import shortcut as sc
import Library.ApplicationConfiguration as AC
from LocalShareVariables import LSV
import pathlib
import os
import Library.GlobalShareVariables as GSV

billingTestCases = "BillingReportsExcel/excelTestCasesTestPackBillingReports_"
billingTestCasesResult = "BillingReportsExcel/excelResultTestPackBillingReports_"
scheduletype = input("Enter '1' to schedule new run and '2' to restart previous run")
appVersion = input("Please entry version for Test Summary Report")
#AppName = input("Please entry (Application Name) for Test Summary Report")
AppName = GSV.appName
print("app name test", AppName)

if scheduletype == '1':
    Originalfile = billingTestCases + AppName + ".xlsx"

elif scheduletype == '2':
    Originalfile = billingTestCasesResult + AppName + appVersion + ".xlsx"
    print("Originalfile:", Originalfile)

duplicatefile = billingTestCasesResult + AppName + appVersion + ".xlsx"
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
        RunNoR = (sc.readData(file1, 'test', r, 4))
        if Status == 'Norun' or Status == 'UnderAnalysis':
            print("Executing Norun and UnderAnalysis test scripts.")
            base_dir = str(pathlib.PureWindowsPath(LSV.SystemTestPath))
            Pythonfilepath = os.path.join(base_dir, Testcase)
            print(Pythonfilepath)
            try:
                exec(open(Pythonfilepath).read())
                sc.writeData(file1, 'test', r, 2, 'Passed')
                sc.fillGreenColor(file1, 'test', r, 2)
            except:
                sc.writeData(file1, 'test', r, 2, 'UnderAnalysis')
                sc.fillYellowColor(file1, 'test', r, 2)
                sc.writeData(file1, 'test', r, 4, RunNoR + 1)

files(Originalfile, duplicatefile, rows)





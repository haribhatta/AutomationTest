from SystemTest import shortcut as sc
import pathlib
import os

def files(file,file1,rows,*args):
    if not args:
        sc.copyoriginal(file,file1)
    for r in range(2, rows + 1):
        Testcase = str(sc.readData(file1, 'test', r, 1))
        Status = sc.readData(file1, 'test', r, 2)
        RunNoR = (sc.readData(file1, 'test', r, 4))
        if Status != 'Passed':
            base_dir = str(pathlib.PureWindowsPath(r'D:\svn\DanpheEMR\SystemTest'))
            Pythonfilepath = os.path.join(base_dir, Testcase)
            print(Pythonfilepath)

            try:
                exec(open(Pythonfilepath).read())
                sc.writeData(file1, 'test', r, 2, 'Passed')
            except:
                sc.writeData(file1, 'test', r, 2, 'Failed')
                sc.writeData(file1, 'test', r, 4, RunNoR + 1)

Originalfile= "SmokeSanityTestCases.xlsx"
duplicatefile = "SmokeSanityExecutionResultV1.48.8.xlsx"
rows = sc.getTotalrows(Originalfile, 'test')
files(Originalfile,duplicatefile,rows)
files(Originalfile,duplicatefile,rows,2) #if you don't want to do test twice then you should comment this





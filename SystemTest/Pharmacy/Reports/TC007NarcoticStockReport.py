from TestActionLibrary import A
from GlobalShareVariables import GSV
nsr = A()

nsr.openBrowser()
nsr.login('pharmacy1', 'pass123')

# scripting blocked due to bug: EMR-2587
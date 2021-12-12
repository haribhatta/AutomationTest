'''
Objective:
To test Pharmacy> Narcotic Stock Report with below check points:
1. Get Narcotic Stock Report
2. Sell Narcotic drug
3. Verify Narcotic Stock Report
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
########

EMR = AC.openBrowser()
AC.login('pharmacy1', 'pass123')

# scripting blocked due to bug: EMR-2587
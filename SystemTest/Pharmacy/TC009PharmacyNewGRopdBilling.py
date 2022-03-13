'''
Objective:
To test below check points:
1. Create pharmacy goods receipt.
2. Verify pharmacy goods receipt.
3. Create pharmacy OPD cash invoice.
4. verify pharmacy OPD cash invoice.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB

paymentmode = "Cash"
qty = 50
EMR = GSV.appName
exec(open("TC008PharmacyNewGRStore2StockTransfer.py").read())
LD.createDispensaryOPDBilling(EMR, qty, paymentmode)
AC.logout()
AC.closeBrowser()

#-------------Objective of this script----------
# To verify Accounting-Reports-Trial Balance Report:
# Transaction amount should be on both Dr and Cr side for each Ledgers

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB
import Library.LibModuleBilling as LB
import Library.LibModuleAccounting as ACC

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

# admin  user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD

#-------------Script Owner: Hari---------------- Log-log-log (333)
#Scripted on: 29.01.2078

EMR = AC.openBrowser()
#add voucher in ledger
AC.login(admUserId, admUserPwd)
ACC.createManualVoucher(EMR)
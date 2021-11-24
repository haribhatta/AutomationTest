from Library import ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
from Library import LibModuleBilling as LB
from Library import LibModuleAppointment as LA
from Library import LibModuleBillingReports as LBR
import time

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID


AC.applicationSelection()
AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation()
time.sleep(2)
InvoiceNo = LA.patientquickentry(0, 'Cash',GSV.departmentGyno , GSV.doctorGyno).InvoiceNo
LBR.getTotalItemsBill()
LBR.preSystemTotalItemsBill()
LB.returnBillingInvoice(InvoiceNo, "This is cash return.")
LBR.getTotalItemsBill()
LBR.verifyTotalItemsBill(returnamt=opdAmt)
time.sleep(2)
AC.logout()
AC.closeBrowser()

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
opdRate = GSV.opdRate

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountpc=50, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno).InvoiceNo
LBR.verifyDiscountReport(danpheEMR=EMR, HospitalNo=HospitalNo, cash=opdRate, discountpc=50)
AC.logout()
AC.closeBrowser()

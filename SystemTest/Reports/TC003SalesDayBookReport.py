import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR

AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
rateOPD = GSV.opdRate
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
LBR.getSalesDayBook()
###
HospitalNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae)
LBR.preSystemSalesDayBook()
LBR.getSalesDayBook()
LBR.verifySalesDayBook(cash=rateOPD, cashreturn=0, credit=0, creditreturn=0)
###
LB.returnBillingInvoice(returnmsg="this is bill return 1")
LBR.preSystemSalesDayBook()
LBR.getSalesDayBook()
LBR.verifySalesDayBook(cash=0, cashreturn=rateOPD, credit=0, creditreturn=0)
###
HospitalNo1 = LA.patientquickentry(discountpc=0, paymentmode='CREDIT', department=departmentGynae, doctor=doctorGynae)
LBR.preSystemSalesDayBook()
LBR.getSalesDayBook()
LBR.verifySalesDayBook(cash=0, cashreturn=0, credit=rateOPD, creditreturn=0)
###
LB.returnBillingInvoice(returnmsg="this is bill retur 2n")
LBR.preSystemSalesDayBook()
LBR.getSalesDayBook()
LBR.verifySalesDayBook(cash=0, cashreturn=0, credit=0, creditreturn=rateOPD)
###
AC.logout()
AC.closeBrowser()

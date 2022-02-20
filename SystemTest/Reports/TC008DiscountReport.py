import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA

# front desk user login
itUserId = GSV.itUserID
itUserPwd = GSV.itUserPwD
opdRate = GSV.opdRate
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(itUserId, itUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=discountScheme, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).HospitalNo
LBR.verifyDiscountReport(danpheEMR=EMR, HospitalNo=HospitalNo, cash=opdRate, discountpc=discountScheme)
AC.logout()
AC.closeBrowser()

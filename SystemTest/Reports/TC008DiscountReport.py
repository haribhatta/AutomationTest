import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModuleSettings as LS
#############
# admin user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
#discountScheme = GSV.discountSchemeName
#############
EMR = AC.openBrowser()
AC.login(admUserId, admUserPwd)
a, b = LS.checkCoreCFGdiscountMembership(EMR)  #membershipTypeDiscountValue, membershipSchemeSettingsValue
discountValue = GSV.discountSchemeName
opdRate = GSV.opdRate
###
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=discountValue, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LBR.verifyDiscountReport(danpheEMR=EMR, HospitalNo=HospitalNo, cash=opdRate, discountpc=discountPercentage)
AC.logout()
AC.closeBrowser()

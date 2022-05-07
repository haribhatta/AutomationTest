'''
System is accepting more discount that that of subtotal
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleDispensary as LD
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
paymode = "CREDIT"
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LD.activateDispensaryCounter(EMR, dispensaryName='MainDispensary')
LD.createDispensarySaleWithDiscount(danpheEMR=EMR, HospitalNo=HospitalNo, qty=1, discountpercentage=101, drugName=GSV.drug1BrandName, paymentmode=paymode)
AC.logout()
AC.closeBrowser()
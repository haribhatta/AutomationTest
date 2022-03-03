'''
Scripted by: Alina
Objective:
To test Pharmacy> Sales Statement Report with below check points:
1. Cash Sale
2. Cash Sale Return
3. Credit Sale
4. Credit Settlement
5. Credit Sale Return

'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleBilling as LB

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
pharmacyUserName = GSV.pharmacyUserName
# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD

drugName = GSV.drug1BrandName
drugRate = GSV.drug1Rate
qty = 1
totalAmount = qty*drugRate
remark = "This is test return."
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
# To get random patient information
AC.login(userid=billingId, pwd=billingPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).HospitalNo
AC.logout()
# Start of User collection report
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName)
LPR.getsalesstatementreport(danpheEMR=EMR)
LPR.presalesstatementreport()
######## Create pharmacy cash sale
pInvoiceNo = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, drugName=drugName, qty=qty, paymentmode='Cash')
LPR.getsalesstatementreport(danpheEMR=EMR)

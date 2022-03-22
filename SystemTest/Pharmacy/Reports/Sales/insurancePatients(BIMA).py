'''
Scripted by: Puskar Khadka
Objective:
To test Pharmacy> Get previous insurance patient (BIMA) sales:
Do a Insurance Sales
verify presales == instance insurance sale - subtotal of a sales

'''

import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleInsurance as LI
import Library.LibModuleDispensary as LD
import Library.ApplicationConfiguration as AC
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LI.getInsurancePatientBimaSummaryValue(EMR)
LI.preInsurancePatientBimaSummaryValue()
AC.logout()
AC.login(GSV.adminUserID, GSV.adminUserPwD)
LB.counteractivation(EMR)
NSHI = LI.insurancePatientRegistration(EMR)
LI.insuranceNewVisit(EMR, NSHI)
print("NSHI NO of given Patient is :", NSHI)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName2)
LI.insuranceDispensarySell(EMR, NSHINO=NSHI, genericname=GSV.drug1GenericName, drugname=GSV.drug1BrandName)
LI.getInsurancePatientBimaSummaryValue(EMR)
LI.verifyinsurancePatientBimaSummaryValue(rate=8)
AC.logout()

print("Testcase Insurance Patient(Bima) report have Passed without Return case")


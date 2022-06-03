'''Scripted by: Hari P. Bhatta
Headline: Test_MMH-Pharmacy: Unable to request drug. Drop down box of drug list is not displayed.
Description:
Issue: No option to select drug to sale items from Pharmacy sale window.

Steps:

go to pharmacy sale window. (/Home/Index#/Pharmacy/Sale/New)

Select drug name in “Drug/Medicine Name” field.

Expected result: field to select drug name must be available.

Actual result: field to select drug name is not available.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD

EMR = AC.openBrowser()
#############
# pharmacy user login
phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
drugSinex = GSV.drugSinexName

paymentMode = 'Cash'
#############
AC.login(phuserid, phuserpwd)
LD.activateDispensaryCounter(danpheEMR=EMR, dispensaryName=GSV.dispensaryName1)
LD.createDispensarySaleRandomPatient(danpheEMR=EMR, qty=1, drugname=drugSinex, paymentmode=paymentMode)
AC.logout()
AC.closeBrowser()

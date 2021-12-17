########Defining Variables for LPH
appName = input("Please enter project/application name:\n"
                "SNCH\n"
                "MMH\n"
                "LPH\n"
                "MPH\n")
if appName == "LPH":
      appURL = "http://202.51.74.168:453/"
###Login Credentials:
      #admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'ashmita' #LPH user
      foUserPwD = 'pass123'
      #Lab user
      labUserID = 'karuna'
      labUserPwD = 'pass123'
      #ER Lab user
      ERlabUserID = 'erlab'
      ERlabUserPwD = 'pass123'
      #radiologist user
      radioUserID = 'radiology'
      radioUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'debika'
      pharmacyUserPwD = 'pass123'
      #nurse user
      nurseUserID = 'admin'
      nurseUserPwD = 'pass123'
      #store user
      storeUserID = 'shreeram'
      storeUserPwD = 'pass123'
###Billing Items Name:
      opdRate = 30
      deposit = 100
      CBC = "CBC"
      TFT = "TFT"
      TFTRate = 800
      LDH = "LDH"
      USG = "USG ABDOMEN/PELVIS"
      usgRate = 700
      admitRate = 30
      UrineRE = "URINE R/E"
      BTCT = "BT/CT"
      btctRate = 100
      erTest = "TC"
      LabType = "ER"
###Pharmacy/Dispensary Items Name:
      drug1BrandName = 'NIKO DROP 15ML BOTTLE'
      drug1BrandRate = 25
      drug1GenericName = 'PARACETAMOL 150MG/ML ORAL DROP 15ML BOTTLE'
      drug1Rate = 25
      drug2BrandName = "MACLAR 500MG TAB"
      drug2GenericName = "CLARITHROMYCIN"
      drug2Rate = 563.5
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3
      Testdrug = "testdrugreport"
###Inventory/Store Items Name:
      Inventory1 = "General Inventory"
      SubStoreName1 = "ADMINISTRATION"
      Dispensary1 = "MainDispensary"
      dispensaryName = "MainDispensary"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      stationaryItem1 = "DOTPEN"
###Sub Stores Name:
      SubStore1 = "General"
      SubStore2 = "PostOps"
###Doctors/Departments Name:
      doctorGyno = "Dr. doctor doctor"
      departmentGyno = "GYNAE & OBS"
      doctor2 = "Mr. admin admin"
###Users Name:
      UserBilling = 'Mr. Bhagawati Pandey'
###############################################################################
########Defining Variables for SNCH
if appName == "SNCH":
      appURL = "http://202.51.74.168:168/"
###Login Credentials:
      # admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'sabitri'
      foUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'shivraj'
      pharmacyUserPwD = 'pass123'
      #laboratory user
      labUserID = 'gayatri'
      labUserPwD = 'pass123'
      # Radiology user
      radioUserID = 'bharat'
      radioUserPwD = 'pass123'
      #Inventory user
      storeUserID = 'admin'
      storeUserPwD = 'pass123'
      #Medical Record user
      MRUserID = 'haris'
      MRUserPwD = 'pass123'
### Bill Items Name:
      opdRate = 500
      deposit = 200
      CBC = "CBC"
      TFT = "FREE TFT"   #TFT(FT3,FT4,TSH) CLLEA
      T3 = "FT3"
      T4 = "FT4"
      TSH = "TSH"
      TFTRate = 1200
      LDH = "LDH"
      UrineRE = "URINE R/E" # this gets changed on V1.49.3
      BTCT = "BT/CT"
      btctRate = 300
      USG = "USG ABDOMIN AND PELVIS"
      usgRate = 1000
      admitRate = 1500
###Pharmacy/Dispensary Items Name:
      dispensaryName = "MainDispensary"
      drug1BrandName = "SINEX TAB"
      drug1GenericName = "quinapril"
      drug1Rate = 1.15
      drug2BrandName = 'ASTHALIN 2 MG TAB'
      drug2BrandRate = 1.14
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3
      drugAasma = 'AASMA 150 XR TAB'
      Testdrug = "Testdrugreport"
###Inventory/Store Items Name:
      GeneralInventory = "General Inventory"
      Dispensary1 = "General Inventory"
      A4Paper = 'A4 PAPER'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      stationaryItem1 = "PENCIL"
      File = "FILE"
###Sub Stores Name:
      SubStoreNameAdmin = "General"
      SubStore1 = "General"
      SubStore2 = "PostOps"
###Doctors/Departments List
      doctorGyno = "Dr. Jyoti Rana"
      departmentGyno = "Gynecology"
      departmentNephro = "Nephro"
###Suppliers Name list
      supplierShremad = "Shremad Tech."
      supplierName2 = "AAKAR ENTERPRISES"
###Users Name:
      user = "admin"
###############################################################################
########Defining Variables for Medi Plus
if appName == "MPH":
      #appURL = "http://192.168.137.1:82/"
      appURL = "http://localhost:5000/"
###Login Credentials:
      #admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'bandana'
      foUserPwD = 'pass123'
      #Lab user
      labUserID = 'supriya'
      labUserPwD = 'pass123'
      #ER Lab user
      ERlabUserID = 'erlab'
      ERlabUserPwD = 'pass123'
      #radiologist user
      radioUserID = 'basudev'
      radioUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'kishor'
      pharmacyUserPwD = 'pass123'
      pharmacyUserName = 'Mr. Kishor Ranabhat'
      #nurse user
      nurseUserID = 'admin'
      nurseUserPwD = 'pass123'
      #store user
      storeUserID = 'radha'
      storeUserPwD = 'pass123'
###Billing Items Name:
      opdRate = 660
      deposit = 1000
      CBC = "COMPLETE BLOOD COUNT-CBC"
      CBCRate = 1100
      TFT = "TFT"
      T3 = "FT3"
      T4 = "FT4"
      TSH = "TSH"
      TFTRate = 500
      LDH = "LDH"
      LDHRate = 600
      USG = "USG ABDOMEN AND PELVIS"
      usgRate = 1300
      admitRate = 30
      UrineRE = "URINE R/E "
      UrineRERare = 125
      BTCT = "BT CT"
      btctRate = 200
      erTest = "TC, DC"
      LabType = "ER"
###Pharmacy/Dispensary Items Name:
      drug1BrandName = "ASTHALIN ROTACAPS "
      drug1GenericName = 'SALBUTAMOL-100MCG'
      drug1Rate = 69.18
      drug2BrandName = "MACLAR 500MG TAB"
      drug2GenericName = "CLARITHROMYCIN"
      drug2Rate = 563.5
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      Testdrug = "testdrugreport"
      drugSinexName = 'SINEX'
      drugSinexRate = 3
###Inventory/Store Items Name:
      GeneralInventory = "General Inventory"
      SubStoreNameAdmin = "Administration Sub Store"
      Dispensary1 = "MainDispensary"
      dispensaryName = "Main Dispensary"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      #stationaryItem1 = "DOTPEN"
      stationaryItem1 = "Pen Holder"
###Sub Stores Name:
      SubStore1 = "General"
      SubStore2 = "PostOps"
###Doctors/Departments Name:
      doctorGyno = "Dr. Anjali Subedi"
      departmentGyno = "OBG Gynae"
      doctor2 = "Dr. Junu Shrestha"
###Wards Name:
      generalWard = "General Non-Covid Ward"
      bedFeature = "General Non-Covid Ward"
###Users Name:
      UserBilling = 'Mr. Bhagawati Pandey'
###############################################################################

   #def __str__():
    #  return
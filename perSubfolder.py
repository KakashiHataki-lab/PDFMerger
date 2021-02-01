# Merge PDF's in multiple subfolders

#list all files
import os
import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

# Call the PdfFileMerger
mergedObject = PdfFileMerger()

rootdir = 'C:\\Users\\leona\\OneDrive - PRODESP\\Prottt(SPSP)\\'

# Loop through all of subfolders and then pdf's and append their pages
for sub in os.listdir(rootdir):
    path = rootdir+sub+"\\"
    mergedObject = PdfFileMerger()
    for filepath in glob.iglob(path+"*.pdf"):
       print(filepath)
       mergedObject.append(PdfFileReader(filepath, 'rb'))
    mergedObject.write(path+"TodosPDFs.pdf")
    mergedObject.close()
    print("PDF Created")
    
    

# Write all the files into a file which is named as shown below


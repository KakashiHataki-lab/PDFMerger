import os
import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

# Call the PdfFileMerger
mergedObject = PdfFileMerger()

# Loop through all of them and append their pages
path = "C:\\Users\\leona\\OneDrive - PRODESP\\Prottt(SPSP)\\536753\\"
for filepath in glob.iglob(path+"*.pdf"):
    print(filepath)
    mergedObject.append(PdfFileReader(filepath, 'rb'))
 
# Write all the files into a file which is named as shown below
mergedObject.write(path+"mergedfilesoutput.pdf")

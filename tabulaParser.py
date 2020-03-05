import tabula
import os
import pandas as pd 
import numpy as np 
currentDir = os.getcwd()
pdfList = []
for file in os.listdir(currentDir):
    if file.endswith(".pdf"):
        pdfList.append(os.path.join(currentDir, file))
for path in pdfList:
    test = tabula.io.read_pdf(path,pages='1')
    pdtest[0][0]

    
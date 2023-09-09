import jpype
jpype.startJVM()

import asposecells
from asposecells.api import Workbook, LoadOptions, SaveFormat


#Create a CSV LoadOptions object:
    loadoptions = LoadOptions.(FileFormatType.CSV)

#Create a Workbook object with CSV selected file and loadoptions:
    workbook = Workbook.("example.csv", loadoptions)

#Save CSV File like as Excel File:
    workbook.save("Excel_file.xlsx", SaveFormat.XLSX)

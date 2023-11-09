# © Nicolas Huber, 2023.
# 11/01/2023

import csv
import os

def checkCSV(path,delimiter,interface):

    status = "success"
    message = "CSV-Datei wurde erfolgreich validiert."
    
    try:
        if not os.path.isfile(path) or not path.endswith(".csv"):
            status = "error"
            message = "CSV-Datei konnte nicht gefunden werden"
        else:
            csv_header = []
            try:
                with open(path, newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=delimiter)
                    csv_header = next(reader)
                    
                    if csv_header != interface:
                        status = "error"
                        message = "CSV-Header deckt sich nicht mit dem Interface (" + str(csv_header) + ")"
                        
            except Exception as e:
                status = "error"
                message = "CSV-Datei konnte nicht gelesen werden (" + str(e) + ")"
    except Exception as e:
        status = "error"
        message = "CSV-Datei konnte nicht gefunden werden (" + str(e) + ")"
        
    return {
        "status": status,
        "message": message
    }
    
def checkPath(path):
    status = "success"
    message = "Ausgabeordner wurde erfolgreich validiert"
    
    if not os.path.isdir(path):
        status = "error"
        message = "Ausgabeordner konnte nicht gefunden werden"
    
    return {
        "status": status,
        "message": message
    }
    
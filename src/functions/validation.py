# © Nicolas Huber, 2023.
# 11/01/2023

def checkCSV(path,delimiter,interface):
    
    import csv
    from pathlib import Path
    
    status = "success"
    message = "CSV-Datei wurde erfolgreich validiert."
    
    try:
        if Path(path).is_file() == False or Path(path).suffix != ".csv":
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
    
    from pathlib import Path
    
    status = "success"
    message = "Ausgabeordner wurde erfolgreich validiert"
    
    if Path(path).is_dir() == False:
        status = "error"
        message = "Ausgabeordner konnte nicht gefunden werden"
    
    return {
        "status": status,
        "message": message
    }
    
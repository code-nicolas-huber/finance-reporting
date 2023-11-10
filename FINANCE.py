# %%

# © Nicolas Huber, 2023.
# 11/10/2023

# ---- HEADER ----

import os
from termcolor import colored
from src.constants.CONSTANTS import *
from src.functions.validation import *
from src.classes.GenerateReport import *

# ---- GLOBALS ----

timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
timestampFilename = datetime.now().strftime("%d%m%Y%H%M%S")

# ---- WELCOME ----

print()
print("------------------------------------------------------------------------")
print("------ < Willkommen im Reporting-Tool von finance.nicolas-huber > ------")
print("------------------------------------------------------------------------")
print()
print("Dieses Tool ergänzt die Funktionalität von finance.nicolas-huber.ch. ")
print()
print("Du erreichst den Autor dieses Tools mit den folgenden Angaben:")
print(" --> Autor: " + colored(AUTHOR, 'blue'))
print(" --> E-Mail: " + colored(AUTHOR_EMAIL, 'blue'))
print(" --> Website: " + colored(AUTHOR_WEBSITE, 'blue'))
print()
print("Wenn du dieses weiterentwickeln möchtest, findest du den Code hier:")
print(" --> Code: " + colored(CODEBASE, 'blue'))
print()
print("Du nutzt die folgende Version dieses Tools:")
print(" --> Version: " + colored(VERSION + " | " + DATE, 'blue'))

# ---- FORMAL ----

print()
print("------------------------------------------------------------------------")
print("------ < FORMAL > ------------------------------------------------------")
print("------------------------------------------------------------------------")
print()
print("Dieses Tool erwarted eine CSV-Datei mit folgendem Interface:")
print(" --> " + colored('ID;User;Konto;Kategorie;Datum;Buchungstext;Transaktionsnummer;Betrag;Währung;Status', 'blue'))
print(" --> Wenn du deine CSV-Datei im Tool finance.nicolas-huber.ch erstellst, wird das Interface automatisch berücksichtigt.")
print()
print("Ausführungszeitpunkt:")
print(" --> Zeitstempfel: " + colored(timestamp, 'blue'))
print(" --> Output-Ordner: " + colored(timestampFilename, 'blue'))

# ---- SETUP ----

print()
print("------------------------------------------------------------------------")
print("------ < Wähle einige Einstellungen für die Auswertung aus > -----------")
print("------------------------------------------------------------------------")
print()

# validate CSV file

csvPath = input("Gib den Pfad zur CSV-Datei ein: \n --> ")
validateCSV = checkCSV(csvPath, CSV_DELIMITER, CSV_INTERFACE)
if validateCSV['status'] == "error":
    print(" --> der Pfad zur CSV-Datei lautet: " + colored(csvPath, 'red'))
    print(f" --> das Programm wird beendet, weil ein Fehler aufgetreten ist: " + colored(validateCSV['message'], 'red'))
    print()
    print("------------------------------------------------------------------------")
    print("------ < ZUSAMMENFASSUNG > ---------------------------------------------")
    print("------------------------------------------------------------------------")
    print("")
    print("Das Programm wurde mit den folgenden Parametern beendet:")
    print(" --> Pfad zur CSV-Datei: " + colored(csvPath, 'red'))
    print()
    exit()
else:
    print(" --> der Pfad wurde erfolgreich validiert")
    print(" --> der Pfad zur CSV-Datei lautet: " + colored(csvPath, 'green'))
    print()

# validate output directory

outputPath = input("Gib den Pfad zum Ausgabeordner ein: \n --> ")
outputPath = os.path.join(outputPath,'')
validatePath = checkPath(outputPath)
if (validatePath['status'] == "error"):
    print(" --> der Pfad zum Ausgabeordner lautet: " + colored(outputPath, 'red'))
    print(f" --> das Programm wird beendet, weil ein Fehler aufgetreten ist: " + colored(validatePath['message'], 'red'))
    print()
    print("------------------------------------------------------------------------")
    print("------ < ZUSAMMENFASSUNG > ---------------------------------------------")
    print("------------------------------------------------------------------------")
    print("")
    print("Das Programm wurde mit den folgenden Parametern beendet:")
    print(" --> Pfad zur CSV-Datei: " + colored(csvPath, 'green'))
    print(" --> Pfad zum Ausgabeordner: " + colored(outputPath, 'red'))
    print()
    exit()
else:
    print(" --> der Pfad zum Ausgabeordner lautet: " + colored(outputPath, 'green'))
    print()
    
# request output formats    

outputHTML = input("Möchtest du deine Auswertung im HTML-Format? (y/n) \n --> ")
if outputHTML == "y":
    outputHTML = True
    print(" --> die Auswertung wird als HTML-Datei erstellt: " + colored("y", 'green'))
    print()
else:
    outputHTML = False
    print(" --> es wird keine HTML-Auswertung erstellt: " + colored("n", 'red'))
    print()
    
if outputHTML == True:
    outputPDF = input("Möchtest du deine Auswertung im PDF-Format? (y/n) \n --> ")
else: 
    outputPDF = "n"
if outputPDF == "y":
    outputPDF = True
    print(" --> die Auswertung wird als PDF-Datei erstellt: " + colored("y", 'green'))
    print()
else:
    outputPDF = False
    print(" --> es wird keine PDF-Auswertung erstellt: " + colored("n", 'red'))
    print()

# verify execution

verifyExecution = input("Sollen die Auswertung und der Report erstellt werden? (y/n) \n --> ")
if verifyExecution == "y":
    print(" --> die Auswertung und der Report werden erstellt: " + colored("y", 'green'))
else:
    print(" --> die Auswertung und der Report werden erstellt: " + colored("n", 'red'))
    print(" --> das Programm wird beendet.")
    print()
    print("------------------------------------------------------------------------")
    print("------ < ZUSAMMENFASSUNG > ---------------------------------------------")
    print("------------------------------------------------------------------------")
    print("")
    print("Das Programm wurde mit den folgenden Parametern beendet:")
    print(" --> Pfad zur CSV-Datei: " + colored(csvPath, 'green'))
    print(" --> Pfad zum Ausgabeordner: " + colored(outputPath, 'green'))
    print(" --> Auswertung als HTML-Datei: " + colored(outputHTML, 'green'))
    print(" --> Auswertung als PDF-Datei: " + colored(outputPDF, 'green'))
    print(" --> Auswertung und Report erstellen: " + colored(verifyExecution, 'red'))
    exit()
    
# ---- REPORT ----

print()
print("------------------------------------------------------------------------")
print("------ < Hier wird dein Report erstellt > ------------------------------")
print("------------------------------------------------------------------------")
print()
print("Nun wird dein Report erstellt. Bitte warte einen Moment.")
print()

Generator = GenerateReport(timestampFilename, csvPath, outputPath, outputHTML, outputPDF)

print("Das Programm erstellt einen Bericht für die folgenden Konten:")
categoriesDict = Generator.prepareData()
generalDict = []
for key in categoriesDict:
    print(" --> " + colored(key, 'green'))
    generalDict.append(categoriesDict[key])
print()

# reporting for each category

for key in categoriesDict:
        
    print("Das Programm erstellt einen Bericht für das Konto " + colored(key, 'green'))
    
    # generate base report

    markdownReport = Generator.generateMarkdownReport(categoriesDict[key], key)
    if markdownReport:
        print(" --> der Basis-Report wurde erfolgreich erstellt und  befindet sich im Ausgabeordner: " + colored(f"{outputPath}{timestampFilename}/markdown/{key}", 'green'))
    else:
        print(" --> der Report konnte nicht erstellt werden")
        print(" --> das Programm wird beendet.")
        print()
        print("------------------------------------------------------------------------")
        print("------ < ZUSAMMENFASSUNG > ---------------------------------------------")
        print("------------------------------------------------------------------------")
        print("")
        print("Das Programm wurde mit den folgenden Parametern beendet:")
        print(" --> Pfad zur CSV-Datei: " + colored(csvPath, 'green'))
        print(" --> Pfad zum Ausgabeordner: " + colored(outputPath, 'green'))
        print(" --> Auswertung als HTML-Datei: " + colored(outputHTML, 'green'))
        print(" --> Auswertung als PDF-Datei: " + colored(outputPDF, 'green'))
        print(" --> Auswertung und Report erstellen: " + colored(verifyExecution, 'green'))
        exit()

    # generate HTML report

    if outputHTML:
        htmlReport = Generator.generateHTMLReport(key)
        if htmlReport:
            print(" --> der HTML-Report wurde erfolgreich erstellt und  befindet sich im Ausgabeordner: " + colored(f"{outputPath}{timestampFilename}/html{key}", 'green'))
        else:
            print(" --> der HTML-Report konnte nicht erstellt werden")
            print(" --> das Programm wird beendet.")
            print()
            print("------------------------------------------------------------------------")
            print("------ < ZUSAMMENFASSUNG > ---------------------------------------------")
            print("------------------------------------------------------------------------")
            print("")
            print("Das Programm wurde mit den folgenden Parametern beendet:")
            print(" --> Pfad zur CSV-Datei: " + colored(csvPath, 'green'))
            print(" --> Pfad zum Ausgabeordner: " + colored(outputPath, 'green'))
            print(" --> Auswertung als HTML-Datei: " + colored(outputHTML, 'green'))
            print(" --> Auswertung als PDF-Datei: " + colored(outputPDF, 'green'))
            print(" --> Auswertung und Report erstellen: " + colored(verifyExecution, 'green'))
            exit()

    # generate PDF report

    if outputPDF:
        pdfReport = Generator.generatePDFReport(key)
        if pdfReport:
            print(" --> der PDF-Report wurde erfolgreich erstellt und  befindet sich im Ausgabeordner: " + colored(f"{outputPath}{timestampFilename}/pdf/{key}", 'green'))
        else:
            print(" --> der PDF-Report konnte nicht erstellt werden")
            print(" --> das Programm wird beendet.")
            print()
            print("------------------------------------------------------------------------")
            print("------ < ZUSAMMENFASSUNG > ---------------------------------------------")
            print("------------------------------------------------------------------------")
            print("")
            print("Das Programm wurde mit den folgenden Parametern beendet:")
            print(" --> Pfad zur CSV-Datei: " + colored(csvPath, 'green'))
            print(" --> Pfad zum Ausgabeordner: " + colored(outputPath, 'green'))
            print(" --> Auswertung als HTML-Datei: " + colored(outputHTML, 'green'))
            print(" --> Auswertung als PDF-Datei: " + colored(outputPDF, 'green'))
            print(" --> Auswertung und Report erstellen: " + colored(verifyExecution, 'green'))
            exit()
            
    print()

# ---- SUMMARY ----

print("------------------------------------------------------------------------")
print("------ < ZUSAMMENFASSUNG > ---------------------------------------------")
print("------------------------------------------------------------------------")
print("")

print("Das Programm wurde mit den folgenden Parametern beendet:")
print(" --> Pfad zur CSV-Datei: " + colored(csvPath, 'green'))
print(" --> Pfad zum Ausgabeordner: " + colored(outputPath, 'green'))
print(" --> Auswertung als HTML-Datei: " + colored(outputHTML, 'green'))
print(" --> Auswertung als PDF-Datei: " + colored(outputPDF, 'green'))
print(" --> Auswertung und Report erstellen: " + colored(verifyExecution, 'green'))
print()
print("Du kannst den Report im Ausgabeordner finden: " + colored(f"{outputPath}{timestampFilename}", 'green'))
print()
print("------------------------------------------------------------------------")
print()
print("Vielen Dank für die Nutzung des Reporting-Tools von finance.nicolas-huber.ch.")
print("© Nicolas Huber, 2023.")
print()
print("------------------------------------------------------------------------")
print()
# %%

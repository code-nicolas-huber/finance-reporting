# © Nicolas Huber, 2023.
# 11/10/2023

import os
import csv
import markdown2
from weasyprint import HTML
from datetime import datetime
from src.functions.graphs import *
from collections import defaultdict
from src.constants.CONSTANTS import *

class GenerateReport:
    
    def __init__(self, timestamp, csvPath, outputPath, outputHTML, outputPDF):
        self.timestamp = timestamp
        self.csvPath = csvPath
        self.outputPath = outputPath
        self.outputHTML = outputHTML
        self.outputPDF = outputPDF
        
    def prepareData(self):
        categoriesDict = defaultdict(list)

        with open(self.csvPath, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=CSV_DELIMITER)

            for row in reader:
                categoriesDict[row['Konto']].append(row)

        return categoriesDict
    
    def generateMarkdownReport(self, data_list, key):
        total_income = 0
        total_expense = 0
        transaction_count = 0
        transactions = []

        outputPathSimple = self.outputPath + self.timestamp

        if not os.path.exists(outputPathSimple):
            os.mkdir(outputPathSimple)
            
        outputPathNested = outputPathSimple + "/" + key
        
        if not os.path.exists(outputPathNested):
            os.mkdir(outputPathNested)
            
        outputPath = outputPathNested
        reportName = self.timestamp + "_finance_financial-report_" + key

        for row in data_list:
            category = row['Kategorie']
            number = row['Transaktionsnummer']
            text = row['Buchungstext']
            amount = float(row['Betrag'].replace(',', '').replace(' ', '').replace('CHF', ''))
            date = datetime.strptime(row['Datum'], '%d.%m.%Y')
            transactions.append((date, category, number, text, amount))
                        
            if amount >= 0:
                total_income += amount
            else:
                total_expense += amount

            transaction_count += 1
            
        report_filename = f"{outputPath}/" + reportName + ".md"
        with open(report_filename, 'w') as report_file:
            report_file.write("# Financial Report\n")
            report_file.write("Dieser Report bezieht sich auf das Konto **" + key + "**. <br><br> \n")
            report_file.write("\n## Übersicht <br>\n")
            report_file.write(f"Gesamteinkommen: {total_income:.2f} <br>\n")
            report_file.write(f"Gesamtausgaben: {total_expense:.2f} <br>\n")
            report_file.write(f"Netto-Einkommen (Profit): {(total_expense + total_income):.2f} <br>\n")
            report_file.write(f"Anzahl Transaktionen: {transaction_count} <br>\n")
            
            barChart(total_income,total_expense,outputPath,reportName,'income-expenses')            
            horizontalBarChartPositive(outputPath,reportName,'income', data_list)
            horizontalBarChartNegative(outputPath,reportName,'payments', data_list)
            
            report_file.write("\n## Charts <br>\n")
            report_file.write(f"![Einnahmen vs. Ausgaben ({reportName}_income-expenses.png)]({outputPath}/{reportName}_income-expenses.png)\n")
            report_file.write(f"![Einnahmen nach Kategorie ({reportName}_income.png)]({outputPath}/{reportName}_income.png)\n")
            report_file.write(f"![Ausgaben nach Kategorie ({reportName}_payments.png)]({outputPath}/{reportName}_payments.png)\n")

            report_file.write("\n## Details\n")
            report_file.write("\n### Einnahmen:\n")

            income_categories = {}
            expense_categories = {}
            for date, category, number, text, amount in transactions:
                if 'ingoing' in category:
                    if category in income_categories:
                        income_categories[category] += amount
                    else:
                        income_categories[category] = amount
                else:
                    if category in expense_categories:
                        expense_categories[category] += amount
                    else:
                        expense_categories[category] = amount

            for category, amount in income_categories.items():
                report_file.write(f"- {category}: {amount:.2f} \n")

            report_file.write("\n### Ausgaben:\n")

            for category, amount in expense_categories.items():
                report_file.write(f"- {category}: {amount:.2f} \n")

            report_file.write("\n## Transaktionen:\n")
            report_file.write("| Datum | Kategorie | Nummer | Buchungstext | Betrag |\n")
            report_file.write("| ----- | --------- | ------ | ------------ | ------ |\n")
            for date, category, number, text, amount in transactions:
                formatted_date = date.strftime('%d.%m.%Y')
                report_file.write(f"| {formatted_date} | {category} | {number} | {text.replace("|",'/')} | {amount:.2f} |\n")

        return True
    
    def generateHTMLReport(self, key):
        
        reportName = self.timestamp + "_finance_financial-report_" + key
        
        with open(self.outputPath + self.timestamp + "/" + key + "/" + reportName + ".md", 'r') as f:
            html = markdown2.markdown(f.read(), extras=['tables'])
        
        css = """
        <style>
        body {
            font-family: Arial, sans-serif;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #1f77b4;
            color: white;
        }
        </style>
        """
        html = css + html
        
        with open(self.outputPath + self.timestamp + "/" + key + "/" + reportName + ".html", 'w') as f:
            f.write(html)
            
        return True
    
    def generatePDFReport(self, key):
        
        reportName = self.timestamp + "_finance_financial-report_" + key
        
        with open(self.outputPath + self.timestamp + "/" + key + "/" + reportName + ".html", 'r') as f:
            html = f.read()
        
        html = HTML(string=html)
        html.write_pdf(self.outputPath + self.timestamp + "/" + key + "/" + reportName + ".pdf")

        return True

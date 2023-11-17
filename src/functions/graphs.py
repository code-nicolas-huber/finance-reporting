# © Nicolas Huber, 2023.
# 11/10/2023

import pandas as pd
import matplotlib.pyplot as plt

def barChart(total_income, total_expense, outputPath, reportName, filename):
    
    plt.figure()
    
    fig, ax = plt.subplots()
    categories = ['Einnahmen', 'Ausgaben']
    amounts = [total_income, total_expense]
    ax.bar(categories, amounts)
    ax.set_ylabel('Betrag')
    ax.set_title('Einnahmen vs. Ausgaben')
    
    plt.tight_layout()
    plt.savefig(f"{outputPath}/{reportName}_{filename}.png")
    plt.close(fig)
    
def horizontalBarChartPositive(outputPath, reportName, filename, data):
    
    plt.figure()
    
    df = pd.DataFrame(data, columns=['Kategorie', 'Betrag'])        
    df['Betrag'] = df['Betrag'].str.replace(',', '')
    df = df.astype({"Betrag": float})    
    df = df[df['Betrag'] >= 0]
    df = df.sort_values(by='Betrag', ascending=True)

    amounts = df.groupby('Kategorie')['Betrag'].sum().reset_index()
    
    x_labels = amounts['Kategorie']
    y_values = amounts['Betrag']
    
    bars = plt.barh(range(len(x_labels)), y_values)
    
    plt.xlabel('Summe')
    plt.ylabel('Kategorie')
    plt.title('Einnahmen nach Kategorie')
    
    plt.yticks(range(len(x_labels)), x_labels)
    
    for bar, value in zip(bars, y_values):
        plt.text(bar.get_width() / 2, bar.get_y() + bar.get_height() / 2, f'{value:.2f}', ha='center', va='center')
        
    plt.tight_layout()
    plt.savefig(f"{outputPath}/{reportName}_{filename}.png")
    
def horizontalBarChartNegative(outputPath, reportName, filename, data):
    
    plt.figure()
    
    df = pd.DataFrame(data, columns=['Kategorie', 'Betrag'])        
    df['Betrag'] = df['Betrag'].str.replace(',', '')
    df = df.astype({"Betrag": float})    
    df = df[df['Betrag'] < 0]
    df = df.sort_values(by='Betrag', ascending=True)

    amounts = df.groupby('Kategorie')['Betrag'].sum().reset_index()
    
    x_labels = amounts['Kategorie']
    y_values = amounts['Betrag']
    
    bars = plt.barh(range(len(x_labels)), y_values)
    
    plt.xlabel('Summe')
    plt.ylabel('Kategorie')
    plt.title('Ausgaben nach Kategorie')
    
    plt.yticks(range(len(x_labels)), x_labels)
    
    for bar, value in zip(bars, y_values):
        plt.text(bar.get_width() / 2, bar.get_y() + bar.get_height() / 2, f'{value:.2f}', ha='center', va='center')
        
    plt.tight_layout()
    plt.savefig(f"{outputPath}/{reportName}_{filename}.png")
import csv
from datetime import datetime

def save_diagnosis(diagnosis, name, id_number):
    with open('diagnosticos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([date, name, id_number, diagnosis])

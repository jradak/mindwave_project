#https://store.neurosky.com/products/pc-developer-tools -> install ->ThinkGear Connector
#https://pypi.org/project/PyNeuro/
#py -m pip install PyNeuro -> terminal
#python 3.7.9

from PyNeuro.PyNeuro import PyNeuro
from time import sleep
import csv

pn = PyNeuro()

def stop():
    pn.disconnect()
    pn.close()

def start():
    pn.connect()
    pn.start()

    fieldnames = ["attention", "meditation", "delta", "theta", "lowalpha", "highalpha", "lowbeta", "highbeta", "lowgamma", "highgamma", "status" ]
    with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    while True:
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "attention": pn.attention,
                "meditation": pn.meditation,
                "delta": pn.delta, 
                "theta": pn.theta, 
                "lowalpha": pn.lowAlpha, 
                "highalpha": pn.highAlpha, 
                "lowbeta": pn.lowBeta, 
                "highbeta": pn.highBeta, 
                "lowgamma": pn.lowGamma, 
                "highgamma": pn.highGamma,
                "status":pn.status
            }
            csv_writer.writerow(info)
        sleep(1)

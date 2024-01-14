# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:22:35 2024

@author: schla
"""

# dsl1.py

import sys
import importlib

if len(sys.argv) != 2:
    sys.exit(1)
    
sys.path.insert(0, 'C:/Users/schla/Desktop/Studium/Master/Module')

file = open(sys.argv[1], 'w')
print ('Eingabe 1: ', end = '')
Eingabe1 = input()
print ('Eingabe 2: ', end = '')
Eingabe2 = input()
file.write ('module1 add' + ' ' + Eingabe1 + ' ' + Eingabe2)

with open(sys.argv[1], 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()
        
    mod = importlib.import_module(parts[0])   

if parts[2].isdigit() and parts[3].isdigit():
    print ('') 
    print ('Wenn es eine Addition zweier int-Zahlen sein soll:')
    print ('Die Attribute werden als int abgerufen und verarbeitet:')
    print ('') 
    print ('Eingabe 1: ', parts[2])
    print ('Eingabe 2: ', parts[3])
    print ('')
    print ('Die Attributübergabe: ')
    print ('')
    print ('getattr(mod, parts[1])(int(parts[2]), int(parts[3]))')
    print ('')
    print ('Die Rechnung: ') 
    print (parts[2], ' + ', parts[3], ' =  ', end = "") 
    getattr(mod, parts[1])(int(parts[2]), int(parts[3]))
    print ('')
else:
   print ('') 
   print ('Wenn es eine Zeichenkette sein soll:')
   print ('Die Attribute werden als str abgerufen und verarbeitet:')
   print ('') 
   print ('Eingabe 1: ', parts[2])
   print ('Eingabe 2: ', parts[3])
   print ('')
   print ('Die Attributübergabe: ')
   print ('')
   print ('getattr(mod, parts[1])((parts[2]), (parts[3]))')
   print ('')
   print ('Die Ausgabe: ') 
   print (parts[2], parts[3], end = "") 
   print ('')
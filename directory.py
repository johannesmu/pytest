import os
import csv

dir = os.getcwd()
print( 'we are working in ' + dir )
filename = input('type name of file:')
print( 'name of the file is ' + filename )

with open( filename ) as csv_filename:
    cs = csv.reader( csv_filename , delimiter=',')
    for row in cs
        print( row[0] )


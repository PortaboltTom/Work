import os
import shutil

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        for name in files:
            yield os.path.join(root, name)

source_dir = 'C:\\Users\\User\\Portabolt\\Portabolt - Documents'
destination_dir = 'C:\\Users\\User\\Documents\\Facturenfolder'

for file in list_files(source_dir):
    if file.endswith('.pdf'):
        shutil.copy(file, destination_dir)
import os
#gebruik dit script om een export te maken van de mappen struktuur
#dit gebruiken om te uploaden naar chatgpt voor advies over strukturering

def list_directories(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

# Gebruik je hoofdmap als startpath
start_directory = r'C:\GIT'  # Pas dit aan naar je gewenste map
list_directories(start_directory)

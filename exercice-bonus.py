# -*- coding: utf-8 -*- 

## Exercie bonus

# Import module
import urllib.request
import zipfile
import os

# Verifier que le répertoire 'départements' existe sinon le créer
if (os.path.exists(r"C:\FORMATION\20210201\departements") == False) :
    os.mkdir(r"C:\FORMATION\20210201\departements")

# Boucler sur les départements
for x in range(1,96):
    
    # Initialisation de la variable dpt
    dpt = ""
    
    # Ajouter le 0 devant le numéro pour les départements 01 à 09
    if x < 10 :
        dpt = "0"+str(x)
    else :
        dpt = str(x)
        
    print("*** Traitement du departement " + dpt + "***")
    
    # Répertoire de destination
    rep_dest = "C:\\FORMATION\\20210201\\departements\\" + dpt
    
    # Verifier que le répertoire associé au département en cours de traitement existe sinon le créer
    if (os.path.exists(rep_dest) == False):
        os.mkdir(rep_dest)
    
    # URL de téléchargement pour le departement en cours de traitement
    url = r"https://cadastre.data.gouv.fr/data/etalab-cadastre/2020-10-01/shp/departements/" + dpt + "/cadastre-" + dpt + "-communes-shp.zip"
    # Destination de l'archive
    dest = rep_dest + "\\cadastre-" + dpt + "-communes-shp.zip"

    # Téléchargement de l'archive
    download = False
    try :
        urllib.request.urlretrieve(url,dest)
        download = True
        print("Téléchargement réussi")
    except :
        print("Téléchargement échoué")

    # Décompresser l'archive
    if (download == True) :
        fzip = zipfile.ZipFile(dest, 'r')
        fzip.extractall(rep_dest)
        fzip.close()
        print("Archive décompressée")
        # Supprimer le .zip
        os.unlink(rep_dest + "\\cadastre-" + dpt + "-communes-shp.zip")
        
print("***********************")
print("TRAITEMENT TERMINÉ")
print("***********************")
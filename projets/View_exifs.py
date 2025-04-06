from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import csv

# Dossier à scanner (ex: "/home/julien/Images")
dossier_images = "/home/artiste/Desktop/test"

# Vérifie si le dossier existe
if not os.path.exists(dossier_images):
    print(f"[!] Le dossier n'existe pas : {dossier_images}")
    exit()

# Vérifie si le dossier contient des fichiers JPG
fichiers = [f for f in os.listdir(dossier_images) if f.lower().endswith((".jpg", ".jpeg"))]
if not fichiers:
    print(f"[!] Aucun fichier JPG trouvé dans : {dossier_images}")
    exit()

# Création du fichier CSV
csv_path = os.path.join(dossier_images, "exif_resultat.csv")
with open(csv_path, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nom du fichier", "Date", "Modèle", "Marque", "Latitude", "Longitude"])

    # Convertir les coordonnées GPS en format décimal
    def convertir_coordonnees(coord, ref):
        deg, min, sec = coord
        valeur = deg[0] / deg[1] + (min[0] / min[1]) / 60 + (sec[0] / sec[1]) / 3600
        if ref in ['S', 'W']:
            valeur = -valeur
        return valeur

    # Fonction pour extraire et écrire les EXIF minimales
    def lire_exif(image_path):
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()
            date, model, make = "", "", ""
            lat, lon = "", ""
            if exif_data:
                gps_info = {}
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag == "DateTimeOriginal":
                        date = value
                    elif tag == "Model":
                        model = value
                    elif tag == "Make":
                        make = value
                    elif tag == "GPSInfo":
                        for t in value:
                            sub_tag = GPSTAGS.get(t, t)
                            gps_info[sub_tag] = value[t]

                if "GPSLatitude" in gps_info and "GPSLatitudeRef" in gps_info:
                    lat = convertir_coordonnees(gps_info["GPSLatitude"], gps_info["GPSLatitudeRef"])
                if "GPSLongitude" in gps_info and "GPSLongitudeRef" in gps_info:
                    lon = convertir_coordonnees(gps_info["GPSLongitude"], gps_info["GPSLongitudeRef"])

                print(f"[+] {os.path.basename(image_path)} : {date}, {model}, {make}, {lat}, {lon}")
            else:
                print(f"[-] {os.path.basename(image_path)} : Aucun EXIF")
            writer.writerow([os.path.basename(image_path), date, model, make, lat, lon])
        except Exception as e:
            print(f"[!] Erreur avec {image_path} : {e}")

    # Parcours des fichiers du dossier
    for fichier in fichiers:
        lire_exif(os.path.join(dossier_images, fichier))

print(f"\n[✔] Résultats enregistrés dans : {csv_path}")

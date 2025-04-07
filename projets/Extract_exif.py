from PIL import Image
import os

# Dossier contenant les images à nettoyer
dossier_images = ":/home/artiste/Téléchargements"

# Fonction pour supprimer les EXIF d'une image
def supprimer_exif(image_path):
    try:
        image = Image.open(image_path)
        data = list(image.getdata())
        clean_image = Image.new(image.mode, image.size)
        clean_image.putdata(data)

        clean_path = os.path.splitext(image_path)[0] + "_clean.jpg"
        clean_image.save(clean_path)
        print(f"[✔] EXIF supprimés : {os.path.basename(clean_path)}")
    except Exception as e:
        print(f"[!] Erreur avec {image_path} : {e}")

# Parcours des fichiers dans le dossier
for fichier in os.listdir(dossier_images):
    if fichier.lower().endswith((".jpg", ".jpeg")):
        image_path = os.path.join(dossier_images, fichier)
        supprimer_exif(image_path)

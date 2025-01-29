import subprocess
import os

# Setze die Pfade zu Meshroom, Blender und den Ordnern
meshroom_path = r"C:\Users\Melon\OneDrive\Dokumente\Meshroom-2023.3.0-win64\Meshroom-2023.3.0\Meshroom.exe"  # Passe den Pfad an
blender_path = r"C:\Users\Melon\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Blender\Blender 4.3.lnk"  # Passe den Pfad an
input_images = r"C:\Users\Melon\OneDrive\Bilder\3D-Modell-Input"
output_folder = r"C:\Users\Melon\OneDrive\Bilder\3D-Modell-Output"
obj_file = os.path.join(output_folder, "texturedMesh.obj")
gltf_file = os.path.join(output_folder, "model.gltf")

# Meshroom ausführen
command_meshroom = [
    meshroom_path,
    "--input", input_images,
    "--output", output_folder
]

print("Starte Meshroom...")
subprocess.run(command_meshroom)
print("Meshroom abgeschlossen.")

# Prüfen, ob die .obj-Datei existiert
if os.path.exists(obj_file):
    print(f"{obj_file} erfolgreich generiert.")
    
    # Blender-Skript für den Import und Export
    blender_script = f"""
import bpy

# Lösche alle vorhandenen Objekte
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importiere das .obj-Modell
bpy.ops.import_scene.obj(filepath="{obj_file}")

# Exportiere als glTF (.gltf)
bpy.ops.export_scene.gltf(filepath="{gltf_file}", export_format='GLTF_SEPARATE')

print("Export in Blender abgeschlossen: " + "{gltf_file}")
"""

    # Blender mit dem Skript starten
    command_blender = [blender_path, "--background", "--python", "-c", blender_script]

    print("Starte Blender...")
    subprocess.run(command_blender)
    print("Blender abgeschlossen. Modell als .gltf exportiert.")

else:
    print("Fehler: Die .obj-Datei wurde nicht gefunden.")

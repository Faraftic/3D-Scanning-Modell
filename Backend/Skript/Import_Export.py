import subprocess
import os
import sys

# Blender-Executable (ggf. anpassen)
blender_exe = r"C:/Program Files/Blender Foundation/Blender 4.3/blender.exe"

# Pfade zur OBJ-Datei und zum Zielordner
obj_datei = r"C:/Users/kaiim/Downloads/mesh 1.obj"
ziel_ordner = r"C:/Users/kaiim/Downloads"

# Temporäres Blender-Skript
blender_script = os.path.join(os.path.dirname(__file__), "blender_script.py")

# Blender-Code, der in einer separaten Datei gespeichert wird
blender_code = f"""\
import bpy
import os
import time

obj_dateipfad = r"{obj_datei}"
ziel_ordner = r"{ziel_ordner}"

if not os.path.exists(obj_dateipfad):
    print("Fehler: Die OBJ-Datei existiert nicht.")
    bpy.ops.wm.quit_blender()

if not os.path.exists(ziel_ordner):
    os.makedirs(ziel_ordner)

temp_export_datei = os.path.join(ziel_ordner, "temp_export.gltf")
endgueltige_datei = os.path.join(ziel_ordner, "scene.gltf")

# Szene leeren
bpy.ops.wm.read_factory_settings(use_empty=True)

# OBJ importieren
try:
    bpy.ops.import_scene.obj(filepath=obj_dateipfad)
    print("✅ OBJ-Datei erfolgreich importiert.")
except Exception as e:
    print("Fehler beim Import:", e)
    bpy.ops.wm.quit_blender()

time.sleep(2)

# Export als glTF
try:
    bpy.ops.export_scene.gltf(filepath=temp_export_datei, export_format='GLTF_SEPARATE')
    print("✅ Export als glTF erfolgreich.")
except Exception as e:
    print("Fehler beim Export:", e)
    bpy.ops.wm.quit_blender()

# Datei umbenennen
if os.path.exists(endgueltige_datei):
    os.remove(endgueltige_datei)
os.rename(temp_export_datei, endgueltige_datei)

print("✅ Datei wurde in scene.gltf umbenannt und gespeichert in:", endgueltige_datei)

# Blender schließen
bpy.ops.wm.quit_blender()
"""

# Skript in eine Datei schreiben (UTF-8 verwenden!)
with open(blender_script, "w", encoding="utf-8") as f:
    f.write(blender_code)

# Blender starten und das Skript ausführen
try:
    subprocess.run([blender_exe, "--background", "--python", blender_script], check=True)
    print("✅ Blender wurde gestartet und das Skript erfolgreich ausgeführt.")
except subprocess.CalledProcessError as e:
    print("❌ Fehler beim Ausführen von Blender:", e)
    sys.exit(1)

# Temporäre Datei entfernen
os.remove(blender_script)

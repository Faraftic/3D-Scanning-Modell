import subprocess
import os
import sys

blender_exe = r"C:/Program Files/Blender Foundation/Blender 4.3/blender-launcher.exe"
obj_datei = r"C:/Users/kaiim/Downloads/mesh 1.obj"
ziel_ordner = r"C:/Users/kaiim/Downloads"
blender_script = os.path.join(os.path.dirname(__file__), "blender_script.py")

blender_code = f"""\
import bpy
import os

obj_dateipfad = r"{obj_datei}"
ziel_ordner = r"{ziel_ordner}"

if not os.path.exists(ziel_ordner):
    os.makedirs(ziel_ordner)

temp_export_datei = os.path.join(ziel_ordner, "temp_export.gltf")
endgueltige_datei = os.path.join(ziel_ordner, "scene.gltf")

bpy.ops.wm.read_factory_settings(use_empty=True)

bpy.ops.import_scene.obj(filepath=obj_dateipfad)

bpy.ops.export_scene.gltf(filepath=temp_export_datei, export_format='GLTF_SEPARATE')

if os.path.exists(endgueltige_datei):
    os.remove(endgueltige_datei)
os.rename(temp_export_datei, endgueltige_datei)

bpy.ops.wm.quit_blender()
"""

with open(blender_script, "w") as f:
    f.write(blender_code)

try:
    subprocess.run([blender_exe, "--python", blender_script], check=True)
    print("✅ Blender wurde gestartet und das Skript erfolgreich ausgeführt.")
except subprocess.CalledProcessError as e:
    print("❌ Fehler beim Ausführen von Blender:", e)
    sys.exit(1)

os.remove(blender_script)

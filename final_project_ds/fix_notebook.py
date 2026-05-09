import json

file = "../notebooks/03_MIH_Modeling.ipynb"

with open(file, "r", encoding="utf-8") as f:
    nb = json.load(f)

# quitar widgets problemáticos
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]

with open(file, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("✔ Widgets eliminados correctamente")
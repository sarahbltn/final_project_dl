import json

file = r"C:\Users\Usuario\Documents\6TO SEMESTRE ITESO\DEEP LEARNING\final_project_dl\notebooks\03_MIH_Modeling.ipynb"

with open(file, "r", encoding="utf-8") as f:
    nb = json.load(f)

# 1. limpiar metadata completa (Colab + widgets)
nb["metadata"] = {}

# 2. limpiar cada celda completamente
for cell in nb.get("cells", []):
    cell["outputs"] = []
    cell["execution_count"] = None
    cell["metadata"] = {}

    # por si hay outputs raros anidados
    if "id" in cell:
        pass

print("✔ limpiando notebook tipo Colab para GitHub")

with open(file, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)
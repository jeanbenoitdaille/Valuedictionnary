employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))
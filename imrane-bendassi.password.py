import hashlib

def verifier_mot_de_passe(mot_de_passe):
    
    # Vérifier la longueur minimale
    if len(mot_de_passe) < 8:
        return False
    
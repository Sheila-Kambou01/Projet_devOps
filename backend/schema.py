from pydantic import BaseModel
from typing import Optional

class Utilisateur(BaseModel):

    id:str
    nom: str
    email:str
    mot_de_passe:str

    class Tache:
        orm_mode = True

class Tache(BaseModel):
    id:str
    titre:str
    description:str
    statut:str
    date_creation: Optional[datetime]
    date_echeance: Optional[datetime]
    class Utilisateur:
        orm_mode = True
    class Tache:
        from_attributes = True

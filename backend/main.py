from fastapi import FastAPI
import uvicorn
from fastapi_sqlalchemy import DBSessionMiddlware, db
import controller
from models import Tache,Utilisateur

import database


app = FastAPI()



@app.post("/taches/", response_model=models.Tache)
def create_tache(titre: str, description: str, date_echeance: str, utilisateur_id: int):
    db_tache = Tache(
        titre=titre,
        description=description,
        date_echeance=date_echeance,
        utilisateur_id=utilisateur_id,
        statut="à faire"
    )
    db.session.add(db_tache)
    db.session.commit()
    #db.refresh(db_tache)
    return db_tache

@app.get("/taches/{utilisateur_id}", response_model=List[Tache])
def get_taches(utilisateur_id: int):
    return db.session.query(Tache).filter(Tache.utilisateur_id == utilisateur_id).all()


if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=8200)
from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from sqlalchemy.orm import Session
#from fastapi_sqlalchemy import DBSessionMiddlware, db
#import controller
#from models import Tache, Utilisateur
from schema import Tache,Utilisateur
from database import get_db
from typing import List


app = FastAPI()



@app.post("/taches/", response_model=Tache)
def create_tache(titre: str, description: str, date_echeance: str, utilisateur_id: int, db: Session = Depends(get_db)):
    db_tache = Tache(
        titre=titre,
        description=description,
        date_echeance=date_echeance,
        utilisateur_id=utilisateur_id,
        statut="à faire"
    )
    db.add(db_tache)
    db.commit()
    #db.refresh(db_tache)
    return db_tache

@app.get("/taches/{utilisateur_id}", response_model=List[Tache])
def get_taches(db: Session, utilisateur_id: int):
    return db.query(Tache).filter(Tache.utilisateur_id == utilisateur_id).all()


@app.get("/tache/{tache_id}", response_model=Tache)
def get_tache(tache_id: int, db: Session = Depends(get_db)):
    tache = db.query(Tache).filter(Tache.id == tache_id).first()
    if tache is None:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return tache

@app.put("/tache/{tache_id}", response_model=Tache)
def update_tache_status(tache_id: int, statut: str, db: Session = Depends(get_db)):
    db_tache = db.query(Tache).filter(Tache.id == tache_id).first()
    if db_tache:
        db_tache.statut = statut
        db.commit()
        db.refresh(db_tache)
    return db_tache

@app.delete("/tache/{tache_id}", response_model=Tache)
def delete_tache(tache_id: int, db: Session = Depends(get_db)):
    db_tache = db.query(Tache).filter(Tache.id == tache_id).first()
    if db_tache:
        db.delete(db_tache)
        db.commit()
    if db_tache is None:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return db_tache



#if __name__=='__main__':
#    uvicorn.run(app, host='0.0.0.0', port=8200)
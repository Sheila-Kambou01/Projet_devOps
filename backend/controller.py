from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
#from . import 
from . import services, models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/taches/", response_model=models.Tache)
def create_tache(titre: str, description: str, date_echeance: str, utilisateur_id: int, db: Session = Depends(get_db)):
    return services.create_tache(db, titre, description, date_echeance, utilisateur_id)

@router.get("/taches/{utilisateur_id}", response_model=List[models.Tache])
def get_taches(utilisateur_id: int, db: Session = Depends(get_db)):
    return services.get_taches(db, utilisateur_id)

@router.get("/tache/{tache_id}", response_model=models.Tache)
def get_tache(tache_id: int, db: Session = Depends(get_db)):
    tache = services.get_tache(db, tache_id)
    if tache is None:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return tache

@router.put("/tache/{tache_id}", response_model=models.Tache)
def update_tache_status(tache_id: int, statut: str, db: Session = Depends(get_db)):
    return services.update_tache_status(db, tache_id, statut)

@router.delete("/tache/{tache_id}", response_model=models.Tache)
def delete_tache(tache_id: int, db: Session = Depends(get_db)):
    tache = services.delete_tache(db, tache_id)
    if tache is None:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return tache

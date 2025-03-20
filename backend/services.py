from sqlalchemy.orm import Session
from . import models
from datetime import datetime

def create_tache(db: Session, titre: str, description: str, date_echeance: datetime, utilisateur_id: int):
    db_tache = models.Tache(
        titre=titre,
        description=description,
        date_echeance=date_echeance,
        utilisateur_id=utilisateur_id,
        statut="à faire"
    )
    db.add(db_tache)
    db.commit()
    db.refresh(db_tache)
    return db_tache

def get_taches(db: Session, utilisateur_id: int):
    return db.query(models.Tache).filter(models.Tache.utilisateur_id == utilisateur_id).all()

def get_tache(db: Session, tache_id: int):
    return db.query(models.Tache).filter(models.Tache.id == tache_id).first()

def update_tache_status(db: Session, tache_id: int, statut: str):
    db_tache = db.query(models.Tache).filter(models.Tache.id == tache_id).first()
    if db_tache:
        db_tache.statut = statut
        db.commit()
        db.refresh(db_tache)
    return db_tache

def delete_tache(db: Session, tache_id: int):
    db_tache = db.query(models.Tache).filter(models.Tache.id == tache_id).first()
    if db_tache:
        db.delete(db_tache)
        db.commit()
    return db_tache

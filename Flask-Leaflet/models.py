from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TableUniqueTemporaire(db.Model):
    __tablename__ = 'table_unique_temporaire'

    id = db.Column(db.Integer, primary_key=True)
    site_cen = db.Column(db.String)
    nom_agri = db.Column(db.String)
    prenom_agri = db.Column(db.String)
    societe = db.Column(db.String)
    contact = db.Column(db.String)
    surf_ha = db.Column(db.Float)
    types_productions = db.Column(db.String)
    produits_finis = db.Column(db.String)
    agriculture_bio = db.Column(db.String)
    type_contrat = db.Column(db.String)
    surf_contractualisee = db.Column(db.Float)
    date_signature = db.Column(db.DateTime)
    date_prise_effet = db.Column(db.DateTime)
    date_fin = db.Column(db.DateTime)
    types_milieux = db.Column(db.String)
    referent = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

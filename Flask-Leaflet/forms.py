from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField, SubmitField, DateField, SelectMultipleField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange, DataRequired
from datetime import date


class MarkerForm(FlaskForm):
    site = SelectField('Site(s) CEN concerné(s)', validators=[DataRequired()], choices = [('value1', 'Choice 1'), ('value2', 'Choice 2'), ('value3', 'Choice 3')]) # Replace the choices with your actual options

    societe = StringField("Société / Appellation de l'exploitation", validators=[DataRequired()])

    nom = StringField('Nom', [InputRequired(),
        # Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=3, max=50, message="Longueur du champ non invalide")
        ])
    
    prenom = StringField('Prénom', [InputRequired(),
        # Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=3, max=25, message="Longueur du champ prénom invalide")
        ])
    
    contact = StringField('Contact', [InputRequired(),
        # Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=6, max=50, message="Longueur du champ contact invalide")
        ])
    
    SAU_surf = FloatField('SAU exploitation (ha)', validators=[NumberRange(min=1, max=1000)], default=0)
    types_prod = SelectMultipleField ('Productions principales', choices=[('prod1', 'Production 1'), ('prod2', 'Production 2')])  # Replace the choices with your actual options
    types_vente = SelectField('Produits finis', choices=[('vente1', 'Vente 1'), ('vente2', 'Vente 2')])  # Replace the choices with your actual options
    bio = BooleanField('Agriculture bio')
    type_contrat_CEN = SelectField('Type de contrat agricole avec le CEN', choices=[('contrat1', 'Contrat 1'), ('contrat2', 'Contrat 2')])  # Replace the choices with your actual options
    surf_contractualisee = FloatField('Surface contractualisée', validators=[NumberRange(min=1, max=1000)], default=0)
    signature = DateField('Date de signature', default=date.today)
    prise_effet = DateField("Date de prise d'effet", default=date.today)
    fin = DateField('Date de fin', default=date.today)
    grands_types_milieux = SelectField('Grands types de milieux', choices=[('milieu1', 'Milieu 1'), ('milieu2', 'Milieu 2')])  # Replace the choices with your actual options

    charge_mission = StringField('Chargé de mission référent', [InputRequired(),
        # Regexp(r'^[A-Za-z\s\-\']+$', message="Invalid sock name"),
        Length(min=3, max=50, message="Longueur du champ 'Chargé de mission référent' invalide")
        ])
    
    remarques = StringField('Remarques')
    latitude = FloatField('Latitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Valider')
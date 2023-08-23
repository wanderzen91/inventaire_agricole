import os
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
import psycopg2
from forms import MarkerForm
import secrets
import json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

secret_key = secrets.token_hex(16)

app.secret_key = secret_key

conn = psycopg2.connect(host='database.cen-nouvelle-aquitaine.dev',
                        database='congres_2023',
                        user='rmodba',
                        password='!Y}?}LY@Tb#o]sz{]8tm',
                        port = '5432')



@app.route('/')
def carte():

    cur = conn.cursor()
    cur.execute("SELECT * FROM volet_agricole.table_unique_temporaire")
    data = cur.fetchall()
    cur.close()
    form = MarkerForm()


    with open('depts_na.geojson') as geojson_file:
        geojson = json.load(geojson_file)
    
    return render_template('index.html', data=data, form=form, geojson=geojson)


def get_selected_marker(marker_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM volet_agricole.table_unique_temporaire WHERE id = %s", (marker_id,))
    marker_data = cur.fetchone()
    cur.close()

    return marker_data

@app.route('/fill_inputs_edit/<marker_id>', methods=['GET', 'POST'])
def fill_inputs_edit(marker_id):
    # Query the database or any other data source to retrieve the marker data based on the marker ID
    # Assuming you have a function called get_marker_data_from_db() to retrieve the data
    marker_data = get_selected_marker(marker_id)

    form = MarkerForm()
    
    return render_template('modal2.html', data = marker_data, form = form)
    # # return f"'markerId: {form.site}"  # Add this line for debugging


@app.route('/edit_modal_data', methods=['GET', 'POST'])
def edit_modal_data():

    form = MarkerForm()

    cur = conn.cursor()


    if request.method == 'POST':
        
        id = request.form.get('id_marker')
        site_cen = request.form.get('site','test')
        nom_agri = request.form.get('nom','test')
        prenom_agri = request.form.get('prenom','test')
        societe = request.form.get('societe','test')
        contact = request.form.get('contact','test')
        surf_ha = request.form.get('SAU_surf',1)
        types_productions = request.form.get('types_prod','test')
        produits_finis = request.form.get('types_vente','test')
        agriculture_bio = request.form.get('bio','test')
        type_contrat = request.form.get('type_contrat_CEN','test')
        surf_contractualisee = request.form.get('surf_contractualisee',1)
        date_signature = request.form.get('signature', '01-01-2000')
        date_prise_effet = request.form.get('prise_effet', '01-01-2000')
        date_fin = request.form.get('fin', '01-01-2000')
        types_milieux = request.form.get('grands_types_milieux','test')
        referent = request.form.get('charge_mission','test')
        remarques = request.form.get('remarques','test')

        sql = "UPDATE volet_agricole.table_unique_temporaire SET site_cen = %s, nom_agri = %s, prenom_agri = %s, societe = %s, contact = %s, surf_ha = %s, types_productions = %s, produits_finis = %s, agriculture_bio = %s, type_contrat = %s, surf_contractualisee = %s, date_signature = %s, date_prise_effet = %s, date_fin = %s, types_milieux = %s, referent = %s, remarques = %s WHERE id = %s"
        data = (site_cen, nom_agri, prenom_agri, societe, contact, surf_ha, types_productions, produits_finis, agriculture_bio, type_contrat, surf_contractualisee, date_signature, date_prise_effet, date_fin, types_milieux, referent, remarques, id)

        cur.execute(sql, data)

        conn.commit()
        cur.close()
        
        # Rest of your code to update the database
            

    return redirect('/')

        

# Handle saving the modal data
@app.route('/save_modal_data', methods=['GET', 'POST'])
def save_modal_data():
    
    try:

        cur = conn.cursor()

        cur.execute("SELECT MAX(id) FROM volet_agricole.table_unique_temporaire")
        max_marker_id = cur.fetchone()[0]

        if request.method == 'POST':
            # Increment the marker ID
            id = max_marker_id + 1
            site_cen = request.form.get('site','test')
            nom_agri = request.form.get('nom','test')
            prenom_agri = request.form.get('prenom','test')
            societe = request.form.get('societe','test')
            contact = request.form.get('contact','test')
            surf_ha = request.form.get('SAU_surf',1)
            types_productions = request.form.get('types_prod','test')
            produits_finis = request.form.get('types_vente','test')
            agriculture_bio = request.form.get('bio','test')
            type_contrat = request.form.get('type_contrat_CEN','test')
            surf_contractualisee = request.form.get('surf_contractualisee',1)
            date_signature = request.form.get('signature', '01-01-2000')
            date_prise_effet = request.form.get('prise_effet', '01-01-2000')
            date_fin = request.form.get('fin', '01-01-2000')
            types_milieux = request.form.get('grands_types_milieux','test')
            referent = request.form.get('charge_mission','test')
            remarques = request.form.get('remarques','test')
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')

        # return jsonify({'markerId': current_marker_id})

        # return f"'markerId: {id}, Longitude: {longitude}, Site: {site_cen}, Nom: {nom_agri}"  # Add this line for debugging

        # Assuming you have a table named 'markers' with columns 'name', 'first_name', 'latitude', 'longitude'
        sql = "INSERT INTO volet_agricole.table_unique_temporaire (id, site_cen, nom_agri, prenom_agri, societe, contact, surf_ha, types_productions, produits_finis, agriculture_bio, type_contrat, surf_contractualisee, date_signature, date_prise_effet, date_fin, types_milieux, referent, remarques, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (id, site_cen, nom_agri, prenom_agri, societe, contact, surf_ha, types_productions, produits_finis, agriculture_bio, type_contrat, surf_contractualisee, date_signature, date_prise_effet, date_fin, types_milieux, referent, remarques, latitude, longitude)

        cur.execute(sql, data)

        conn.commit()
        cur.close()

        flash('Donnée bien enregistrée !', 'success')
    except psycopg2.Error as e:
        # Handle database-related errors
        flash('Une erreur a été rencontrée au moment de la sauvegarde de la donnée : {}'.format(str(e)), 'error')
    except Exception as e:
        # Handle other exceptions
        flash('Une erreur a été rencontrée au moment de la sauvegarde de la donnée : {}'.format(str(e)), 'error')

    # Redirect to the appropriate page after deletion
    return redirect('/')

    # return "Data saved successfully"
@app.route('/delete_marker/<int:marker_id>', methods=['GET', 'POST'])
def delete_marker(marker_id):
        
    try:

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Construct the DELETE query
        delete_query = "DELETE FROM volet_agricole.table_unique_temporaire WHERE id = %s"

        # Execute the DELETE query with the row ID
        cursor.execute(delete_query, (marker_id,))
        # Commit the changes to the database
        conn.commit()

        # Close the cursor and connection
        cursor.close()
 
        flash('Donnée bien supprimée !', 'success')
    except psycopg2.Error as e:
        # Handle database-related errors
        flash('Une erreur a été rencontrée au moment de la suppression de la donnée : {}'.format(str(e)), 'error')
    except Exception as e:
        # Handle other exceptions
        flash('Une erreur a été rencontrée au moment de la suppression de la donnée : {}'.format(str(e)), 'error')

    # Redirect to the appropriate page after deletion
    return redirect('/')

@app.route('/tableau')
def tableau():
    cur = conn.cursor()
    cur.execute("SELECT * FROM volet_agricole.table_unique_temporaire")
    rows = cur.fetchall()

    # Get the column names from the cursor description
    columns = [desc[0] for desc in cur.description]

    # Pass the columns and data to the template
    return render_template('tableau.html', columns=columns, data=rows)

if __name__ == '__main__':
    app.run(debug=True)
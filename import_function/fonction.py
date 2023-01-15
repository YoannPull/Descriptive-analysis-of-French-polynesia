# ==================================================================================================
"""Fonctions : Group of functiuns used in studies on french Polynesia"""
# ==================================================================================================
__author__  = "Guiraud Paul"
__version__ = "1.0"
__date__    = "2022-01-06"

# ==================================================================================================
## Carte Introduction 
def PF_map():   
    
    import folium
    from folium import plugins
    import IPython.display as dp
    
    #Création de la carte
    PF = folium.Map(location=[-0.65946, -179.417145], width=500,height=500, zoom_start=1.5)
    folium.Marker(location=[-17.65946, -149.417145],  tooltip=  'Polynésie française', color='red').add_to(PF)
    folium.CircleMarker(location=[-17.65946, -149.417145],radius=10, fill_color='red').add_to(PF)
    return PF

# ==================================================================================================
## Carte Tourisme
def Carte_tourisme(df) :
    from IPython.display import IFrame
    from ipywidgets import interact
    import folium
    @interact(n=(2007,2022))
    
    def affichage_carte_Provenance_tourisme(n): 

        ##Création de la carte
        Provenance_tourisme = folium.Map(location=[32.30230141364259, 9.042608177267951], zoom_start=1.5)

        ##Ajout marqueur sur chaque pays de provenance

        #Différencier les marqueurs par couleurs sur les different quantiles
        COLOR=['beige','orange','red','darkred', 'black']

        for i in range (0,len(df['Provenance'])) :

            if df[str(n)][i] <= df[str(n)].quantile(q=0.2) :
                c=COLOR[0]

            if df[str(n)].quantile(q=0.2) < df[str(n)][i] <= df[str(n)].quantile(q=0.4) :
                c=COLOR[1]

            if df[str(n)].quantile(q=0.4) < df[str(n)][i] <= df[str(n)].quantile(q=0.6) :
                c=COLOR[2]

            if df[str(n)].quantile(q=0.6) < df[str(n)][i] <= df[str(n)].quantile(q=0.8) :
                c=COLOR[3]

            if df[str(n)].quantile(q=0.8) < df[str(n)][i] <= df[str(n)].quantile(q=1) :
                c=COLOR[4]

        #Ajout du marqueur
            folium.Marker([df['Latitude'][i], df['Longitude'][i]], tooltip= " <br> ".join([df['Provenance'][i], str(df[str(n)][i])]), icon=folium.Icon(color=c) ).add_to(Provenance_tourisme)

        return Provenance_tourisme
# ==================================================================================================
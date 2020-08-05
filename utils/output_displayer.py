#coding:utf-8

def lastfm_output_displayer(preferences, artists):
    prefered_artists = []
    for p in preferences.item.unique():
        prefered_artists.append(artists[artists.id == p].name.iloc[0])
    return prefered_artists

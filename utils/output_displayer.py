#coding:utf-8

def lastfm_output_displayer(preferences, artists, behaviour):
    prefered_artists = []
    for p in preferences.item.unique():
        prefered_artists.append(artists[artists.id == p].name.iloc[0])
    if behaviour == "WARM":
        return "I'm sure you would like to listen for " + ", ".join(prefered_artists[:-1]) + " and " + prefered_artists[-1] + "!"
    elif behaviour == "COMP":
        return "I recommend you to listen for " + ", ".join(prefered_artists[:-1]) + " and " + prefered_artists[-1] + "."
    return ", ".join(prefered_artists)

#coding:utf-8

def lastfm_output_displayer(preferences, artists, behaviour):
    prefered_artists = []
    for p in preferences.item.unique():
        prefered_artists.append(artists[artists.id == p].name.iloc[0])
    if behaviour == "WARM":
        if len(prefered_artists) > 1:
            return "I'm sure you would like to listen for " + ", ".join(prefered_artists[:-1]) + " and " + prefered_artists[-1] + "!"
        else:
            return "I'm sure you would like to listen for " + prefered_artists[0] + "!"
    elif behaviour == "COMP":
        if len(prefered_artists) > 1:
            return "I recommend you to listen for " + ", ".join(prefered_artists[:-1]) + " and " + prefered_artists[-1] + "."
        else:
            return "I recommend you to listen for " + prefered_artists[0] + "."
    return ", ".join(prefered_artists)

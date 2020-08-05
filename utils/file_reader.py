#coding:utf-8

import pickle
import pandas as pd

# LASTFM

def read_lastfm(directory):
    d = directory
    if d[-1] != "/":
        d += "/"

    artists = pd.read_csv(d + "artists.dat", sep="\t", usecols=['id', 'name', 'url', 'pictureURL'])
    with open(d + "tags.dat") as f:
        lines = f.readlines()
        ids = []
        values = []
        for i, line in enumerate(lines[1:]):
            ids.append(line.strip().split("\t")[0])
            values.append(line.strip().split("\t")[1])
        tags = pd.DataFrame({'tagID': ids, 'tagValue': values})
    tags.tagID = tags.tagID.transform(int)
    user_artists = pd.read_csv(d + "user_artists.dat", sep="\t", usecols=['userID', 'artistID', 'weight'])
    user_friends = pd.read_csv(d + "user_friends.dat", sep="\t", usecols=['userID', 'friendID'])
    user_taggedartists = pd.read_csv(d + "user_taggedartists.dat", sep="\t", usecols=['userID', 'artistID', 'tagID', 'day', 'month', 'year'])

    return artists, tags, user_artists, user_friends, user_taggedartists

def experiment_lastfm(directory, load=False, filename='experiment_df_lastfm.pkl'):
    d = directory
    if d[-1] != "/":
        d += "/"

    artists, tags, user_artists, user_friends, user_taggedartists = read_lastfm(d+"lastfm")
    if not load:
        df = create_experiment_df(user_artists, tags, user_taggedartists, 500)

        f = d+filename
        outfile = open(f,'wb')
        pickle.dump(df,outfile,protocol=4)
        outfile.close()
    else:
        f = open(d+filename,'rb')
        df = pickle.load(f)
        f.close()
    return df, tags, artists

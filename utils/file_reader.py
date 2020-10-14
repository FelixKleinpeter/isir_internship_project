#coding:utf-8

import pickle
import pandas as pd
from os import path

# LASTFM

from utils.cleaning import create_experiment_df

def read_lastfm(directory):
    d = directory
    if d[-1] != "/":
        d += "/"

    with open(d + "tags.dat") as f:
        lines = f.readlines()
        ids = []
        values = []
        for i, line in enumerate(lines[1:]):
            ids.append(line.strip().split("\t")[0])
            values.append(line.strip().split("\t")[1])
        tags = pd.DataFrame({'tagID': ids, 'tagValue': values})
    tags.tagID = tags.tagID.transform(int)
    artists = pickle.load( open( d + "artists.p", "rb" ) )
    user_artists = pickle.load( open( d + "user_artists.p", "rb" ) )
    user_taggedartists = pickle.load( open( d + "user_taggedartists.p", "rb" ) )

    return artists, tags, user_artists, user_taggedartists

def experiment_lastfm(directory, force_create=False, filename='experiment_df_lastfm.pkl'):
    d = directory
    if d[-1] != "/":
        d += "/"

    artists, tags, user_artists, user_taggedartists = read_lastfm(d+"lastfm")
    if path.exists(d+filename) and force_create == False:
        f = open(d+filename,'rb')
        df = pickle.load(f)
        f.close()
    else:
        df = create_experiment_df(user_artists, tags, user_taggedartists, 500)
        f = d+filename
        outfile = open(f,'wb')
        pickle.dump(df,outfile,protocol=4)
        outfile.close()
    return df, tags, artists

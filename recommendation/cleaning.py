
import pandas as pd
import numpy as np

from recommendation.functions import get_X

#LASTFM

def remove_useless_tags(tags, user_taggedartists, threshold):
    counts = user_taggedartists.tagID.value_counts()
    selected = counts[counts > threshold].index
    selected_tags = tags[[(i in selected) for i in tags.tagID]]
    selected_user_taggedartists = user_taggedartists[[(i in selected) for i in user_taggedartists.tagID]]

    meaningless_tags = ["chillout", "ambient", "downtempo", "seen live", "beautiful", "amazing", "sexy", "awesome", "cover", "mellow"]
    meaningless_tagIDs = []
    for t in meaningless_tags:
        meaningless_tagIDs.append(selected_tags[selected_tags.tagValue == t].index[0])
    selected_tags.drop(meaningless_tagIDs)
    selected.remove(meaningless_tagIDs)

    names_to_replace = {"idm": "intelligent dance", "ebm":"electronic body", "00s": "2000s"}
    ids, values = selected_tags.tagID.values, selected_tags.tagValue.values
    for i, v in enumerate(values):
        if v in names_to_replace.keys():
            values[i] = names_to_replace[v]
    selected_tags = pd.DataFrame({'tagID': ids, 'tagValue': values})

    ###Remove tags from user_taggedartists

    return selected_tags, selected_user_taggedartists

def create_experiment_df(user_artists, tags, user_taggedartists, threshold):
    selected_tags, selected_user_taggedartists = remove_useless_tags(tags, user_taggedartists, threshold)
    weights = user_artists.weight
    maxw = np.max(weights)
    threshold = np.exp(0.5 * np.log(maxw))
    ratings = np.zeros(weights.size, dtype=int)
    for i in range(len(ratings)):
        ratings[i] = (-5) * np.log(weights.iloc[i] / maxw) / np.log(maxw)

    experiment_dict = {
        "item":user_artists.artistID,
        "user":user_artists.userID,
        "rating":ratings,
    }

    l = user_artists.artistID.size
    for tag in selected_tags.tagID:
        experiment_dict[int(tag)] = np.zeros(l, dtype=int)

    for i in range(selected_user_taggedartists.userID.size):
        experiment_dict[selected_user_taggedartists.tagID.iloc[i]][user_artists.artistID == selected_user_taggedartists.artistID.iloc[i]] += 1

    experiment_df = pd.DataFrame(experiment_dict)

    df = experiment_df.copy()
    for c in get_X(experiment_df):
        df[c] = df[c].map(lambda x : 1 if x >= 1 else 0)

    return df

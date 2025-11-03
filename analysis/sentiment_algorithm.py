# this would probably be better as a json for less clutter but i am lazy
adjustments = {
    'danceability': {
        'excitement': 0.1,
        'amusement': 0.05,
        'joy': 0.025
    },
    'energy': {
        'excitement': 0.1,
        'joy': 0.05,
        'amusement': 0.025
    },
    'loudness': {
        'anger': 0.1,
        'excitement': 0.05,
        'surprise': 0.025
    },
    'tempo': {
        'excitement': 0.1,
        'joy': 0.025,
    },
    'valence': {
        'optimism': 0.1,
        'approval': 0.05,
        'joy': 0.025
    }
}

def standardize_features(features):
    features['tempo'] = features['tempo'] / 250
    features['loudness'] = features['loudness'] / -60
    return features

def get_sentiments(song, artist, debug=False):
    from analysis.sentiment_analyzer import analyze
    from analysis.audio_features import get_audio_features
    from analysis.lyric_grabber import get_lyrics_tester
    import copy

    sentiments = analyze(get_lyrics_tester(song, artist))
    base_sentiments = copy.deepcopy(sentiments)
    features = get_audio_features(song, artist)

    if not features:
        if debug:
            print(f"no features for {song} by {artist}")
        return base_sentiments

    features = standardize_features(features)

    for feature, emotiondict in adjustments.items():
        for sentiment in sentiments:
            label = sentiment['label']
            if label in emotiondict:
                sentiment['score'] += emotiondict[label] * features[feature]

    return sentiments
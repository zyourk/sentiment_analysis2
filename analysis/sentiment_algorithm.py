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

def get_sentiment_single(song, artist, debug=False):
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

def get_sentiments(songs, debug=False):
    from analysis.sentiment_analyzer import analyze
    from analysis.audio_features import get_audio_features_batch
    from analysis.lyric_grabber import get_batched_lyrics
    import copy

    lyric_map = get_batched_lyrics(songs)

    batch_lyrics = [lyric_map[(s["song"], s["artist"])] for s in songs]

    batch_sentiments = analyze(batch_lyrics)
    batch_features = get_audio_features_batch(songs)

    results = {}
    for i, song in enumerate(songs):
        sentiments = batch_sentiments[i]
        features = batch_features.get((song["song"], song["artist"]))

        if not features:
            if debug:
                print(f"no features for {song['song']} by {song['artist']}")
            results[(song["song"], song["artist"])] = sentiments
            continue

        features = standardize_features(features)

        # Apply sentiment adjustments
        for feature, emotiondict in adjustments.items():
            for sentiment in sentiments:
                label = sentiment["label"]
                if label in emotiondict:
                    sentiment["score"] += emotiondict[label] * features[feature]

        results[(song["song"], song["artist"])] = sentiments

    return results

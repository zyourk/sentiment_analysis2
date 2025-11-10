from numpy import dot
from numpy.linalg import norm
import numpy as np

def get_best_rec(song, artist, debug=False):
    from analysis.track_recs import return_recs
    from analysis.sentiment_algorithm import get_sentiments, get_sentiment_single
    from analysis.audio_features import get_audio_features, get_audio_features_batch

    candidates = return_recs(song=song, artist=artist)
    if not candidates:
        return None, None, None

    sentiments = get_sentiment_single(song=song, artist=artist)
    features = get_audio_features(song=song, artist=artist)

    candidates = return_recs(song=song, artist=artist)
    candidates = [{"song": c["song"], "artist": c["artist"]} for c in candidates]
    batched_cand_sents = get_sentiments(candidates)
    batched_cand_feats = get_audio_features_batch(candidates)
    candidate_map = []
    songs = []
    for candidate in candidates:
        if debug:
            print(f"candidate: {candidate['song']} by {candidate['artist']}")
        songs.append({"song": candidate['song'], "artist": candidate['artist']})
        cand_sent = batched_cand_sents.get((candidate["song"], candidate["artist"]), [])
        cand_feat = batched_cand_feats.get((candidate["song"], candidate["artist"]), [])
        if debug:
            print(sentiments)
            print(cand_sent)
            print(features)
            print(cand_feat)
        if cand_feat and features:
            cand_score = score_song(song_sent=sentiments, song_feat=features, cand_sent=cand_sent, cand_feat=cand_feat)
        else:
            cand_score = score_song_no_features(song_sent=sentiments, cand_sent=cand_sent)
        candidate_map.append({
            "song": candidate["song"],
            "artist": candidate["artist"],
            "score": cand_score
        })
    candidate_map = sorted(candidate_map, key=lambda x: x["score"], reverse=True)
    for sorted_song in candidate_map:
        if sorted_song["artist"].lower() == artist.lower():
            same_artist_song = sorted_song
            break
    for sorted_song in candidate_map:
        if sorted_song["artist"].lower() != artist.lower():
            different_artist_song = sorted_song
            break
    return same_artist_song, different_artist_song, sentiments[0]

def score_song(song_sent, song_feat, cand_sent, cand_feat):
    return score_sentiments(song_sent, cand_sent) * 0.7 + score_features(song_feat, cand_feat) * 0.3

def score_song_no_features(song_sent, cand_sent):
    return score_sentiments(song_sent, cand_sent)

def score_sentiments(song_sent, cand_sent) -> float:
    song_map = {sent['label']: sent['score'] for sent in song_sent}
    cand_map = {sent['label']: sent['score'] for sent in cand_sent}

    shared_sents = set(song_map.keys()) & set(cand_map.keys())
    if not shared_sents:
        return 0.0

    similarity = sum(1 - abs(song_map[emotion] - cand_map[emotion]) for emotion in shared_sents)
    avg_similarity = similarity / len(song_map)

    overlap_adjustment = len(shared_sents) / len(song_map)

    return 0.6 * avg_similarity + 0.4 * overlap_adjustment

def score_features(song_feat, cand_feat) -> float:
    song_feat, cand_feat = np.array(list(song_feat.values())), np.array(list(cand_feat.values()))
    if norm(song_feat) == 0 or norm(cand_feat) == 0:
        return 0.0
    return dot(song_feat, cand_feat) / (norm(cand_feat) * norm(song_feat))
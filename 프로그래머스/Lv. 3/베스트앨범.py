from collections import defaultdict

def solution(genres, plays):
    
    genre_dict = defaultdict(list)
    play_dict = defaultdict(int)
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        play_dict[genre] += play
        genre_dict[genre].append((play, index))
    
    result = []
    for key, value in sorted(play_dict.items(), key=lambda x: x[1], reverse=True):
        result += [i[1] for i in sorted(genre_dict[key], key=lambda x: (-x[0], x[1]))[:2]]
    
    return result

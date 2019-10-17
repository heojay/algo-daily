# Programmers Coding Test
# 17683. SAMPLE TEMPLATE
# https://programmers.co.kr/learn/courses/30/lessons/17683

'''
2018년 카카오 블라인드 코딩 테스트 기출 문제 중 하나.
구현을 얼마나 효율적으로 할 수 있는가..를 평가할 수 있지 않을까.
파이썬의 위대한 문자열 처리 기술을 확인할 수 있다.
'''


def solution(m, musicinfos):
    answer = "(None)"
    
    musicinfos = [x.split(',') for x in musicinfos]
    d = {'C#': 'H', 'D#': 'I', 'F#': 'J', 'G#': 'K', 'A#': 'L'}
    
    for i in range(len(musicinfos)):
        for k in d.keys():
            musicinfos[i][3] = musicinfos[i][3].replace(k, d[k])
    
    for k in d.keys():
        m = m.replace(k, d[k])
    
    def time_m(a, b):
        return (int(b[:2])-int(a[:2]))*60 + (int(b[3:])-int(a[3:]))
    
    def whole_song(song, time):
        song_l = len(song)
        return song*(time // song_l) + song[:time%song_l]
        
    cand = []
    
    for i, x in enumerate(musicinfos):
        song_name = x[2]
        s_time = time_m(x[0], x[1])
        w_song = whole_song(x[3], s_time)
        cand.append([s_time, len(musicinfos)-i, song_name, w_song])
    
    cand.sort(reverse = True)
    
    for x in cand:
        if(m in x[3]):
            answer = x[2]
            break
    
    return answer
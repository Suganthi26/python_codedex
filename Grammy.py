# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

#function to find somgs longer than 5 minutes
def longer_than_five_minutes (song):
 return song [1] > 5.00

#function to convert song duration from minute to seconds
def minutes_to_seconds(song):
  duration = song[1]
  minutes = int(duration)
  seconds = (duration - minutes) * 60
  total_seconds = minutes * 60 + round(seconds)
  return total_seconds

#function to add total duration of songs
from functools import reduce 

def add_durations (total, song):
  duration = song[1]
  return total + duration

print(playlist)
long_songs = list(filter(longer_than_five_minutes, playlist))
print('Songs that are longer than 5 minutes:', long_songs)

duration = list(map(minutes_to_seconds, playlist))
print("Total seconds of all songs:", duration)

total_time = reduce(add_durations, playlist, 0)
print("Total playtime of all songs:", total_time, 'minutes')

#results:
#[('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ("I Can't Breath", 4.47), ('Bad Guy', 3.14)]
#Songs that are longer than 5 minutes: [('Just Like That', 5.05), ('Song 3', 6.55)]
#Total seconds of all songs: [205, 303, 393, 241, 268, 188]
#Total playtime of all songs: 26.65
  

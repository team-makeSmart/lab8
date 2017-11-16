# MakeSmart
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee
# Lab 8


# problem 1
def decreaseVolume(sound):
  """ decreases the volume of the sound by 1/2 """
  """ sound:(string) the sound file """
  for sample in getSamples(sound):
    value = getSample(sample)
    setSample(sample,value * 0.5)
  play(sound)

# problem 2  
def changeVolume(sound, factor):
  """ increases the volume of the sound by a factor """
  """ sound:(string) the sound file """
  """ factor:(int/float)the factor to increase the sound """
  for sample in getSamples(sound):
    value = getSample(sample)
    setSample(sample,value * factor)
  play(sound)

# problem 3
def maxSample(sound):
  """ sound:(string) the sound file """
  """ returns the largest sample value in a sound """
  largest = 0
  for s in getSamples(sound):
    largest = max(largest,getSample(s))
  factor = 32767.0 / largest
  return largest

def maxVolume(sound):
  """ sets the maximum posible volume """
  """ sound:(string) the sound file """
  factor = 32767.0 / maxSample(sound)
  for s in getSamples(sound):
    louder = factor * getSample(s)
    setSample(s,louder)
  play (sound)

# problem 4
def goToEleven(sound):
  """ if the sample value is greater than 0 """  
  """ sets the maximum posible volume """
  """ if the sample value is less than 0 """
  """ sets the minimum posible volume """
  """ sound:(string) the sound file """
  for sample in getSamples(sound):
    value = getSample(sample)
    if value > 0:
      setSample(sample,32767)
    if value < 0:
      setSample(sample,-32768)
  play(sound)
from pygame import mixer

mixer.init()
mixer.music.load("filename.mp3")
mixer.music.play(-1)
print("Loop Playing")

try:
	while True:
		continue

except KeyboardInterrupt:
	print(" App Closed")

# ThisIsARaspberryPiProjectWhichTakesAudioSignalsAndTurnsThemIntoLights
see repo name

- Two rpis on network
- hardcoded addresses
- raftos
- replicated list of songs (mp3 paths)
	- if not stored in local: make sure pis have same soundtrack
- talk to each other
	- calibrate
- when list depleted, wait for new additions
- audio sources: fixed directory (best library evar)

- html
	- ul button list for adding songs to queue
	- asyncio flask
- python runs audio popped from list

- synchronization but like ronnie i wanna have synchronization because that's a cool word

- look up how to take 
	- play audio and get stream of volume concurrently
	- convert audio to raw equivalent, then pressures 44k matrix microphone pressure

- flask, pyaudio, raftos, venv
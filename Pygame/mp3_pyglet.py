import pyglet


song = pyglet.media.load('sound.mp3')
song.play()
pyglet.app.run()

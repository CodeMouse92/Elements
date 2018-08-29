"""
SoundPlayer [Elements]
The sound playback module and functionality.

Author(s): Jason C. McDonald
"""

from elements import playqueue

class SoundPlayer(object):
    """
    The actual sound player for Elements. Also stores state information.
    The callbacks in elements.py should be used to call most of these
    functions, as those callbacks also handle UI changes.
    """

    def __init__(self):
        self._queue = playqueue.PlayQueue()
        self._pause_pos = 0
        self._sound = None
        self.track = None
        self.load_queued()

    # STATUS FUNCTIONS

    def is_playing(self):
        """
        Returns playback status.
        """
        if self._sound:
            return self._sound.state == 'play'
        else:
            return False

    # PLAYBACK FUNCTIONS

    def toggle(self):
        """
        Toggle play/pause.
        """
        if self.is_playing():
            self.pause()
        else:
            self.play()

    def play(self, allow_restart=True):
        """
        Start playing audio from current position.

        The no_restart boolean argument ensures we don't wind up with
        infinite recursion, and prevents unexpected "restart queue"
        behaviors.
        """
        # If we have audio loaded...
        if self._sound:
            self._sound.play()
            if self._pause_pos != 0:
                self._sound.seek(self._pause_pos)
        # Otherwise, if nothing is loaded, but we have something in the queue.
        elif self._queue.is_queued() and allow_restart:
            # Load the first item in the queue.
            self._queue.front()
            self.load_queued()
            # Call the play function, preventing recursion.
            self.play(False)

    def pause(self):
        """
        Stop audio while storing position.
        """
        self._pause_pos = self._sound.get_pos()
        self._sound.stop()

    def stop(self):
        """
        Stop audio altogether.
        """
        # If we have audio loaded...
        if self._sound:
            self._sound.stop()
            self._pause_pos = 0

    def prev(self):
        """
        Restart current item or skip to previous queued item.
        """
        # If we have audio loaded...
        if self._sound:
            # If we're less than 1% of the way through the track...
            if (self._sound.get_pos() / self._sound.length) < 0.01:
                # Stop the current track.
                self.stop()
                # Go to the previous track and load it.
                self._queue.prev()
                self.load_queued()
                # Play the new queued track.
                self.play()
            # Otherwise, if we're more than 1% of the way through the track...
            else:
                # Start the track over.
                self._sound.seek(0)
        # Otherwise, if we have no audio loaded...
        else:
            # Go to the previous track and load it.
            self._queue.prev()
            self.load_queued()
            # Play the new queued track.
            self.play(False)

    def next(self):
        """
        Skip to next queued item.
        """
        # Stop the current track.
        self.stop()
        # Go to the next track and load it.
        self._queue.next()
        self.load_queued()
        # Play the next track.
        self.play(False)

    # QUEUE FUNCTIONS

    def load_queued(self):
        """
        Load the scheduled track from the queue.
        """
        self.track = self._queue.load()

        # If sound is loaded...
        if self._sound:
            # Unload the sound from memory.
            self._sound.unload()
            # Remove the sound object to prevent crashes.
            self._sound = None

        # If we actually got a track to load...
        if self.track:
            # Load the track into our sound object.
            ## TODO: Play sound
            pass

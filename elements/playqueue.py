"""
PlayQueue [Elements]
The playback queue.

Author(s): Jason C. McDonald
"""

from elements import track

class PlayQueue(object):
    """
    A queue of tracks to play. SoundPlayer stores and controls this.
    """

    def __init__(self):
        """
        Initialize a new playqueue.
        """
        self._queued = [track.Track(0), track.Track(1)]
        # The 1-based index. BE CAREFUL OF OFF-BY-ONES!
        self._item = 1

    def is_queued(self):
        """
        Returns true if items are queued, else false.
        """
        return len(self._queued) > 0

    def load(self):
        """
        Returns the next track to play, or None if there is no queued
        track.
        """
        print("LOAD: " + str(self._item))
        # If the index is out of range...
        if self._item < 1 or self._item > len(self._queued):
            # Return a None
            return None
        else:
            return self._queued[self._item-1]

    def front(self):
        """
        Move to the first item in the queue.
        """
        if len(self._queued) > 0:
            self._item = 1

    def prev(self):
        """
        Move back in the queue.
        """
        # If there are items behind us...
        if self._item > 1:
            # Go back one item.
            self._item -= 1
        # Else if no item is loaded...
        elif self._item == 0:
            # Jump to the end of the queue.
            self._item = len(self._queued)

    def next(self):
        """
        Move forward in the queue.
        """
        # If there are items ahead of us...
        if self._item <= len(self._queued):
            self._item += 1

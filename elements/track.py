"""
Track [Elements]
A single track.

Author(s): Jason C. McDonald
"""

from tinytag import TinyTag

class Track(object):
    """
    A single playable track to be stored in PlayQueue.
    """

    def __init__(self, key):
        """
        Define a new track, linking it to a database entry.
        """
        # Store the key to look the track up in the database.
        self._database_key = key

        # TEMPORARY
        if key == 0:
            self._filepath = r"/home/jason/testaudio.ogg"
        else:
            self._filepath = r"/home/jason/testaudio2.ogg"

    def get_path(self):
        """
        Return the file path for loading the song.
        """
        return self._filepath

    def get_tags(self):
        """
        Return the tag object for the currently playing track.
        """
        if self._filepath:
            return TinyTag.get(self._filepath)

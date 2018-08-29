"""
Track [Elements]
A single track.

Author(s): Jason C. McDonald
"""


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
        # Store the filepath
        self._filepath = None

        # HACK: TEMPORARY
        if key == 0:
            self._filepath = r"/home/jason/testaudio.ogg"
        else:
            self._filepath = r"/home/jason/testaudio2.ogg"
        # END TEMPORARY

    def get_path(self):
        """
        Return the file path for loading the song.
        """
        return self._filepath

    # TODO: We will retrieve tags via the database functions.

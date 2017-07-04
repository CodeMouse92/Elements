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
        # Store the filepath
        self._filepath = None

        # TEMPORARY
        if key == 0:
            self._filepath = r"/home/jason/testaudio.ogg"
        else:
            self._filepath = r"/home/jason/testaudio2.ogg"
        # END TEMPORARY

        self._tags = TinyTag.get(self._filepath)


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
            return self._tags

    # TRACK INFORMATION
    # We retrieve this data through these functions because the database
    # may override the track's ID3 metadata.

    def album(self):
        """
        Return the album title.
        """
        return self._tags.album

    def albumartist(self):
        """
        Return the album artist.
        """
        return self._tags.albumartist

    def artist(self):
        """
        Return the track artist.
        """
        return self._tags.artist

    def disc(self):
        """
        Return the disc number.
        """
        return self._tags.disc

    def disc_total(self):
        """
        Return the total number of discs in the set.
        """
        return self._tags.disc_total

    def duration(self):
        """
        Return the track duration.
        """
        return self._tags.duration

    def genre(self):
        """
        Return the genre.
        """
        return self._tags.genre

    def title(self):
        """
        Return the track title.
        """
        return self._tags.title

    def track(self):
        """
        Return the track number.
        """
        return self._tags.track

    def track_total(self):
        """
        Return the total number of tracks on the album.
        """
        return self._tags.track_total

    def year(self):
        """
        Return the track year.
        """
        return self._tags.year

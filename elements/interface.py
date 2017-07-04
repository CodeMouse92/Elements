"""
Interface [Elements]
Kivy GUI and callbacks. Everything else is ultimately called by this.

Author(s): Jason C. McDonald
"""

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.compat import PY2
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
#from kivy.uix.bubble import Bubble
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from elements import soundplayer

# Make sure we're using the right version of Kivy.
kivy.require('1.10.0')


class ElementsWindow(FloatLayout):
    """
    Parent class for the app. Most of the callback functions needed by the
    application will need to go here, so they can be accessed by any
    Kivy widget via `root.whatever()`
    """

    def __init__(self, **kwargs):
        """
        Initialize a new ElementsWindow.
        """
        # Derive the initializer from the parent class initializer.
        if PY2:
            super(ElementsWindow, self).__init__(**kwargs)
        else:
            super().__init__(**kwargs)

        self.player = soundplayer.SoundPlayer()

    # Playback functions.
    def playback_toggle(self):
        """
        Toggle playback of audio.
        """
        self.player.toggle()
        self.refresh_playback_ui()


    def playback_stop(self):
        """
        Stop playback.
        """
        self.player.stop()
        self.refresh_playback_ui()

    def playback_prev(self):
        """
        Restart current item or go to previous item in queue.
        """
        self.player.prev()
        self.refresh_playback_ui()

    def playback_next(self):
        """
        Go to next item in queue.
        """
        self.player.next()
        self.refresh_playback_ui()

    def refresh_playback_ui(self):
        """
        Update interface to reflect playback status.
        """
        # Update play/pause button.
        if self.player.is_playing():
            self.ids.img_btnPlayback.source = "icons/ui/elements_pause.png"
        else:
            self.ids.img_btnPlayback.source = "icons/ui/elements_play.png"

        # Update displayed metadata.
        tags = self.player.get_tags()
        if tags:
            self.ids.lbl_NowPlaying_TrackNumberTitle.text = tags.track + ". " + tags.title
            self.ids.lbl_NowPlaying_TrackArtist.text = tags.artist
            self.ids.lbl_NowPlaying_TrackAlbumYear.text = tags.album + " (" + tags.year + ")"
        else:
            self.ids.lbl_NowPlaying_TrackNumberTitle.text = "Elements"
            self.ids.lbl_NowPlaying_TrackArtist.text = ""
            self.ids.lbl_NowPlaying_TrackAlbumYear.text = "(Nothing Playing...)"

class Tooltip(Label):
    """
    Extending the Label class to create a tooltip.
    Defined further in elements.kv
    """
    visible = False

class UIButton(Button):
    """
    Extending the button class to allow for additional functionality,
    including tooltips.
    """

    # To get the instance of Tooltip above, we have to define a new ObjectProperty().
    # We're not sure why. (Thanks to Aritodo of #kivy for figuring this out.)
    tooltip = ObjectProperty()

    def __init__(self, **kwargs):
        """
        Initialize a new UIButton widget.
        """
        # Watch the window's mouse movement event.
        Window.bind(mouse_pos=self.on_mouse_pos)
        # Derive the initializer from the parent class initializer.
        if PY2:
            super(UIButton, self).__init__(**kwargs)
        else:
            super().__init__(**kwargs)

        # Define a new Tooltip.
        self.tooltip = Tooltip()

    def on_mouse_pos(self, *args):
        """
        Callback for when the mouse moves on the window.
        """
        # If we're not in the root window, forget it.
        if not self.get_root_window():
            return

        # Get the position (x,y) from the arguments.
        pos = args[1]

        # Cancel any scheduled events since the cursor was moved.
        Clock.unschedule(self.display_tooltip)

        # If we can see the tooltip, remove it.
        if self.tooltip.visible:
            self.close_tooltip()

        # If we are moving the mouse over this widget...
        if self.collide_point(*self.to_widget(*pos)):
            # Schedule the tooltip to appear after half a second.
            Clock.schedule_once(self.display_tooltip, 0.5)
            # Set the tooltip's x to the position of the cursor.
            if App.get_running_app().root.width - pos[0] < 50:
                # However, if we're too close to the right edge (and thus would
                # have cutoff on the tooltip), move its position back a bit.
                self.tooltip.x = pos[0] - 50
            else:
                self.tooltip.x = pos[0]

            # Set the tooltip's y to the position of the cursor.
            if App.get_running_app().root.height - pos[1] < 30:
                # If we're too close to the top edge (and thus would have
                # cutoff), move the tooltip down a bit.
                self.tooltip.y = pos[1] - 30
                # Also, move it to the right a little more, so the cursor
                # doesn't cover up part of the first letter.
                self.tooltip.x = self.tooltip.x + 7
            else:
                self.tooltip.y = pos[1]

    def display_tooltip(self, *args):
        """
        Display the tooltip. The location is set in the event listener
        that calls this.
        """
        # Mark the tooltip as visible (for event listener reference only)
        self.tooltip.visible = True
        # Get the tooltip text from this widget's properties in the .kv file.
        self.tooltip.text = self.info
        # Add the widget to the app.
        App.get_running_app().root.add_widget(self.tooltip)
        # Ignore unusued arguments that get passed anyway.
        # Basically, shut the linter up.
        del args

    def close_tooltip(self):
        """
        Remove the tooltip from the screen.
        """
        # Mark the tooltip as invisible (for event listener reference only).
        self.tooltip.visible = False
        # Remove the tooltip from the app.
        App.get_running_app().root.remove_widget(self.tooltip)

class ElementsApp(App):
    """
   Application-level class, builds the application
   """

    def build_config(self, config):
        """
       Configure the application.
       """

        # Prevent the window from resizing too small. (SDL2 windows only).
        Config.set('graphics', 'minimum_width', '500')
        Config.set('graphics', 'minimum_height', '300')

    def build(self):
        """
       This function starts the applicaif __name__ == '__main__':
    ElementsApp().run()tion by constructing
       it from widgets and properties.
       """

        # Set the title and icon.
        self.title = "Elements"
        self.icon = "icons/app/elements_icon_512.png"

        # Create the window.
        elements_app = ElementsWindow()
        return elements_app

def alive():
    """Check if Elements is detected. We'll drop this once we have some
   other tests."""
    return True

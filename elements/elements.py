import kivy
kivy.require('1.9.2')

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


class ElementsWindow(FloatLayout):
    """
   Parent class for the app
   """
    pass

class Tooltip(Label):
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
        if(self.tooltip.visible):
            self.close_tooltip()

        # If we are moving the mouse over this widget...
        if self.collide_point(*self.to_widget(*pos)):
            # Schedule the tooltip to appear.
            Clock.schedule_once(self.display_tooltip, 1)
            # Set the tooltip's x to the position of the cursor.
            if(App.get_running_app().root.width - pos[0] < 50):
                # However, if we're too close to the right edge (and thus would
                # have cutoff on the tooltip), move its position back a bit.
                self.tooltip.x = pos[0] - 50
            else:
                self.tooltip.x = pos[0]

            # Set the tooltip's y to the position of the cursor.
            if(App.get_running_app().root.height - pos[1] < 30):
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
        self.tooltip.text=self.info
        # Add the widget to the app.
        App.get_running_app().root.add_widget(self.tooltip)

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
       This function starts the application by constructing
       it from widgets and properties.
       """

        # Set the title and icon.
        self.title = "Elements"
        self.icon = "icons/app/elements_icon_512.png"

        # Create the window.
        elements_app = ElementsWindow()
        return elements_app

if __name__ == '__main__':
    ElementsApp().run()

def alive():
    """Check if Elements is detected. We'll drop this once we have some
   other tests."""
    return True

import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.bubble import Bubble
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

    tooltip = Tooltip()

    def __init__(self, **kwargs):
        Window.bind(mouse_pos=self.on_mouse_pos)
        super().__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        #self.tooltip.pos = pos
        #Clock.unschedule(self.display_tooltip) # cancel scheduled event since I moved the cursor

        if(self.tooltip.visible):
            self.close_tooltip() # close if it's opened

        if self.collide_point(*self.to_widget(*pos)):
            #Clock.schedule_once(self.display_tooltip, 1)
            self.display_tooltip(pos)

    def display_tooltip(self, pos):
        self.tooltip.visible = True
        self.tooltip.text=self.info
        self.tooltip.x = pos[0]
        #self.tooltip.x = 100
        self.tooltip.y = pos[1]
        #self.tooltip.y = 100
        App.get_running_app().root.add_widget(self.tooltip)
        print("Open tooltip: " + str(pos) + " vs (" + str(self.tooltip.x) + ", " + str(self.tooltip.y) + ")")
        print("    " + str(self.tooltip.width) + "x" + str(self.tooltip.height))

    def close_tooltip(self):
        self.tooltip.visible = False
        App.get_running_app().root.remove_widget(self.tooltip)
        print("Close tooltip")

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

import kivy
kivy.require('1.9.2')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.bubble import Bubble

class ElementsWindow(FloatLayout):
    """
    Parent class for the app
    """

    def menu_toggle_tag_bubble(self):
        print("Yo!" + str(self))
        bubble = BubbleTags()
        self.add_widget(bubble)
        print(self.ids['btnTags'].y)
        print(bubble.height)
        bubble.x = self.ids['btnTags'].x + (self.ids['btnTags'].width/2)
        bubble.y = self.ids['btnTags'].y - bubble.height

class BubbleTags(Bubble):
    pass

class ElementsApp(App):
    """
    Application-level class, builds the application
    """

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

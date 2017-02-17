import kivy
kivy.require('1.9.2')



from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ElementsWindow(BoxLayout):
    """
    Parent class for the app
    """
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

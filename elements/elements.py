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
        Builds the app out of widgets
        """
        elements_app = ElementsWindow()
        return elements_app

if __name__ == '__main__':
    ElementsApp().run()

def alive():
    """Check if Elements is detected. We'll drop this once we have some
    other tests."""
    return True

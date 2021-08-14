"""
app.py

Contains the gui app

TODO export config
"""

# from ctypes import windll
import tkinter as tk

from .. import config, main
from .convert import ConvertFrame
from .examples import ExamplesFrame
from .output import OutputFrame
from .settings import SettingsFrame
from .sidebar import Sidebar

# windll.shcore.SetProcessDpiAwareness(True)


def run_app():
    """Runs the GUI App"""
    App().mainloop()


class App(tk.Tk):
    """Main App class"""

    def __init__(self):
        super().__init__()
        self.title("sb3topy")

        # Create config variables
        self.init_config()
        self.read_config()

        self.mode = tk.StringVar()
        self.mode.trace_add('write', self.cb_mode)

        sidebar = Sidebar(self, self.mode)
        self.convert = ConvertFrame(self, padding="5 0 5 5")
        self.examples = ExamplesFrame(self, padding="5 0 5 5")
        self.output = OutputFrame(self, padding="5 0 5 5")
        self.settings = SettingsFrame(self, padding="5 0 5 5")

        sidebar.grid(column=0, row=0, sticky="NSEW")
        self.convert.grid(column=1, row=0, sticky="NSWE")
        self.examples.grid(column=1, row=0, sticky="NSEW")
        self.output.grid(column=1, row=0, sticky="NSWE")
        self.settings.grid(column=1, row=0, sticky="NSWE")

        self.columnconfigure(0, minsize=100)
        self.columnconfigure(1, minsize=300, weight=1)
        self.rowconfigure(0, minsize=300, weight=1)

        self.mode.set(config.DEFAULT_GUI_TAB)

        self.geometry("720x480")
        self.resizable(0, 0)

    def cb_mode(self, *_):
        """Called when the mode switches"""
        self.convert.grid_remove()
        self.examples.grid_remove()
        self.output.grid_remove()
        self.settings.grid_remove()

        mode = self.mode.get()
        if mode == "convert":
            self.convert.grid()
        elif mode == "examples":
            self.examples.grid()
            self.examples.switch_to()
        elif mode == "output":
            self.output.grid()
        elif mode == "settings":
            self.settings.grid()

    def init_config(self):
        """Creates config variables"""
        tk.StringVar(self, name="OUTPUT_PATH")
        tk.StringVar(self, name="PROJECT_PATH")
        tk.StringVar(self, name="PROJECT_URL")
        tk.BooleanVar(self, name="AUTORUN")
        tk.Variable(self, name="JSON_SHA")

    def run_main(self):
        """Runs the converter with the current config"""
        self.mode.set("output")
        process, queue = main.run_mp()
        self.output.start_watching(process, queue)

    def read_config(self):
        """
        Loads values from the config module into variables of this Tk.
        """
        self.setvar("OUTPUT_PATH", config.OUTPUT_PATH)
        self.setvar("PROJECT_PATH", config.PROJECT_PATH)
        self.setvar("PROJECT_URL", config.PROJECT_URL)
        self.setvar("AUTORUN", config.AUTORUN)
        self.setvar("JSON_SHA", config.JSON_SHA)
        print(self.getvar("OUTPUT_PATH"))

    def write_config(self):
        """
        Writes values from variables of this Tk to the config module.
        """
        config.OUTPUT_PATH = self.getvar("OUTPUT_PATH")
        config.PROJECT_PATH = self.getvar("PROJECT_PATH")
        config.PROJECT_URL = self.getvar("PROJECT_URL")
        config.AUTORUN = self.getvar("AUTORUN")
        config.JSON_SHA = self.getvar("JSON_SHA")

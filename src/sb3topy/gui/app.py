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

        # Adjust the window size
        scale = round(self.winfo_fpixels('1i')) / 96
        self.geometry(f"{round(720*scale)}x{round(480*scale)}")
        # self.resizable(0, 0)
        self.scale = scale

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

        # config.config.set_all(1)
        # self.read_config()

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
            self.output.switch_to()
        elif mode == "settings":
            self.settings.grid()

    def init_config(self):
        """Creates config variables"""
        # Unsorted
        tk.BooleanVar(self, name="AUTORUN")
        tk.Variable(self, name="JSON_SHA")
        tk.BooleanVar(self, name="CONVERT_ASSETS")
        tk.StringVar(self, name="CONFIG_PATH")
        tk.BooleanVar(self, name="AUTOLOAD_CONFIG")

        # General / Paths
        tk.StringVar(self, name="OUTPUT_PATH")
        tk.StringVar(self, name="PROJECT_PATH")
        tk.StringVar(self, name="PROJECT_URL")

        # Assets / Extraction
        tk.BooleanVar(self, name="VERIFY_ASSETS")
        tk.BooleanVar(self, name="FRESHEN_ASSETS")
        tk.BooleanVar(self, name="RECONVERT_SOUNDS")
        tk.BooleanVar(self, name="RECONVERT_IMAGES")

        # Assets / Workers
        tk.IntVar(self, name="DOWNLOAD_THREADS")
        tk.IntVar(self, name="CONVERT_THREADS")
        tk.IntVar(self, name="CONVERT_TIMEOUT")

        # Assets / SVGs
        tk.BooleanVar(self, name="USE_SVG_CMD")
        tk.StringVar(self, name="SVG_COMMAND")
        tk.IntVar(self, name="SVG_SCALE")
        # tk.IntVar(self, name="SVG_DPI")
        tk.BooleanVar(self, name="CONVERT_COSTUMES")

        # Assets / MP3s
        tk.BooleanVar(self, name="CONVERT_SOUNDS")
        tk.StringVar(self, name="MP3_COMMAND")

        # Optimizations / Basic
        tk.BooleanVar(self, name="LEGACY_LISTS")
        tk.BooleanVar(self, name="VAR_TYPES")
        tk.BooleanVar(self, name="ARG_TYPES")
        tk.BooleanVar(self, name="LIST_TYPES")

        # Optimizations / Advanced
        tk.BooleanVar(self, name="DISABLE_ANY_CAST")
        tk.BooleanVar(self, name="AGGRESSIVE_NUM_CAST")
        tk.BooleanVar(self, name="CHANGED_NUM_CAST")
        tk.BooleanVar(self, name="DISABLE_STR_CAST")
        tk.BooleanVar(self, name="DISABLE_INT_CAST")

        # Project / Timings
        tk.IntVar(self, name="TARGET_FPS")
        tk.BooleanVar(self, name="TURBO_MODE")
        tk.IntVar(self, name="WORK_TIME_INV")
        tk.DoubleVar(self, name="WARP_TIME")

        # Project / Display
        tk.IntVar(self, name="STAGE_WIDTH")
        tk.IntVar(self, name="STAGE_HEIGHT")
        tk.IntVar(self, name="DISPLAY_WIDTH")
        tk.IntVar(self, name="DISPLAY_HEIGHT")
        tk.BooleanVar(self, name="ALLOW_RESIZE")
        tk.BooleanVar(self, name="SCALED_DISPLAY")
        tk.IntVar(self, name="FS_SCALE")
        tk.IntVar(self, name="FLIP_THRESHOLD_INV")

        # Project / Title
        tk.BooleanVar(self, name="DYNAMIC_TITLE")
        tk.StringVar(self, name="TITLE")

        # Project / Audio
        tk.IntVar(self, name="AUDIO_CHANNELS")
        tk.IntVar(self, name="MASTER_VOLUME")

        # Project / Limits
        tk.IntVar(self, name="MAX_CLONES")
        tk.IntVar(self, name="MAX_LIST")

        # Project / Hotkeys
        tk.BooleanVar(self, name="TURBO_HOTKEY")
        tk.BooleanVar(self, name="FULLSCREEN_HOTKEY")
        tk.BooleanVar(self, name="DEBUG_HOTKEYS")

        # Project / Miscellaneous
        tk.BooleanVar(self, name="DRAW_FPS")
        tk.StringVar(self, name="USERNAME")
        tk.IntVar(self, name="RANDOM_SEED")

        # Debug / Debug
        tk.IntVar(self, name="LOG_LEVEL")
        tk.BooleanVar(self, name="DEBUG_JSON")
        tk.BooleanVar(self, name="FORMAT_JSON")
        tk.BooleanVar(self, name="OVERWRITE_ENGINE")

    def run_main(self):
        """Runs the converter with the current config"""
        self.mode.set("output")
        process, queue = main.run_mp()
        self.output.start_watching(process, queue)

    def read_config(self):
        """
        Loads values from the config module into variables of this Tk.

        re.sub('tk.+name="(.+)"', r'self.setvar("\1", config.\1)', text)
        """
        # Unsorted
        self.setvar("AUTORUN", config.AUTORUN)
        self.setvar("JSON_SHA", config.JSON_SHA)
        self.setvar("CONVERT_ASSETS", config.CONVERT_ASSETS)
        self.setvar("CONFIG_PATH", config.CONFIG_PATH)
        self.setvar("AUTOLOAD_CONFIG", config.AUTOLOAD_CONFIG)

        # General / Paths
        self.setvar("OUTPUT_PATH", config.OUTPUT_PATH)
        self.setvar("PROJECT_PATH", config.PROJECT_PATH)
        self.setvar("PROJECT_URL", config.PROJECT_URL)

        # Assets / Extraction
        self.setvar("VERIFY_ASSETS", config.VERIFY_ASSETS)
        self.setvar("FRESHEN_ASSETS", config.FRESHEN_ASSETS)
        self.setvar("RECONVERT_SOUNDS", config.RECONVERT_SOUNDS)
        self.setvar("RECONVERT_IMAGES", config.RECONVERT_IMAGES)

        # Assets / Workers
        self.setvar("DOWNLOAD_THREADS", config.DOWNLOAD_THREADS)
        self.setvar("CONVERT_THREADS", config.CONVERT_THREADS)
        self.setvar("CONVERT_TIMEOUT", config.CONVERT_TIMEOUT)

        # Assets / SVGs
        self.setvar("USE_SVG_CMD", config.USE_SVG_CMD)
        self.setvar("SVG_COMMAND", config.SVG_COMMAND)
        self.setvar("SVG_SCALE", config.SVG_SCALE)
        # self.setvar("SVG_DPI", config.SVG_DPI)
        self.setvar("CONVERT_COSTUMES", config.CONVERT_COSTUMES)

        # Assets / MP3s
        self.setvar("CONVERT_SOUNDS", config.CONVERT_SOUNDS)
        self.setvar("MP3_COMMAND", config.MP3_COMMAND)

        # Optimizations / Basic
        self.setvar("LEGACY_LISTS", config.LEGACY_LISTS)
        self.setvar("VAR_TYPES", config.VAR_TYPES)
        self.setvar("ARG_TYPES", config.ARG_TYPES)
        self.setvar("LIST_TYPES", config.LIST_TYPES)
        self.setvar("SOLO_BROADCASTS", config.SOLO_BROADCASTS)
        self.setvar("WARP_ALL", config.WARP_ALL)

        # Optimizations / Advanced
        self.setvar("DISABLE_ANY_CAST", config.DISABLE_ANY_CAST)
        self.setvar("AGGRESSIVE_NUM_CAST", config.AGGRESSIVE_NUM_CAST)
        self.setvar("CHANGED_NUM_CAST", config.CHANGED_NUM_CAST)
        self.setvar("DISABLE_STR_CAST", config.DISABLE_STR_CAST)
        self.setvar("DISABLE_INT_CAST", config.DISABLE_INT_CAST)

        # Project / Timings
        self.setvar("TARGET_FPS", config.TARGET_FPS)
        self.setvar("TURBO_MODE", config.TURBO_MODE)
        self.setvar("WORK_TIME_INV", config.WORK_TIME_INV)
        self.setvar("WARP_TIME", config.WARP_TIME)

        # Project / Display
        self.setvar("STAGE_WIDTH", config.STAGE_WIDTH)
        self.setvar("STAGE_HEIGHT", config.STAGE_HEIGHT)
        self.setvar("DISPLAY_WIDTH", config.DISPLAY_WIDTH)
        self.setvar("DISPLAY_HEIGHT", config.DISPLAY_HEIGHT)
        self.setvar("ALLOW_RESIZE", config.ALLOW_RESIZE)
        self.setvar("SCALED_DISPLAY", config.SCALED_DISPLAY)
        self.setvar("FS_SCALE", config.FS_SCALE)
        self.setvar("FLIP_THRESHOLD_INV", config.FLIP_THRESHOLD_INV)

        # Project / Title
        self.setvar("DYNAMIC_TITLE", config.DYNAMIC_TITLE)
        self.setvar("TITLE", config.TITLE)

        # Project / Audio
        self.setvar("AUDIO_CHANNELS", config.AUDIO_CHANNELS)
        self.setvar("MASTER_VOLUME", config.MASTER_VOLUME * 100)

        # Project / Limits
        self.setvar("MAX_CLONES", config.MAX_CLONES)
        self.setvar("MAX_LIST", config.MAX_LIST)

        # Project / Hotkeys
        self.setvar("TURBO_HOTKEY", config.TURBO_HOTKEY)
        self.setvar("FULLSCREEN_HOTKEY", config.FULLSCREEN_HOTKEY)
        self.setvar("DEBUG_HOTKEYS", config.DEBUG_HOTKEYS)

        # Project / Miscellaneous
        self.setvar("DRAW_FPS", config.DRAW_FPS)
        self.setvar("USERNAME", config.USERNAME)
        self.setvar("RANDOM_SEED", config.RANDOM_SEED)

        # Debug / Debug
        self.setvar("LOG_LEVEL", config.LOG_LEVEL)
        self.setvar("DEBUG_JSON", config.DEBUG_JSON)
        self.setvar("FORMAT_JSON", config.FORMAT_JSON)
        self.setvar("OVERWRITE_ENGINE", config.OVERWRITE_ENGINE)

    def write_config(self):
        """
        Writes values from variables of this Tk to the config module.

        re.sub('tk.+name="(.+)".+', r'self.setvar("\1", config.\1)', text)
        """
        # Unsorted
        config.AUTORUN = tkbool(self.getvar("AUTORUN"))
        config.JSON_SHA = self.getvar("JSON_SHA")
        config.CONVERT_ASSETS = tkbool(self.getvar("CONVERT_ASSETS"))
        config.CONFIG_PATH = self.getvar("CONFIG_PATH")
        config.AUTOLOAD_CONFIG = tkbool(self.getvar("AUTOLOAD_CONFIG"))

        # General / Paths
        config.OUTPUT_PATH = self.getvar("OUTPUT_PATH")
        config.PROJECT_PATH = self.getvar("PROJECT_PATH")
        config.PROJECT_URL = self.getvar("PROJECT_URL")

        # Assets / Extraction
        config.VERIFY_ASSETS = tkbool(self.getvar("VERIFY_ASSETS"))
        config.FRESHEN_ASSETS = tkbool(self.getvar("FRESHEN_ASSETS"))
        config.RECONVERT_SOUNDS = tkbool(self.getvar("RECONVERT_SOUNDS"))
        config.RECONVERT_IMAGES = tkbool(self.getvar("RECONVERT_IMAGES"))

        # Assets / Workers
        config.DOWNLOAD_THREADS = self.getvar("DOWNLOAD_THREADS")
        config.CONVERT_THREADS = self.getvar("CONVERT_THREADS")
        config.CONVERT_TIMEOUT = self.getvar("CONVERT_TIMEOUT")

        # Assets / SVGs
        config.USE_SVG_CMD = tkbool(self.getvar("USE_SVG_CMD"))
        config.SVG_COMMAND = self.getvar("SVG_COMMAND")
        config.SVG_SCALE = self.getvar("SVG_SCALE")
        # config.SVG_DPI = self.getvar("SVG_DPI")
        config.CONVERT_COSTUMES = tkbool(self.getvar("CONVERT_COSTUMES"))

        # Assets / MP3s
        config.CONVERT_SOUNDS = tkbool(self.getvar("CONVERT_SOUNDS"))
        config.MP3_COMMAND = self.getvar("MP3_COMMAND")

        # Optimizations / Basic
        config.LEGACY_LISTS = tkbool(self.getvar("LEGACY_LISTS"))
        config.VAR_TYPES = tkbool(self.getvar("VAR_TYPES"))
        config.ARG_TYPES = tkbool(self.getvar("ARG_TYPES"))
        config.LIST_TYPES = tkbool(self.getvar("LIST_TYPES"))
        config.SOLO_BROADCASTS = tkbool(self.getvar("SOLO_BROADCASTS"))
        config.WARP_ALL = tkbool(self.getvar("WARP_ALL"))

        # Optimizations / Advanced
        config.DISABLE_ANY_CAST = tkbool(self.getvar("DISABLE_ANY_CAST"))
        config.AGGRESSIVE_NUM_CAST = tkbool(self.getvar("AGGRESSIVE_NUM_CAST"))
        config.CHANGED_NUM_CAST = tkbool(self.getvar("CHANGED_NUM_CAST"))
        config.DISABLE_STR_CAST = tkbool(self.getvar("DISABLE_STR_CAST"))
        config.DISABLE_INT_CAST = tkbool(self.getvar("DISABLE_INT_CAST"))

        # Project / Timings
        config.TARGET_FPS = self.getvar("TARGET_FPS")
        config.TURBO_MODE = tkbool(self.getvar("TURBO_MODE"))
        config.WORK_TIME_INV = self.getvar("WORK_TIME_INV")
        config.WARP_TIME = self.getvar("WARP_TIME")

        # Project / Display
        config.STAGE_WIDTH = self.getvar("STAGE_WIDTH")
        config.STAGE_HEIGHT = self.getvar("STAGE_HEIGHT")
        config.DISPLAY_WIDTH = self.getvar("DISPLAY_WIDTH")
        config.DISPLAY_HEIGHT = self.getvar("DISPLAY_HEIGHT")
        config.ALLOW_RESIZE = tkbool(self.getvar("ALLOW_RESIZE"))
        config.SCALED_DISPLAY = tkbool(self.getvar("SCALED_DISPLAY"))
        config.FS_SCALE = self.getvar("FS_SCALE")
        config.FLIP_THRESHOLD_INV = self.getvar("FLIP_THRESHOLD_INV")

        # Project / Title
        config.DYNAMIC_TITLE = tkbool(self.getvar("DYNAMIC_TITLE"))
        config.TITLE = self.getvar("TITLE")

        # Project / Audio
        config.AUDIO_CHANNELS = self.getvar("AUDIO_CHANNELS")
        config.MASTER_VOLUME = int(self.getvar("MASTER_VOLUME")) / 100

        # Project / Limits
        config.MAX_CLONES = self.getvar("MAX_CLONES")
        config.MAX_LIST = self.getvar("MAX_LIST")

        # Project / Hotkeys
        config.TURBO_HOTKEY = tkbool(self.getvar("TURBO_HOTKEY"))
        config.FULLSCREEN_HOTKEY = tkbool(self.getvar("FULLSCREEN_HOTKEY"))
        config.DEBUG_HOTKEYS = tkbool(self.getvar("DEBUG_HOTKEYS"))

        # Project / Miscellaneous
        config.USERNAME = self.getvar("USERNAME")
        config.RANDOM_SEED = self.getvar("RANDOM_SEED")

        # Debug / Debug
        config.LOG_LEVEL = int(self.getvar("LOG_LEVEL"))
        config.DEBUG_JSON = tkbool(self.getvar("DEBUG_JSON"))
        config.FORMAT_JSON = tkbool(self.getvar("FORMAT_JSON"))
        config.OVERWRITE_ENGINE = tkbool(self.getvar("OVERWRITE_ENGINE"))


def tkbool(value):
    """
    False for '0' and falsey values, otherwise true

    tk checkboxes use '1' and '0' for True and False
    """
    return False if value == '0' else bool(value)

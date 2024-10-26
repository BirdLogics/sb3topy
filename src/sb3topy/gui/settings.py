"""
settings.py

Contains the Settings tab of the gui

Locks config path to config path in src/sb3topy/config/config.json


General:
    File Paths
        Project path
        Project url
        Output path

        zip path
        exe path

    Quick Config:
        fps
        turbo mode
        clone limit
        list limit
        master volume
        svg scale
        type guessing
        debug json

Assets:
    Integrity
        verify
        reconvert images
        reconvert sounds

    Workers
        download workers
        conversion workers
        timeout

    SVGs
        svg command
        svg scale

    MP3s
        mp3 command
        enable conversion

Optimizations:
    Basic
        legacy lists
        var types
        arg types
        static lists
        solo broadcasts

    Advanced
        disable any cast
        aggressive num cast
        changed num cast
        disable str cast
        disable int cast
        warp all

Project:
    Timings
        target fps
        turbo
        work time
        warp time

    Display
        stage size
        display size
        allow resize
        scaled display
        fs scale
        flip threshold

    Title
        text
        enable

    Audio
        channels
        master volume

    Limits
        clones
        max list

    Hotkeys
        turbo hotkey
        fullscreen hotkey
        debug hotkeys

    Miscellaneous
        username
        draw fps
        random seed

Debug
    Debug
        debug json
        format json
        overwrite engine

Export:
    Ask for file
    If is autoload, prompt to turn on
    Save
    Update buttons

Save:
    If exists and is not last loaded, prompt
    Update last loaded
    Update buttons

Load:
    Load
    Set last loaded

"""

import tkinter as tk
from os import path
from tkinter import filedialog, messagebox, ttk

from .. import config


class SettingsFrame(ttk.Frame):
    """Handles the Settings tab"""

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)
        self.app = app

        notebook = ttk.Notebook(self)

        self.general = GeneralSettings(app, notebook, padding="3 5 5 5")
        self.assets = AssetSettings(app, notebook, padding="3 5 5 5")
        self.opts = OptimizationSettings(app, notebook, padding="3 5 5 5")
        self.project = ProjectFrame(app, notebook, padding="3 5 5 5")
        self.debug = DebugFrame(app, notebook, padding="3 5 5 5")

        notebook.add(self.general, text="General")
        notebook.add(self.project, text="Project")
        notebook.add(self.assets, text="Assets")
        notebook.add(self.opts, text="Optimizations")
        notebook.add(self.debug, text="Debug")

        notebook.grid(sticky='NSEW')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        notebook.bind("<<NotebookTabChanged>>", self.switch)

        # general.grid(sticky='NSEW')

    def switch(self, _):
        """Called when the tab is switched"""
        self.general.switch()
        self.project.switch()
        self.assets.cairo_toggle()
        self.debug.switch()


class GeneralSettings(ttk.Frame):
    """Handles the General tab of settings"""

    def __init__(self, app, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.app = app

        paths_frame = ttk.Labelframe(self, text="Paths", padding=5)
        quick_frame = ttk.Labelframe(self, text="Quick Config", padding=5)
        config_frame = ttk.LabelFrame(
            self, text="Configuration File", padding=5)

        self.project_path = tk.StringVar(app, name="PROJECT_PATH")
        self.project_url = tk.StringVar(app, name="PROJECT_URL")
        self.output_path = tk.StringVar(app, name="OUTPUT_PATH")

        path_label = ttk.Label(paths_frame, text="Project Path:")
        path_box = ttk.Entry(paths_frame, textvariable=self.project_path)
        url_label = ttk.Label(paths_frame, text="Project URL:")
        url_box = ttk.Entry(paths_frame, textvariable=self.project_url)
        output_label = ttk.Label(paths_frame, text="Output Path:")
        output_box = ttk.Entry(paths_frame, textvariable=self.output_path)

        self.target_fps = tk.IntVar(app, name="TARGET_FPS")
        self.turbo_mode = tk.BooleanVar(app, name="TURBO_MODE")
        self.clone_limit = tk.BooleanVar()
        self.list_limit = tk.BooleanVar()
        self.master_volume = tk.IntVar(app, name="MASTER_VOLUME")
        self.svg_scale = tk.IntVar(app, name="SVG_SCALE")
        self.type_guessing = tk.IntVar()
        self.debug_json = tk.BooleanVar(app, name="DEBUG_JSON")

        fps_label = ttk.Label(quick_frame, text="Target FPS:")
        fps_spin = ttk.Spinbox(
            quick_frame, from_=0, to=9999, width=7,
            textvariable=self.target_fps)
        turbo_check = ttk.Checkbutton(
            quick_frame, text="Turbo Mode", variable=self.turbo_mode)
        clone_check = ttk.Checkbutton(
            quick_frame, text="Clone Limit", variable=self.clone_limit,
            command=self.clone_toggle)
        list_check = ttk.Checkbutton(
            quick_frame, text="List Limit", variable=self.list_limit,
            command=self.list_toggle)
        volume_label = ttk.Label(quick_frame, text="Master Volume:")
        volume_spin = ttk.Spinbox(
            quick_frame, from_=0, to=100, width=7,
            textvariable=self.master_volume)
        type_check = ttk.Checkbutton(
            quick_frame, text="Type Guessing", variable=self.type_guessing,
            command=self.type_guess_toggle)
        json_check = ttk.Checkbutton(
            quick_frame, text="Save project.json", variable=self.debug_json)

        self.config_path = tk.StringVar(app, name="CONFIG_PATH")
        self.autoload = tk.BooleanVar(app, name="AUTOLOAD_CONFIG")
        self.autoload.set(True)

        # If autoload is None, config_path is not None
        self.autoload_saved = config.AUTOLOAD_CONFIG
        if config.AUTOLOAD_CONFIG is None:
            self.last_saved = config.CONFIG_PATH
        elif config.AUTOLOAD_CONFIG:
            self.last_saved = config.AUTOLOAD_PATH
        else:
            self.last_saved = ""

        config_label = ttk.Label(config_frame, text="Path:")
        config_box = ttk.Entry(config_frame, textvariable=self.config_path,
                               validate="focusout", validatecommand=self.config_changed)
        export_button = ttk.Button(
            config_frame, text="Export...", command=self.config_export)
        self.save_button = ttk.Button(
            config_frame, text="Save", command=self.config_save)
        self.load_button = ttk.Button(
            config_frame, text="Load", command=self.config_load)
        self.load_check = ttk.Checkbutton(
            config_frame, text="Load on Start",
            variable=self.autoload, command=self.update_buttons)
        # TODO Restore defaults button

        self.config_path.trace_add("write", self.update_buttons)
        self.update_buttons()

        path_label.grid(column=0, row=0, sticky='W')
        path_box.grid(column=1, row=0, sticky='EW',
                      padx=3, pady=3, columnspan=2)
        url_label.grid(column=0, row=1, sticky='W')
        url_box.grid(column=1, row=1, sticky='EW',
                     padx=3, pady=3, columnspan=2)
        output_label.grid(column=0, row=2, sticky='W')
        output_box.grid(column=1, row=2, sticky='EW',
                        padx=3, pady=3, columnspan=2)

        fps_label.grid(column=0, row=0, sticky='W')
        fps_spin.grid(column=1, row=0, sticky='W', padx=3, pady=3)
        volume_label.grid(column=0, row=1, sticky='W')
        volume_spin.grid(column=1, row=1, sticky='W', padx=3, pady=3)
        turbo_check.grid(column=2, row=0, columnspan=2, sticky='W', padx=3)
        clone_check.grid(column=0, row=2, columnspan=1, sticky='W')
        list_check.grid(column=1, row=2, columnspan=2, sticky='W')
        type_check.grid(column=0, row=3, columnspan=2, sticky='W')
        json_check.grid(column=0, row=4, columnspan=2, sticky='W')

        config_label.grid(column=0, row=0, sticky="W")
        self.load_check.grid(column=1, row=0, sticky="W", padx=6, columnspan=3)
        config_box.grid(column=0, row=1, sticky="EW",
                        padx=3, pady=0, columnspan=2)
        export_button.grid(column=3, row=1, sticky="W")
        self.save_button.grid(column=4, row=1, sticky="W")
        self.load_button.grid(column=5, row=1, sticky="W")

        paths_frame.grid(column=0, row=0, sticky="NSEW")
        quick_frame.grid(column=0, row=1, sticky="NSEW")
        config_frame.grid(column=0, row=2, sticky="SEW")

        paths_frame.columnconfigure(1, weight=1)
        quick_frame.columnconfigure(2, weight=1)
        config_frame.columnconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

    def type_guess_toggle(self, _):
        """Called when the type_gussing checkbox is toggled"""
        value = self.type_guessing.get()
        if value == 0:
            self.app.setvar("VAR_TYPES", False)
            self.app.setvar("ARG_TYPES", False)
        elif value == 1:
            self.app.setvar("VAR_TYPES", True)
            self.app.setvar("ARG_TYPES", True)
        # value is 2 during mixed state

    def clone_toggle(self):
        """Called when the clone limit checkbox is toggled"""
        if self.clone_limit.get():
            self.app.setvar("MAX_CLONES", config.project.MAX_CLONES)
        else:
            self.app.setvar("MAX_CLONES", 0)

    def list_toggle(self):
        """CAlled when the list limit checkbox is toggled"""
        if self.list_limit.get():
            self.app.setvar("MAX_LIST", config.project.MAX_LIST)
        else:
            self.app.setvar("MAX_LIST", 0)

    def switch(self):
        """Called when the tab is switched to"""
        var_types = self.app.getvar("VAR_TYPES")
        arg_types = self.app.getvar("ARG_TYPES")

        if var_types == arg_types:
            self.type_guessing.set(var_types)
        else:
            self.type_guessing.set(2)

        self.list_limit.set(self.app.getvar("MAX_LIST"))
        self.clone_limit.set(self.app.getvar("MAX_CLONES"))

    def config_changed(self):
        """Called when focus leaves the config path entry"""
        if not self.config_path.get():
            self.config_path.set(config.AUTOLOAD_PATH)

    def config_export(self):
        """Browse to export config"""
        # Prompt for a file
        config_path = filedialog.asksaveasfilename(
            filetypes=[("JSON Files", "*.json"),
                       ("All Files", "*.*")])

        if samefile_safe(config_path, config.AUTOLOAD_PATH):
            # Prompt to enable autoload
            if not self.autoload.get():
                self.autoload.set(messagebox.askyesno(
                    "sb3topy", (
                        "Would you like to load these settings next "
                        "time sb3topy opens?")
                ))

            # Update the saved autoload value
            self.autoload_saved = self.autoload.get()

        if config_path:
            # Update the config path
            self.config_path.set(config_path)

            # Save the config data
            self.app.write_config()
            config.save_config(config_path)

            # Update button states
            self.update_buttons()

    def config_save(self):
        """Save to the config path"""
        # Get the config path
        config_path = self.config_path.get()

        # Prompt for overwriting files
        if samefile_safe(config_path, self.last_saved) is False:
            basename = path.basename(config_path)
            result = messagebox.askyesno(
                "sb3topy",
                f"{basename} already exists.\nDo you want to replace it?",
                icon="warning")
            if not result:
                return

        # Update the saved autoload value
        if samefile_safe(config_path, config.AUTOLOAD_PATH):
            self.autoload_saved = self.autoload.get()

        # Update the last loaded value
        self.last_saved = config_path

        # Save the config data
        self.app.write_config()
        config.save_config(config_path)

        # Update button states
        self.update_buttons()

    def config_load(self):
        """Load from the config path"""
        config_path = self.config_path.get()

        # Load config
        config.load_config(config_path)
        self.app.read_config()

        # Update last saved
        self.last_saved = config_path
        self.update_buttons()

    def update_buttons(self, *_):
        """Called to update the state of the load button and check"""
        config_path = self.config_path.get()

        # Disable load if it isn't a file
        if path.isfile(config_path):
            self.load_button.state(["!disabled"])
        else:
            self.load_button.state(["disabled"])

        # Disable autoload if it isn't the autoload config
        if samefile_safe(config_path, config.AUTOLOAD_PATH):
            # Enable the check
            self.load_check.state(["!disabled"])

            # Update the unsaved marker
            if self.autoload.get() == self.autoload_saved:
                self.load_check["text"] = "Load on Start"
            else:
                self.load_check["text"] = "Load on Start*"

        else:
            # Disable the check
            self.load_check.state(["disabled"])

            # Change the check to the saved state
            self.load_check["text"] = "Load on Start"
            self.autoload.set(bool(self.autoload_saved))  # TODO Error here

        # Disable save if it isn't a valid directory
        if path.isdir(path.dirname(config_path)):
            self.save_button.state(["!disabled"])
        else:
            self.save_button.state(["disabled"])
        return True


def samefile_safe(path1, path2):
    """
    Checks if two files are the same, catching errors. If an error
    occurs, eg. because one file doesn't exist, None will be returned.

    May not work correctly with symlinks.
    """
    try:
        return path.samefile(path1, path2)
    except OSError:
        return None


class AssetSettings(ttk.Frame):
    """Handles the Assets tab of settings"""

    def __init__(self, app, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.app = app

        integ_frame = ttk.Labelframe(self, text="Integrity", padding=5)
        worker_frame = ttk.Labelframe(self, text="Workers", padding=5)
        svg_frame = ttk.Labelframe(self, text="SVGs", padding=5)
        mp3_frame = ttk.Labelframe(self, text="MP3s", padding=5)

        self.verify_assets = tk.BooleanVar(app, name="VERIFY_ASSETS")
        self.reconvert_images = tk.BooleanVar(app, name="RECONVERT_IMAGES")
        self.reconvert_sounds = tk.BooleanVar(app, name="RECONVERT_SOUNDS")

        verify_check = ttk.Checkbutton(
            integ_frame, text="Verify Assets", variable=self.verify_assets)
        re_images_check = ttk.Checkbutton(
            integ_frame, text="Reconvert Images",
            variable=self.reconvert_images)
        re_sounds_check = ttk.Checkbutton(
            integ_frame, text="Reconvert Sounds",
            variable=self.reconvert_sounds)

        self.download_workers = tk.IntVar(app, name="DOWNLOAD_THREADS")
        self.convert_workers = tk.IntVar(app, name="CONVERT_THREADS")
        self.convert_timeout = tk.IntVar(app, name="CONVERT_TIMEOUT")

        dw_workers_label = ttk.Label(worker_frame, text="Download Workers:")
        dw_workers_spin = ttk.Spinbox(
            worker_frame, textvariable=self.download_workers)
        cv_workers_label = ttk.Label(worker_frame, text="Convert Workers:")
        self.cv_workers_spin = ttk.Spinbox(
            worker_frame, textvariable=self.convert_workers)
        timout_label = ttk.Label(worker_frame, text="Timeout (seconds):")
        timeout_spin = ttk.Spinbox(
            worker_frame, textvariable=self.convert_timeout)

        self.use_svg_cmd = tk.BooleanVar(app, name="USE_SVG_CMD")
        self.svg_command = tk.StringVar(app, name="SVG_COMMAND")
        self.svg_scale = tk.IntVar(app, name="SVG_SCALE")
        self.convert_costumes = tk.BooleanVar(app, name="CONVERT_COSTUMES")

        svg_cairo_box = ttk.Checkbutton(
            svg_frame, text="Use SVG Command",
            variable=self.use_svg_cmd, command=self.cairo_toggle)
        svg_comm_label = ttk.Label(svg_frame, text="Convert Command:")
        self.svg_comm_box = ttk.Entry(svg_frame, textvariable=self.svg_command)
        svg_scale_label = ttk.Label(svg_frame, text="Converted Scale:")
        svg_scale_spin = ttk.Spinbox(svg_frame, from_=1, to=128, width=7,
                                     textvariable=self.svg_scale)
        convert_svg_check = ttk.Checkbutton(svg_frame, text="Convert costumes",
                                            variable=self.convert_costumes)

        self.mp3_command = tk.StringVar(app, name="MP3_COMMAND")
        self.convert_sounds = tk.BooleanVar(app, name="CONVERT_SOUNDS")

        mp3_comm_label = ttk.Label(mp3_frame, text="Convert Command:")
        mp3_comm_box = ttk.Entry(mp3_frame, textvariable=self.mp3_command)
        convert_mp3_check = ttk.Checkbutton(mp3_frame, text="Convert sounds",
                                            variable=self.convert_sounds)

        verify_check.grid(column=0, row=0, sticky="W")
        re_images_check.grid(column=0, row=1, sticky="W")
        re_sounds_check.grid(column=0, row=2, sticky="W")

        dw_workers_label.grid(column=0, row=0, sticky="W")
        dw_workers_spin.grid(column=1, row=0, sticky="W", padx=3, pady=3)
        cv_workers_label.grid(column=0, row=1, sticky="W")
        self.cv_workers_spin.grid(column=1, row=1, sticky="W", padx=3, pady=3)
        timout_label.grid(column=0, row=2, sticky="W")
        timeout_spin.grid(column=1, row=2, sticky="W", padx=3, pady=3)

        svg_cairo_box.grid(column=0, row=0, sticky="W")
        svg_comm_label.grid(column=0, row=1, sticky="W")
        self.svg_comm_box.grid(column=1, row=1, sticky="EW", padx=3, pady=3)
        svg_scale_label.grid(column=0, row=2, sticky="W")
        svg_scale_spin.grid(column=1, row=2, sticky="W", padx=3, pady=3)
        convert_svg_check.grid(column=0, row=3, columnspan=2,
                               sticky="W", padx=3, pady=3)

        mp3_comm_label.grid(column=0, row=0, sticky="W")
        mp3_comm_box.grid(column=1, row=0, sticky="EW", padx=3, pady=3)
        convert_mp3_check.grid(column=0, row=2, columnspan=2,
                               sticky="W", padx=3, pady=3)

        integ_frame.grid(column=0, row=0, sticky="NEW")
        worker_frame.grid(column=0, row=1, sticky="NEW")
        svg_frame.grid(column=0, row=2, sticky="NEW")
        mp3_frame.grid(column=0, row=3, sticky="NEW")

        integ_frame.columnconfigure(1, weight=1)
        worker_frame.columnconfigure(1, weight=1)
        svg_frame.columnconfigure(1, weight=1)
        mp3_frame.columnconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)

    def cairo_toggle(self):
        """Called when USE_SVG_CMD is toggled"""
        if self.use_svg_cmd.get():
            self.svg_comm_box.state(["!disabled"])
        else:
            self.svg_comm_box.state(["disabled"])


class OptimizationSettings(ttk.Frame):
    """Handles the Optimizations tab of settings"""

    def __init__(self, app, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.app = app

        toggle_frame = ttk.LabelFrame(self, text="Toggles", padding=5)
        compat_frame = ttk.LabelFrame(self, text="Compatibility", padding=5)
        adv_frame = ttk.LabelFrame(self, text="Advanced Casting", padding=5)

        self.static_lists = tk.BooleanVar(app, name="LIST_TYPES")
        self.var_types = tk.BooleanVar(app, name="VAR_TYPES")
        self.arg_types = tk.BooleanVar(app, name="ARG_TYPES")
        self.solo_broadcasts = tk.BooleanVar(app, name="SOLO_BROADCASTS")
        self.warp_all = tk.BooleanVar(app, name="WARP_ALL")

        var_check = ttk.Checkbutton(
            toggle_frame, text="Variable Type Guessing", variable=self.var_types)
        arg_check = ttk.Checkbutton(
            toggle_frame, text="CB Arg Type Guessing", variable=self.arg_types)
        static_check = ttk.Checkbutton(
            toggle_frame, text="Static Lists", variable=self.static_lists)
        solo_check = ttk.Checkbutton(
            toggle_frame, text="Solo Broadcast Detection",
            variable=self.solo_broadcasts)
        warp_check = ttk.Checkbutton(
            toggle_frame, text="Warp All (Not Recommended)", variable=self.warp_all)

        self.legacy_lists = tk.BooleanVar(app, name="LEGACY_LISTS")
        self.disable_int = tk.BooleanVar(app, name="DISABLE_INT_CAST")

        legacy_check = ttk.Checkbutton(
            compat_frame, text="Legacy Lists", variable=self.legacy_lists)
        dint_check = ttk.Checkbutton(
            compat_frame, text="Disable Int Cast", variable=self.disable_int)

        self.disable_any = tk.BooleanVar(app, name="DISABLE_ANY_CAST")
        self.aggressive_num = tk.BooleanVar(app, name="AGGRESSIVE_NUM_CAST")
        self.changed_num = tk.BooleanVar(app, name="CHANGED_NUM_CAST")
        self.disable_str = tk.BooleanVar(app, name="DISABLE_STR_CAST")

        dany_check = ttk.Checkbutton(
            adv_frame, text="Disable Any Cast", variable=self.disable_any)
        dstr_check = ttk.Checkbutton(
            adv_frame, text="Relaxed Str Cast", variable=self.disable_str)
        changed_check = ttk.Checkbutton(
            adv_frame, text="Changed Var Cast", variable=self.changed_num)
        aggressive_check = ttk.Checkbutton(
            adv_frame, text="Aggressive Num Cast",
            variable=self.aggressive_num)

        var_check.grid(column=0, row=0, sticky="W")
        arg_check.grid(column=0, row=1, sticky="W")
        static_check.grid(column=0, row=2, sticky="W")
        solo_check.grid(column=0, row=3, sticky="W")
        warp_check.grid(column=0, row=4, sticky="W")

        legacy_check.grid(column=0, row=3, sticky="W")
        dint_check.grid(column=0, row=4, sticky="W")

        dany_check.grid(column=0, row=0, sticky="W")
        dstr_check.grid(column=0, row=1, sticky="W")
        aggressive_check.grid(column=0, row=2, sticky="W")
        changed_check.grid(column=0, row=3, sticky="W")

        toggle_frame.grid(column=0, row=0, sticky="NSEW")
        compat_frame.grid(column=0, row=1, sticky="NSEW")
        adv_frame.grid(column=0, row=2, sticky="NSEW")

        toggle_frame.columnconfigure(0, weight=1)
        compat_frame.columnconfigure(0, weight=1)
        adv_frame.columnconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)


class ProjectFrame(ttk.Frame):
    """Handles the Project tab of settings"""

    def __init__(self, app, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.app = app

        timing_frame = ttk.LabelFrame(self, text="Timings", padding=5)
        display_frame = ttk.LabelFrame(self, text="Display", padding=5)
        title_frame = ttk.LabelFrame(self, text="Title", padding=5)
        audio_frame = ttk.LabelFrame(self, text="Audio", padding=5)
        limits_frame = ttk.LabelFrame(self, text="Limits", padding=5)
        hotkey_frame = ttk.LabelFrame(self, text="Hotkeys", padding=5)
        misc_frame = ttk.LabelFrame(self, text="Miscellaneous", padding=5)

        self.target_fps = tk.IntVar(app, name="TARGET_FPS")
        self.turbo_mode = tk.BooleanVar(app, name="TURBO_MODE")
        self.iwork_time = tk.IntVar(app, name="WORK_TIME_INV")
        self.warp_time = tk.IntVar(app, name="WARP_TIME")

        fps_label = ttk.Label(timing_frame, text="Target FPS:")
        fps_spin = ttk.Spinbox(timing_frame, from_=1, to=9999, width=7,
                               textvariable=self.target_fps)
        turbo_check = ttk.Checkbutton(
            timing_frame, text="Turbo Mode", variable=self.turbo_mode)
        warp_label = ttk.Label(timing_frame, text="Warp Time (s):")
        warp_spin = ttk.Spinbox(timing_frame, from_=0, to_=20000, width=7,
                                increment=0.1, textvariable=self.warp_time)
        work_label = ttk.Label(timing_frame, text="Work Time (1/s):")
        work_spin = ttk.Spinbox(timing_frame, from_=1, to_=9999, width=7,
                                textvariable=self.iwork_time)

        self.stage_width = tk.IntVar(app, name="STAGE_WIDTH")
        self.stage_height = tk.IntVar(app, name="STAGE_HEIGHT")
        self.display_width = tk.IntVar(app, name="DISPLAY_WIDTH")
        self.display_height = tk.IntVar(app, name="DISPLAY_HEIGHT")
        self.allow_resize = tk.BooleanVar(app, name="ALLOW_RESIZE")
        self.scaled_display = tk.BooleanVar(app, name="SCALED_DISPLAY")
        self.fs_scale = tk.IntVar(app, name="FS_SCALE")
        self.iflip_threshold = tk.IntVar(app, name="FLIP_THRESHOLD_INV")

        stage_label = ttk.Label(display_frame, text="Stage Size:")
        stagew_spin = ttk.Spinbox(
            display_frame, from_=1, to=9999, width=7,
            textvariable=self.stage_width)
        stageh_spin = ttk.Spinbox(
            display_frame, from_=1, to=9999, width=7,
            textvariable=self.stage_height)
        display_label = ttk.Label(display_frame, text="Display Size:")
        displayw_spin = ttk.Spinbox(
            display_frame, from_=1, to=9999, width=7,
            textvariable=self.display_width)
        displayh_spin = ttk.Spinbox(
            display_frame, from_=1, to=9999, width=7,
            textvariable=self.display_height)
        resize_check = ttk.Checkbutton(
            display_frame, text="Resizable Display",
            variable=self.allow_resize)
        scaled_check = ttk.Checkbutton(
            display_frame, text="Scaled Display",
            variable=self.scaled_display, state="!enabled")
        fs_label = ttk.Label(display_frame, text="Fullscreen Scale:")
        fs_spin = ttk.Spinbox(
            display_frame, from_=1, to=128, width=7,
            textvariable=self.fs_scale)
        flip_label = ttk.Label(display_frame, text="Flip Threshold (1/s):")
        flip_spin = ttk.Spinbox(
            display_frame, from_=1, to=9999, width=7,
            textvariable=self.iflip_threshold)

        self.title_text = tk.StringVar(app, name="TITLE")
        self.dynamic_title = tk.BooleanVar(app, name="DYNAMIC_TITLE")

        title_label = ttk.Label(title_frame, text="Title Text:")
        title_box = ttk.Entry(title_frame, textvariable=self.title_text)
        title_check = ttk.Checkbutton(
            title_frame, text="Dynamic Title",
            variable=self.dynamic_title)

        self.audio_channels = tk.IntVar(app, name="AUDIO_CHANNELS")
        self.master_volume = tk.IntVar(app, name="MASTER_VOLUME")

        channels_label = ttk.Label(audio_frame, text="Mixer Channels:")
        channels_spin = ttk.Spinbox(
            audio_frame, from_=1, to=9999, width=7,
            textvariable=self.audio_channels)
        volume_label = ttk.Label(audio_frame, text="Master Volume:")
        volume_spin = ttk.Spinbox(
            audio_frame, from_=0, to=100, width=7,
            textvariable=self.master_volume)

        self.max_clones = tk.IntVar(app, name="MAX_CLONES")
        self.clone_limit = tk.BooleanVar(value=True)
        self.max_list = tk.IntVar(app, name="MAX_LIST")
        self.list_limit = tk.BooleanVar(value=True)

        clones_label = ttk.Label(limits_frame, text="Clone Limit:")
        self.clones_spin = ttk.Spinbox(
            limits_frame, from_=0, to=9999, width=10,
            textvariable=self.max_clones)
        clones_check = ttk.Checkbutton(
            limits_frame, text="Enable?",
            variable=self.clone_limit, command=self.toggle_clones)
        list_label = ttk.Label(limits_frame, text="List Limit:")
        self.list_spin = ttk.Spinbox(
            limits_frame, from_=0, to=999999999, width=10,
            textvariable=self.max_list)
        list_check = ttk.Checkbutton(
            limits_frame, text="Enable?",
            variable=self.list_limit, command=self.toggle_list)

        self.turbo_hotkey = tk.BooleanVar(app, name="TURBO_HOTKEY")
        self.fullscreen_hotkey = tk.BooleanVar(app, name="FULLSCREEN_HOTKEY")
        self.debug_hotkeys = tk.BooleanVar(app, name="DEBUG_HOTKEYS")

        turbo_hk_check = ttk.Checkbutton(
            hotkey_frame, text="Turbo Hotkey (F10)",
            variable=self.turbo_hotkey)
        fullscreen_check = ttk.Checkbutton(
            hotkey_frame, text="Fullscreen Hotkey (F11)",
            variable=self.fullscreen_hotkey)
        debug_check = ttk.Checkbutton(
            hotkey_frame, text="Debug Hotkeys (F3 + F,R,S,P)",
            variable=self.debug_hotkeys)

        self.username = tk.StringVar(app, name="USERNAME")
        self.draw_fps = tk.BooleanVar(app, name="DRAW_FPS")
        self.random_seed = tk.IntVar(app, name="RANDOM_SEED")

        username_label = ttk.Label(misc_frame, text="Username:")
        username_box = ttk.Entry(misc_frame, textvariable=self.username)
        random_label = ttk.Label(misc_frame, text="Random Seed:")
        random_spin = ttk.Spinbox(
            misc_frame, from_=0, to=99999, width=7,
            textvariable=self.random_seed)
        fps_check = ttk.Checkbutton(
            misc_frame, text="Draw FPS",
            variable=self.draw_fps)

        fps_label.grid(column=0, row=0, sticky="W")
        fps_spin.grid(column=2, row=0, sticky="W", padx=3, pady=3)
        turbo_check.grid(column=3, row=0, sticky="W", padx=3)
        warp_label.grid(column=0, row=1, sticky="W")
        warp_spin.grid(column=2, row=1, sticky="W", padx=3, pady=3)
        work_label.grid(column=0, row=2, sticky="W")
        work_spin.grid(column=2, row=2, sticky="W", padx=3, pady=3)

        stage_label.grid(column=0, row=0, sticky="W")
        stagew_spin.grid(column=1, row=0, sticky="W",
                         padx=3, pady=3, columnspan=2)
        stageh_spin.grid(column=3, row=0, sticky="W", padx=3, pady=3)
        display_label.grid(column=0, row=1, sticky="W")
        displayw_spin.grid(column=1, row=1, sticky="W",
                           padx=3, pady=3, columnspan=2)
        displayh_spin.grid(column=3, row=1, sticky="W", padx=3, pady=3)
        resize_check.grid(column=0, row=2, sticky="W", columnspan=2)
        scaled_check.grid(column=0, row=3, sticky="W", columnspan=2)
        fs_label.grid(column=0, row=4, sticky="W", columnspan=2)
        fs_spin.grid(column=2, row=4, sticky="W", padx=3, pady=3, columnspan=2)
        flip_label.grid(column=0, row=5, sticky="W", columnspan=2)
        flip_spin.grid(column=2, row=5, sticky="W",
                       padx=3, pady=3, columnspan=2)
        scaled_check.state(["disabled"])

        title_label.grid(column=0, row=0, sticky="W")
        title_box.grid(column=1, row=0, sticky="EW", padx=3, pady=3)
        title_check.grid(column=0, row=1, sticky="W", columnspan=2)

        channels_label.grid(column=0, row=0, sticky="W")
        channels_spin.grid(column=1, row=0, sticky="W", padx=3, pady=3)
        volume_label.grid(column=0, row=1, sticky="W")
        volume_spin.grid(column=1, row=1, sticky="W", padx=3, pady=3)

        clones_label.grid(column=0, row=0, sticky="W")
        self.clones_spin.grid(column=1, row=0, sticky="W", padx=3, pady=3)
        clones_check.grid(column=2, row=0, sticky="W", padx=3)
        list_label.grid(column=0, row=1, sticky="W")
        self.list_spin.grid(column=1, row=1, sticky="W", padx=3, pady=3)
        list_check.grid(column=2, row=1, sticky="W", padx=3)

        turbo_hk_check.grid(column=0, row=0, sticky="W")
        fullscreen_check.grid(column=0, row=1, sticky="W")
        debug_check.grid(column=0, row=2, sticky="W")

        username_label.grid(column=0, row=0, sticky="W")
        username_box.grid(column=1, row=0, sticky="EW", padx=3, pady=3)
        random_label.grid(column=0, row=1, sticky="W")
        random_spin.grid(column=1, row=1, sticky="W", padx=3, pady=3)
        fps_check.grid(column=0, row=2, sticky="W", columnspan=2)

        timing_frame.grid(column=0, row=0, sticky="NSEW", padx=3)
        display_frame.grid(column=1, row=0, sticky="NSEW", padx=3, rowspan=2)
        title_frame.grid(column=0, row=1, sticky="NSEW", padx=3, columnspan=1)
        audio_frame.grid(column=0, row=3, sticky="NSEW", padx=3)
        limits_frame.grid(column=1, row=3, sticky="NSEW", padx=3)
        hotkey_frame.grid(column=0, row=4, sticky="NSEW", padx=3)
        misc_frame.grid(column=1, row=4, sticky="NSEW", padx=3)

        timing_frame.columnconfigure(3, weight=1)
        display_frame.columnconfigure(4, weight=1)
        title_frame.columnconfigure(1, weight=1)
        audio_frame.columnconfigure(1, weight=1)
        limits_frame.columnconfigure(2, weight=1)
        hotkey_frame.columnconfigure(1, weight=1)
        misc_frame.columnconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def toggle_clones(self):
        """Toggles the clone limit"""
        if self.clone_limit.get():
            self.max_clones.set(config.project.MAX_CLONES)
            self.clones_spin.state(['!disabled'])
        else:
            self.max_clones.set(0)
            self.clones_spin.state(['disabled'])

    def toggle_list(self):
        """Toggles the clone limit"""
        if self.list_limit.get():
            self.max_list.set(config.project.MAX_LIST)
            self.list_spin.state(['!disabled'])
        else:
            self.max_list.set(0)
            self.list_spin.state(['disabled'])

    def switch(self):
        """Called when this tab is switched to"""
        if self.max_list.get():
            self.list_spin.state(['!disabled'])
        if self.max_clones.get():
            self.clones_spin.state(['!disabled'])


class DebugFrame(ttk.Frame):
    """Handles the Debug tab of settings"""

    def __init__(self, app, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.app = app

        debug_frame = ttk.Labelframe(self, text="Debug", padding=5)
        log_frame = ttk.Labelframe(self, text="Logging", padding=5)

        self.debug_json = tk.BooleanVar(app, name="DEBUG_JSON")
        self.format_json = tk.BooleanVar(app, name="FORMAT_JSON")
        self.overwrite_engine = tk.BooleanVar(app, name="OVERWRITE_ENGINE")

        d_json_check = ttk.Checkbutton(
            debug_frame, text="Save project.json",
            variable=self.debug_json, command=self.json_toggle)
        self.f_json_check = ttk.Checkbutton(
            debug_frame, text="Format project.json",
            variable=self.format_json)
        engine_check = ttk.Checkbutton(
            debug_frame, text="Overwrite Engine",
            variable=self.overwrite_engine)

        self.log_level = tk.StringVar(app, name="LOG_LEVEL")
        self.log_path = tk.StringVar(app, name="LOG_PATH")
        self.save_log = tk.StringVar(app, name="SAVE_LOG")

        level_label = ttk.Label(log_frame, text="Log Level:")
        level_spin = ttk.Spinbox(log_frame, from_=10, to=50, increment=10,
                                 textvariable=self.log_level, width=7)
        path_label = ttk.Label(log_frame, text="Log Path:")
        path_box = ttk.Entry(
            log_frame, textvariable=self.log_path, state="disabled")
        save_box = ttk.Checkbutton(log_frame, text="Save Log", state="disabled",
                                   variable=self.save_log)

        d_json_check.grid(column=0, row=0, sticky="W")
        self.f_json_check.grid(column=0, row=1, sticky="W")
        engine_check.grid(column=0, row=2, sticky="W")

        level_label.grid(column=0, row=0, sticky="W")
        level_spin.grid(column=1, row=0, sticky="W", padx=3, pady=3)
        path_label.grid(column=0, row=1, sticky="W")
        path_box.grid(column=1, row=1, sticky="EW", padx=3, pady=3)
        save_box.grid(column=0, row=2, sticky="W", columnspan=2)

        debug_frame.grid(column=0, row=0, stick="NSEW")
        debug_frame.columnconfigure(0, weight=1)

        log_frame.grid(column=0, row=1, sticky="NSEW")
        log_frame.columnconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)

    def json_toggle(self):
        """Called when save project.json is toggled"""
        if self.debug_json.get():
            self.f_json_check.state(["!disabled"])
        else:
            self.f_json_check.state(["disabled"])

    switch = json_toggle

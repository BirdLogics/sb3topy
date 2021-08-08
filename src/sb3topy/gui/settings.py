"""
settings.py

Contains the Settings tab of the gui
"""

import tkinter as tk
from tkinter import ttk


class SettingsFrame(ttk.Frame):
    """Handles the Settings tab"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.app = parent

        notebook = ttk.Notebook(self)

        disp_tab = ttk.Frame(notebook, padding="3 5 5 5")
        gen_tab = ttk.Frame(notebook, padding="3 5 5 5")

        notebook.add(gen_tab, text="General")
        notebook.add(disp_tab, text="Display")

        # General tab
        # Timings
        time_frame = ttk.Labelframe(gen_tab, text='Timings')

        self.target_fps = tk.StringVar(value=31)
        fps_label = ttk.Label(time_frame, text="Target FPS:")
        fps_spin = ttk.Spinbox(time_frame, from_=0, to=9999, width=7,
                               textvariable=self.target_fps)

        self.turbo_mode = tk.BooleanVar(value=False)
        turbo_check = ttk.Checkbutton(time_frame, text="Turbo mode",
                                      variable=self.turbo_mode)

        self.warp_time = tk.StringVar(value=0.5)
        warp_label = ttk.Label(time_frame, text="Warp time:")
        warp_spin = ttk.Spinbox(
            time_frame, from_=0.0, to=999.0, increment=0.1,
            width=7, textvariable=self.warp_time)

        self.work_time = tk.StringVar(value=60)
        work_label = ttk.Label(time_frame, text="Work time:    1/")
        work_spin = ttk.Spinbox(time_frame, from_=1, to=999, width=7,
                                textvariable=self.work_time)

        self.flip_thresh = tk.StringVar(value=25)
        flip_label = ttk.Label(time_frame, text="Flip threshold:")
        flip_spin = ttk.Spinbox(time_frame, from_=0, to=999, width=7,
                                textvariable=self.flip_thresh)

        # Audio
        audio_frame = ttk.LabelFrame(gen_tab, text="Audio")

        self.channels = tk.StringVar(value=16)
        channels_label = ttk.Label(audio_frame, text="Mixer channels:")
        channels_spin = ttk.Spinbox(audio_frame, from_=0, to=999, width=7,
                                    textvariable=self.channels)

        self.volume = tk.StringVar(value=100)
        volume_label = ttk.Label(audio_frame, text="Master volume:")
        volume_spin = ttk.Spinbox(audio_frame, from_=0, to=100, width=7,
                                  textvariable=self.volume)

        # Misc
        misc_frame = ttk.LabelFrame(gen_tab, text="Misc")

        self.clone_limit = tk.StringVar(value=300)
        clones_label = ttk.Label(misc_frame, text="Clone limit:")
        clones_spin = ttk.Spinbox(misc_frame, from_=0, to=99999, width=7,
                                  textvariable=self.clone_limit)

        self.list_limit = tk.BooleanVar(value=True)
        list_check = ttk.Checkbutton(misc_frame, text="List limit",
                                     variable=self.list_limit)

        # Display tab
        self.display_width = tk.StringVar(value=480)
        self.display_height = tk.StringVar(value=360)
        display_label = ttk.Label(disp_tab, text="Display size:")
        displayw_spin = ttk.Spinbox(disp_tab, from_=120, to=4800, width=7,
                                    textvariable=self.display_width)
        displayh_spin = ttk.Spinbox(disp_tab, from_=90, to=3600, width=7,
                                    textvariable=self.display_height)

        self.stage_width = tk.StringVar(value=480)
        self.stage_height = tk.StringVar(value=360)
        stage_label = ttk.Label(disp_tab, text="Stage size:")
        stagew_spin = ttk.Spinbox(disp_tab, from_=120, to=4800, width=7,
                                  textvariable=self.stage_width)
        stageh_spin = ttk.Spinbox(disp_tab, from_=90, to=3600, width=7,
                                  textvariable=self.stage_height)

        self.allow_resize = tk.BooleanVar(value=True)
        self.scaled_display = tk.BooleanVar(value=True)
        resize_check = ttk.Checkbutton(disp_tab, text="Resizable display",
                                       variable=self.allow_resize)
        scaled_check = ttk.Checkbutton(disp_tab, text="Scaled display",
                                       variable=self.scaled_display)

        self.title_text = tk.StringVar(
            value="project.py (fps: {FPS:.2f}{TURBO})")
        self.dynamic_title = tk.BooleanVar(value=True)
        title_label = ttk.Label(disp_tab, text="Title:")
        title_box = ttk.Entry(disp_tab, textvariable=self.title_text)
        title_check = ttk.Checkbutton(disp_tab, text="Dynamic title",
                                      variable=self.dynamic_title)

        # Grid everything
        notebook.grid(sticky='NSEW')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Grid general
        # Timings
        time_frame.grid(column=0, row=0, columnspan=3, sticky='NSEW')

        fps_label.grid(column=0, row=0, pady=3, sticky='W')
        fps_spin.grid(column=1, row=0, pady=3, sticky='W')
        turbo_check.grid(column=3, row=0, pady=3, padx=5, sticky='W')

        warp_label.grid(column=0, row=2, pady=3, sticky='W')
        warp_spin.grid(column=1, row=2, pady=3, sticky='W')

        work_label.grid(column=0, row=3, pady=3, sticky='W')
        work_spin.grid(column=1, row=3, pady=3, sticky='W')

        flip_label.grid(column=0, row=4, pady=3, columnspan=1, sticky='W')
        flip_spin.grid(column=1, row=4, pady=3, sticky='W')

        # Mixer
        audio_frame.grid(column=0, row=1, sticky="NSEW")

        channels_label.grid(column=0, row=0, pady=3, padx=(0, 5),
                            sticky='W')
        channels_spin.grid(column=1, row=0, pady=3, sticky='W')

        volume_label.grid(column=0, row=1, pady=3, sticky='W')
        volume_spin.grid(column=1, row=1, pady=3, sticky='W')

        # Misc
        misc_frame.grid(column=0, row=2, sticky="NSEW")

        clones_label.grid(column=0, row=0, sticky='W')
        clones_spin.grid(column=1, row=0, padx=3, sticky='W')

        list_check.grid(column=0, row=1, columnspan=2, pady=3, sticky='W')

        gen_tab.columnconfigure(0, weight=1)
        # gen_tab.rowconfigure(0, weight=1)

        # Grid display

        display_label.grid(column=0, row=1, pady=3, sticky='W')
        displayh_spin.grid(column=1, row=1, pady=3, padx=3, sticky='W')
        displayw_spin.grid(column=2, row=1, pady=3, padx=3, sticky='W')

        stage_label.grid(column=0, row=2, pady=3, sticky='W')
        stageh_spin.grid(column=1, row=2, pady=3, padx=3, sticky='W')
        stagew_spin.grid(column=2, row=2, pady=3, padx=3, sticky='W')

        title_label.grid(column=0, row=3, pady=3, sticky='W')
        title_box.grid(column=1, row=3, pady=3, columnspan=4, sticky='EW')

        title_check.grid(column=0, row=4, pady=5, columnspan=3, sticky='W')
        resize_check.grid(column=0, row=5, pady=5, columnspan=3, sticky='W')
        scaled_check.grid(column=0, row=6, pady=5, columnspan=3, sticky='W')

        disp_tab.columnconfigure(2, weight=1)

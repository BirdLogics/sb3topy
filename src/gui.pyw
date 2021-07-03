"""

"""

import json
import queue
import subprocess
import threading
import time
import tkinter as tk
from tkinter import filedialog, ttk

FORMATS = {
    '[DEBUG]': "debug",
    '[INFO]': "info",
    '[WARNING]': "warn",
    '[ERROR]': "error",
    '[CRITICAL]': "critical"
}

# TODO Scaling for 4k displays
# from ctypes import windll
# windll.shcore.SetProcessDpiAwareness(True)
# self.tk.call('tk', 'scaling', 4.0)


class Task:
    """
    Runs a task in a new process and creates
    a thread to read its output without blocking.

    queue - Holds lines read from the subprocess
    popen - Holds the Popen subprocess
    thread - Holds the thread watching the subprocess
    """

    def __init__(self):
        self.queue = queue.Queue()
        self.popen = None
        self.thread = None

    def start(self, cmd):
        """Start the task with a command"""
        # Start the subprocess
        self.popen = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)

        # Start the watching thread
        self.thread = threading.Thread(
            target=self._thread_reader,
            args=(self.popen, self.queue),
            daemon=True)
        self.thread.start()

    @staticmethod
    def _thread_reader(popen, data_queue):
        while popen.poll() is None:
            data_queue.put(popen.stdout.readline())

    def read_queue(self):
        """Returns the string data on the queue"""
        data = ""
        while not self.queue.empty():
            try:
                data = data + self.queue.get_nowait().decode('utf-8')
            except queue.Empty:
                break
        return data or None

    def kill_task(self):
        """Terminates the task. The thread should follow."""
        self.popen.kill()


class ConvertFrame(ttk.Frame):
    """
    ConvertFrame

    project_path
    folder_path

    zip_path
    create_zip, overwrite_zip

    exe_path
    create_exe, overwrite_exe
    """

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="5 0 5 5")
        self.app = parent

        self.project_path = tk.StringVar()
        project_label = ttk.Label(self, text="Input Project:")
        project_box = ttk.Entry(self, textvariable=self.project_path)
        project_button = ttk.Button(
            self, text="Browse...", command=self.browse_project)

        self.folder_path = tk.StringVar()
        folder_label = ttk.Label(self, text="Output Folder:")
        folder_box = ttk.Entry(self, textvariable=self.folder_path)
        folder_button = ttk.Button(
            self, text="Browse...", command=self.browse_folder)
        # folder_button2 = ttk.Button(
        #     self, text="Create Now", command=self.delete_assets)

        convert_button = ttk.Button(
            self, text="Convert Now", command=self.convert)
        seperator = ttk.Separator(self, orient=tk.HORIZONTAL)

        self.zip_path = tk.StringVar()
        self.zip_create = tk.BooleanVar()
        self.zip_overwrite = tk.BooleanVar()
        zip_label = ttk.Label(self, text="Output zip:")
        zip_box = ttk.Entry(self, textvariable=self.zip_path)
        zip_button = ttk.Button(
            self, text="Browse...", command=self.browse_zip)
        zip_check1 = ttk.Checkbutton(
            self, text="Create zip", variable=self.zip_create)
        zip_check2 = ttk.Checkbutton(
            self, text="Allow Overwrite", variable=self.zip_overwrite)
        zip_button2 = ttk.Button(
            self, text="Export Now", command=self.create_zip)

        self.exe_path = tk.StringVar()
        self.exe_create = tk.BooleanVar()
        self.exe_overwrite = tk.BooleanVar()
        exe_label = ttk.Label(self, text="Output exe:")
        exe_box = ttk.Entry(self, textvariable=self.exe_path)
        exe_button = ttk.Button(
            self, text="Browse...", command=self.browse_exe)
        exe_check1 = ttk.Checkbutton(
            self, text="Create exe", variable=self.exe_create)
        exe_check2 = ttk.Checkbutton(
            self, text="Allow Overwrite", variable=self.exe_overwrite)
        exe_button2 = ttk.Button(
            self, text="Export Now", command=self.create_exe)

        # Grid everything
        project_label.grid(column=0, row=0, sticky="W")
        project_box.grid(column=0, row=1, columnspan=2, sticky="WE")
        project_button.grid(column=2, row=1, sticky="WE", padx=(5, 0))

        folder_label.grid(column=0, row=2, sticky="W", pady=(10, 0))
        folder_box.grid(column=0, row=3, columnspan=2, sticky="WE")
        folder_button.grid(column=2, row=3, sticky="WE", padx=(5, 0))

        convert_button.grid(column=2, row=4, columnspan=1,
                            sticky="WE", pady=(0, 5), padx=(5, 0))
        seperator.grid(column=0, row=5, columnspan=3, sticky="WE")

        zip_label.grid(column=0, row=6, sticky="W")
        zip_box.grid(column=0, row=7, columnspan=2, sticky="WE")
        zip_button.grid(column=2, row=7, sticky="WE", padx=(5, 0))
        zip_check1.grid(column=0, row=8, sticky="W")
        zip_check2.grid(column=1, row=8, sticky="W")
        zip_button2.grid(column=2, row=8, sticky="WE", padx=(5, 0))

        exe_label.grid(column=0, row=9, sticky="W", pady=(10, 0))
        exe_box.grid(column=0, row=10, columnspan=2, sticky="WE")
        exe_button.grid(column=2, row=10, sticky="WE", padx=(5, 0))
        exe_check1.grid(column=0, row=11, sticky="W")
        exe_check2.grid(column=1, row=11, sticky="W")
        exe_button2.grid(column=2, row=11, sticky="WE", padx=(5, 0))

        self.columnconfigure(1, weight=1)

    def browse_project(self):
        """Show a dialog to select the project file"""
        path = filedialog.askopenfilename(
            filetypes=[("Project Files", "*.sb3;*.zip"),
                       ("All Files", "*.*")])
        if path:
            self.project_path.set(path)

    def browse_folder(self):
        """Show a dialog to select the output folder"""
        self.folder_path.set(filedialog.askdirectory())

    def convert(self):
        """Run the converter"""
        self.app.run_main()

    def delete_assets(self):
        """Clear the contents of the assets folder"""

    def browse_zip(self):
        """Show a dialog to select the output zip path"""
        path = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("ZIP Files", "*.zip"),
                       ("All Files", "*.*")])
        if path:
            self.zip_path.set(path)

    def create_zip(self):
        """Create a zip from the last conversion"""

    def browse_exe(self):
        """Show a dialog to select the output exe path"""
        path = filedialog.asksaveasfilename(
            defaultextension=".exe",
            filetypes=[("EXE Files", "*.exe"),
                       ("All Files", "*.*")])
        if path:
            self.exe_path.set(path)

    def create_exe(self):
        """Create a zip from the last conversion"""


class OutputFrame(ttk.Frame):
    """Handles the Output tab, logging"""

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="5 0 5 5")

        self.text = tk.Text(self, width=32, height=17.5, state="disabled")
        scroll = ttk.Scrollbar(self, orient="vertical",
                               command=self.text.yview)
        self.text['yscrollcommand'] = scroll.set

        self.show_info = tk.BooleanVar(value=True)
        self.show_debug = tk.BooleanVar()
        verbose_check = ttk.Checkbutton(
            self, text="Verbose Ouput",
            variable=self.show_info, command=self.info_tag)
        debug_check = ttk.Checkbutton(
            self, text="Debug Ouput",
            variable=self.show_debug, command=self.debug_tag)

        export_button = ttk.Button(
            self, text="Export Log...", command=self.export_log)

        # Grid everything
        self.text.grid(column=0, row=0, columnspan=4,
                       sticky="NSEW", pady=5)
        scroll.grid(column=4, row=0, sticky="NS", pady=5)

        verbose_check.grid(column=0, row=1, sticky="NSW")
        debug_check.grid(column=1, row=1, sticky="NSW", padx=15)

        export_button.grid(row=1, column=3, sticky="NSW")

        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)

        # Output theme
        self.font = "Courier 10"
        self.debug_tag()
        self.info_tag()
        self.text.tag_config("warn", foreground="gold", font=self.font+" bold")
        self.text.tag_config("warn_text", font=self.font)
        self.text.tag_config("error", foreground="red", font=self.font+" bold")
        self.text.tag_config("error_text", foreground="red", font=self.font)
        self.text.tag_config(
            "critical", foreground="dark red", font=self.font+" bold")
        self.text.tag_config(
            "critical_text", foreground="dark red", font=self.font+" bold")
        self.text.tag_config("default", font=self.font)
        self.text.tag_config("default_text", font=self.font)

    def log_line(self, line):
        """Display and format a line"""
        self.text["state"] = "normal"

        # Get a tag based on the first word
        keyword = line.split(' ', 1)[0]
        tag = FORMATS.get(keyword, "default")

        self.text.insert("end", keyword, (tag,))
        self.text.insert("end", line.lstrip(keyword), (tag+"_text",))

        self.text["state"] = "disabled"

    def debug_tag(self):
        """Configures debug text tags, shown/hidden"""
        value = not self.show_debug.get()
        self.text.tag_config("debug", foreground="grey",
                             font=self.font, elide=value)
        self.text.tag_config("debug_text", foreground="grey",
                             font=self.font, elide=value)
        self.text.see("end")

    def info_tag(self):
        """Configures info text tags, shown/hidden"""
        value = not self.show_info.get()
        self.text.tag_config("info", foreground="green",
                             font=self.font+" bold", elide=value)
        self.text.tag_config("info_text", font=self.font, elide=value)
        self.text.see("end")

    def export_log(self):
        """Save the current log to a file"""
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text File", "*.txt;*.log"),
                       ("All Files", "*.*")])

        with open(path, 'w') as file:
            file.write('\n'.join(
                self.text.get('1.0', 'end').splitlines()
            ))


class SettingsFrame(ttk.Frame):
    """Handles the Settings tab"""

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="5 0 5 5")
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


class FlatRadio(ttk.Label):
    """A custom flat radio button"""

    def __init__(self, parent, text, variable, **args):
        ttk.Label.__init__(
            self, parent, text=text,
            style="FlatRadio.TLabel", **args)
        self.value = text.lower()
        self.variable = variable

        variable.trace_add("write", self.cb_variable)
        self.bind("<Enter>", self.mouse_enter)
        self.bind("<Leave>", self.mouse_leave)
        self.bind("<Button-1>", self.mouse_click)

    def mouse_enter(self, _):
        """Called when the mouse hovers"""
        self.state(["active"])

    def mouse_leave(self, _):
        """Called when the mouse stops hovering"""
        self.state(["!active"])

    def mouse_click(self, _):
        """Called when the mouse clicks"""
        self.variable.set(self.value)

    def cb_variable(self, name, index, operation):
        """Called when the variable is updated"""
        state = self.variable.get()
        if state == self.value:
            self.state(["selected"])
        else:
            self.state(["!selected"])


class Sidebar(ttk.Frame):
    """Handles the sidebar on the left and frames put in it"""

    def __init__(self, root, variable):
        ttk.Frame.__init__(self, root)

        style = ttk.Style(self)
        style.map(
            "FlatRadio.TLabel",
            background=[('selected', 'lightgrey'),
                        ('active', '#dfdfdf')],
            font=[('', 'TkMenuFont 14')])

        convert_button = FlatRadio(self, "Convert", variable=variable)
        output_button = FlatRadio(self, "Output", variable=variable)
        settings_button = FlatRadio(self, "Settings", variable=variable)

        convert_button.grid(column=0, row=0, sticky="NSEW")
        output_button.grid(column=0, row=1, sticky="NSEW")
        settings_button.grid(column=0, row=2, sticky="NSEW")

        self.columnconfigure(0, weight=1)


class App(tk.Tk):
    """Main App class"""

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("sb3topy")

        self.mode = tk.StringVar(self)
        self.mode.trace_add('write', self.cb_mode)

        sidebar = Sidebar(self, self.mode)
        self.convert = ConvertFrame(self)
        self.output = OutputFrame(self)
        self.settings = SettingsFrame(self)

        sidebar.grid(column=0, row=0, sticky="NSEW")
        self.convert.grid(column=1, row=0, sticky="NSWE")
        self.output.grid(column=1, row=0, sticky="NSWE")
        self.settings.grid(column=1, row=0, sticky="NSWE")

        self.columnconfigure(0, minsize=100)
        self.columnconfigure(1, minsize=300, weight=1)
        self.rowconfigure(0, minsize=300, weight=1)

        self.mode.set("convert")

        self.task = Task()
        # self.start_task("python -u junkprov.py")

        self.load_config("data/config.json")

    def cb_mode(self, *_):
        """Called when the mode switches"""
        self.convert.grid_remove()
        self.output.grid_remove()
        self.settings.grid_remove()

        mode = self.mode.get()
        if mode == "convert":
            self.convert.grid()
        elif mode == "output":
            self.output.grid()
        elif mode == "settings":
            self.settings.grid()

    def save_config(self, path):
        """Saves the config to a json file"""
        with open(path, 'r') as file:
            config = json.load(file)

        config.update(
            project_path=self.convert.project_path.get(),
            temp_folder=self.convert.folder_path.get(),

            zip_create=self.convert.zip_create.get(),
            zip_overwrite=self.convert.zip_overwrite.get(),
            zip_path=self.convert.zip_path.get(),

            exe_create=self.convert.exe_create.get(),
            exe_overwrite=self.convert.exe_overwrite.get(),
            exe_path=self.convert.exe_path.get()
        )

        with open(path, 'w') as file:
            json.dump(config, file, indent=0)

        return path

    def load_config(self, path):
        """Loads the config from a json file"""
        with open(path, 'r') as file:
            config = json.load(file)

        self.convert.project_path.set(config.get("project_path"))
        self.convert.folder_path.set(config.get("temp_folder"))

        self.convert.zip_create.set(config.get("zip_create"))
        self.convert.zip_overwrite.set(config.get("zip_overwrite"))
        self.convert.zip_path.set(config.get("zip_path"))

        self.convert.exe_create.set(config.get("exe_create"))
        self.convert.exe_overwrite.set(config.get("exe_overwrite"))
        self.convert.exe_path.set(config.get("exe_path"))

    def run_main(self, options=None):
        """Runs the converter with options"""
        self.mode.set("output")

        cmd = [
            "py", "-3.8", "-u", "main.py",
            "-c", self.save_config("data/config.json"),
            self.convert.project_path.get()
        ]
        if options:
            cmd.extend(options)

        self.output.log_line(' '.join(cmd) + "\n")
        self.start_task(cmd)

    def start_task(self, cmd):
        """Starts running a task of cmd"""
        self.task.start(cmd)
        self.after(1, self.loop)

    def end_task(self):
        """Kills the currently running task"""
        self.task.popen.kill()

    def loop(self):
        """Update the log"""
        start_time = time.monotonic()
        while not self.task.queue.empty() and \
                time.monotonic() - start_time < 0.05:
            try:
                self.output.log_line(
                    self.task.queue.get_nowait().decode('utf-8'))
            except queue.Empty:
                break
        self.output.text.see("end")

        # Keep the loop until the task stops and the queue is empty
        if self.task.popen.poll() is None or not self.task.queue.empty():
            self.after(1, self.loop)


def main():
    """Run the app"""
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

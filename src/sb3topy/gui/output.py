"""
output.py

Contains the Output tab of the GUI
"""

import tkinter as tk
from tkinter import ttk

LOG_FORMATS = {
    '[DEBUG]': "debug",
    '[INFO]': "info",
    '[WARNING]': "warn",
    '[ERROR]': "error",
    '[CRITICAL]': "critical"
}


class OutputFrame(ttk.Frame):
    """Handles the Output tab, logging"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

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
        tag = LOG_FORMATS.get(keyword, "default")

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
        path = tk.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text File", "*.txt;*.log"),
                       ("All Files", "*.*")])

        with open(path, 'w') as file:
            file.write('\n'.join(
                self.text.get('1.0', 'end').splitlines()
            ))

"""
output.py

Contains the Output tab of the GUI
"""

import tkinter as tk
from tkinter import ttk

import queue
import logging


class OutputFrame(ttk.Frame):
    """Handles the Output tab, logging"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.app = parent

        self.process = None
        self.queue = None

        self.text = tk.Text(self, width=32, height=17.5, state="disabled")
        scroll = ttk.Scrollbar(self, orient="vertical",
                               command=self.text.yview)
        self.text['yscrollcommand'] = scroll.set

        self.show_info = tk.BooleanVar(value=True)
        self.show_debug = tk.BooleanVar()
        self.debug_check = ttk.Checkbutton(
            self, text="Debug Ouput",
            variable=self.show_debug, command=self.debug_tag)

        export_button = ttk.Button(
            self, text="Export Log...", command=self.export_log)

        # Grid everything
        self.text.grid(column=0, row=0, columnspan=4,
                       sticky="NSEW", pady=5)
        scroll.grid(column=4, row=0, sticky="NS", pady=5)

        self.debug_check.grid(column=0, row=1, sticky="NSW", padx=15)

        export_button.grid(row=1, column=3, sticky="NSW")

        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)

        # Output theme
        self.font = "Courier 10"
        self.debug_tag()
        self.text.tag_config("INFO", foreground="green",
                             font=self.font+" bold")
        self.text.tag_config("INFO_text", font=self.font)
        self.text.tag_config("WARNING", foreground="orange",
                             font=self.font+" bold")
        self.text.tag_config("WARNING_text", font=self.font)
        self.text.tag_config("ERROR", foreground="red", font=self.font+" bold")
        self.text.tag_config("ERROR_text", foreground="red", font=self.font)
        self.text.tag_config(
            "CRITICAL", foreground="dark red", font=self.font+" bold")
        self.text.tag_config(
            "CRITICAL_text", foreground="dark red", font=self.font+" bold")

    def debug_tag(self):
        """Configures debug text tags, shown/hidden"""
        value = not self.show_debug.get()
        self.text.tag_config("DEBUG", foreground="grey",
                             font=self.font, elide=value)
        self.text.tag_config("DEBUG_text", foreground="grey",
                             font=self.font, elide=value)
        self.text.see("end")

    def start_watching(self, process, log_queue):
        """Starts watching a queue for log records until process ends"""
        self.process = process
        self.queue = log_queue

        self.text["state"] = "normal"
        self.text.delete("1.0", "end")
        self.text["state"] = "disabled"

        self.after(1, self.update_loop)

    def handle_record(self, record: logging.LogRecord):
        """
        Display and formats a log record. The internal Text widget
        must be set to the active state before calling this function
        """
        levelname = record.levelname
        self.text.insert("end", f"[{levelname}] ", (levelname,))
        self.text.insert("end", record.message + "\n", (levelname+"_text",))

    def update_loop(self):
        """Updates the textbox with log messages"""

        if not self.queue.empty():
            self.text["state"] = "normal"

            while True:
                try:
                    self.handle_record(self.queue.get_nowait())
                except queue.Empty:
                    break

            self.text.see("end")
            self.text["state"] = "disabled"

        if self.process.is_alive():
            self.after(10, self.update_loop)

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

    def switch_to(self):
        """
        Disable the debug check if the log level is not debug
        """
        if int(self.app.getvar("LOG_LEVEL")) > logging.DEBUG:
            self.show_debug.set(False)
            self.debug_check.state(["disabled"])
        else:
            self.debug_check.state(["!disabled"])

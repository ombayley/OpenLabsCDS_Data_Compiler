#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: O. Bayley

Description: GUI for easy setup of the directory monitor.
"""
import tkinter as tk
import os
from tkinter import ttk, filedialog
from directory_monitor import Monitor


class MonitorGUI:
    """
    Simple GUI, to run the monitoring program.
    """

    def __init__(self):
        self.monitor = Monitor()  # Assuming Monitor() is modified to accept parameters or has defaults
        self.monitor_active = False
        self.directory_path = None
        self.root = tk.Tk()
        self.selected_directory = None

    def main(self):
        """
        Main method to start running the GUI
        """
        self.selected_directory = tk.StringVar(self.root)
        self.setup_gui()
        self.root.mainloop()

    def start_monitoring(self):
        """
        Method to start running the directory monitor program
        """
        if self.directory_path and not self.monitor_active:  # Prevent reactivation if active
            self.monitor_active = True
            self.update_button_states()
            self.monitor.start_monitoring()

    def stop_monitoring(self):
        """
        Method to stop the directory monitor program running
        """
        if self.monitor_active:  # Only callable if active
            self.monitor_active = False
            self.update_button_states()
            self.monitor.stop_monitoring()

    def open_directory(self):
        """
        Pulls up a second UI to select the desired primary directory
        """
        self.directory_path = filedialog.askdirectory()
        dir_name = os.path.basename(self.directory_path)
        if self.directory_path:
            self.selected_directory.set(dir_name)  # Update the StringVar with the selected directory path
            self.monitor.set_dir(self.directory_path)
        self.start_monitoring()

    def setup_gui(self):
        """
        Sets up the GUI to display the buttons and text
        """
        self.root.title("Directory Monitoring Tool")

        style = ttk.Style()
        style.configure('TButton', font=('Arial', 10))
        style.configure('Active.TButton', font=('Arial', 10), background='light green')
        style.configure('Inactive.TButton', font=('Arial', 10), background='light coral')

        main_frame = ttk.Frame(self.root)
        main_frame.pack(pady=10, padx=10)

        # Adjust control_frame to not expand, ensuring buttons align left
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=2)

        self.start_btn = ttk.Button(control_frame, text="Start", command=self.start_monitoring, style='TButton')
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = ttk.Button(control_frame, text="Stop", command=self.stop_monitoring, style='TButton')
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        directory_frame = ttk.Frame(main_frame)
        directory_frame.pack(fill=tk.X, expand=True, pady=2)

        open_dir_btn = ttk.Button(directory_frame, text="Open Directory", command=self.open_directory, style='TButton')
        open_dir_btn.pack(side=tk.LEFT, padx=5)

        directory_entry = ttk.Entry(directory_frame, textvariable=self.selected_directory, state='readonly', width=35)
        directory_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.update_button_states()

    def update_button_states(self):
        """
        Gives outlines to the stop and start buttons to help the user see if the program is running or not
        """
        if self.monitor_active:
            self.start_btn['style'] = 'Active.TButton'
            self.stop_btn['style'] = 'TButton'
        else:
            self.start_btn['style'] = 'TButton'
            self.stop_btn['style'] = 'Inactive.TButton'


if __name__ == "__main__":
    gui = MonitorGUI()
    gui.main()

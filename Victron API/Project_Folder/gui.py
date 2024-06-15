import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from api import login, get_installations, get_data_download
from data_processing import process_data
from config import USERNAME, PASSWORD, SMS_TOKEN

class PowerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Power Output and Input Analysis")

        self.token, self.user_id = login(USERNAME, PASSWORD, SMS_TOKEN)
        self.installations = get_installations(self.token, self.user_id)
        self.installations_dict = {inst['name']: inst for inst in self.installations}

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.window, text="Select Installation:").pack()
        self.installation_combobox = ttk.Combobox(self.window, values=list(self.installations_dict.keys()))
        self.installation_combobox.pack()

        tk.Label(self.window, text="Select Timeframe:").pack()
        self.timeframe_combobox = ttk.Combobox(self.window, values=["Last 24 Hours", "Last 7 Days", "Last 30 Days"])
        self.timeframe_combobox.pack()
        self.timeframe_combobox.set("Last 24 Hours")

        tk.Button(self.window, text="Update Graph", command=self.update_graph).pack()

    def update_graph(self):
        selected_installation = self.installation_combobox.get()
        timeframe = self.timeframe_combobox.get()

        if not selected_installation:
            return

        end_time = datetime.now()
        if timeframe == "Last 24 Hours":
            start_time = end_time - timedelta(days=1)
        elif timeframe == "Last 7 Days":
            start_time = end_time - timedelta(days=7)
        elif timeframe == "Last 30 Days":
            start_time = end_time - timedelta(days=30)
        else:
            start_time = end_time - timedelta(days=1)  # Default to last 24 hours

        installation_id = self.installations_dict[selected_installation]['idSite']
        csv_content = get_data_download(self.token, installation_id, start_time, end_time)
        df, total_kwh_used = process_data(csv_content)

        self.plot_graph(df)

    def plot_graph(self, df):
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))

        power_output_columns = ['VE.Bus System [276].1', 'VE.Bus System [276].2', 'VE.Bus System [276].3']
        power_input_columns = ['VE.Bus System [276].4', 'VE.Bus System [276].5', 'VE.Bus System [276].6']

        for col in power_output_columns:
            ax[0].plot(df.index, df[col], label=f'Phase {col[-1]}')
        ax[0].plot(df.index, df['Total Power Output'], label='Total Power Output', linestyle='--', color='black')
        ax[0].set_title('Power Output')
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Power (W)')
        ax[0].legend()

        for col in power_input_columns:
            ax[1].plot(df.index, df[col], label=f'Phase {col[-1]}')
        ax[1].plot(df.index, df['Total Power Input'], label='Total Power Input', linestyle='--', color='black')
        ax[1].set_title('Power Input')
        ax[1].set_xlabel('Time')
        ax[1].set_ylabel('Power (W)')
        ax[1].legend()

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

    def run(self):
        self.window.after(5000, self.update_graph)
        self.window.mainloop()

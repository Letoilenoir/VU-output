import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft

def load_audio_file():
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        entry_audio_path.delete(0, tk.END)
        entry_audio_path.insert(0, file_path)

def plot_power_spectrum_over_time():
    file_path = entry_audio_path.get()
    if file_path:
        sampling_rate, data = wavfile.read(file_path)
        if len(data.shape) > 1:
            data = data.mean(axis=1)
        fft_output = fft(data)
        power_spectrum = np.abs(fft_output) ** 2  # Calculate power spectrum
        decibels = 10 * np.log10(power_spectrum)  # Convert power spectrum to decibels
        
        # Calculate time axis
        duration = len(data) / sampling_rate
        time_axis = np.linspace(0, duration, len(data))
        
        # Plot power spectrum over time as a line
        plt.figure(figsize=(10, 6))
        plt.plot(time_axis, decibels, linewidth=1, color='blue')  # Plot decibels against time
        plt.title('Power Spectrum over Time (in dB)')
        plt.xlabel('Time (s)')
        plt.ylabel('Decibels (dB)')
        plt.grid(True)
        plt.show()

# Create the main window
root = tk.Tk()
root.title("Audio Power Spectrum Analyzer")

# Create and pack widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_audio_path = tk.Label(frame, text="Audio File Path:")
label_audio_path.grid(row=0, column=0, padx=5, pady=5)

entry_audio_path = tk.Entry(frame, width=50)
entry_audio_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(frame, text="Browse", command=load_audio_file)
button_browse.grid(row=0, column=2, padx=5, pady=5)

button_plot = tk.Button(root, text="Plot Power Spectrum over Time (in dB)", command=plot_power_spectrum_over_time)
button_plot.pack(padx=10, pady=5)

# Run the main event loop
root.mainloop()


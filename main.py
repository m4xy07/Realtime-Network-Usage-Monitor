import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import psutil
import time

# Function to calculate network speed
def get_net_speed():
    old_stats = psutil.net_io_counters()  # Get the network I/O counters
    old_recv = old_stats.bytes_recv  # Get the number of bytes received
    old_sent = old_stats.bytes_sent  # Get the number of bytes sent
    time.sleep(1)  # Wait for 1 second
    new_stats = psutil.net_io_counters()  # Get the updated network I/O counters
    new_recv = new_stats.bytes_recv  # Get the updated number of bytes received
    new_sent = new_stats.bytes_sent  # Get the updated number of bytes sent
    down_speed = (new_recv - old_recv) / 1024 / 1024 * 8  # Calculate download speed in Mbps
    up_speed = (new_sent - old_sent) / 1024 / 1024 * 8  # Calculate upload speed in Mbps
    return down_speed, up_speed

# Function to update the network speed labels
def refresh():
    down_speed, up_speed = get_net_speed()  # Get the network speeds
    download_speed_label.config(text=f"Download Speed: {down_speed:.2f} Mbps")  # Update the download speed label
    upload_speed_label.config(text=f"Upload Speed: {up_speed:.2f} Mbps")  # Update the upload speed label
    root.after(250, refresh)  # Schedule the next update after 250 milliseconds

root = ThemedTk(theme="arc")  # Create a themed Tkinter window
root.title("RealTime Network Speed Monitor")  # Set the window title

download_speed_label = ttk.Label(root, text="Download Speed: - Mbps", font=('Roboto', 12))  # Create a label for download speed
download_speed_label.pack(pady=5)  # Add the download speed label to the window

upload_speed_label = ttk.Label(root, text="Upload Speed: - Mbps", font=('Roboto', 12))  # Create a label for upload speed
upload_speed_label.pack(pady=5)  # Add the upload speed label to the window

refresh()  # Initial call to start the loop

root.mainloop()  # Start the Tkinter event loop

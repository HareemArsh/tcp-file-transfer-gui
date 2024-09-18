import socket
import tkinter as tk
from tkinter import filedialog
import os

# Set up GUI window
client_window = tk.Tk()
client_window.title('Client')
client_window.geometry('300x200')
client_window.configure(bg='#ADD8E6')

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server name and port
host = '10.5.152.107'
port = 9999

# Connect to the server
client_socket.connect((host, port))

status_label = tk.Label(client_window, text='Select a file to transfer:', bg='#f0f0f0', font=('Arial', 12))
status_label.pack(pady=20)

# Open a file dialog to select the file to transfer
def select_file():
    file_path = filedialog.askopenfilename()
    file_name = os.path.basename(file_path)
    file_name_label.config(text=file_name)
    return file_path, file_name

# Send the file to the server
def send_file():
    file_path, file_name = select_file()
    with open(file_path, 'rb') as f:
        bytes_to_send = f.read()
        client_socket.send(file_name.encode())
        client_socket.send(bytes_to_send)
    status_label.config(text='File sent successfully!')
    client_socket.close()

# Create GUI elements
select_button = tk.Button(client_window, text='Select File', command=select_file)
select_button.pack()

file_name_label = tk.Label(client_window, text='No file selected', bg='#f0f0f0', font=('Arial', 10))
file_name_label.pack()

send_button = tk.Button(client_window, text='Send File', command=send_file)
send_button.pack(pady=20)

client_window.mainloop()

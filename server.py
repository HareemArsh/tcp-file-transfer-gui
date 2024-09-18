import socket
import os
import tkinter as tk

# Set up GUI window
server_window = tk.Tk()
server_window.title('Server')
server_window.geometry('300x200')
server_window.configure(bg='#ADD8E6')

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

port = 9999

# Bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

status_label = tk.Label(server_window, text='Waiting for a client connection...', bg='#f0f0f0', font=('Arial', 12))
status_label.pack(pady=20)

# Accept a client connection
client_socket, addr = server_socket.accept()
status_label.config(text='Connection from: ' + str(addr))

# Receive the file name
file_name = client_socket.recv(1024).decode()
status_label.config(text='File name: ' + file_name)

# Open the file and send its contents to the client
with open(file_name, 'rb') as f:
    bytes_to_send = f.read()
    client_socket.send(bytes_to_send)

status_label.config(text='File sent successfully!')

# Close the socket and the connection
client_socket.close()
server_socket.close()

server_window.mainloop()

# TCP File Transfer with GUI

## Introduction

This project demonstrates a file transfer application that enables a client to send files (including video files) to a server using TCP sockets. The application includes a graphical user interface (GUI) built with the Tkinter library in Python, providing users with an intuitive way to transfer files over a network.

## Features

- **File Transfer**: Transfer files between client and server using TCP.
- **Video File Transfer**: Supports transfer of video files.
- **Graphical User Interface (GUI)**: Built using Tkinter.
- **Progress Bar**: Tracks file transfer status.
- **Completion Notification**: Displays a message box upon successful transfer.
- **Text and Binary Files**: Supports both text and binary file transfers.

## Requirements

- **Python 3.x**
- **Tkinter**: For GUI.
- **Socket**: For network communication.

## Code Structure

- **`client.py`**: Handles file selection and sending the file to the server.
- **`server.py`**: Receives the file from the client and saves it on the server's side.

## Handling Large File Transfers

- File I/O and networking are managed using binary mode (`rb`), and files are transferred in chunks for efficient and error-free transmission.

## User-Friendly GUI

- Tkinter widgets such as file dialogs, labels, buttons, and progress bars are used to create an intuitive interface.

## Future Enhancements

- **Error Handling**: Improve error handling during file transfers.
- **Encryption**: Support for encryption to secure file transfer.
- **Retry Mechanisms**: Add retry mechanisms for interrupted transfers.
- **Transfer Metrics**: Display transfer speed and estimated time.


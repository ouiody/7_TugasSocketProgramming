import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Setup server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 11111))  # Bind ke semua interface pada port 11111

clients = {}
server_password = "samsungdagostore"

# Fungsi untuk menangani pesan klien
def handle_client_messages():
    while True:
        try:
            message, client_address = server_socket.recvfrom(1024)

            if is_login_message(message):
                username, password = parse_login_message(message)
                if password == server_password and username not in clients:
                    clients[username] = client_address
                    send_message_to_client(client_address, "Login berhasil!")
                    log(f"{username} telah bergabung ke chatroom.")
                elif username in clients:
                    send_message_to_client(client_address, "USERNAME_TAKEN")
                else:
                    send_message_to_client(client_address, "Password salah!")
            else:
                broadcast_message(message, client_address)
        except Exception as e:
            log(f"Error handling client message: {e}")

# Fungsi untuk memeriksa dan parsing pesan login
def is_login_message(message):
    return message.decode().startswith("LOGIN")

def parse_login_message(message):
    parts = message.decode().split()
    if len(parts) == 3 and parts[0] == "LOGIN":
        return parts[1], parts[2]  # Mengembalikan username dan password
    return None, None

def send_message_to_client(client_address, message):
    """Mengirim pesan ke klien tertentu."""
    try:
        server_socket.sendto(message.encode(), client_address)
    except Exception as e:
        log(f"Error sending message to {client_address}: {e}")

def broadcast_message(message, sender_address):
    """Mengirim pesan ke semua klien kecuali pengirim."""
    sender_username = get_username_by_address(sender_address)
    if sender_username:
        formatted_message = f"{sender_username}: {message.decode()}"
        for username, client_address in clients.items():
            if client_address != sender_address:
                try:
                    server_socket.sendto(formatted_message.encode(), client_address)
                    log(f"Pesan dikirim ke {username} di {client_address}")
                except Exception as e:
                    log(f"Error mengirim pesan ke {username}: {e}")

def get_username_by_address(address):
    """Mencari username berdasarkan alamat klien."""
    for username, client_address in clients.items():
        if client_address == address:
            return username
    return None

def log(message):
    """Menampilkan pesan log di GUI server."""
    log_display.config(state='normal')
    log_display.insert(tk.END, f"{message}\n")
    log_display.config(state='disabled')
    log_display.yview(tk.END)  # Scroll otomatis ke pesan terbaru

# Membuat GUI untuk server
window = tk.Tk()
window.title("SamsungChat Server")
window.geometry("400x300")

log_display = scrolledtext.ScrolledText(window, state='disabled', wrap='word', height=15, width=50)
log_display.pack(padx=10, pady=10)

# Mulai thread untuk menangani pesan klien
threading.Thread(target=handle_client_messages, daemon=True).start()

# Menjalankan aplikasi server
log("Server sedang berjalan.....")
window.mainloop()

import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Setup client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)  # Tambahkan timeout untuk menerima respons

# Variabel global untuk IP dan port server
server_ip = ""
server_port = 0
server_address = ()
username = ""

# Fungsi untuk mengirim pesan
def send_messages_to_server():
    message = message_entry.get()
    if message:
        formatted_message = f"{username}: {message}"
        client_socket.sendto(formatted_message.encode(), server_address)
        chat_display.config(state='normal')
        chat_display.insert(tk.END, f"{formatted_message}\n")
        chat_display.config(state='disabled')
        message_entry.delete(0, tk.END)

# Fungsi untuk menerima pesan dari server
def receive_messages_from_server():
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            chat_display.config(state='normal')
            chat_display.insert(tk.END, f"{message.decode()}\n")
            chat_display.config(state='disabled')
        except:
            break

# Fungsi untuk login
def login():
    global username, server_ip, server_port, server_address
    username = username_entry.get()
    password = password_entry.get()
    server_ip = ip_entry.get()

    try:
        server_port = int(port_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Port harus berupa angka.")
        return

    server_address = (server_ip, server_port)

    if not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong.")
        return

    if not server_ip or not server_port:
        messagebox.showerror("Error", "IP dan port server tidak boleh kosong.")
        return

    # Kirim data login ke server
    login_message = f"LOGIN {username} {password}"
    try:
        client_socket.sendto(login_message.encode(), server_address)
        # Tunggu respons login dari server
        response, _ = client_socket.recvfrom(1024)
        response_message = response.decode()

        if response_message == "USERNAME_TAKEN":
            messagebox.showerror("Error", "Username sudah digunakan. Harap memasukkan username baru.")
            return  # Meminta pengguna untuk memasukkan username yang berbeda
        elif response_message == "Login berhasil!":
            messagebox.showinfo("Info", f"Password benar, {username} sudah bergabung.")
            login_frame.pack_forget()
            chat_frame.pack(padx=10, pady=10)
            # Mulai thread untuk menerima pesan
            threading.Thread(target=receive_messages_from_server, daemon=True).start()
        else:
            messagebox.showerror("Error", "Password yang Anda masukkan salah, coba lagi.")
    except socket.timeout:
        # Jika terjadi timeout, berarti server tidak merespons
        messagebox.showerror("Error", "IP Address atau port salah! Harap memasukkan IP Address dan port yang sesuai.")
    except Exception as e:
        # Menangani kesalahan lainnya yang mungkin terjadi
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat GUI
window = tk.Tk()
window.title("SamsungChat Client")
window.geometry("400x500")

# Frame untuk login
login_frame = tk.Frame(window)
login_frame.pack(padx=10, pady=10)

tk.Label(login_frame, text="IP Address:").pack()
ip_entry = tk.Entry(login_frame)
ip_entry.pack()

tk.Label(login_frame, text="Port Number:").pack()
port_entry = tk.Entry(login_frame)
port_entry.pack()

tk.Label(login_frame, text="Username:").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password:").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(pady=10)

# Frame untuk chat
chat_frame = tk.Frame(window)

chat_display = scrolledtext.ScrolledText(chat_frame, state='disabled', wrap='word', height=20, width=50)
chat_display.pack(padx=10, pady=10)

message_entry = tk.Entry(chat_frame, width=40)
message_entry.pack(side=tk.LEFT, padx=5, pady=5)

send_button = tk.Button(chat_frame, text="Send", command=send_messages_to_server)
send_button.pack(side=tk.LEFT, padx=5, pady=5)

# Menjalankan aplikasi
window.mainloop()

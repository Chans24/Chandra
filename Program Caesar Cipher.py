import tkinter as tk
from tkinter import messagebox

# Fungsi Caesar Cipher untuk enkripsi dan dekripsi
def caesar_cipher(text, shift):
    result = ''
    process_steps = []  # Menyimpan langkah proses enkripsi
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_char = char

        result += encrypted_char
        process_steps.append(f"{char} -> {encrypted_char}")  # Menyimpan langkah enkripsi

    return result, process_steps

# Fungsi keluar program
def close_program(window):
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        window.destroy()

# Fungsi menghapus riwayat chat
def clear_chat_history(chat_history):
    if messagebox.askokcancel("Hapus Riwayat", "Apakah Anda yakin ingin menghapus riwayat chat?"):
        chat_history.config(state='normal')
        chat_history.delete(1.0, tk.END)
        chat_history.insert(tk.END, "Riwayat Chat:\n")
        chat_history.config(state='disabled')

# Fungsi kirim pesan dari Pengguna 1 ke Pengguna 2 (dienkripsi)
def send_message_user1(chat_history_user1, chat_history_user2, entry_message_user1, entry_key_user1):
    message = entry_message_user1.get()

    if message.lower() == "exit" or message.lower() == "keluar":
        close_program(window_user1)
        return

    try:
        key = int(entry_key_user1.get())
    except ValueError:
        messagebox.showerror("Error", "Key harus berupa angka!")
        return

    # Enkripsi pesan dan dapatkan langkah proses
    encrypted_message, process_steps = caesar_cipher(message, key)

    # Tampilkan langkah proses enkripsi
    process_steps_display = "\n".join(process_steps)
    chat_history_user1.config(state='normal')
    chat_history_user1.insert(tk.END, f"Proses Enkripsi:\n{process_steps_display}\n")
    chat_history_user1.insert(tk.END, f"Pengguna 1 (terenkripsi): {encrypted_message}\n")
    
    # Dekripsi pesan untuk ditampilkan di pengguna 2
    decrypted_message, _ = caesar_cipher(encrypted_message, -key)
    chat_history_user2.config(state='normal')
    chat_history_user2.insert(tk.END, f"Pengguna 1 (didekripsi): {decrypted_message}\n")
    
    # Mengatur kembali state teks
    chat_history_user1.config(state='disabled')
    chat_history_user2.config(state='disabled')
    
    # Hapus input
    entry_message_user1.delete(0, tk.END)

# Fungsi kirim pesan dari Pengguna 2 ke Pengguna 1 (dienkripsi)
def send_message_user2(chat_history_user1, chat_history_user2, entry_message_user2, entry_key_user2):
    message = entry_message_user2.get()

    if message.lower() == "exit" or message.lower() == "keluar":
        close_program(window_user2)
        return

    try:
        key = int(entry_key_user2.get())
    except ValueError:
        messagebox.showerror("Error", "Key harus berupa angka!")
        return

    # Enkripsi pesan dan dapatkan langkah proses
    encrypted_message, process_steps = caesar_cipher(message, key)

    # Tampilkan langkah proses enkripsi
    process_steps_display = "\n".join(process_steps)
    chat_history_user2.config(state='normal')
    chat_history_user2.insert(tk.END, f"Proses Enkripsi:\n{process_steps_display}\n")
    chat_history_user2.insert(tk.END, f"Pengguna 2 (terenkripsi): {encrypted_message}\n")
    
    # Dekripsi pesan untuk ditampilkan di pengguna 1
    decrypted_message, _ = caesar_cipher(encrypted_message, -key)
    chat_history_user1.config(state='normal')
    chat_history_user1.insert(tk.END, f"Pengguna 2 (didekripsi): {decrypted_message}\n")
    
    # Mengatur kembali state teks
    chat_history_user1.config(state='disabled')
    chat_history_user2.config(state='disabled')
    
    # Hapus input
    entry_message_user2.delete(0, tk.END)

# Membuat GUI menggunakan Tkinter untuk Pengguna 1
window_user1 = tk.Tk()
window_user1.title("Caesar Cipher - Pengguna 1")
window_user1.geometry("500x600")
window_user1.configure(bg="#6a0dad")

# History chat untuk Pengguna 1
chat_history_user1 = tk.Text(window_user1, height=15, width=58, state='disabled')
chat_history_user1.pack(pady=10)
chat_history_user1.config(state='normal')
chat_history_user1.insert(tk.END, "Riwayat Chat:\n")
chat_history_user1.config(state='disabled')

# Input untuk Pengguna 1
frame_user1 = tk.Frame(window_user1, bg="#6a0dad")
frame_user1.pack(pady=10)

label_user1 = tk.Label(frame_user1, text="Pengguna 1", bg="#6a0dad", fg="white", font=("Arial", 12))
label_user1.grid(row=0, column=0, padx=5)

entry_message_user1 = tk.Entry(frame_user1, width=30)
entry_message_user1.grid(row=0, column=1, padx=5)

entry_key_user1 = tk.Entry(frame_user1, width=5)
entry_key_user1.grid(row=0, column=2, padx=5)
entry_key_user1.insert(0, "Key")

button_send_user1 = tk.Button(frame_user1, text="Kirim", command=lambda: send_message_user1(chat_history_user1, chat_history_user2, entry_message_user1, entry_key_user1), bg="#007bff", fg="white")
button_send_user1.grid(row=0, column=3, padx=5)

# Tombol Hapus Riwayat dan Keluar untuk Pengguna 1
button_clear_chat_user1 = tk.Button(window_user1, text="Hapus Riwayat", command=lambda: clear_chat_history(chat_history_user1), bg="#dc3545", fg="white", width=15)
button_clear_chat_user1.pack(pady=10)

button_exit_user1 = tk.Button(window_user1, text="Keluar", command=lambda: close_program(window_user1), bg="#343a40", fg="white", width=15)
button_exit_user1.pack(pady=10)

# Membuat GUI menggunakan Tkinter untuk Pengguna 2
window_user2 = tk.Tk()
window_user2.title("Caesar Cipher - Pengguna 2")
window_user2.geometry("500x600")
window_user2.configure(bg="#6a0dad")

# History chat untuk Pengguna 2
chat_history_user2 = tk.Text(window_user2, height=15, width=58, state='disabled')
chat_history_user2.pack(pady=10)
chat_history_user2.config(state='normal')
chat_history_user2.insert(tk.END, "Riwayat Chat:\n")
chat_history_user2.config(state='disabled')

# Input untuk Pengguna 2
frame_user2 = tk.Frame(window_user2, bg="#6a0dad")
frame_user2.pack(pady=10)

label_user2 = tk.Label(frame_user2, text="Pengguna 2", bg="#6a0dad", fg="white", font=("Arial", 12))
label_user2.grid(row=0, column=0, padx=5)

entry_message_user2 = tk.Entry(frame_user2, width=30)
entry_message_user2.grid(row=0, column=1, padx=5)

entry_key_user2 = tk.Entry(frame_user2, width=5)
entry_key_user2.grid(row=0, column=2, padx=5)
entry_key_user2.insert(0, "Key")

button_send_user2 = tk.Button(frame_user2, text="Kirim", command=lambda: send_message_user2(chat_history_user1, chat_history_user2, entry_message_user2, entry_key_user2), bg="#28a745", fg="white")
button_send_user2.grid(row=0, column=3, padx=5)

# Tombol Hapus Riwayat dan Keluar untuk Pengguna 2
button_clear_chat_user2 = tk.Button(window_user2, text="Hapus Riwayat", command=lambda: clear_chat_history(chat_history_user2), bg="#dc3545", fg="white", width=15)
button_clear_chat_user2.pack(pady=10)

button_exit_user2 = tk.Button(window_user2, text="Keluar", command=lambda: close_program(window_user2), bg="#343a40", fg="white", width=15)
button_exit_user2.pack(pady=10)

# Mengatur protocol untuk menutup jendela
window_user1.protocol("WM_DELETE_WINDOW", lambda: close_program(window_user1))
window_user2.protocol("WM_DELETE_WINDOW", lambda: close_program(window_user2))

# Menjalankan kedua aplikasi secara bersamaan
window_user1.mainloop()
window_user2.mainloop()

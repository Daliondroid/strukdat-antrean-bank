import csv
from collections import deque
import os

class BankQueue:
    def __init__(self, filename='queue_data.csv'):
        self.queue = deque()
        self.filename = filename
        self.counter = 1
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        self.queue.append(f"{row[0]} - {row[1]}")
                        num = int(row[0])
                        if num >= self.counter:
                            self.counter = num + 1

    def save_data(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in self.queue:
                parts = item.split(" - ")
                writer.writerow(parts)

    def generate_next_number(self):
        return f"{self.counter:03d}"

    def enqueue(self, customer_number, service_type):
        self.queue.append(f"{customer_number} - {service_type}")
        self.counter += 1
        self.save_data()

    def dequeue(self):
        if self.queue:
            customer = self.queue.popleft()
            print(f"[Pelanggan {customer} sedang dilayani...] → Selesai")
            customer_number = customer.split(" - ")[0]
            print(f"Antrian setelah {customer_number} keluar:")
            self.display_queue()
            if not self.queue:
                print("Semua pelanggan telah terlayani.")
            self.save_data()
        else:
            print("Antrian kosong. Tidak ada pelanggan yang dapat dilayani.")

    def display_queue(self):
        if self.queue:
            for idx, item in enumerate(self.queue, 1):
                print(f"{idx}. {item}")
        else:
            print("Antrian kosong.")

    def update_queue(self, customer_number, new_service_type):
        for i, item in enumerate(self.queue):
            if item.split(" - ")[0] == customer_number:
                self.queue[i] = f"{customer_number} - {new_service_type}"
                print(f"Data pelanggan {customer_number} berhasil diperbarui.")
                self.save_data()
                return
        print(f"Pelanggan dengan nomor {customer_number} tidak ditemukan.")

    def remove_queue(self, customer_number):
        for item in list(self.queue):
            if item.split(" - ")[0] == customer_number:
                self.queue.remove(item)
                print(f"Pelanggan {item} telah dihapus dari antrian.")
                self.save_data()
                return
        print(f"Pelanggan dengan nomor {customer_number} tidak ditemukan.")

# =======================
# Program Utama
# =======================
bank = BankQueue()

# Data awal
bank.enqueue(bank.generate_next_number(), "Setor Tunai")
bank.enqueue(bank.generate_next_number(), "Tarik Tunai")
bank.enqueue(bank.generate_next_number(), "Pembukaan Rekening")
bank.enqueue(bank.generate_next_number(), "Tarik Tunai")

print("\n\n\n\n\n\n\n\n\n\n\n")
print("=== Selamat datang di Sistem Antrian Bank ===")
print("Masuk sebagai:")
print("1. Operator Bank (Admin)")
print("2. Nasabah/Pelanggan (User)")
print("3. Keluar")

role = input("Pilih peran (1/2/3): ")

if role == "1":
    while True:
        print("\n=== Menu Operator Bank ===")
        print("1. Proses pelanggan berikutnya")
        print("2. Lihat daftar antrian")
        print("3. Edit jenis layanan pelanggan")
        print("4. Hapus pelanggan dari antrian")
        print("5. Keluar")

        choice = input("Pilih operasi (1/2/3/4/5): ")

        if choice == "1":
            def clear_screen():
                print("\n" * 100)
            clear_screen()
            bank.dequeue()
        elif choice == "2":
            def clear_screen():
                print("\n" * 100)
            clear_screen()
            bank.display_queue()
        elif choice == "3":
            def clear_screen():
                print("\n" * 100)
            clear_screen()
            bank.display_queue()
            customer_number = input("Masukkan nomor pelanggan yang ingin diubah: ")
            new_service = input("Masukkan jenis layanan baru: ")
            bank.update_queue(customer_number, new_service)
        elif choice == "4":
            def clear_screen():
                print("\n" * 100)
            clear_screen()
            bank.display_queue()
            customer_number = input("Masukkan nomor pelanggan yang ingin dihapus: ")
            bank.remove_queue(customer_number)
        elif choice == "5":
            print("Keluar dari sistem Admin. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")



elif role == "2":
    my_number = None

    while True:
        def clear_screen():
                print("\n" * 100)
        clear_screen()
        print("\n=== Menu Nasabah/Pelanggan ===")
        if my_number:
            print(f"Anda telah mengambil nomor antrian: {my_number}")
        print("1. Ambil nomor antrian")
        print("2. Lihat jumlah antrean & posisi Anda")
        print("3. Keluar")

        choice = input("Pilih operasi (1/2/3): ")

        if choice == "1":
            if my_number:
                def clear_screen():
                    print("\n" * 100)
                clear_screen()
                print("Anda sudah mengambil nomor antrian. Tidak bisa mengambil lagi.")
            else:
                def clear_screen():
                    print("\n" * 100)
                clear_screen()
                service_type = input("Masukkan jenis layanan: ")
                next_number = bank.generate_next_number()
                bank.enqueue(next_number, service_type)
                my_number = next_number
                print(f"Nomor antrian Anda adalah: {my_number}")

        elif choice == "2":
            def clear_screen():
                print("\n" * 100)
            clear_screen()
            print("\n=== Daftar Antrian Saat Ini ===")
            bank.display_queue()

            if not my_number:
                def clear_screen():
                    print("\n" * 100)
                clear_screen()
                print("Anda belum mengambil nomor antrian.")
            else:
                position = 0
                for item in bank.queue:
                    if item.split(" - ")[0] == my_number:
                        break
                    position += 1
                def clear_screen():
                    print("\n" * 100)
                clear_screen()
                print(f"\nJumlah antrean sebelum giliran Anda ({my_number}): {position} orang.")

        elif choice == "3":
            print("Terima kasih telah menggunakan sistem antrian.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

elif role == "3":
    print("Keluar dari sistem. Terima kasih!")
    
else:
    print("Pilihan tidak valid. Silakan coba lagi.")

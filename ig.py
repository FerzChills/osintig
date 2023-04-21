import instaloader
import os
import ipaddress
import socket

#Variable Wajib Jan Sampe Ke Hapus
nameadd = socket.gethostname()
ipsadd = socket.gethostbyname(nameadd)

#Instance Instaloader
L = instaloader.Instaloader()

#data Untuk mengunduh snapig
asep = L.download_pic

#data Untuk Mengambil Username
os.system("clear")
print("┏━┓┏━┓╻┏┓╻╺┳╸┏━╸┏━┓┏━┓┏┳┓")
print("┃ ┃┗━┓┃┃┗┫ ┃ ┃╺┓┣┳┛┣━┫┃┃┃")
print("┗━┛┗━┛╹╹ ╹ ╹ ┗━┛╹┗╸╹ ╹╹ ╹")
print("Your HOSTNAME:" + nameadd)
print("Your IP      :" + ipsadd)
username = input("Enter Instagram Username: ")
profile = instaloader.Profile.from_username(L.context, username)

# Print the number of followers for the profile
print("Username:", profile.username)
print("Nama Lengkap Akun:", profile.full_name)
print("Bio:", profile.biography)
print("Total Postingan:", profile.mediacount)
print("Mengikuti:", profile.followees)
print("Pengikut:", profile.followers)
print("Id Akun:", profile.userid)
print("Link Profil:", profile.profile_pic_url)
asep = input("Masukan Link Foto Atau Vidio Yang Ingin Di Ambil: ")
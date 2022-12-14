import os  
import check_camera
import Capture_Image
import Train_Image
import Recognize
import yoklamasil
import first
import mysql.connector as mysql
import time
import datetime
from mysql.connector import Error

if os.path.exists('oto.txt'):
        f = open("oto.txt", "r")
        kontrol=f.read()
        f.close()
        
if os.path.isfile("key.lock")==False:
    while True:
        try:
            conn = mysql.connect(host='localhost', user='root', password='',database='admin')
            if conn.is_connected():               
                cursor = conn.cursor()
                cursor.execute("SELECT * from giris")
                taninanOgrenci = cursor.fetchone()
                admin_kullanici_adi,admin_sifre = taninanOgrenci
        except:
            print("Sifre ya da Kullanici Adi Duzgun Olusturulamamis, ya da MySQL Kapalidir\nLutfen Kontol Ediniz, Aksi Takdirde Kurucuya Haber Veriniz")
            print("Tekrar denemk icin bir tusa basiniz")
            key = input("Ana menuye donmek icin bir tusa basin...")
        
        else:
            while True:
                os.system('cls') 
                
                print("Giris Yapmak Icin Lutfen Kullanici Adi ve Sifrenizi Giriniz")
                kullanici_adi=input("Kullanici Adinizi Giriniz -->")
                sifre=input("Sifrenizi Giriniz -->")
                if kullanici_adi==admin_kullanici_adi and sifre==admin_sifre:
                    print("Basariyla Giris Yapildi...")
                    time.sleep(3)
                    break
                
                else:
                    print("Kullanici Adi veya Sifreniz Yanlis Lutfen Tekrar Deneyiniz...")
                    time.sleep(2)
            break
       




def title_bar():
    os.system('cls') 

    

    print("\t**********************************************")
    print("\t******** Yuz Algilama Yoklama Sistemi ********")
    print("\t**********************************************")



def anaMenu(oto):
    if kontrol=='0':
        
        title_bar()
        print()
        print(10 * "*", "HOSGELDIN", 10 * "*")
        print("[1] Kamera Kontrol")
        print("[2] Ogrenci Tanit")
        print("[3] Resimleri Kaydet")
        print("[4] Yoklama Al")
        print("[5] Kapat")
        
        while True:
            
            try:
                secim = int(input("Secim Yapin: "))
                
                if secim == 0 and os.path.isfile("key.lock")==True:
                    Setup()
                    break
                if os.path.isfile("key.lock")==True:
                    print("Setup Calistirilmamis!!!")
     
                elif secim == 1:
                    kameraKontrol()
                    break
                elif secim == 2:
                    ogrenciTanit()
                    break
                elif secim == 3:
                    Trainimages()
                    break
                elif secim ==4:
                    YoklamaBaslat()
                    break
                elif secim == 5:
                    print("Gorusuruz")
                    break
                elif secim == 8:
                    YoklamaSil()
                    break
                    
                else:
                    print("Yanlis Secim. 1-6 Arasinda Bir Deger Girin")
                    anaMenu(kontrol)
                
            except ValueError:
                print("Yanlis secim. 1-6 Arasinda Girin\n Tekrar Deneyin")
        exit
    elif kontrol=='1':
        if os.path.isfile("key.lock")==True:
            Setup()
        YoklamaBaslat()
        
            
        


# ---------------------------------------------------------


def kameraKontrol():
    check_camera.camer()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu(kontrol)


# --------------------------------------------------------------


def ogrenciTanit():
    Capture_Image.takeImages()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu(kontrol)


# -----------------------------------------------------------------


def Trainimages():
    Train_Image.TrainImages()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu(kontrol)

# --------------------------------------------------------------------


def YoklamaBaslat():
    Recognize.recognize_attendence()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu(kontrol)
    
# --------------------------------------------------------------------

def YoklamaSil():
    yoklamasil.tarih_sil()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu(kontrol)

# --------------------------------------------------------------------

def Setup():
    first.setup()
    key = input("Ana menuye donmek icin bir tusa basin...")
    anaMenu(kontrol)

anaMenu(kontrol)



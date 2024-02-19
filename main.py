from tkinter import *
from tkinter import messagebox

class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        messagebox.showinfo("Bilgilendirme","Kitaplar hakkında detaylı bilgi için kitaplara çift tıklayın.")
        def kitap_detaylari(çift_tıklama):
            seçilen_dize = list1.curselection()[0]
            seçilen_kitap = kitaplar[seçilen_dize]
            kitap_bilgileri3 = seçilen_kitap.split(",")
            detay = f"Kitap: {kitap_bilgileri3[0]}\nYazar: {kitap_bilgileri3[1]}\nBasım Yılı: {kitap_bilgileri3[2]}\nSayfa Sayısı: {kitap_bilgileri3[3]}"
            messagebox.showinfo(kitap_bilgileri3[0], detay)
        def kapat_listbox():
                list1.destroy()
                kapat.destroy()

        self.file.seek(0)
        list = self.file.read()
        kitaplar = list.splitlines()

        if not kitaplar:
            messagebox.showinfo("Hata!","Henüz eklenmiş kitap bulunmamakta. ")
        else:
            list1=Listbox(font="Arial 14",border="4",width=58, height=17)
            list1.place(x=230,y=190)
            kapat = Button(text="Kitap listesini kapat",bg="#FA8072", width=20, command=kapat_listbox) 
            kapat.place(x=761,y=587)     
            list1.bind("<Double-Button-1>", kitap_detaylari)
            
            for i in kitaplar:
                kitap_bilgileri = i.split(",")
                list1.insert(END, f"Kitap: {kitap_bilgileri[0]}   Yazar: {kitap_bilgileri[1]}")
                
    
    def add_book(self):
        def kapat_kitap_ekleme():
            kitapekle.destroy(),kitap_adı_etiket.destroy(),yazar_etiket.destroy(),
            title_label.destroy(),kitap_adı_gir.destroy(),yazarı_gir.destroy(),
            basım_yılı_etiket.destroy(),basım_yılı_gir.destroy(),
            sayfa_sayısı_etiket.destroy(),sayfa_sayısı_gir.destroy(),ekle.destroy(),kapat.destroy()

        def kitabı_kaydet():
            kitap_adı = kitap_adı_gir.get()
            yazar =yazarı_gir.get()
            basım_yılı = basım_yılı_gir.get()
            sayfa_sayısı = sayfa_sayısı_gir.get()
            kitap_detayları = (f"{kitap_adı},{yazar},{basım_yılı},{sayfa_sayısı}\n")
            with open("books.txt", "a") as data_file:
                data_file.write(kitap_detayları)
                messagebox.showinfo("Kitap Eklendi",f"{kitap_adı} Kitabı başarıyla eklenmiştir. ")
                kitap_adı_gir.delete(0,END)
                yazarı_gir.delete(0,END)
                basım_yılı_gir.delete(0,END)
                sayfa_sayısı_gir.delete(0,END)
            
            

        kitapekle= Canvas(width=500,height=420, highlightthickness=0)
        kitapekle.place(x=340, y=200)

        title_label = Label(text="Kitap Ekleme",fg="black",font=(None,20))
        title_label.place(x=500,y=220)  
        
        kitap_adı_etiket = Label(text="Kitap Adı:")
        kitap_adı_etiket.place(x=450, y=280)
        kitap_adı_gir=Entry(width=25,background="#B8E1E0")
        kitap_adı_gir.place(x=550,y=280)
        
        yazar_etiket = Label(text="Yazar:",)
        yazar_etiket.place(x=450, y=340)
        yazarı_gir=Entry(width=25,background="#B8E1E0")
        yazarı_gir.place(x=550,y=340)

        basım_yılı_etiket = Label(text="Basım Yılı:")
        basım_yılı_etiket.place(x=450, y=400)
        basım_yılı_gir=Entry(width=25,background="#B8E1E0")
        basım_yılı_gir.place(x=550,y=400)

        sayfa_sayısı_etiket = Label(text="Sayfa Sayısı:")
        sayfa_sayısı_etiket.place(x=450, y=460)
        sayfa_sayısı_gir=Entry(width=25,background="#B8E1E0")
        sayfa_sayısı_gir.place(x=550,y=460)

        ekle = Button(text="Kitabı Kaydet",bg="#8BE554", width=20, command=kitabı_kaydet)
        ekle.place(x=400,y=580)

        kapat = Button(text="Kitap Eklemeyi Kapat",bg="#FA8072", width=20, command=kapat_kitap_ekleme) 
        kapat.place(x=600,y=580)  
    
    def remove_book(self):
        def kitap_sil():
            silinecek_kitap = silinecek_kitap_gir.get().lower()
            with open("books.txt", "r") as file:
                lines = file.readlines()
            with open("books.txt", "w") as file:
                kitap_bulundu = False
                for line in lines:
                    kitap_bilgileri = line.strip().lower().split(",")
                    if kitap_bilgileri[0] != silinecek_kitap:
                        file.write(line)
                    else:
                        kitap_bulundu = True
                if kitap_bulundu:
                    messagebox.showinfo("Başarılı", f"{silinecek_kitap} kitabı başarıyla silindi.")
                else:
                    messagebox.showinfo("Hata", f"{silinecek_kitap} kitabı bulunamadı.")
            silinecek_kitap_gir.delete(0, 'end')
            
        def kitap_sil_kapatma():
            kitapsil.destroy(),sil_label.destroy(),silinecek_kitap.destroy(),silinecek_kitap_gir.destroy(),
            sil.destroy(),sil_kapatma.destroy()
        
        kitapsil= Canvas(width=500,height=420, highlightthickness=0)
        kitapsil.place(x=350, y=200)

        sil_label = Label(text="Kitap Sil",fg="black",font=(None,20))
        sil_label.place(x=550,y=220) 

        silinecek_kitap = Label(text="Silmek istenilen kitap : ",font=(None,11))
        silinecek_kitap.place(x=380, y=400)
        silinecek_kitap_gir=Entry(width=25,background="#B8E1E0")
        silinecek_kitap_gir.place(x=550,y=400)

        sil = Button(text="Kitabı Sil",bg="#8BE554", width=20,command=kitap_sil)
        sil.place(x=410,y=580)

        sil_kapatma = Button(text="Kitap Silmeyi Kapat",bg="#FA8072", width=20,command=kitap_sil_kapatma) 
        sil_kapatma.place(x=610,y=580)  

                    


lib = Library()

window = Tk()
window.title("Kütüphane Yönetim Sistemi")

canvas = Canvas(width=1100 , height=900)
library_image = PhotoImage(file="image/ailibrary.png")
canvas.create_image(600, 450 , image=library_image)
canvas.grid(column=1, row=1)

menü = Canvas(width=444,height=415, highlightthickness=0)
menü_image = PhotoImage(file="image/aimenü.png")
menü.create_image(266,262, image=menü_image)
menü.place(x=350, y=200)

menü_label = Label(text="Menü",background="white",font=(None,25))
menü_label.place(x=525,y=280)     

menü_text = Label(text="1) Kitapları Listele \n 2) Kitap Ekle \n 3) Kitap Sil \n 4) Uygulamadan Çıkış Yap",background="white",font=(None,14))
menü_text.place(x=450,y=340)

menü_text2 = Label(text="Yapmak istediğiniz işlemin numarasını giriniz.",background="white",font=(None,11))
menü_text2.place(x=415,y=500)


def giriş():
    
    global lib
    seçim = işlem.get()
    if seçim == '1':
        lib.list_books()
    elif seçim == '2':
        lib.add_book()
    elif seçim == '3':
        lib.remove_book()
    elif seçim == '4':
        exit()    
    else:
        messagebox.showinfo("Hata!","Lütfen 1-4 arası seçim yapınız. ")
    işlem.delete(0, 'end')
   







    
işlem = Entry(width=15,background="#F7FF55")
işlem.place(x=510,y=540)

işlem_buton = Button(text="Seç",background="#8BE554", width=15, command=giriş)
işlem_buton.place(x=507,y=570)



window.mainloop()
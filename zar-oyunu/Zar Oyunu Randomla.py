import random
import time


class ZarOyunu():
    

    def __init__(self , tahminhak1 , tahminhak2):
        print('******************\nZar Tahmin Oyunu\n******************')
        self.tahminhak1=tahminhak1
        self.tahminhak2=tahminhak2


    def game (self):
        zar1=random.randint(1,6)
        zar2=random.randint(1,6)
        print("1.zar için tahmin başlasın!")
        while True:
            tahmin1=int(input("1.zar için tahminde bulununuz"))
            print("tahmininiz kontrol ediliyor")
            time.sleep(1)
            if(tahmin1==zar1):
                print("Tebrikler! Doğru tahminde bulundunuz.")
                puan1=self.tahminhak1*10
                print(f"1.zardan aldığınız puanınız:{puan1}")
                print(f"1.zardan aldığınız puanınız:")
                print("2.zar tahminine geçebilirsiniz")
                break
            else:
                (self.tahminhak1)-=1
                print("Malesef yanlış tahminde bulundunuz")
                print(f"Kalan tahmin hakkınız:{self.tahminhak1}")
            
            if(self.tahminhak1==0):
                print(f"Tahmin hakkınız bitmiştir.")
                print(f"1.zarın değeri:{tahmin1}di")
                break
        print(".\n.\n.\n")   

        print("2.zar için tahmin başlasın!")       
        while True:    
            tahmin2=int(input("2.zar için tahminde bulununuz"))
            print("tahmininiz kontrol ediliyor")
            time.sleep(1)
            if(tahmin2==zar2):
                print("Tebrikler! Doğru tahminde bulundunuz.")
                puan2=self.tahminhak2*10
                print(f"2.zardan aldığınız puanınız:{puan2}")
                break
            
            else:
                (self.tahminhak2)-=1
                print("Malesef yanlış tahminde bulundunuz")
                print(f"Kalan tahmin hakkınız:{self.tahminhak2}")
            
            if(self.tahminhak2==0):
                print(f"Tahmin hakkınız bitmiştir.")
                print(f"2.zarın değeri:{tahmin2}di")
                break
    
        print(".\n.\n.\n")  

        toplam=puan1+puan2
        print(f"toplam kazandığınız puan:{toplam}")      

        if(toplam<=120 and toplam>=100):
            print("Durumunuz : Çok iyi!")  
        elif(toplam<100 and toplam>70):
            print("Durumunuz : İyi!")
        elif(toplam<70 and toplam>40):
            print("Durumunuz : Orta!")
        elif(toplam<40 and toplam>=0):
            print("Durumunuz : Kötü!")


zey = ZarOyunu(6,6)
zey.game()
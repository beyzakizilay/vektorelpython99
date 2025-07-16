def menu(): #ana menüyü (fonksiyon) tanımlar
    print("1-oyun")
    print("2-çizim")
    secim = input("seçiminiz: ")
    if secim == "1": oyunmenu()
    if secim == "2":
        print("güzel çizimler")
        cizimmenu
    if int(secim)<1 or int(secim)>2:
        print("yanlıs seçim")
    menu()
def oyunmenu():
    print("1-yılan")
    print("2-tetris")
    secim = input("seçiminiz: ")
    if secim == "1": print("yılan oyunu kodlar")
    if secim == "2":
        print("tetris oyununa geçildi")

def cizimmenu():
    print("kare")
    print("üçgen")
print("vektörel app")

menu()
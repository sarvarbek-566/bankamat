import time
class BankHisok:
    def __init__(self,ism,balans,pinkod):
        self.ism = ism
        self.__balans = balans
        self.__pinkod = pinkod
        
    def balans_korish(self):
        print(f'sizning balansingiz {self.__balans}')
        
    def pul_qoshish(self, miqdor):
        self.__balans += miqdor
        print(f'{self.ism} siz {miqdor}$ miqdorda pul qushdingiz endi sizning balansingiz {self.__balans}$: ni tashkil etadi')

    def pul_olish(self, miqdor):
        if miqdor <= self.__balans:
            self.__balans -= miqdor
            print(f'Siz muvofaqyatli {miqdor}$ pulni yechib oldingiz endi sizning balansingiz {self.__balans}')
        else:
            print('balansingizda uncha pul yoq')

    def pinkod_uzgartirish(self, pinkod):
        self.__pinkod = pinkod
        print(f'sizning yangi pin kodingiz {self.__pinkod}')
    
foydalanuvchi = BankHisok('sarvar', 40000, 5454)
while True:
    print('1-Balansni korish \n 2-pul qoshish\n 3-pul olish\n 4- pin kod uzgartirish \n 5- chiqish')
    surash = input('Tanlovingizni kiriting: ')
    if surash == '1':
        foydalanuvchi.balans_korish()
    elif surash == "2":
        miqdor = float(input('qancha: '))
        foydalanuvchi.pul_qoshish(miqdor)
    elif surash == '3':
        miqdor = float(input('qancha: '))
        foydalanuvchi.pul_olish(miqdor)
    elif surash == '4':
        newpin = int(input('pin kod uchun 4 ta raqam kiriting: '))
        foydalanuvchi.pinkod_uzgartirish(newpin)
    elif surash == '5':
        break
    else:
        print('boshqa narsa kiritganga uxshaysiz')
    time.sleep(5)
    
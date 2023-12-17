import tkinter as tk
from datetime import datetime


def birthday_information():

    #当日の日付との差分を出す関数
    def delta_day(date):

        #今日の日付と時刻
        dt_now = datetime.now().date()#dateオブジェクトで今日の日付を取得
        
        #日付の差分を出す
        delta=dt_now-date#日付の差分を計算
        delta=delta.days#日数のみを取得

        life_label=tk.Label(text="誕生日から今日までの日数は"+str(delta)+"日です", font=('*', 12))
        life_label.place(x=40, y=100)
        
    #星座を出す関数
    def zodiac(date):

        #birthdayから月と日を取得
        birthmonth = date.month
        birthday = date.day


        #星座のリスト
        zodiac = [
            ["山羊座", 12, 22],
            ["水瓶座", 1, 20],
            ["魚座", 2, 19],
            ["牡羊座", 3, 21],
            ["牡牛座", 4, 20],
            ["双子座", 5, 21],
            ["蟹座", 6, 22],
            ["獅子座", 7, 23],
            ["乙女座", 8, 23],
            ["天秤座", 9, 23],
            ["蠍座", 10, 24],
            ["射手座", 11, 23]
        ]

        for i in range(len(zodiac)):
            if zodiac[i][1] == int(birthmonth):
                if zodiac[i][2] <= int(birthday):
                    zodiac=str(zodiac[i][0])
                    zodiac_label=tk.Label(text="あなたの星座は"+zodiac+"です", font=('*', 12))
                    zodiac_label.place(x=40, y=120)
                    break
                else:
                    zodiac=str(zodiac[i-1][0])
                    zodiac_label=tk.Label(text="あなたの星座は"+zodiac+"です", font=('*', 12))
                    zodiac_label.place(x=40, y=120)
                    break
            
    #干支を出す関数
    def eto(date):
        birthyear=date.year

        #十干十二支定義
        KAN = {4:'甲',5:'乙',6:'丙',7:'丁',8:'戊',9:'己',0:'庚',1:'辛',2:'壬',3:'癸'}
        SHI = {4:'子',5:'丑',6:'寅',7:'卯',8:'辰',9:'巳',10:'午',11:'未',0:'申',1:'酉',2:'戌',3:'亥'}

        #十干十二支を取得
        kan = int(birthyear) % 10
        shi = int(birthyear) % 12

        eto_label=tk.Label(text="あなたの干支は"+KAN[kan]+SHI[shi]+"です", font=('*', 12))
        eto_label.place(x=40, y=140)


    day=entry.get()#エントリーに入力した値をstrで取得
    enter_date = datetime.strptime(day, '%Y/%m/%d')#入力した値をdatetimeオブジェクトに変換
    enter_date = enter_date.date()#dateオブジェクトに変換

    delta_day(enter_date)
    zodiac(enter_date) 
    eto(enter_date)


#ウィンドウの設定
root = tk.Tk()
root.title("誕生日についてのあれこれ")
root.geometry("380x200")

label_top = tk.Label(root, text="誕生日をYYYY/MM/DDの形で入力してください")
#表示する
label_top.place(x=40, y=20)

#誕生日入力のエントリー 
entry = tk.Entry(root)
entry.place(x=40, y=40)

#ボタン
button = tk.Button(root, text="情報取得", command=birthday_information)
button.place(x=40, y=70)

root.mainloop()
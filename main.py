import tkinter


class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=650, borderwidth=1, relief="groove")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        button = tkinter.Button(self, text="実行", command=self.submit)
        button.pack()

        # テキスト
        self.text = tkinter.Entry(self, width=30)
        self.text.pack()

        # テキストエリア
        self.text_area = tkinter.Text(self, width=20, height=10)
        self.text_area.pack()

        # メッセージ
        message = tkinter.Message(self, text="これはアプリです", width=200)
        message.pack()

        # ラベル
        label = tkinter.Label(self, text="ラベル1")
        label.pack()

        # チェックボタン
        self.is_student = tkinter.BooleanVar()
        chk_btn = tkinter.Checkbutton(self, text="学生", variable=self.is_student)
        chk_btn.pack()

        # ラジオボタン
        self.selected_radio = tkinter.StringVar()
        radio_1 = tkinter.Radiobutton(
            self, text="A型", value="A", variable=self.selected_radio
        )
        radio_2 = tkinter.Radiobutton(
            self, text="B型", value="B", variable=self.selected_radio
        )
        radio_3 = tkinter.Radiobutton(
            self, text="O型", value="O", variable=self.selected_radio
        )
        radio_4 = tkinter.Radiobutton(
            self, text="AB型", value="AB", variable=self.selected_radio
        )
        radio_1.pack()
        radio_2.pack()
        radio_3.pack()
        radio_4.pack()

        # リストボックス
        self.items = ["東京", "千葉", "埼玉", "茨木", "神奈川"]
        list_items = tkinter.StringVar(value=self.items)
        self.list_box = tkinter.Listbox(self, listvariable=list_items)
        self.list_box.pack()

        # スピンボックス
        items = ["大阪", "京都", "兵庫", "滋賀", "和歌山", "奈良"]
        self.sp = tkinter.Spinbox(self, state="readonly", values=items)
        self.sp.pack()

        # メニュー
        menu = tkinter.Menu(self.root)
        menu1 = tkinter.Menu(menu, tearoff=False)
        menu1.add_command(label="画面設定", command=self.screen_setting)
        menu1.add_command(label="音量設定", command=self.volume_setting)
        menu.add_cascade(label="設定", menu=menu1)
        self.root.config(menu=menu)

    def submit(self):
        print("ボタンが押されました")

        text = self.text.get()
        print(f"text: {text}")

        # tkinter.ENDだけだと最後に改行が入るので、-1cを追加して改行を削除
        text_area = self.text_area.get(1.0, tkinter.END + "-1c")
        print(f"text area: {text_area}")

        print(self.is_student.get())

        print(self.selected_radio.get())

        selected_index = self.list_box.curselection()[0]
        print(self.items[selected_index])

        print(self.sp.get())

    def screen_setting(self):
        print("画面設定が押されました")

    def volume_setting(self):
        print("音量設定が押されました")


root = tkinter.Tk()
root.title("sample app")
root.geometry("800x700")
app = Application(root=root)
app.mainloop()

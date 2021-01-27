#!/usr/bin/env python3
import tkinter as tk
import time

root = tk.Tk()


class TimeCounter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_val()
        self.create_widgets()
        self.count_time()

    def init_val(self):
        """init_val"""
        # self.time_delta = timedelta()
        # self.second_delta = timedelta(seconds=1)
        self.time_delta = 0

        # self.trigle_date_val = tk.StringVar(
        #     value=datetime.today().strftime("%Y-%m-%d 周%w")
        # )
        # self.trigle_time_val = tk.StringVar(value=datetime.today().strftime("%H:%M:%S"))
        self.trigle_datetime_val = tk.StringVar(
            value=time.strftime("trigled in  %H:%M 周%w %Y-%m-%d ", time.localtime())
        )
        self.counted_time_val = tk.StringVar()

    def create_widgets(self):
        """create_widgets"""

        # self.master.geome
        # self.trigle_date_label = tk.Label(
        #     self, textvariable=self.trigle_date_val, font=("", 10)
        # )
        # self.trigle_time_label = tk.Label(
        #     self, textvariable=self.trigle_time_val, font=("", 10)
        # )
        self.trigle_datetime_label = tk.Label(
            self, textvariable=self.trigle_datetime_val, font=("", 10)
        )
        self.counted_time_label = tk.Label(
            self, textvariable=self.counted_time_val, font=("", 80)
        )

        self.counted_time_label.pack(expand=1)
        self.trigle_datetime_label.pack()
        # self.trigle_date_label.pack(expand=0)
        # self.trigle_time_label.pack(expand=0)

    def count_time(self):
        """count_time"""
        self.time_delta += 1
        self.counted_time_val.set(time.strftime("%H:%M:%S", time.gmtime(self.time_delta)))

        self.master.after(1000, self.count_time)


"""程序入口"""


# def main():
#     global trigle_date, counted_time
#     root.title("珍惜时间")
#     trigle_date = tk.StringVar()
#     counted_time = tk.StringVar()

#     trigle_date.set(cur_date)

#     l2 = tk.Label(root, textvariable=trigle_date, font=("Arial", 20))
#     l1 = tk.Label(root, textvariable=counted_time, font=("", 50))

#     l2.pack(expand=1)
#     l1.pack(expand=1)

#     count_time()

#     # panel1 = tk.Frame(root)
#     # panel1.pack(expand=1)

#     root.mainloop()


"""程序入口"""

if __name__ == "__main__":
    # main()
    app = TimeCounter(master=root)
    app.mainloop()
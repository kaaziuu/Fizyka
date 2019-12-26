from tkinter import *
import json
from old import licz as h_f
from ruchob import licz as p_d

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.main_frame = Frame(self.master)
        self.centers = {}
        self.load_centers()
        self.lis = None
        self.main_view()
        self.main_frame.pack()

    # ladowanie z json osrodkow
    def load_centers(self):
        with open('save.json', 'r') as f:
            read = f.read()
            self.centers = json.loads(read)
        # print(self.centers)

    # metoda czysci ekran lub frame
    def cls(self, frame=None):
        if frame:
            frame.destory()
        else:
            for child in self.main_frame.winfo_children():
                child.destroy()

    # metoda pokazuje glowne menu
    def main_view(self):
        self.cls()
        print("test")
        frame = Frame(self.main_frame)
        btn1 = Button(frame, text='dodaj osrodek', width=20, command=self.add_centers)
        btn1.grid(row=0, column=0)

        btn2 = Button(frame, text='pokaz osrodki', width=20, command=self.show_centers)
        btn2.grid(row=1, column=0)

        btn3 = Button(frame, text='olbicz odleglosc', width=20, command=self.how_far)
        btn3.grid(row=2, column=0)

        btn4 = Button(frame, text='oblicz predkosc detektora', width=20)
        btn4.grid(row=3, column=0)

        btn5 = Button(frame, text="nie wiem co to robi XD", width=20)
        btn5.grid(row=4, column=0)
        frame.pack()

    # pokazuje wszystkie zapisane osrodki
    def show_centers(self, is_add=False, other_frame=None, show_mode=False):
        frame = None
        if not is_add and not show_mode:
            self.cls()
            frame = Frame(self.main_frame)
        else:
            frame = other_frame
        scroll = Scrollbar(frame)
        scroll.grid(row=0, column=1, sticky=NS+W)
        self.lis = Listbox(frame, yscrollcommand=scroll.set)
        for center, item in self.centers.items():
            self.lis.insert(END, f"{center} - {item}")
        self.lis.grid(row=0, column=0, sticky=E)
        scroll.config(command=self.lis.yview())
        if not is_add and not show_mode:
            exit_btn = Button(frame, text='powrot', command=self.main_view)
            exit_btn.grid(row=1, column=0, columnspan=2, sticky=EW)
        frame.pack()

    # metoda dodaje lub usówa osrodki
    def add_centers(self):
        self.cls()
        frame = Frame(self.main_frame)
        self.show_centers(True, frame)
        lb = Label(frame, text='nazwa osrodka: ')
        lb.grid(row=1, column=0)

        entr = Entry(frame)
        entr.grid(row=1, column=1)

        lb = Label(frame, text='predkosc: ')
        lb.grid(row=2, column=0)

        entr2 = Entry(frame)
        entr2.grid(row=2, column=1)

        btn1 = Button(frame, text="add", command=lambda: self.add(entr.get(), float(entr2.get())))
        btn1.grid(row=3, column=0)

        btn1 = Button(frame, text="remove", command=lambda: self.remove(entr.get()))
        btn1.grid(row=3, column=1)

        exit_btn = Button(frame, text='powrot', command=self.main_view)
        exit_btn.grid(row=4, column=0, columnspan=2, sticky=EW)

        frame.pack()

    # metoda dodaje ośrodki do listy i zapisuje je
    def add(self, name, speed):
        if not name in self.centers.keys():
            self.centers[name] = speed
            with open('save.json', 'w') as f:
                json_tab = json.dumps(self.centers)
                f.write(json_tab)
            self.lis.insert(END, f"{name} - {speed}")

    def remove(self, name):
        print(name)
        if name in self.centers.keys():
            speed = self.centers[name]
            del self.centers[name]
            with open('save.json', 'w') as f:
                json_tab = json.dumps(self.centers)
                f.write(json_tab)

            index = self.lis.get(0, END).index(f'{name} - {speed}')
            self.lis.delete(index)

    # metoda pokazuje jak daleko jest obiekt oba stateczne
    def how_far(self,show_result=False, **kwargs):
        self.cls()
        print(kwargs)
        frame = Frame(self.main_frame)
        self.show_centers(other_frame=frame, show_mode=True)

        lb_1 = Label(frame, text="Podaj czas po ktorym dzwiek powrocil do zrodla w s: ")
        lb_1.grid(row=1, column=0)
        time = Entry(frame)
        time.grid(row=1, column=1)

        lb_2 = Label(frame, text="Podaj nazwe osrodka lub predkosc dzwieku w osrodku: ")
        lb_2.grid(row=2, column=0)
        center = Entry(frame)
        center.grid(row=2, column=1)

        btn = Button(frame, text='licz', command=lambda: self.how_far(show_result=True, time=time.get(), center=center.get()))
        btn.grid(row=3, column=0, columnspan=2)

        result_lb = Label(frame, text='wynik: ')
        result_lb.grid(row=4, column=0, columnspan=2, sticky=EW)

        if show_result:
            print(kwargs)
            result = self.how_far_result(kwargs['time'], kwargs['center'])
            result_label = Label(frame, text=f'Odleglosc wynosi: {result}')
            result_label.grid(row=5, column=0, columnspan=2, sticky=EW)

        frame.pack()


    # oblicznie odleglosci
    def how_far_result(self, time, center):
        if center in self.centers.keys():
            center = self.centers[center]
        else:
            center = float(center)
        time = float(time)
        return h_f(time, center)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400")
    root.title("Project")
    app = App(root)
    app.mainloop()
    app.destroy()
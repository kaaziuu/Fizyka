from tkinter import *
import json
from calc import how_far as h_f
from calc import detector_speed as p_d
from calc import calculations as calc
from calc import Hz

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

        btn4 = Button(frame, text='oblicz predkosc detektora', width=20, command=self.detector_speed)
        btn4.grid(row=3, column=0)

        btn5 = Button(frame, text="wiele pomiarow", width=20, command=self.calculations_p1)
        btn5.grid(row=4, column=0)

        btn6 = Button(frame, text="czestotliwosc fali", width=20, command=self.Hz_calc)
        btn6.grid(row=5, column=0)

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

        lb_1 = Label(frame, text="Podaj czas po ktorym\n dzwiek powrocil do zrodla w s: ")
        lb_1.grid(row=1, column=0)
        time = Entry(frame)
        time.grid(row=1, column=1)

        lb_2 = Label(frame, text="Podaj nazwe osrodka\n lub predkosc dzwieku w osrodku: ")
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

        exit_btn = Button(frame, text='powrot', command=self.main_view)
        exit_btn.grid(row=6, column=0, columnspan=2, sticky=EW)

        frame.pack()

    # oblicznie odleglosci
    def how_far_result(self, time, center):
        center = self.center_speed(center)
        time = float(time)
        return h_f(time, center)

    def center_speed(self, center):
        if center in self.centers.keys():
            center = self.centers[center]
        else:
            center = float(center)

        return center

    def detector_speed(self, show_result=False, **kwargs):
        self.cls()
        frame = Frame(self.main_frame)
        self.show_centers(other_frame=frame, show_mode=True)

        lb_1 = Label(frame, text="Podaj czestotliwosc emisji: ")
        lb_1.grid(row=1, column=0)
        frequency_s = Entry(frame)
        frequency_s.grid(row=1, column=1)

        lb_2 = Label(frame, text="Podaj nazwe osrodka\n lub predkosc dzwieku w osrodku: ")
        lb_2.grid(row=2, column=0)
        center = Entry(frame)
        center.grid(row=2, column=1)

        lb_3 = Label(frame, text="Podaj czestotliwosc zwrotna: ")
        lb_3.grid(row=3, column=0)
        frequency_e = Entry(frame)
        frequency_e.grid(row=3, column=1)

        btn = Button(frame, text='licz', command=lambda: self.detector_speed(show_result=True, frequency_s=frequency_s.get(), frequency_e=frequency_e.get(), center=center.get()))
        btn.grid(row=4, column=0, columnspan=2)

        result_lb = Label(frame, text='wynik: ')
        result_lb.grid(row=5, column=0, columnspan=2, sticky=EW)

        if show_result:
            kwargs['center'] = self.center_speed(kwargs['center'])
            result = p_d(kwargs['center'], float(kwargs['frequency_s']), float(kwargs['frequency_e']))
            print(result)
            rst = Label(frame, text=f"Predkosc detektora wynosi: {result} m/s")
            rst.grid(row=6, column=0, columnspan=2, sticky=EW)

        exit_btn = Button(frame, text='powrot', command=self.main_view)
        exit_btn.grid(row=7, column=0, columnspan=2, sticky=EW)

        frame.pack()

    def calculations_p1(self, how_many_oth = None, isUpdate = False):
        self.cls()
        frame = Frame(self.main_frame)
        self.show_centers(other_frame=frame, show_mode=True)
        if not isUpdate:
            how_many_lb = Label(frame, text='ilosc_pomiarow: ')
            how_many_lb.grid(row=1, column=0)
            how_many = Entry(frame)
            how_many.grid(row=1, column=1, sticky=W)
            btn = Button(frame, text='dalej', command=lambda: self.calculations_p1(how_many.get(), True))
            btn.grid(row=2, column=0, columnspan=2, sticky=EW)

        if isUpdate:
            Label(frame, text='Podaj nazwe osrodka lub predkosc\n dzwieku w osrodku: ').grid(row=3, column=0)
            center_entr = Entry(frame)
            center_entr.grid(row=3, column=1)

            Label(frame, text='Podaj okres fali: ').grid(row=4, column=0)
            wave_entr = Entry(frame)
            wave_entr.grid(row=4, column=1)

            entrys = []
            for i in range(1, int(how_many_oth)+1):
                Label(frame, text=f"czas {i}").grid(row=i+4, column=0)
                entry = Entry(frame)
                entry.grid(row=i+4, column=1)
                entrys.append(entry)

            btn_calc = Button(frame, text='licz', command=lambda: self.calculations_p2(entrys, wave_entr.get(), center_entr.get()))
            btn_calc.grid(row=98, column=0, columnspan=2, sticky=EW)
        exit_btn = Button(frame, text='wroc', command=self.main_view)
        exit_btn.grid(row=99, column=0, columnspan=2, sticky=EW)
        frame.pack()

    def calculations_p2(self, entrys, waves, center):
        times = [int(time.get()) for time in entrys]
        center = self.center_speed(center)
        data = calc(center, float(waves), times)
        distansces = data[0]
        speeds = data[1]
        self.cls()
        frame = Frame(self.main_frame)

        Label(frame, text='time').grid(row=0, column=0)
        scroll_1 = Scrollbar(frame)
        scroll_1.grid(row=1, column=1, sticky=W+NS)
        list_1 = Listbox(frame, yscrollcommand=scroll_1.set)
        for i, time in enumerate(times):
            list_1.insert(END, f"{i} - {time}")
        list_1.grid(row=1, column=0)
        scroll_1.config(command=list_1.yview())

        Label(frame, text='predkosc').grid(row=0, column=2)
        scroll_2 = Scrollbar(frame)
        scroll_2.grid(row=1, column=3, sticky=W+NS)
        list_2 = Listbox(frame, yscrollcommand=scroll_2.set)
        for i, speed in enumerate(speeds):
            list_2.insert(END, f"{i} - {speed}")
        list_2.grid(row=1, column=2)
        scroll_2.config(command=list_2.yview())

        Label(frame, text='odleglosc').grid(row=0, column=4)
        scroll_3 = Scrollbar(frame)
        scroll_3.grid(row=1, column=5, sticky=W+NS)
        list_3 = Listbox(frame, yscrollcommand=scroll_3.set)
        for i, dis in enumerate(distansces):
            list_3.insert(END, f"{i} - {dis}")
        list_3.grid(row=1, column=4)
        scroll_3.config(command=list_3.yview())

        exit_btn = Button(frame, text='wroc', command=self.main_view)
        exit_btn.grid(row=99, column=0, sticky=EW)

        agian_btn = Button(frame, text='powtorz', command=self.calculations_p1)
        agian_btn.grid(row=99, column=2, sticky=EW)


        frame.pack()


    def Hz_calc(self, is_result=False, **kwargs):
        self.cls()
        frame = Frame(self.main_frame)
        self.show_centers(other_frame=frame, show_mode=True)

        Label(frame, text="predkosc obserwatora").grid(row=1, column=0)
        Label(frame, text="predkosc fali\n lub nazwa osrodka").grid(row=2, column=0)
        Label(frame, text="dlugosc fali").grid(row=3, column=0)
        Label(frame, text="czas dotarcia").grid(row=4, column=0)

        observer_speed = Entry(frame)
        observer_speed.grid(row=1, column=1)

        center_entr = Entry(frame)
        center_entr.grid(row=2, column=1)

        lenght_wave = Entry(frame)
        lenght_wave.grid(row=3, column=1)

        time_entr = Entry(frame)
        time_entr.grid(row=4, column=1)

        btn = Button(frame, text='licz', command=lambda: self.Hz_calc(True,
                                                                      observer_speed=observer_speed.get(),
                                                                      center_entr=center_entr.get(),
                                                                      lenght_wave=lenght_wave.get(),
                                                        time_entr=time_entr.get()))

        btn.grid(row=5, column=0, columnspan=2, sticky=EW)
        if is_result:
            kwargs['center_entr'] = self.center_speed(kwargs['center_entr'])
            result = Hz(float(kwargs['observer_speed']),
                        float(kwargs['center_entr']),
                        float(kwargs['lenght_wave']),
                        float(kwargs['time_entr']))

            Label(frame, text=f'wynik to {result}').grid(row=6, column=0, columnspan=2)

        exit_btn = Button(frame, text='wroc', command=self.main_view)
        exit_btn.grid(row=99, column=0, sticky=EW)

        frame.pack()

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400")
    root.title("Project")
    app = App(root)
    app.mainloop()
    app.destroy()
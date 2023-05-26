from tkinter import *
import tkinter.font as tkfont
import mp3_snapsave as mp3
import mp4_savefrom as mp4
import get_urllist_musicpaty as mp3_list
import json
import multiprocessing


def process_download_mp3():
    with open('pach_download.txt', 'r') as f:
        pach = f.read()

    mp3.download(pach)

def process_download_mp3_list():
    mp3_list.get_urllist()

def process_download_mp4():
    with open('pach_download.txt', 'r') as f:
        pach = f.read()

    mp4.download(pach)

def process_download_mp3_list_debag():
    e = multiprocessing.Process(target = process_download_mp3_list)
    q = multiprocessing.Process(target = process_download_mp3)

    e.start()
    e.join()
    q.start()
    q.join()

def main():
    def input_get_mp3():
        pach = input_pachdownload.get()
        url = [input_urlinput.get()]
        with open('pach_download.txt', 'w') as f:
            f.write(pach)

        with open('Temp.json', 'w') as f:
            json.dump(url, f, indent=4, ensure_ascii=False)

        url_share = url[-1].split('=')[-1]
        if url_share == 'share':
            q = multiprocessing.Process(target = process_download_mp3)
            q.start()
            # q.join()
        else:
            e = multiprocessing.Process(target = process_download_mp3_list_debag)
            e.start()
            # e.join()


    def input_get_mp4():
        pach = input_pachdownload.get()
        url = [input_urlinput.get()]
        with open('pach_download.txt', 'w') as f:
            f.write(pach)

        with open('Temp.json', 'w') as f:
            json.dump(url, f, indent=4, ensure_ascii=False)

        q = multiprocessing.Process(target = process_download_mp4)
        q.start()
        # q.join()


    root = Tk()

    with open('pach_download.txt', 'r') as f:
        pach_download = f.read()
    input_pachdownload_var = StringVar()
    input_pachdownload_var.set(pach_download)

    COLOR_BACKGRAUND = '#212121'
    COLOR_MAINFONT = '#04ff00'
    COLOR_INFOFONT = '#e600ff'
    COLOR_BUTTON = '#ff0000'
    COLOR_BLACK = '#000000'

    custom_font_main = tkfont.Font(family="Montserrat-SemiBold", size=14)
    custom_font_button = tkfont.Font(family='Montserrat-Bold.ttf', size=18)

    WIDTH = int(root.winfo_screenwidth() * 0.6)
    HEIGHT = int(root.winfo_screenheight() * 0.4)

    WIDTH = 500
    HEIGHT = 300

    root.geometry(f"{WIDTH}x{HEIGHT}")  # Размер окна
    root.resizable(height=False, width=False)
    root.title('Download youtube.mp3')
    # root.iconphoto(True, PhotoImage(file=('icon.ico')))
    root['bg'] = COLOR_BACKGRAUND

    label_pachdownload = Label(root, text='Pach download')
    label_urlinput = Label(root, text='Input URL')
    label_answer = Label(root)

    input_pachdownload = Entry(root, textvariable=input_pachdownload_var)
    input_urlinput = Entry(root)

    button_download_mp3 = Button(root, text='Download mp3', command=input_get_mp3)
    button_download_mp4 = Button(root, text='Download mp4', command=input_get_mp4)

    list_vidget_label = [label_pachdownload, label_urlinput, label_answer]
    list_vidget_input = [input_pachdownload, input_urlinput]
    list_vidget_button = [button_download_mp3, button_download_mp4]

    for label in list_vidget_label:
        label.config(fg=COLOR_MAINFONT, bg=COLOR_BACKGRAUND, font=custom_font_main)

    for input in list_vidget_input:
        input.config(fg=COLOR_INFOFONT, bg=COLOR_BACKGRAUND, font=custom_font_main)

    for button in list_vidget_button:
        button.config(fg=COLOR_BUTTON, bg=COLOR_BACKGRAUND, font=custom_font_main, activebackground=COLOR_BLACK, activeforeground=COLOR_BUTTON)


    label_pachdownload.place(x=50, y=20, width=150, height=40)
    label_urlinput.place(x=300, y=20, width=150, height=40)
    label_answer.place(x=200, y=250, width=100, height=40)

    input_pachdownload.place(x=20, y=80, width=200, height=40)
    input_urlinput.place(x=280, y=80, width=200, height=40)

    button_download_mp3.place(x=WIDTH * 0.35, y=150, width=150, height=50)
    button_download_mp4.place(x=WIDTH * 0.35, y=210, width=150, height=50)

    # def handle_paste(event):
    #     text = root.clipboard_get()
    #     input_urlinput.insert(INSERT, text)

    # input_urlinput.bind("<Control-v>", handle_paste)


    root.mainloop()


if __name__ == '__main__':
    main()
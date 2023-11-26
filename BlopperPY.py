#import modules
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser

#root configuration
root = tk.Tk(className="BlopperPY")
root.title("BlopperPY")
root.geometry("600x460")
root.resizable(width=False, height=False)
root.config(background="#451952")
icon = tk.PhotoImage(file="bpy_icon.png")
root.iconphoto(True,icon)

#commands
def exit():
	root.destroy()

def about():
	tk.messagebox.showinfo(title="about this application", message="this is a pentesting/hacking simulator that pretends to do that. It doesn't harm your computer or add viruses." "\n" "All of the things it does are fake and are meant only for fun!! Please remember that." "\n" "This application is open source and licensed under the BSD-3 Clause license." "\n" "Proudly programmed in Ubuntu!!" "\n" "The mascot (Blopperina) and all of her artwork are licensed under CC-BY-SA 4.0.")
	
def openfile():
	filedialog.askopenfilename(title="run scripts or open files...")
	
def gitrepo():
	webbrowser.open_new(r"https://github.com/01adrianrdgz/BlopperPY")

#terminal window class
class terminalwindow(tk.Toplevel):
	
	def __init__(self, root = None):

		super().__init__(root = root)
		self.title("BlopperPY terminal")
		self.geometry("300x300")
		self.resizable(width=False, height=False)
		self.config(background="#451952")
		
		bpina_wl = Image.open("blopperina_hack.png")
		bpina_wl = bpina_wl.resize((120, 120,), Image.ANTIALIAS)
		self.photo = ImageTk.PhotoImage(bpina_wl)
		blopperina_wl = tk.Label(self, image=self.photo, background="#451952")
		blopperina_wl.place(x=5, y=175)
		
		text_user = tk.Entry(self, insertbackground="#F39F5A", background="#451952", foreground="#F39F5A", highlightbackground="#F39F5A", highlightcolor="#F39F5A", borderwidth=0, font=("System", 14))
		text_user.insert(tk.END, "")
		text_user.place(x=5, y=15)
		
		title = tk.Label(self, anchor="w", justify="left", text="type the command you" "\n" "want to use and then click" "\n" "on the run button", background="#451952", foreground="#F39F5A", font=("System", 14))
		title.place(x=5, y=50)
		
		button = tk.Button(self, text="RUN CODE", background="#F39F5A", foreground="#451952", activebackground="#451952", activeforeground="#F39F5A", font=("System", 16), command=exit)
		button.config(highlightbackground="#F39F5A", borderwidth=0)
		button.place(x=5, y=130)
		
		self.focus_set()
		self.grab_set()
		
#wireless drivers window class
class wirelessdrivers(tk.Toplevel):
	
	def __init__(self, root = None):

		super().__init__(root = root)
		self.title("searching for wireless drivers to hack...")
		self.geometry("300x300")
		self.resizable(width=False, height=False)
		self.config(background="#451952")
		
		bpina_wl = Image.open("wireless_blopperina.png")
		bpina_wl = bpina_wl.resize((130, 130,), Image.ANTIALIAS)
		self.photo = ImageTk.PhotoImage(bpina_wl)
		blopperina_wl = tk.Label(self, image=self.photo, background="#451952")
		blopperina_wl.place(x=5, y=160)
		
		title = tk.Label(self, anchor="w", justify="left", text="if your Bluetooth settings" "\n" "are on, then expect phones" "\n" "and wifi routers to" "\n" "appear here.", background="#451952", foreground="#F39F5A", font=("System", 14))
		title.place(x=5, y=20)
		
		title = tk.Label(self, anchor="w", justify="left", text="...", background="#451952", foreground="#F39F5A", font=("System", 16))
		title.place(x=5, y=120)
		
		self.after(10000, lambda: self.destroy())
		
		self.focus_set()
		self.grab_set()

#graphical interface
bpina = Image.open("blopperina.png")
bpina = bpina.resize((310, 310,), Image.ANTIALIAS)
bpina_img = ImageTk.PhotoImage(bpina)
blopperina = tk.Label(root, image=bpina_img, background="#451952")
blopperina.place(x=295, y=30)

frame = tk.Frame(root, width=585, height=2)
frame.pack(fill="both")
frame.config(background="#F39F5A")
frame.place(x=5, y=15)

title = tk.Label(root, text="BlopperPY", background="#451952", foreground="#F39F5A", font=("System", 16))
title.place(x=5, y=2)

button = tk.Button(root, text="about this application", background="#451952", foreground="#F39F5A", activebackground="#F39F5A", activeforeground="#451952", font=("System", 14), command=about)
button.config(highlightbackground="#F39F5A", borderwidth=0)
button.place(x=5, y=50)

button = tk.Button(root, text="open files to hack...", background="#451952", foreground="#F39F5A", activebackground="#F39F5A", activeforeground="#451952", font=("System", 14), command=openfile)
button.config(highlightbackground="#F39F5A", borderwidth=0)
button.place(x=5, y=100)

button = tk.Button(root, text="search for wireless drivers", background="#451952", foreground="#F39F5A", activebackground="#F39F5A", activeforeground="#451952", font=("System", 14), command=wirelessdrivers)
button.config(highlightbackground="#F39F5A", borderwidth=0)
button.place(x=5, y=150)

button = tk.Button(root, text="run scripts", background="#451952", foreground="#F39F5A", activebackground="#F39F5A", activeforeground="#451952", font=("System", 14), command=openfile)
button.config(highlightbackground="#F39F5A", borderwidth=0)
button.place(x=5, y=200)

button = tk.Button(root, text="terminal", background="#451952", foreground="#F39F5A", activebackground="#F39F5A", activeforeground="#451952", font=("System", 14), command=terminalwindow)
button.config(highlightbackground="#F39F5A", borderwidth=0)
button.place(x=5, y=250)

button = tk.Button(root, text="exit app", background="#F39F5A", foreground="#451952", activebackground="#451952", activeforeground="#F39F5A", font=("System", 14), command=exit)
button.config(highlightbackground="#F39F5A", borderwidth=0)
button.place(x=5, y=300)

frame = tk.Frame(root, width=585, height=2)
frame.pack(fill="both")
frame.config(background="#F39F5A")
frame.place(x=5, y=350)

title = tk.Label(root, text="made by Adrian Rodriguez", background="#451952", foreground="#F39F5A", font=("System", 14))
title.place(x=5, y=360)

image1 = Image.open("github-mark-white.png")
image1 = image1.resize((60, 60,), Image.ANTIALIAS)
github_img = ImageTk.PhotoImage(image1)
repo = tk.Button(root, image=github_img, background="#451952", foreground="#F39F5A", activebackground="#F39F5A", activeforeground="#451952", command=gitrepo)
repo.config(highlightbackground="#F39F5A", borderwidth=0)
repo.place(x=5, y=390)

#main loop
root.mainloop()

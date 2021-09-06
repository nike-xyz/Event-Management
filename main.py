from tkinter import *
from tkinter import font as tkFont 
from PIL import Image, ImageTk
from tkinter import ttk

root=Tk()
homepage_res = "450x450"
root.geometry(homepage_res) #600x400

tc=ttk.Notebook(root, width=650)
tc.pack(pady=0,padx=0)

page0 = Frame(tc)
decor_page=Frame(tc)
cater_page=Frame(tc)
photo_page=Frame(tc)

page0.pack(expand = 1,fill="both")
decor_page.pack(expand = 1,fill="both")
cater_page.pack(expand = 1,fill="both")
photo_page.pack(expand = 1,fill="both") 

tc.add(page0 , text='WELCOME')
tc.add(decor_page , text='DECORATION')
tc.add(cater_page, text="CATERING")
tc.add(photo_page, text="PHOTOGRAPHY")

tc.hide(1)
tc.hide(2)
tc.hide(3)

page0_bg=Image.open("assets/bg3.jpeg")
resize=page0_bg.resize((450, 450),Image.ANTIALIAS)
n_page0_bg=ImageTk.PhotoImage(resize)
bg = Label(page0, image=n_page0_bg)
bg.place(x=0,y=0)

'''
Page 1
'''

font1 = tkFont.Font(size=20, family="Gabriola")
font0 = tkFont.Font(size=25, family="Times New Roman")
width=14

# photo=Image.open("assets/Image.png")
# photo_resized=photo.resize((100,40),Image.ANTIALIAS)
# image=ImageTk.PhotoImage(photo_resized)

title = Label(page0, text="PY Wedding",background="pink", font=font0)
title.pack(pady=10)

def decor():
	tc.select(1)
	tc.hide(0)
	root.geometry("450x420")

decor=Button(page0, text="Decoration", background="white",font=font1, command=decor,width=width, ) 
decor.pack(pady=10)

def cater():
	tc.select(2)
	tc.hide(0)
	root.geometry("650x700")

cat=Button(page0 ,text="Catering",background="white",font=font1, command=cater, width=width)
cat.pack(pady=10)

def photo():
	tc.select(3)
	tc.hide(0)
	root.geometry("400x400")

photo=Button(page0 ,text="Photo",background="white",font=font1, command=photo, width=width)
photo.pack(pady=10)

'''
page2
'''
'''
Labels
'''

def back0():
	tc.select(0)
	tc.hide(1)
	root.geometry(homepage_res)

b_but = Button(decor_page, text="Back", command=back0)
b_but.grid(row=0, column=0)

font2 = tkFont.Font(size=15)

padx=25
pady=25
stage_lbl = Label(decor_page, text="Stage: ", font=font2, padx=padx, pady=pady)
hall_lbl = Label(decor_page, text="Hall: ", font=font2, padx=padx, pady=pady)
entrance_lbl = Label(decor_page, text="Entrance: ", font=font2, padx=padx, pady=pady)
car_lbl = Label(decor_page, text="Car: ", font=font2, padx=padx, pady=pady)

rst=1 #row start
cst=1 #column start
stage_lbl.grid(row=rst, column=cst)
hall_lbl.grid(row=rst+1, column=cst)
entrance_lbl.grid(row=rst+2, column=cst)
car_lbl.grid(row=rst+3, column=cst)

'''
Dropdowns
'''

#Stage-Dropdown
stage_options_dic = {
	"stage 1_(rs:40000)": ("assets/Decor/Stage1.jpeg", 40000),
 	"stage 2_(rs:40000)": ("assets/Decor/Stage2.jpeg", 40000),
 	"stage 3_(rs:30000)": ("assets/Decor/Stage3.jpeg", 30000),
 	"stage 4_(rs:35000)": ("assets/Decor/Stage4.jpeg", 35000),
 	"stage 5_(rs:35000)": ("assets/Decor/Stage5.jpeg", 35000),
 	"stage 6_(rs:38000)": ("assets/Decor/Stage6.jpeg", 38000)
}
stage_options = list(stage_options_dic.keys())
selected_stage = StringVar()
selected_stage.set(stage_options[0])

stage_dropdown = ttk.Combobox(decor_page, width=20, textvariable=selected_stage)
stage_dropdown['values'] = stage_options
stage_dropdown.grid(row=rst, column=cst+1)

#Hall-Dropdown
hall_options_dic = {
	"hall 1_(rs:10000)": ("assets/Decor/Hall1.jpeg", 10000),
	"hall 2_(rs:10000)": ("assets/Decor/Hall2.jpeg", 10000),
	"hall 3_(rs:10000)": ("assets/Decor/Hall3.jpeg", 10000),
	"hall 4_(rs:10000)": ("assets/Decor/Hall4.jpeg", 10000),
	"hall 5_(rs:10000)": ("assets/Decor/Hall5.jpeg", 10000)
}
hall_options = list(hall_options_dic.keys())
selected_hall = StringVar()
selected_hall.set(hall_options[0])

hall_dropdown = ttk.Combobox(decor_page, width=20, textvariable=selected_hall)
hall_dropdown['values'] = hall_options
hall_dropdown.grid(row=rst+1, column=cst+1)

#Entrance-Dropdown
entrance_options_dic = {
	"entry 1_(rs:10000)": ("assets/Decor/Entrance1.jpeg", 10000),
	"entry 2_(rs:10000)": ("assets/Decor/Entrance2.jpeg", 10000),
	"entry 3_(rs:10000)": ("assets/Decor/Entrance3.jpeg", 10000),
	"entry 4_(rs:15000)": ("assets/Decor/Entrance4.jpeg", 15000),
	"entry 5_(rs:15000)": ("assets/Decor/Entrance5.jpeg", 15000),
	"entry 6_(rs:15000)": ("assets/Decor/Entrance6.jpeg", 15000),
	"entry 7_(rs:15000)": ("assets/Decor/Entrance7.jpeg", 15000)
}
entrance_options = list(entrance_options_dic.keys())
selected_entrance = StringVar()
selected_entrance.set(entrance_options[0])

entrance_dropdown = ttk.Combobox(decor_page, width=20, textvariable=selected_entrance)
entrance_dropdown['values'] = entrance_options
entrance_dropdown.grid(row=rst+2, column=cst+1)

#Car-Dropdown
car_options_dic = {
	"car 1_(rs:5000)": ("assets/Decor/Car1.jpeg", 5000),
	"car 2_(rs:4000)": ("assets/Decor/Car2.jpeg", 4000),
	"car 3_(rs:5000)": ("assets/Decor/Car3.jpeg", 5000),
	"car 4_(rs:5000)": ("assets/Decor/Car4.jpeg", 5000),
	"car 5_(rs:5000)": ("assets/Decor/Car5.jpeg", 5000)
}
car_options = list(car_options_dic.keys())
selected_car = StringVar()
selected_car.set(car_options[0])

car_dropdown = ttk.Combobox(decor_page, width=20, textvariable=selected_car)
car_dropdown['values'] = car_options
car_dropdown.grid(row=rst+3, column=cst+1)

'''
Dropdowns
'''

def sub(title, impathlist, imnames):
	global index 
	index= 0

	from PIL import Image, ImageTk		
	sub1 =Toplevel()
	sub1.title(title)
	sub1.geometry('800x630+250+10')

	imlist=[]
	for path in impathlist:
		image = Image.open(path)
		resize=image.resize((800,600),Image.ANTIALIAS)
		ne=ImageTk.PhotoImage(resize)

		imlist.append(ne)

	mylabel=Label(sub1,image=imlist[0])
	mylabel.place(x=0,y=0)

	im_name = Label(sub1, text=imnames[index])
	im_name.place(x=10, y=605)

	def forward(mylabel):
		global index
		index+=1
		if index == len(imlist)-1:
			b_for.configure(state=DISABLED)
		if index>0:
			b_back.configure(state=NORMAL)	
		mylabel.destroy()
		mylabel=Label(sub1,image=imlist[index])
		mylabel.place(x=0,y=0)

		im_name = Label(sub1, text=imnames[index])
		im_name.place(x=10, y=605)

	def back(mylabel):
		global index
		index-=1
		if index == 0:
			b_back.configure(state=DISABLED)
		if index<len(imlist)-1:
			b_for.configure(state=NORMAL)
		mylabel.destroy()
		mylabel=Label(sub1,image=imlist[index])
		mylabel.place(x=0,y=0)

		im_name = Label(sub1, text=imnames[index])
		im_name.place(x=10, y=605)
		
	b_back=Button(sub1,text="<<",command=lambda: back(mylabel),state=DISABLED)
	b_exit=Button(sub1,text="EXIT",command=sub1.destroy)
	b_for=Button(sub1,text=">>",command=lambda: forward(mylabel))
	
	b_back.place(x=350,y=605)
	b_exit.place(x=400,y=605)
	b_for.place(x=450,y=605)

	sub1.mainloop()    

#Stage-preview

stage_images_list= [e[1] for e in stage_options_dic.values()]
stage_paths =  [e[0] for e in stage_options_dic.values()]
stage_preview = Button(decor_page, text="Show Pictures", command=lambda: sub("STAGES", stage_paths, stage_options))
stage_preview.grid(row=rst, column=cst+2, padx=20)

#Hall-preview

hall_images_list= [e[1] for e in hall_options_dic.values()]
hall_paths = [e[0] for e in hall_options_dic.values()]
stage_preview = Button(decor_page, text="Show Pictures", command=lambda: sub("HALLS", hall_paths, hall_options))
stage_preview.grid(row=rst+1, column=cst+2, padx=20)

#Entrance-preview

entrance_images_list= [e[1] for e in entrance_options_dic.values()]
entrance_paths = [e[0] for e in entrance_options_dic.values()]	
stage_preview = Button(decor_page, text="Show Pictures", command=lambda: sub("ENTRANCES", entrance_paths, entrance_options))
stage_preview.grid(row=rst+2, column=cst+2, padx=20)

#Car-preview

car_images_list= [e[1] for e in car_options_dic.values()]
car_paths = [e[0] for e in car_options_dic.values()]	
car_preview = Button(decor_page, text="Show Pictures", command=lambda: sub("CARS", car_paths, car_options))
car_preview.grid(row=rst+3, column=cst+2, padx=20)
#------------

def calc_total():
	global tot_label

	total = stage_options_dic[stage_dropdown.get()][1] + hall_options_dic[hall_dropdown.get()][1] + entrance_options_dic[entrance_dropdown.get()][1] + car_options_dic[car_dropdown.get()][1]
	tot_label.destroy()
	tot_label = Label(decor_page, text=f"Rs.{total}")
	tot_label.grid(row=rst+5, column=cst+1)

tot_button = Button(decor_page, text="Calculate Total: ", command=calc_total)
tot_button.grid(row=rst+5, column=cst)

tot_label = Label(decor_page, text="")
tot_label.grid(row=rst+5, column=cst+1)

'''
Page3
'''
def back1():
	tc.select(0)
	tc.hide(2)
	root.geometry(homepage_res)

b_but = Button(cater_page, text="Back", command=back1)
b_but.grid(row=0, column=0)
	
itemvars = []
itemprices = []
#STARTER - DRINKS
font0 = tkFont.Font(size=15)
stdk = Label(cater_page, text="Starter - Drinks", font=font0)
stdk.grid(row=1, column=1, columnspan=4, padx=10, pady=10, sticky="W")

font1 = tkFont.Font(size=12)

itemvars.append(IntVar())
item1box = Checkbutton(cater_page, variable=itemvars[0], onvalue=1, offvalue=0)
item1box.grid(row=2, column=1, sticky="E")
item1label = Label(cater_page, text="Kokum Juice (rs:30/1cup)", font=font1)
item1label.grid(row=2, column=2, sticky="W")
itemprices.append(30)

itemvars.append(IntVar())
item2box = Checkbutton(cater_page, variable=itemvars[1], onvalue=1, offvalue=0)
item2box.grid(row=3, column=1, sticky="E")
item2label = Label(cater_page, text="Melon Juice (rs:20/1cup)", font=font1)
item2label.grid(row=3, column=2, sticky="W") 
itemprices.append(20)

itemvars.append(IntVar())
item3box = Checkbutton(cater_page, variable=itemvars[2], onvalue=1, offvalue=0)
item3box.grid(row=2, column=3, padx=(30,0), sticky="E")
item3label = Label(cater_page, text="Mango Juice (rs:40/1cup)", font=font1)
item3label.grid(row=2, column=4, sticky="W") 
itemprices.append(40)

itemvars.append(IntVar())
item4box = Checkbutton(cater_page, variable=itemvars[3], onvalue=1, offvalue=0)
item4box.grid(row=3, column=3, padx=(30,0), sticky="E")
item4label = Label(cater_page, text="Lemon Soda (rs:20/1cup)", font=font1)
item4label.grid(row=3, column=4, sticky="W") 
itemprices.append(20)

#STARTER-SNACKS
font0 = tkFont.Font(size=15)
stdk = Label(cater_page, text="Starter - Snacks", font=font0)
stdk.grid(row=5, column=1, columnspan=4, padx=10, pady=(20,10), sticky="W")

font1 = tkFont.Font(size=12)

itemvars.append(IntVar())
item5box = Checkbutton(cater_page, variable=itemvars[4], onvalue=1, offvalue=0)
item5box.grid(row=6, column=1)
item5label = Label(cater_page, text="Soup (rs:50/1plate)", font=font1)
item5label.grid(row=6, column=2, sticky="W") 
itemprices.append(50)

itemvars.append(IntVar())
item6box = Checkbutton(cater_page, variable=itemvars[5], onvalue=1, offvalue=0)
item6box.grid(row=7, column=1)
item6label = Label(cater_page, text="Hara Bhara Kebab (rs:80/1plate)", font=font1)
item6label.grid(row=7, column=2, sticky="W") 
itemprices.append(80)

itemvars.append(IntVar())
item7box = Checkbutton(cater_page, variable=itemvars[6], onvalue=1, offvalue=0)
item7box.grid(row=8, column=1, sticky="E")
item7label = Label(cater_page, text="Peri-Peri Fries (rs:80/1plate)", font=font1)
item7label.grid(row=8, column=2, sticky="W") 
itemprices.append(80)

itemvars.append(IntVar())
item8box = Checkbutton(cater_page, variable=itemvars[7], onvalue=1, offvalue=0)
item8box.grid(row=6, column=3, sticky="E")
item8label = Label(cater_page, text="Swiss Roll (rs:80/1plate)", font=font1)
item8label.grid(row=6, column=4, sticky="W") 
itemprices.append(80)

itemvars.append(IntVar())
item9box = Checkbutton(cater_page, variable=itemvars[8], onvalue=1, offvalue=0)
item9box.grid(row=7, column=3, sticky="E")
item9label = Label(cater_page, text="Noodles (rs:80/1plate)", font=font1)
item9label.grid(row=7, column=4, sticky="W") 
itemprices.append(80)

itemvars.append(IntVar())
item10box = Checkbutton(cater_page, variable=itemvars[9], onvalue=1, offvalue=0)
item10box.grid(row=8, column=3, sticky="E")
item10label = Label(cater_page, text="Cutlet (rs:80/1plate)", font=font1)
item10label.grid(row=8, column=4, sticky="W") 
itemprices.append(80)

#main course

font0 = tkFont.Font(size=15)
stdk = Label(cater_page, text="Main course", font=font0)
stdk.grid(row=10, column=1, columnspan=4, padx=10, pady=(20,10), sticky="W")

font1 = tkFont.Font(size=12)

itemvars.append(IntVar())
item11box = Checkbutton(cater_page, variable=itemvars[10], onvalue=1, offvalue=0)
item11box.grid(row=11, column=1)
item111label = Label(cater_page, text="Roti (rs:25/1plate)", font=font1)
item111label.grid(row=11, column=2, sticky="W") 
itemprices.append(25)

itemvars.append(IntVar())
item12box = Checkbutton(cater_page, variable=itemvars[11], onvalue=1, offvalue=0)
item12box.grid(row=12, column=1)
item122label = Label(cater_page, text="Pulka (rs:30/1plate)", font=font1)
item122label.grid(row=12, column=2, sticky="W") 
itemprices.append(30)

itemvars.append(IntVar())
item13box = Checkbutton(cater_page, variable=itemvars[12], onvalue=1, offvalue=0)
item13box.grid(row=11, column=3, sticky="E")
item133label = Label(cater_page, text="Channa (rs:50/1plate)", font=font1)
item133label.grid(row=11, column=4, sticky="W")
itemprices.append(50) 

itemvars.append(IntVar())
item14box = Checkbutton(cater_page, variable=itemvars[13], onvalue=1, offvalue=0)
item14box.grid(row=12, column=3, sticky="E")
item144label = Label(cater_page, text="Paneer masala (rs:70/1plate)", font=font1)
item144label.grid(row=12, column=4, sticky="W") 
itemprices.append(70)

itemvars.append(IntVar())
item11box = Checkbutton(cater_page, variable=itemvars[14], onvalue=1, offvalue=0)
item11box.grid(row=13, column=1)
item111label = Label(cater_page, text="Rice (rs:40/1plate)", font=font1)
item111label.grid(row=13, column=2, sticky="W") 
itemprices.append(40)

itemvars.append(IntVar())
item12box = Checkbutton(cater_page, variable=itemvars[15], onvalue=1, offvalue=0)
item12box.grid(row=14, column=1)
item122label = Label(cater_page, text="Fried rice (rs:60/1plate)", font=font1)
item122label.grid(row=14, column=2, sticky="W") 
itemprices.append(60)

itemvars.append(IntVar())
item13box = Checkbutton(cater_page, variable=itemvars[16], onvalue=1, offvalue=0)
item13box.grid(row=13, column=3, sticky="E")
item133label = Label(cater_page, text="Rasam (rs:30/1plate)", font=font1)
item133label.grid(row=13, column=4, sticky="W") 
itemprices.append(30)

itemvars.append(IntVar())
item14box = Checkbutton(cater_page, variable=itemvars[17], onvalue=1, offvalue=0)
item14box.grid(row=14, column=3, sticky="E")
item144label = Label(cater_page, text="Sambar (rs:40/1plate)", font=font1)
item144label.grid(row=14, column=4, sticky="W")
itemprices.append(40) 

itemvars.append(IntVar())
item15box = Checkbutton(cater_page, variable=itemvars[18], onvalue=1, offvalue=0)
item15box.grid(row=15, column=1)
item155label = Label(cater_page, text="Curd rice (rs:50/1plate)", font=font1)
item155label.grid(row=15, column=2, sticky="W")
itemprices.append(50) 

#fruit salad

font0 = tkFont.Font(size=15)
stdk = Label(cater_page, text="Fruit salad with Ice cream", font=font0)
stdk.grid(row=16, column=1, columnspan=4, padx=10, pady=(20,10), sticky="W")

font1 = tkFont.Font(size=12)

itemvars.append(IntVar())
item17box = Checkbutton(cater_page, variable=itemvars[19], onvalue=1, offvalue=0)
item17box.grid(row=17, column=1)
item177label = Label(cater_page, text="Apple fruit(rs:20)", font=font1)
item177label.grid(row=17, column=2, sticky="W") 
itemprices.append(20) 

itemvars.append(IntVar())
item18box = Checkbutton(cater_page, variable=itemvars[20], onvalue=1, offvalue=0)
item18box.grid(row=18, column=1)
item188label = Label(cater_page, text="Banana fruit (rs:20)", font=font1)
item188label.grid(row=18, column=2, sticky="W")
itemprices.append(20) 

itemvars.append(IntVar())
item19box = Checkbutton(cater_page, variable=itemvars[21], onvalue=1, offvalue=0)
item19box.grid(row=17, column=3, sticky="E")
item199label = Label(cater_page, text="Mango fruit (rs:20)", font=font1)
item199label.grid(row=17, column=4, sticky="W") 
itemprices.append(20)

itemvars.append(IntVar())
item20box = Checkbutton(cater_page, variable=itemvars[22], onvalue=1, offvalue=0)
item20box.grid(row=18, column=3, sticky="E")
item200label = Label(cater_page, text="Strawberry fruit (rs:20)", font=font1)
item200label.grid(row=18, column=4, sticky="W")
itemprices.append(20)

itemvars.append(IntVar())
item21box = Checkbutton(cater_page, variable=itemvars[23], onvalue=1, offvalue=0)
item21box.grid(row=19, column=1)
item211label = Label(cater_page, text="Chiccu fruit (rs:20)", font=font1)
item211label.grid(row=19, column=2, sticky="W")
itemprices.append(20) 

itemvars.append(IntVar())
item22box = Checkbutton(cater_page, variable=itemvars[24], onvalue=1, offvalue=0)
item22box.grid(row=19, column=3, sticky="E")
item22label = Label(cater_page, text="Mango fruit (rs:20)", font=font1)
item22label.grid(row=19, column=4, sticky="W")
itemprices.append(20)

itemvars.append(IntVar())
item23box = Checkbutton(cater_page, variable=itemvars[25], onvalue=1, offvalue=0)
item23box.grid(row=21, column=1)
item23label = Label(cater_page, text="Butter scotch ice cream (rs:30/scoop)", font=font1)
item23label.grid(row=21, column=2, sticky="W") 
itemprices.append(30)

itemvars.append(IntVar())
item24box = Checkbutton(cater_page, variable=itemvars[26], onvalue=1, offvalue=0)
item24box.grid(row=22, column=1)
item24label = Label(cater_page, text="Vanilla ice cream (rs:25/scoop)", font=font1)
item24label.grid(row=22, column=2, sticky="W") 
itemprices.append(25)

itemvars.append(IntVar())
item25box = Checkbutton(cater_page, variable=itemvars[27], onvalue=1, offvalue=0)
item25box.grid(row=21, column=3, sticky="E")
item25label = Label(cater_page, text="Strawberry ice cream\n (rs:25/scoop)", font=font1)
item25label.grid(row=21, column=4, sticky="W") 
itemprices.append(25)

def cater_tot():
	global cater_tot_label
	total = 0
	for i in range(len(itemvars)):
		total+=itemvars[i].get()*itemprices[i]
	cater_tot_label.destroy()
	cater_tot_label = Label(cater_page, text=f"Rs{total}")
	cater_tot_label.grid(row=0, column=4, padx=10,sticky="W")

cater_tot_button = Button(cater_page, text="Show Total: ", command=cater_tot)
cater_tot_button.grid(row=0, column=3)

cater_tot_label = Label(cater_page, text="")
cater_tot_label.grid(row=0, column=4, padx=10,sticky="W")

'''
Page4
'''
def back2():
	tc.hide(3)
	tc.select(0)
	root.geometry(homepage_res)

b_but = Button(photo_page, text="Back", command=back2)
b_but.grid(row=0, column=0)

#photography
font0 = tkFont.Font(size=15)
stdk = Label(photo_page, text="Photo", font=font0)
stdk.grid(row=1, column=1, columnspan=4, padx=10, pady=10, sticky="W")

font1 = tkFont.Font(size=12)

photo_vars=[]
photo_prices=[]

photo_vars.append(IntVar())
item26box = Checkbutton(photo_page, variable=photo_vars[0], onvalue=1, offvalue=0)
item26box.grid(row=2, column=1)
item266label = Label(photo_page, text="Traditional photo (rs:20000)", font=font1)
item266label.grid(row=2, column=2, ) 
photo_prices.append(20000)

photo_vars.append(IntVar())
item27box = Checkbutton(photo_page, variable=photo_vars[1], onvalue=1, offvalue=0)
item27box.grid(row=3, column=1)
item277label = Label(photo_page, text="Candid photo (rs:30000)", font=font1)
item277label.grid(row=3, column=2, sticky="W") 
photo_prices.append(30000)

font0 = tkFont.Font(size=15)
stdk = Label(photo_page, text="Video", font=font0)
stdk.grid(row=4, column=1, columnspan=4, padx=10, pady=10, sticky="W")

font1 = tkFont.Font(size=12)

photo_vars.append(IntVar())
item28box = Checkbutton(photo_page, variable=photo_vars[2], onvalue=1, offvalue=0)
item28box.grid(row=5, column=1)
item288label = Label(photo_page, text="Traditional video (rs:25000)", font=font1)
item288label.grid(row=5, column=2, sticky="W")
photo_prices.append(25000) 

photo_vars.append(IntVar())
item29box = Checkbutton(photo_page, variable=photo_vars[3], onvalue=1, offvalue=0)
item29box.grid(row=6, column=1)
item299label = Label(photo_page, text="Candid video (rs:50000)", font=font1)
item299label.grid(row=6, column=2, sticky="W") 
photo_prices.append(50000)

photo_vars.append(IntVar())
item30box = Checkbutton(photo_page, variable=photo_vars[4], onvalue=1, offvalue=0)
item30box.grid(row=7, column=1)
item300label = Label(photo_page, text="Drone (rs:20000)", font=font0)
item300label.grid(row=7, column=2, pady=10, sticky="W")
photo_prices.append(20000)  

def photo_tot():
	global photo_tot_label
	total=0
	for i in range(len(photo_prices)):
		total+=photo_vars[i].get()*photo_prices[i]
	photo_tot_label.destroy()
	photo_tot_label=Label(photo_page,text=f"Rs.{total}")
	photo_tot_label.grid(row=8, column=2)	

photo_tot_button = Button(photo_page,text="Calculate total: ", command=photo_tot)
photo_tot_button.grid(row=8, column=1,pady=20)

photo_tot_label=Label(photo_page,text="")
photo_tot_label.grid(row=8, column=2, sticky="W")

root.mainloop()

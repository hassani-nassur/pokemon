import tkinter as tk
from tkinter import ttk
from Class.Fichier import *
import requests,random
from PIL import Image,ImageTk
from io import BytesIO
from Class.TypePockemone import *

class Combat(Fichier):
    
    def __init__(self,fenetre):
        
        Fichier.__init__(self)
        self.fenetre = fenetre
        self.names_pockemone = []
        self.pockemone_player = None
        self.pockemone_ordinateur = None
        
        self.fenetre.geometry("600x500+500+160")
        self.fenetre.resizable(width=False,height=False)
        self.menu_game()
    
    # recuperation de la liste des pockemone
    def get_pockemon(self):
        for i in self.get_data_files("db\pokedex.json"):
            self.names_pockemone.append(i["name"]["french"]) 
    
    # initialisation des objet pocketmone 
    def create_pockemone(self):
        
        self.pockemone_player = TypePockemone(list_pockemone.get())
        self.pockemone_ordinateur = TypePockemone(random.choice(self.names_pockemone))
        
        self.clean_fenetre()
        self.display()
    
    # fonction qui s'occupe de l'affichage
    def display(self):
       
        # affichage des informations du pockemone player
        requet_http1 = requests.get(self.pockemone_player._images["thumbnail"])
        self.image_player = ImageTk.PhotoImage(Image.open(BytesIO(requet_http1.content)))
        
        pockemone_image_player = tk.Label(self.fenetre,text=self.pockemone_player.get_name(),image=self.image_player)
        pockemone_image_player.place(x=50,y=300)
        
        canvas_Element_player = tk.Canvas(self.fenetre,width=350,height=120,bg="#c2d4f6")
        canvas_Element_player.place(x=200,y=300)
        
        # affichage du vie 
        label_life_player = tk.Label(canvas_Element_player,text="Vie : {}".format(self.pockemone_player.get_point_life()))
        label_life_player.place(x=10,y=10)
        
        label_name_player = tk.Label(canvas_Element_player,text="Name : {}".format(self.pockemone_player.get_name()))
        label_name_player.place(x=10,y=30)
        
        label_puissance_attak_player = tk.Label(canvas_Element_player,text="Puissance d'attaque : {}".format(self.pockemone_player.get_puissance_attaque()))
        label_puissance_attak_player.place(x=10,y=50)
        
        label_puissance_defence_player = tk.Label(canvas_Element_player,text="Puissance de defence: {}".format(self.pockemone_player.get_defence()))
        label_puissance_defence_player.place(x=10,y=70)
        
        y = 100
        x = 10
        for i in self.pockemone_player.get_type_names():
            label_type_player = tk.Button(canvas_Element_player,text=i)
            label_type_player.place(x=x,y=y)
            
            x +=50
            if x == 300:
                x = 10
                y += 40
        canvas_Element_player.bind_all('<Button>',self.batail)
        
        
        # affichage des information du pockemone ordinateuR
        requet_http2 = requests.get(self.pockemone_ordinateur._images["thumbnail"])
        self.image_ordinateur = ImageTk.PhotoImage(Image.open(BytesIO(requet_http2.content)))
        
        pockemone_image_ordinateur = tk.Label(self.fenetre,text=self.pockemone_ordinateur.get_name(),image=self.image_ordinateur)
        pockemone_image_ordinateur.place(x=450,y=50)
        
        canvas_Element_ordinateur = tk.Canvas(self.fenetre,width=350,height=120,bg="#c2d4f6")
        canvas_Element_ordinateur.place(x=60,y=50)
        
        label_life_ordinateur = tk.Label(canvas_Element_ordinateur,text="Vie : {}".format(self.pockemone_ordinateur.get_point_life()))
        label_life_ordinateur.place(x=10,y=10)
        
        label_name_ordinateur = tk.Label(canvas_Element_ordinateur,text="Name : {}".format(self.pockemone_ordinateur.get_name()))
        label_name_ordinateur.place(x=10,y=30)
        
        label_puissance_attak_ordinateur = tk.Label(canvas_Element_ordinateur,text="Puissance d'attaque : {}".format(self.pockemone_ordinateur.get_puissance_attaque()))
        label_puissance_attak_ordinateur.place(x=10,y=50)
        
        label_puissance_defence_ordinateur = tk.Label(canvas_Element_ordinateur,text="Puissance de defence: {}".format(self.pockemone_ordinateur.get_defence()))
        label_puissance_defence_ordinateur.place(x=10,y=70)
        
        y = 100
        x = 10
        
        for i in self.pockemone_ordinateur.get_type_names():
            label_type_ordinateur = tk.Label(canvas_Element_ordinateur,text=i,bg="#c496f0")
            label_type_ordinateur.place(x=x,y=y)
            
            x +=50
            if x == 300:
                x = 10
                y += 40
        
        if(not self.__est_vivant(self.pockemone_ordinateur) or not self.__est_vivant(self.pockemone_player)):
            print("le gagnant est : ",self.get_name_winner())
            print("le perdant est ",self.get_name_loser())
        
    def menu_game(self):
        menu = tk.Menu(self.fenetre)
        menu.add_command(label="Accueil",command=self.run)
        
        self.fenetre.config(menu=menu)

    # lancement du jeu   
    def run(self):
        
        self.fenetre.unbind_all('<Button>')
        self.clean_fenetre()
        
        self.get_pockemon()
        canvas = tk.Canvas(self.fenetre,width=300,height=300)
        canvas.pack(padx=12,pady=32)
        
        label = tk.Label(canvas,text="Choisez un pockemone").pack()
        
        global list_pockemone
        list_pockemone = ttk.Combobox(canvas,state='readonly')
        list_pockemone["values"] = tuple(self.names_pockemone)
        list_pockemone.current(0)
        list_pockemone.pack()
        
        button = tk.Button(self.fenetre,text="Valider",command=self.create_pockemone)
        button.pack()
        
        self.fenetre.mainloop()

    def batail(self,event):
        
        if(type( event.widget) is tk.Button ):
            element_type = event.widget
            
            self.pockemone_player.set_type_attaque(element_type.cget("text"))
            self.pockemone_player.set_type_defence(element_type.cget("text"))
            
            self.pockemone_ordinateur.set_type_defence(random.choice(self.pockemone_ordinateur.get_type_names()))
            self.pockemone_ordinateur.set_type_attaque(random.choice(self.pockemone_ordinateur.get_type_names()))
            
            if self.get_name_winner() == False:       
                self.duel(self.pockemone_player,self.pockemone_ordinateur)
                self.duel(self.pockemone_ordinateur,self.pockemone_player)
    
    
    def __est_vivant(self,pockemone):
        if(pockemone.get_point_life() <= 0):
            return False
        else:
            return True
    
    def clean_fenetre(self):
        for widget in self.fenetre.winfo_children():
            if str(widget) !=".!menu":
                widget.destroy()
    
    def duel(self, pockemone_one, pockemone_two):
        
        vie_pock_two = pockemone_two.get_point_life()
        
        type_attaque = pockemone_one.get_type_attaque()
        type_defence = pockemone_two.get_type_defence()
        
        point_attaque = pockemone_one.get_puissance_attaque()
        
        info_type = self.get_data_files("db/types.json")
        
        type_exist = False
        
        for contenue in info_type :
           if(contenue["attack"] == type_attaque and contenue["defense"] == type_defence):
                type_exist = True
                vie_pock_two -= point_attaque * contenue["constant"]
                    
                if(vie_pock_two >= 0):
                    pockemone_two.set_point_life(vie_pock_two)
                else:
                    vie_pock_two = 0
                    pockemone_two.set_point_life(vie_pock_two)
        
        if(not type_exist):
          
            vie_pock_two -= point_attaque
            if(vie_pock_two >=0):
                pockemone_two.set_point_life(vie_pock_two)
            else:
                vie_pock_two = 0
                pockemone_two.set_point_life(vie_pock_two)
            self.clean_fenetre()
            self.display()
    
    def get_name_winner(self):
        if not self.__est_vivant(self.pockemone_ordinateur):
            return self.pockemone_player.get_name()
        elif not self.__est_vivant(self.pockemone_player):
            return self.pockemone_ordinateur.get_name()
        else:
            return False
        
    def get_name_loser(self):
        
        if not self.__est_vivant(self.pockemone_ordinateur):
            return self.pockemone_ordinateur.get_name()
        elif not self.__est_vivant(self.pockemone_player):
            return self.pockemone_player.get_name()
        else:
            return False
# fentre 
fenetre = tk.Tk()

combat = Combat(fenetre)
combat.run()
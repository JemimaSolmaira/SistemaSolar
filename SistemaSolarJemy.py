from tkinter import *
from math import *
from time import *

class Planeta:
    def __init__(self, diseno, OrbSol, Dias,  radio, color, ):
        self.diseno = diseno
        self.radio = radio
        self.color = color
        self.PixRad= int(self.diseno["width"])/2    
        self.radioOrbita= OrbSol * self.PixRad/2.5 
        self.anguloActual=0
        self.Angulo2= (2*pi)/Dias
     
    def seno(self):
        x= self.PixRad+self.radioOrbita*sin(self.anguloActual)
        return x
    
    def coseno(self):
        y= self.PixRad+self.radioOrbita*cos(self.anguloActual)
        return y 
           
    def calculos(self,x,y,r):
        x0 = x-r
        y0 = y-r
        x1 = x+r
        y1 = y+r  
        return x0, y0, x1, y1
        
    def Orbita(self):
        x= self.PixRad
        y= self.PixRad
        r= self.radioOrbita
        self.figOrbita = self.diseno.create_oval(self.calculos(x,y,r), outline=self.color)
        
    def DPlaneta(self):
        x= self.seno()
        y= self.coseno()
        r= self.radio
        self.Planeta = self.diseno.create_oval(self.calculos(x,y,r), outline=self.color, fill=self.color)
    
    def moverEnOrbita(self):
        self.anguloActual= self.anguloActual+self.Angulo2
        x= self.seno()
        y= self.coseno()
        r= self.radio

        self.diseno.coords(self.Planeta, self.calculos(x,y,r))
        

class Luna:
    def __init__(self, planeta, radio, color, DiasO):
        self.diseno=planeta.diseno
        self.radio=radio
        self.color=color
        self.planeta=planeta
        self.PixRad= 25 
        self.anguloActual=0
        self.Angulo2= (2*pi)/DiasO
    
      
    def seno(self):
        x= self.planeta.PixRad+self.planeta.radioOrbita*sin(self.planeta.anguloActual)
        return x
    
    def coseno(self):
        y= self.planeta.PixRad+self.planeta.radioOrbita*cos(self.planeta.anguloActual)
        return y 
        
    def calculos(self,x,y,r):
        x0 = x-r
        y0 = y-r
        x1 = x+r
        y1 = y+r  
        return x0, y0, x1, y1
        
    def Orbita(self):
        x= self.seno()
        y= self.coseno()
        r= self.PixRad
        self.fOrbita = self.diseno.create_oval(self.calculos(x,y,r), outline=self.color)
        
    def DSatelite(self):
        x=self.seno() + self.PixRad*sin(self.anguloActual)
        y=self.coseno() + self.PixRad*cos(self.anguloActual)
        r=self.radio
        self.fSatelite = self.diseno.create_oval(self.calculos(x,y,r), outline=self.color, fill=self.color)
        
        
    def moverO(self):
        x = self.seno()
        y= self.coseno()
        r= self.PixRad
        self.diseno.coords(self.fOrbita, self.calculos(x,y,r))
         
        
    def moverSatelite(self):
        self.anguloActual= self.anguloActual+self.Angulo2
        x= self.seno()+self.PixRad*sin(self.anguloActual)
        y= self.coseno()+self.PixRad*cos(self.anguloActual)
        r= self.radio
        self.diseno.coords(self.fSatelite, self.calculos(x,y,r))    
        
        


class SistemaSolar(Tk):
    def __init__(self,Tamano):
        super().__init__()
        self.TamanoVent = str(Tamano)
        self.geometry(self.TamanoVent +"x"+ self.TamanoVent)
        self.title("Sistema Solar Jemy")
        self.diseno = Canvas(self, width=self.TamanoVent, height=self.TamanoVent)
        self.diseno.pack(expand=YES, fill=BOTH)
        self.diseno.photo = PhotoImage(file="sol.png")
        self.diseno.create_image(Tamano/2, Tamano/2 , image=self.diseno.photo)
        self.Planetas=[]
        self.Satelites=[]
  
    def ListaPlanetas(self):
        #Mercurio
        self.Planetas.append(Planeta(self.diseno, 0.5791, 87.9, 7, "Brown"))
        #Venus
        self.Planetas.append(Planeta(self.diseno, 1.082, 224.7, 10, "DarkOrange" ))
        #Tierra
        self.Planetas.append(Planeta(self.diseno, 1.496, 365, 12, "Blue"))
        #Marte
        self.Planetas.append(Planeta(self.diseno, 2.28, 687, 10, "Red" ))
        
    def Luna(self):
        self.Satelites.append(Luna(self.Planetas[2], 4, "White", 27))
        
    def DSistemaSolar(self):
        self.ListaPlanetas()
        self.Luna()
        for i in self.Planetas:
            i.Orbita()
            i.DPlaneta()
            for j in self.Satelites:
                j.Orbita()
                j.DSatelite()
            
    
    def Movimiento(self):
        for i in self.Planetas:
            i.moverEnOrbita()
            for j in self.Satelites:
                j.moverO()
                j.moverSatelite()
        self.after(25, self.Movimiento)    
            
if (__name__ == "__main__"):
    S = SistemaSolar(600)
    S.DSistemaSolar()
    S.Movimiento()
    
    mainloop()

                
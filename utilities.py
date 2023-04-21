from PIL import Image, ImageDraw

class utilities:
    global img
    global pen 
    global CONST_DIVISEUR
    CONST_DIVISEUR =  0b10100110111
    

    def __init__(self,img):
        self.img = img
        
    def placer_module(self,img, x, y, couleur):
        img.putpixel((x, y), couleur)

    def DrawLine(self,x1,y1,x2,y2,color,img):
        pen = ImageDraw.Draw(img)
        pen.line(((x1,y1),(x2,y2)),fill=color,width=0)

    def PlacePixel(self,x,y,color,img):
        pen = ImageDraw.Draw(img)
        img.putpixel((x,y),color)

    def PlaceRectangle(self,x1,y1,x2,y2,color,img):
        pen = ImageDraw.Draw(img)
        pen.rectangle((x1,y1,x2,y2), fill=color, outline=None)
    
    def degre(self,n):
        d = -1
        while n > 0:
            n = n >> 1
            d += 1
        return d

    def modulo(self,dividende, diviseur): #Division longue de polynomes dans G(2) => {1,2}
        while (self.degre(diviseur)<=self.degre(dividende)):
            d = self.degre(dividende) - self.degre(diviseur)
            dividende = (dividende^(diviseur<<d))
        return dividende

    def encode_format(self,mode,masque): # Divise le polynome Mode + masque 
        dividende = ((mode << 3) | (masque)) # Concatenation
        dividende = dividende <<10
        print(bin(dividende))
        # return bin(res)
        diviseur = CONST_DIVISEUR
        reste = self.modulo(dividende,diviseur)
        print(bin(reste))
        dividende = dividende | reste # concatenation 
        dividende = dividende^0b101010000010010 # constante trouvée par des gens intelligents
        return dividende
    

    def applique_masque(self,x, y, b):
        m = 1 if (x + y) % 3 == 0 else 0
        return b ^ m
    
    def ToBin(self,a):
        bin_a = bin(a)
        return (int(bin_a, 2)) #Base 2(binary)
    
    def BlackListCheck(self,x,y):
        if (y <=8):
            return False
        else:
            return True

    def Ascendant(self,POSX):
        cordsXDesendant = [19,15,11]
        cordsXAscendant = [17,13,9]
        for i in cordsXDesendant:
            if (POSX == i):
                return False
        return True


        

    
        



    
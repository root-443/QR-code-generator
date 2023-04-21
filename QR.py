from PIL import Image, ImageDraw
import utilities

class QR:
    global Tools
    global img
    global BLANC, NOIR

    BLANC = (255,255,255)
    NOIR = (0,0,0)
    img = Image.new("RGB",(21,21),color = "gray")
    Tools = utilities.utilities(img)
    
    def BigSquare(self,x0,y0):
        # Gros carré
        Tools.DrawLine(x0,y0,x0+6,y0,(0,0,0),img)   
        Tools.DrawLine(x0+6,y0,x0+6,y0+6,(0,0,0),img)
        Tools.DrawLine(x0+6,y0+6,x0,y0+6,(0,0,0),img)
        Tools.DrawLine(x0,y0+6,x0,y0,(0,0,0),img)
        # petit carré
        Tools.PlaceRectangle(x0+1,y0+1,x0+5,y0+5,(255,255,255),img)
        Tools.PlaceRectangle(x0+2,y0+2,x0+4,y0+4,(0,0,0),img)

    def timingPatern(self,x0,y0,horizontal):
        if (horizontal == True):
            for i in range(5):
                if i%2 == 0:
                    Tools.PlacePixel(x0+i,y0,(0,0,0),img)
                else :
                    Tools.PlacePixel(x0+i,y0,(255,255,255),img)

        else :
            for i in range(5):
                if i%2 == 0:
                    Tools.PlacePixel(x0,y0+i,(0,0,0),img)
                else:
                    Tools.PlacePixel(x0,y0+i,(255,255,255),img)


    def SpacingSchemes(self):
        #first square
        Tools.DrawLine(7,0,7,6,(255,255,255),img)
        Tools.DrawLine(7,7,0,7,(255,255,255),img)
        #Second square
        Tools.DrawLine(0,13,7,13,(255,255,255),img)
        Tools.DrawLine(7,13,7,21,(255,255,255),img)
        #Third square
        Tools.DrawLine(13,0,13,7,(255,255,255),img)
        Tools.DrawLine(13,7,21,7,(255,255,255),img)

    def bit(self,n, i):
        return (n >> i) & 1

    def couleur_module(self,b):
        if b == 1:
            return NOIR
        return BLANC
    
    def placer_modules_format(self,format_encode): 
        index = 0 
        PX = 0

       # Vertical 1
        for PX in range(9):
            if (PX == 6):
                continue
            else :
                Tools.PlacePixel(8,PX,self.couleur_module(self.bit(format_encode,index)),img)
                index = index+1
        #Horizontal 1
        index = 7
        for PX in range(9):
            if (8-PX == 6):
                continue
            else :
                Tools.PlacePixel(8-PX,8,self.couleur_module(self.bit(format_encode,index)),img)
                index = index+1
        
        #Hoeizontal 2
        index = 0
        for PX in range(8):
            Tools.PlacePixel(20-PX,8,self.couleur_module(self.bit(format_encode,index)),img)
            index = index+1
        index = 8

        for PX in range(14,21):
            Tools.PlacePixel(8,PX,self.couleur_module(self.bit(format_encode,index)),img)
            index = index+1
    
    def placer_module_donnee(self, x, y, b):
        Tools.placer_module(img, x, y, self.couleur_module(Tools.applique_masque(x, y, b)))
    
    def placer_octet_montant(self,img, octets, x0, y0):
        PLACES = [[x0,y0],[x0+1,y0],[x0,y0-1],[x0+1,y0-1],[x0,y0-2],[x0+1,y0-2],[x0,y0-3],[x0+1,y0-3]]
        for i in range(len(PLACES)):
            # print(PLACES[i])
            self.placer_module_donnee(PLACES[i][0],PLACES[i][1],self.bit(octets,i))

    def placer_octet_descendant(self,img, octet, x0, y0):

        PLACES = [[x0,y0],[x0+1,y0],[x0,y0+1],[x0+1,y0+1],[x0,y0+2],[x0+1,y0+2],[x0,y0+3],[x0+1,y0+3]]
        for i in range(len(PLACES)):
            # print(PLACES[i])
            self.placer_module_donnee(PLACES[i][0],PLACES[i][1],self.bit(octet,i))
    
    def placer_octet_montant_separe(self,img, octet, x0, y0):
        PLACES = [[x0,y0],[x0+1,y0],[x0,y0-1],[x0+1,y0-1],[x0,y0-3],[x0+1,y0-3],[x0,y0-4],[x0+1,y0-4]]
        for i in range(len(PLACES)):
            # print(PLACES[i])
            self.placer_module_donnee(PLACES[i][0],PLACES[i][1],self.bit(octet,i))

    def placer_octet_descendant_separe(self,img, octet, x0, y0):
        PLACES = [[x0,y0],[x0+1,y0],[x0,y0+1],[x0+1,y0+1],[x0,y0+3],[x0+1,y0+3],[x0,y0+4],[x0+1,y0+4]]
        for i in range(len(PLACES)):
            # print(PLACES[i])
            self.placer_module_donnee(PLACES[i][0],PLACES[i][1],self.bit(octet,i))

    def placer_octets_donnees(self,octets):
        global last_index
        cordsX = [19,17,15,13,11,9] # Paire => descendant
        
        index = 0
        i = 0
        x = 19
        y = 17
        coef = 0
        for i in range(0,3):
            self.placer_octet_descendant(img,Tools.ToBin(octets[i]),x,y-coef*4)
            coef = coef+1
        coef = 0
        x = 17
        y = 12
        for i in range(3,6):
            self.placer_octet_montant(img,Tools.ToBin(octets[i]),x,y+coef*4)
            coef = coef+1
        
        coef = 0
        x = 15
        y = 17
        for i in range(6,9):
            self.placer_octet_descendant(img,Tools.ToBin(octets[i]),x,y-coef*4)
            coef = coef+1
        
        coef = 0
        x = 13
        y = 12
        for i in range(9,12):
            self.placer_octet_montant(img,Tools.ToBin(octets[i]),x,y+coef*4)
            coef = coef+1
        
        coef = 0
        x = 11
        y = 17
        for i in range(12,15):
            print(y-coef*4)
            self.placer_octet_descendant(img,Tools.ToBin(octets[i]),x,y-coef*4)
            coef = coef+1
        
        self.placer_octet_descendant_separe(img,Tools.ToBin(octets[15]),x,4)
        self.placer_octet_descendant(img,Tools.ToBin(octets[16]),x,0)

        x = 9

        self.placer_octet_montant(img,Tools.ToBin(octets[17]),x,3)
        self.placer_octet_montant_separe(img,Tools.ToBin(octets[18]),x,8)
        # self.timingPatern(8,6,True)

        y = 12
        coef = 0

        for i in range(19,22):
            self.placer_octet_montant(img,Tools.ToBin(octets[i]),x,y+coef*4)
            coef =coef+1

        self.placer_octet_descendant(img,Tools.ToBin(octets[22]),7,9)
        self.placer_octet_montant(img,Tools.ToBin(octets[23]),4,12)
        self.placer_octet_descendant(img,Tools.ToBin(octets[24]),2,9)
        self.placer_octet_montant(img,Tools.ToBin(octets[23]),0,12)

    def encode_message(self,message):
        bits = 0b0100  # Le mode d'encodage, sur 4 bits.
        octets_message = message.encode('iso-8859-1')
        octet_de_rembourage_1 = 0b11101100
        octet_de_rembourage_2 = 0b00010001
        longueur = len(octets_message)
        if longueur > 17:
            raise ValueError('Le message est trop long')

    # Ajouter la longueur du message, sur 8 bits.
        bits <<=8
        bits = bits | longueur
    # Ajouter les octets du message.
        for octet in octets_message:
            bits<<=8
            bits = bits | octet 
    # Ajouter 4 bits à zéro.
        bits <<=4
    # Ajouter les octets de "rembourrage".
        for i in  range(17-longueur):
            if (i%2 == 0):
                bits<<=8
                bits = bits | octet_de_rembourage_1
            else :
                bits<<=8
                bits = bits | octet_de_rembourage_2

    # Regroupement des bits en octets.
        octets = []
        for i in range(19):
            octets.insert(0, bits & 255)
            bits >>= 8
    
        return octets
            


        



        



    

        


        
        



            

    

            
            
            
            


        
    
    
    def Show(self):
        img.resize((500,500),Image.BOX).show()





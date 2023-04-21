import QR
import utilities
import Galois
import argparse
from Galois import AnneauPolynome
from Galois import Correcteur


MESSAGE_DU_PROF = [64, 116, 39, 38, 23, 102, 242, 2, 16, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 154, 167, 72, 123, 58, 205, 160]
MESSAGE =[0, 32, 55, 146, 146, 25, 224, 25, 146, 146, 63, 32, 0, 224, 54, 25, 146, 25, 54, 224, 0, 63, 146, 146, 55, 32]


POLYNOME_PRIMITIF = 285 # en binaire, 0b100011101

Gal = Galois.CorpsGalois(POLYNOME_PRIMITIF)
Poly = AnneauPolynome(Gal)

parser = argparse.ArgumentParser()
parser.add_argument("-s1", "--step1", help="Shows step 1",
                    action="store_true")
parser.add_argument("-s2", "--step2", help="Shows step 2",
                    action="store_true")
parser.add_argument("-s3", "--step3", help="Shows step 3",
                    action="store_true")
parser.add_argument("-t", "--test", help="Test",
                    action="store_true")

args = parser.parse_args()
tool = QR.QR()
Util = utilities.utilities(QR.img)

print(bin(116))

def step1():



    tool.BigSquare(0,0)
    tool.BigSquare(14,0)
    tool.BigSquare(0,14)

    tool.SpacingSchemes()

    tool.timingPatern(8,6,True)
    tool.timingPatern(6,8,False)



    QR.Tools.PlacePixel(8,13,(0,0,0),QR.img)



def step2():
    encode_format =Util.encode_format(0b1,0b11)
    print(bin(encode_format))
    tool.placer_modules_format(encode_format)

if args.step1:
    step1()

if args.step2:
    step1()
    step2()

if args.step3:
    step1()
    step2()
    tool.placer_octets_donnees(MESSAGE_DU_PROF)
    tool.Show()


if args.test:
    step1()
    step2()
    Message = ""
    donnees = tool.encode_message(Message)
    correcteur = Correcteur(7, 0b100011101)
    donnees += correcteur.encode(donnees)
    tool.placer_octets_donnees(donnees)
    tool.Show()
    
    
    
    
    
    




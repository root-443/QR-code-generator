  if (index>=0 and index<=2) and 17-index*4>6:
                self.placer_octet_descendant(img,Tools.ToBin(octet),19,17-(index)*4)
                last_index = index+1

               

            if (index>=3 and index <=5) and 12+(index-last_index)*4<=21:
                # print("Last index =",last_index)
                print("printing byte n°",index,"at ",17,12+(index-last_index)*4)
                self.placer_octet_montant(img,Tools.ToBin(octet),17,12+(index-last_index)*4)
                
                
            if (index>=6 and index<=9) and 17-(index-last_index)*4>9:
                print("Printing byte n°",index,"at ",15,17-(index-last_index)*4)
                print(index,last_index)
                self.placer_octet_descendant(img,Tools.ToBin(octet),15,17-(count*4))
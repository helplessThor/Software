import os

def isBinod(filename):
    with open(filename,"r", encoding = 'utf-8') as f:
        filecontent = f.read()
    spcl = "বিনোদ"
    if "binod" in filecontent.lower():
        return True
    elif spcl in filecontent:
        return True
    else:
        False
        
    
if __name__ == "__main__":
    
    #listing contents of the folder
    folder_cont = os.listdir()
    nBinod = 0
    
    #For each text file
    for item in folder_cont:
        if item.endswith("txt") or item.endswith("pdf"):
            print(f"Detecting Binod in {item}")
            flag = isBinod(item)
            
            if(flag):
                print(f"Binod found in {item}")
                nBinod+=1
            else:
                print(f"Binod not found in {item}")
                
    print("*******Binod Detector Summary*******")
    print(f"{nBinod} file(s) found with BINOD hidden in them.")
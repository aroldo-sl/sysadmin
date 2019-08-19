from Thread import Thread
class Forum():
    Thread={}
    Name=""
    counter=0
    
    
    def __init__(self,n="",c=0):
         self.Name=n
         self.counter=c
         
    def erstelleThread(self,Titel="",Ersteller=""):
        #Erhoehen des Counters um 1
        self.counter=self.counter+1
        #Speichern des Counters unter ID
        ID=self.counter
        #Schreibe in die Variable Forumname den Namen aus der Klassenvariable Name
        Forumname=self.Name
        #Zusammensetzung der neuen ID mit dem Forumnamen+die ID aus dem Counter
        _ID=""
        _ID=Forumname+"_"+str(ID)
        #Erstelle ein neues Thread-Objekt im ThreadDictionary von Forum
        self.Thread[str(_ID)]=Thread()   
        #Setzen der Attribute
        self.Thread[str(_ID)].Ersteller=Ersteller
        self.Thread[str(_ID)].Titel=Titel
        self.Thread[str(_ID)].ID=_ID
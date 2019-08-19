from Post import Post
class Thread():
    Name=""
    Post={}
    counter=0
    ID=""
    Ersteller=""
    views=0
    
    def __init__(self,N="",ID="",creator="",v=""):
        self.Name=N;
        self.ID=ID;
        self.Ersteller=creator
        self.views=v
        
    def erstellePost(self,Titel="",Ersteller="",Inhalt="",ThreadID=""):
        #Erhoehung des counter um 1
        self.counter=self.counter+1
        #Speichert den Wert von counter in ID
        ID=self.counter
        #Neue ID aus der uebergebenen Thread-ID und der ID aus count
        _ID=str(ThreadID)+"_"+str(ID)
        #Erzeugung eines neuen Objekts von Post unter der neu erstellteb ID als Key im Post-Dictionary von Thread
        self.Post[str(_ID)]=Post()
        
        #Setzen der Attribute
        self.Post[str(_ID)].Ersteller=Ersteller
        self.Post[str(_ID)].Titel=Titel
        self.Post[str(_ID)].Inhalt=Inhalt
        self.Post[str(_ID)].ID=_ID
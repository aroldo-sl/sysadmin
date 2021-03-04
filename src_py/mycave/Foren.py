#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
# @file:    C:/Users/mario/workspace/global_workspace/src/mycave/Foren.py
# @date:    07.11.2012
# @author:  Mario Gusset
# @mail:    gusset@mitcon.de

'''
short description of what the code does

longer description of what the code does
'''
from __future__ import print_function
from Forum import Forum
import os,sys

class Foren():
    Forum={}
    
    
   
        
    def erstelleForum(self,Name=""): 
        self.Forum[Name]=Forum()   
        self.Forum[Name].Name=Name

def _script():
    '''
    To be called if this module is called as a script.
    '''
    filename = sys.argv[0]
    msg = 'running {filename} as a script'.\
           format(filename=os.path.abspath(filename))
           
    #Erzeuge ein neues Objekt von Forum
    F=Foren()
    #Aufruf der Methode zur Erstellung eines neuen Forums innerhalb des Foren Objekts
    #Der übergebene Name dient als key für das Dictionary, indem das neue Forum-Objekt erzeugt wurd
    F.erstelleForum(Name="test")
    #Speichere das Foren-Objekt in die Variable Test Forum
    TestForum=F.Forum["test"]
    #Aufruf der Methode zur Erstellung eines neuen Threads im Forum-Objekt
    TestForum.erstelleThread(Titel="Thread Name",Ersteller="Max")
    #Hole die Keys/IDs der vorhanden Threads innerhalb des Forums
    Threadkeylist=[]
    Threadkeylist=F.Forum["test"].Thread.keys()
    #Speichern des Threads in die Variable TestThread
    TestThread=F.Forum["test"].Thread[Threadkeylist[0]]
    #Aufruf der Methode zur Erstellung eines neuen Posts
    TestThread.erstellePost(Titel="Post 1 Heading",Ersteller="Max",Inhalt="This is a Post",ThreadID=TestThread.ID)
    #Hole die Keys/IDs der vorhandenen Posts aus dem ThreadDictionary
    PostKeyList=[]
    PostKeyList=TestThread.Post.keys()
    #Speichern des Threads in die Variable TestThread
    Post=TestThread.Post[PostKeyList[0]]
    # Setzen eines Werts für das Attribut date von Post
    Post.date="09.11.12"
    
    print("Forum Objekt:")
    print( F.Forum["test"])
    print("Thread Objekt:")
    print(TestThread)
    print("Post Objekt:")
    print(Post)
    print("Name des Forums:")
    print(TestForum.Name)
    print("Thread ID:")
    print(TestThread.ID)
    print("Thread Titel:")
    print(TestThread.Titel)
    print("Thread Ersteller:")
    print(TestThread.Ersteller)
    
    print("Erstellungs Datum des Posts:")
    print(Post.date)
    print("Beitragsersteller:")
    print(Post.Ersteller)
    print("Titel des Posts:")
    print(Post.Titel)
    print("Inhalt des Posts:")
    print(Post.Inhalt)
    print("ID des Posts:")
    print(Post.ID)

  
    
    print(msg)

if __name__=='__main__':
    
    _script()

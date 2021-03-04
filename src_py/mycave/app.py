import grok
import lb.slog 
from time import gmtime, strftime

from zope.session.interfaces import ISession

from mycave import resource
from .hgacl import branches

class Mycave(grok.Application, grok.Container):
    pass

class Index(grok.View):
    def update(self):
        '''
        Needs some keys in the persistent objects.

        
        Read-only: this view reads data from the object database.
        TODO: implement a view that writes data in the object database.

        This view  works  only if the (dict-like) persistent
        context objects in the object database have the following keys:
       
        context['nickname'] - the nickname of an application
        context['price'] - the price of an application.

        These keys are not needed in production.
        This only to show that this view can publish
        the corresponding values in the web.

        These keys and their values were inserted in the
        object database using the 'interactive_debugger' - 
        this is not a part of this application.
        '''
        date = datetime.now()
        second = date.second
        self.nickname = self.context['nickname'].upper()
        self.price = "$$" + self.context['price']
        if second % 2 == 0:
            self.price = self.price + ' with a good rebate'
        self.date = date
        self.lb_slog = lb.slog.__file__
        slog.info("This update method seems to be working well.")
        slog.warning("The static resource subsystem seems SOMETIMES to have a problem. An error follows (PERHAPS):")
        resource.style.need()

class HgBranches(grok.View):
    '''
    Shows the Mercurial branches and permissions.

    Reads data from a file in hgrc format (ini).
    '''
    grok.name('hgb')
    def update(self):

        date = datetime.now()
        second = date.second
        self.nickname = self.context['nickname'].upper()
        self.price = "$$" + self.context['price']
        if second % 2 == 0:
            self.price = self.price + ' with a good rebate'
        self.date = date
        self.branches_info = branches()
        self.lb_slog = lb.slog.__file__
        resource.style.need()
        
        
#-------------------------------------------------------------------------------        
class MainView(grok.View):
    ''' this is the main view class '''
    grok.context(Mycave)
    grok.name('main')
    grok.template('main')
    
    def update(self,section="",get_firstname="",get_lastname="",createForum="",Forumname="",deleteAnyForum="",
               showForum="", createThread=""):
        
        self.lb_slog = lb.slog.__file__
        resource.style.need()
        now=self.getTime()
        specific_visits="0"
        specific_visits_int=0
        pagevisits=0
        content={}
        cookie_firstname=""
        cookie_lastname=""
        cookie_startTime=""
        cookie_currentTime=""
        isActive=""
        wasActive=True
        cookie_online_Time=0
        formatted_date_available=False
        section_1_counter=0
        section_2_counter=0
        section_3_counter=0
        section_4_counter=0
        section_1_counter_cookie=""
        section_2_counter_cookie=""
        section_3_counter_cookie=""
        section_4_counter_cookie=""
        fav_section_list=[]
        fav_section_name=""
        fav_section_clicks=""
        dislike_section_name=""
        dislike_section_clicks=""
        cookie_first_visit=""
        str_createForum="False"
        ForumViews=0
        ThreadViews=0
        
        try:
            section_1_counter_cookie=self.request.cookies['sect_1']
        except:
            
            print("No Cookie set")
        try:
            cookie_first_visit=self.request.cookies['first_Visit']
            print("COOKIE FIRST VISIT")
            print(cookie_first_visit)
        except:
            
            print("No Cookie set")
        
        try:
            section_2_counter_cookie=self.request.cookies['sect_2']
        except:
            
            print("No Cookie set")
            
        try:
            section_3_counter_cookie=self.request.cookies['sect_3']
        except:
            
            print("No Cookie set")
            
        try:
            section_4_counter_cookie=self.request.cookies['sect_4']
        except:
            
            print("No Cookie set")
        
        
        try:
           cookie_online_Time=self.request.cookies['online_Time']
        except:
            
            print("No Cookie set")
        
        try:
            isActive=self.request.cookies['active']
        except:
            
            wasActive=False
        
        try:
            cookie_startTime=self.request.cookies['startTime']
            print("got start Time")
        except:
            
            print("Didn't get start time") 
            cookie_startTime=now
            
     
        print(cookie_startTime)
        
        try:
            cookie_firstname=self.request.cookies['firstname']
            cookie_lastname=self.request.cookies['lastname']
        except:
            print("No Cookies set!")
        
        try:
            specific_visits=self.request.cookies['visit_count']
        except:
            print("No Cookies set!")
            
        specific_visits_int=int(specific_visits)+1
        specific_visits=str(specific_visits_int)
        
        content=self.read_Database()
        
        try:
            section_1_counter=int(section_1_counter_cookie)
            section_2_counter=int(section_2_counter_cookie)
            section_3_counter=int(section_3_counter_cookie)
            section_4_counter=int(section_4_counter_cookie)
        except:
            print("Error")
        visitcount=0
        
        if not createForum=="":
            str_createForum="True"
        
     
            
        
        if "visits" in content:
            
            try:
                visitcount=int(content["visits"])+1
                content['visits']=visitcount
                
            except ValueError:
                print("Error")
                    
            
            pagevisits=str(visitcount)
        else:
            print("true")
            content["visits"]=0
        
           
        
        self.response.setCookie(name="visit_count",value=specific_visits,max_age=9999999)
        _section="content_s1"
        if section=="1":
            section_1_counter=section_1_counter+1
        
        if section=="2":
            _section="content_s2"
            section_2_counter=section_2_counter+1
            
        elif section=="3":
            _section="content_s3"
            section_3_counter=section_3_counter+1
            
        elif section=="4":
            _section="content_s4"
            section_4_counter=section_4_counter+1
            
        if not get_firstname=="" and not get_lastname=="":
            self.response.setCookie(name="firstname",value=get_firstname,max_age=300)
            self.response.setCookie(name="lastname",value=get_lastname,max_age=300)
            _section="content_s2"
            cookie_firstname=get_firstname
            cookie_lastname=get_lastname
            
        
        self.response.setCookie(name="sect_1",value=str(section_1_counter),max_age=9999999) 
        self.response.setCookie(name="sect_2",value=str(section_2_counter),max_age=9999999) 
        self.response.setCookie(name="sect_3",value=str(section_3_counter),max_age=9999999) 
        self.response.setCookie(name="sect_4",value=str(section_4_counter),max_age=9999999) 
        
        if cookie_first_visit=="":
            self.response.setCookie(name="first_Visit",value=str(now),max_age=9999999) 
            cookie_first_visit=now
            
        
        fav_section_list=self.fav_section(section_1_counter, section_2_counter, section_3_counter, section_4_counter)
        fav_section_clicks=fav_section_list[0]
        fav_section_name=fav_section_list[1]
        fav_section_name +=" "
        fav_section_name +="("
        fav_section_name +=str(fav_section_clicks)
        fav_section_name +=" "
        fav_section_name +="views)"
        
        dislike_section_clicks=fav_section_list[2]
        dislike_section_name=fav_section_list[3]
        dislike_section_name +=" "
        dislike_section_name +="("
        dislike_section_name +=str(dislike_section_clicks)
        dislike_section_name +=" "
        dislike_section_name +="views)"
        
        cookie_currentTime=now
        date=[]
        date=now.split(";")
        startdate=[]
        startdate=cookie_startTime.split(";")
        time_online_formatted={}
       
        
       
        if wasActive:    
            try:
                time_online_formatted=self.calculateTime(startdate,date,cookie_online_Time)
                time_online_sec=time_online_formatted["online_time_sec"]
                self.response.setCookie(name="online_Time",value=str(time_online_sec),max_age=9999999)
                self.response.setCookie(name="startTime",value=now,max_age=9999999)
                self.response.setCookie(name="currentTime",value=now,max_age=100)
                formatted_date_available=True
                
            except:
                self.response.setCookie(name="startTime",value=now,max_age=9999999)
                self.response.setCookie(name="currentTime",value=now,max_age=100)
                self.response.setCookie(name="online_Time",value=str(cookie_online_Time),max_age=9999999)
                
         
        else:
            self.response.setCookie(name="startTime",value=now,max_age=9999999)
            self.response.setCookie(name="currentTime",value=now,max_age=100)
            time_online_formatted=self.convertInProperTimeFormat(float(cookie_online_Time))
            formatted_date_available=True
        
        if formatted_date_available:
            returnedTime=self.returnTime(time_online_formatted) 
            
        else:
            returnedTime= "Error occurred: No online time available"
            
        if not Forumname=="":
            _section="content_s3" 
            self.createForum(content, Forumname,str(ForumViews))
        Forums=[]
        if "Forum" in content:
            Forums=content["Forum"].keys()
            
            
        for Forumcount in range(len(Forums)):
            Forums[Forumcount]=self.createForumLink(Forums[Forumcount])
                               
            
        
        first_Visit=cookie_first_visit.split(";") 
        clicks_per_day={}
        clicks_per_day=self.ascertain_visits_per_Day(first_Visit, date,specific_visits)
        
        self.write_to_Database(content) 
        ThreadDict={}
        
        int_forumViews=0
        str_forumViews=""
        createThreadForumLink=""
        
        
        print ("===============================")
        # set session
        session = ISession(self.request)['showforum']
        # read request paramter
        if self.request.form.get('showForum', ""):
            print ("have to write session data:", self.request.form.get('showForum') )
            session['lastforum'] = self.request.form.get('showForum')
        # set var by using session data
        showForum = session['lastforum']
        print ("Session data filled with:", showForum)
        print ("===============================")
        
        
        if not showForum=="":
            print("\t\tHIER", showForum)
            
            # save the last known forum in session data
            
            session['lastforum'] = showForum
            
            if "Forum" in content:
                
                if showForum in content["Forum"]:
                    ForumViews=content["Forum"][showForum]["views"]
                    int_forumViews=int(ForumViews)+1
                    str_forumViews=str(int_forumViews)
                    content["Forum"][showForum]["views"]=str_forumViews
                    ThreadDict=content["Forum"][showForum]
        print(showForum)
        createThreadForumLink=self.createForumLink_Thread_Creation(showForum)
        
        print(":::_:_:_:_")
        print(createThreadForumLink)
        print(ThreadDict)
        print(showForum)
        
        _createThread="False"
        
        if not createThread=="":
            _createThread="True"
                
        if not deleteAnyForum=="":
            content=self.delete_all_Forums(content)
            self.write_to_Database(content)
        
        self.createThread=_createThread
        self.createThreadForumLink=createThreadForumLink
        self.ThreadDict=ThreadDict    
        self.Forums=Forums
        self.ForumToShow=showForum
        self.createForum=str_createForum
        self.section=_section
        self.clicks_per_day=clicks_per_day
        self.dislike_section_name=dislike_section_name
        self.fav_section_name=fav_section_name
        self.onlineTime=returnedTime
        self.pagevisits=pagevisits
        self.specific_visits=specific_visits
        self.firstname=cookie_firstname
        self.lastname=cookie_lastname
        self.response.setCookie(name="active",value="True",max_age=180)
    
    
    def ascertain_visits_per_Day(self,startdate=[],currentdate=[],visits=0):
        '''
        Ascertains how often a user visited the page per day, by means of the start date, which is the first date
        the user ever visited the page and the current date. The amount of clicks per day is the result of the interval the user
        visited the page divided by the visits he made.
        '''
        time_online_dict={}
        time_online_dict=self.calculateTime(startdate, currentdate, 0)
        time_online_sec=0
        time_online_day=0
        clicks_per_day=0
        time_online_sec=time_online_dict["online_time_sec"]
       
        if time_online_sec>60*60*24:
            time_online_day=time_online_sec/60/60/24
            clicks_per_day=float(visits)/float(time_online_day)
            
        else:
            clicks_per_day=visits
            
        clicks_per_day=format(float(clicks_per_day), '.2f') 
        return clicks_per_day
            
    
    def fav_section(self,section_1_counter=0,section_2_counter=0,section_3_counter=0,section_4_counter=0):
        '''
        Returns the most visited sections in ascending order by comparing the committed section counter.
        '''
        listsections=[]
        listsections.append(section_1_counter)
        listsections.append(section_2_counter)
        listsections.append(section_3_counter)
        listsections.append(section_4_counter)
        listsections_name=[]
        listsections_name.append("Home")
        listsections_name.append("Registration")
        listsections_name.append("Forum")
        listsections_name.append("Statistics")
        fav_section_name=""
        dislike_section_name=""
        dislike_section_clicks=0
        fav_section_clicks=0
        fav_section_list=[]
        print(listsections)
        length=len(listsections)
        buffer=0
        namebuffer=""
        
        for _sections in range(length):
        
            for sections in range(length):
                  
                try:    
                    if listsections[sections]<listsections[sections+1]:
                        buffer=listsections[sections]
                        listsections[sections]=listsections[sections+1]
                        listsections[sections+1]=buffer
                        
                        namebuffer=listsections_name[sections]
                        listsections_name[sections]=listsections_name[sections+1]
                        listsections_name[sections+1]=namebuffer
                        
                       
                except:
                    print("Index out of range")
                    
        fav_section_name=listsections_name[0]
        fav_section_clicks=listsections[0]
        dislike_section_name=listsections_name[-1]    
        dislike_section_clicks=listsections[-1]          
        fav_section_list.append(fav_section_clicks)
        fav_section_list.append(fav_section_name)
        fav_section_list.append(dislike_section_clicks)
        fav_section_list.append(dislike_section_name)
        
        return fav_section_list
                
        
    def write_to_Database(self,com_contend={}):
        '''
        Writes the committed dictionary in the database.
        '''
        
        if "db" in self.context:
            del self.context['db']
            self.context['db']=com_contend
            
        else:    
            self.context['db']={}
            self.context['db']=com_contend
            
            
        
    
    def read_Database(self):
        '''
        Reads data out of the database and returns it.
        '''
        content=""
    
        if "db" in self.context:
            content=self.context['db']
            
        else:    
            self.context['db']={}
            content=self.context['db']
            
        
        return content    
            
    def getTime(self):
        '''
        This method ascertains the current time
        '''
        now=strftime("%a", gmtime())
        now +=";"
        now +=strftime("%d", gmtime())
        now +=";"
        now +=strftime("%b", gmtime())
        now +=";"
        now +=strftime("%Y", gmtime())
        now +=";"
        now +=strftime("%H", gmtime())
        now +=";"
        now +=strftime("%M", gmtime())
        now +=";"
        now +=strftime("%S", gmtime())
        return now     
    
    def calculateTime(self,time_list=[],current_time_list=[],cookie_online_Time=0):
        '''
        This function manages the committed time lists and splits them into their single units. Afterwards it will be converted
        into seconds and be forwarded to the 'convertInProperTimeFormat' function which returns the online time in a proper 
        time format.
        '''
        time_online=0
        time_online_formatted={}
        startTime_hr=0
        startTime_min=0
        startTime_sec=0
        startTime_month=""
        startTime_year=0
        startTime_month_int=0
        startTime_year=int(time_list[3])
        startTime_month=time_list[2]
        startTime_sec=int(time_list[6])
        startTime_hr=int(time_list[4])
        startTime_min=int(time_list[5])
        start_day=int(time_list[1])
        
        startTime_month_int=self.convert_month(startTime_month)
            
        currentTime_hr=0
        currentTime_min=0
        currentTime_sec=0
        currentTime_year=0
        currentTime_month=""
        currentTime_month_int=0
        currentTime_month=current_time_list[2]
        currentTime_year=int(current_time_list[3])
        currentTime_sec=int(current_time_list[6])
        currentTime_hr=int(current_time_list[4])
        currentTime_min=int(current_time_list[5])
        current_day=int(current_time_list[1])

    
        currentTime_month_int=self.convert_month(currentTime_month)
    
        
        actual_currentTime_sec=self.convertTosec(currentTime_hr, currentTime_min, currentTime_sec, currentTime_year,currentTime_month_int, current_day)
        actual_startTime_sec=self.convertTosec(startTime_hr, startTime_min, startTime_sec, startTime_year,startTime_month_int, start_day)
     
        time_online=actual_currentTime_sec-actual_startTime_sec+float(cookie_online_Time)
        time_online_formatted=self.convertInProperTimeFormat(time_online)
        
        return time_online_formatted
        
    
    def convert_month(self,Time_month=""):
        Time_month_int=0
        if Time_month=="Jan":
            Time_month_int=1
        elif Time_month=="Feb":
            Time_month_int=2
        elif Time_month=="Mar":
            Time_month_int=3
        elif Time_month=="Apr":
            Time_month_int=4
        elif Time_month=="May":
            Time_month_int=5
        elif Time_month=="Jun":
            Time_month_int=6
        elif Time_month=="Jul":
            Time_month_int=7
        elif Time_month=="Aug":
            Time_month_int=8
        elif Time_month=="Sep":
            Time_month_int=9
        elif Time_month=="Oct":
            Time_month_int=10
        elif Time_month=="Nov":
            Time_month_int=11
        elif Time_month=="Dec":
            Time_month_int=12    
        return Time_month_int
    
    def convertTosec(self,startTime_hr=0,startTime_min=0,startTime_sec=0,startTime_year=0, startTime_month=0,start_day=0):
         return float(startTime_sec)+float(startTime_min)*60+float(startTime_hr)*60*60+float(start_day)*60*60*24+startTime_month*60*60*24*30.43668+float(startTime_year)*60*60*24*365.2425
    
    def convertInProperTimeFormat(self,time_online=0):
        '''
        Obtains the online time in seconds and returns it in a proper time format: 
        years,month,weeks,days,hours,minutes,seconds.
        '''
        time_format_dict={}
        print(time_online)
        final_years=0
        final_month=0
        final_weeks=0
        final_days=0
        years=int(time_online)/60/60/24/365.2425
        month=int(time_online)/60/60/24/30.43688
        weeks=int(time_online)/60/60/24/7
        days=int(time_online)/60/60/24
        hours=int(time_online)/60/60
        minutes=int(time_online)/60
        seconds=time_online
        
        fl_years=float(time_online)/60/60/24/365.2425
        print(years)
        
        if int(years)>0:
            final_years=int(years)
            remaining_years=fl_years-years
            final_month=int(remaining_years*12)
            remaining_month=float(remaining_years*12)-final_month
            final_weeks=int(remaining_month*(30.436881/7))
            remaining_weeks=float(remaining_month*(30.436881/7))-final_weeks
            final_days=int(remaining_weeks*7)
            remaining_days=float(remaining_weeks*7)-final_days
            final_hours=int(remaining_days*24)
            remaining_hours=float(remaining_days*24)-final_hours
            final_minutes=int(remaining_hours*60)
            remaining_minutes=float(remaining_hours*60)-final_minutes
            final_seconds=int(remaining_minutes*60)
            remaining_seconds=float(remaining_minutes*60)-final_seconds        
            
        
        elif int(month)>0:
            final_years=0
            fl_month=float(time_online)/60/60/24/31
            final_month=int(month)
            remaining_month=fl_month-month
            final_weeks=int(remaining_month*(31/7))
            remaining_weeks=float(remaining_month*(31/7))-final_weeks
            final_days=int(remaining_weeks*7)
            remaining_days=float(remaining_weeks*7)-final_days
            final_hours=int(remaining_days*24)
            remaining_hours=float(remaining_days*24)-final_hours
            final_minutes=int(remaining_hours*60)
            remaining_minutes=float(remaining_hours*60)-final_minutes
            final_seconds=int(remaining_minutes*60)
            remaining_seconds=float(remaining_minutes*60)-final_seconds
     
        
        elif int(weeks)>0:
            final_years=0
            final_month=0
            fl_weeks=float(time_online)/60/60/24/7
            remaining_weeks=fl_weeks-weeks
            final_weeks=int(weeks)
            final_days=int(remaining_weeks*7)
            remaining_days=float(remaining_weeks*7)-final_days
            final_hours=int(remaining_days*24)
            remaining_hours=float(remaining_days*24)-final_hours
            final_minutes=int(remaining_hours*60)
            remaining_minutes=float(remaining_hours*60)-final_minutes
            final_seconds=int(remaining_minutes*60)
            remaining_seconds=float(remaining_minutes*60)-final_seconds
      
    
        elif int(days)>0:
            
            final_years=0
            final_month=0
            final_weeks=0
            fl_days=float(time_online)/60/60/24
            remaining_days=fl_days-days
            final_days=int(days)
            final_hours=int(remaining_days*24)
            remaining_hours=float(remaining_days*24)-final_hours
            final_minutes=int(remaining_hours*60)
            remaining_minutes=float(remaining_hours*60)-final_minutes
            final_seconds=int(remaining_minutes*60)
            remaining_seconds=float(remaining_minutes*60)-final_seconds
        
        elif int(hours)>0:
            final_years=0
            final_month=0
            final_weeks=0
            final_days=0
            fl_hours=float(time_online)/60/60
            remaining_hours=fl_hours-hours
            final_hours=int(hours)
            final_minutes=int(remaining_hours*60)
            remaining_minutes=float(remaining_hours*60)-final_minutes
            final_seconds=int(remaining_minutes*60)
            remaining_seconds=float(remaining_minutes*60)-final_seconds
        
            
        elif int(minutes)>0:
            final_years=0
            final_month=0
            final_weeks=0
            final_days=0
            final_hours=0
            fl_minutes=float(time_online)/60
            remaining_minutes=fl_minutes-minutes
            final_minutes=int(minutes)
            final_seconds=int(remaining_minutes*60)
            remaining_seconds=float(remaining_minutes*60)-final_seconds
            
            
        elif int(seconds)>0:
            final_years=0
            final_month=0
            final_weeks=0
            final_days=0
            final_hours=0
            final_minutes=0
            final_seconds=int(seconds)
            
            
        else:
            final_years=0
            final_month=0
            final_weeks=0
            final_days=0
            final_hours=0
            final_minutes=0
            final_seconds=0
            
        time_format_dict["years"]=final_years
        time_format_dict["month"]=final_month
        time_format_dict["weeks"]=final_weeks
        time_format_dict["days"]=final_days
        time_format_dict["hours"]=final_hours
        time_format_dict["minutes"]=final_minutes
        time_format_dict["seconds"]=final_seconds
        time_format_dict["online_time_sec"]=time_online
        
        print(time_format_dict)
        
        return time_format_dict
    
    def returnTime(self,formatted_online_Time={}):
        '''
        Obtains the formatted online time and creates a string for the template, by considering which 
        units are necessary for the output.
        '''
        returnTime=""
        time_type_list=[]
        isAvailable=False
        
        if formatted_online_Time["years"]==0:
            pass
        
        else:
            isAvailable=True
            time_type_list.append("years")
            
        if formatted_online_Time["month"]==0 and isAvailable==False:
            pass
        
        else:
            isAvailable=True
            time_type_list.append("month")
            
        if formatted_online_Time["weeks"]==0 and isAvailable==False:
            pass
        
        else:
            isAvailable=True
            time_type_list.append("weeks")
            
        if formatted_online_Time["hours"]==0 and isAvailable==False:
            pass
        
        else:
            isAvailable=True
            time_type_list.append("hours")
            
        if formatted_online_Time["minutes"]==0 and isAvailable==False:
            pass
        
        else:
            time_type_list.append("minutes")
        
        time_type_list.append("seconds")
        
        
        for type_count in time_type_list:
            type=""
            returnTime +=str(formatted_online_Time[type_count])
            returnTime +=" "
            
            if int(formatted_online_Time[type_count])==1:
                type=str(type_count[0:-1])
            else:
                type=str(type_count)
                
            returnTime += str(type)
            returnTime += " "
            
        print(returnTime)
        
        return returnTime
    
    def date_string(self,date=[]):
        date_str=""
        Time_hr=0
        Time_min=0
        Time_sec=0
        Time_year=0
        Time_month=""
        Time_month_int=0
        Time_month_int=0
        Time_month=current_time_list[2]
        Time_month_int=self.convert_month(Time_month)
        Time_year=int(current_time_list[3])
        Time_sec=int(current_time_list[6])
        Time_hr=int(current_time_list[4])
        Time_min=int(current_time_list[5])
        Time_day=int(current_time_list[1])
        date_str=Time_Day+"."+Time_month_int+"."+Time_year+" "+Time_hr+":"+Time_min+":"+Time_sec
        
        return date_str
        
    def delete_all_Forums(self,content):
        del content["Forum"]
        return content
    
    def createForumLink(self,Forum=""):
        ForumLink=""
        ForumLink="<a href='./main?section=3&&showForum="+Forum+"'>"+Forum+"</a>"
        print(ForumLink)
        return ForumLink
        
    def createForumLink_Thread_Creation(self,Forum):    
        ForumLink=""
        ForumLink="<a href='./main?section=3&&createThread=1&&showForum="+Forum+"'"+" class='button'>"+"Create a new Thread"+"</a>"
        print(ForumLink)
        return ForumLink
    
    def createForum(self,content={},Forumname="",views=""):
        print(content)
        print(Forumname)
        propriateForumName=False
        namecounter=1
        unedited_Forumname=Forumname
        name_is_modified=False
        
        if not "Forum" in content:
            content["Forum"]={}
        
        while propriateForumName==False:
            if Forumname in content["Forum"]:
                if not name_is_modified:
                    Forumname=Forumname+str("(")+str(namecounter)+str(")")
                    name_is_modified=True
                else:
                    Forumname=unedited_Forumname+str("(")+str(namecounter)+str(")")
                    
                namecounter=namecounter+1
            else:
                propriateForumName=True
                
        content["Forum"][Forumname]={}
        content["Forum"][Forumname]["views"]=views
        print(content)
        return content
    
    def createThread(self,content={},ThreadName="",Forumname="",Contributer="",date="",views=""):
        ThreadID=0
        ThreadID_List=[]
        date_list=[]
        date_list=date.split(";")
        date_str=""
        date_str=self.date_string(date_list)
        if Contributer=="":
            Cotributer="guest"
        if Forumname in content["Forum"]:
            ThreadID_List=content[Forumname].keys()
            ThreadID_List.sort()
            ThreadID=int(ThreadID_List[-1])+1
            
            content["Forum"][Forumname]=ThreadID
            content["Forum"][Forumname][ThreadID]={}
            content["Forum"][Forumname][ThreadID]=ThreadName
            content["Forum"][Forumname][ThreadID][ThreadName]={}
            content["Forum"][Forumname][ThreadID][ThreadName][Contributer]=""
            content["Forum"][Forumname][ThreadID][ThreadName][date_str]=""
            content["Forum"][Forumname][ThreadID][ThreadName]["views"]=views
        
        return content
    
    def createPost(self,content={},ThreadName="",ThreadID=0,Forumname="",Post="",Contributer="",date=""):
        PostID_Nr=0
        PostID=""
        PostID_Nr_List=[]
        PostID_List=[]
        date_list=[]
        date_list=date.split(";")
        date_str=""
        date_str=self.date_string(date_list)
        Post_ID_orderList=[]
       
        
        if Contributer=="":
            Contributer="guest"
            
        if Forumname in content["Forum"]:
            
            if ThreadID in content["Forum"][Forumname]:
                
                if PostID_order in content["Forum"][Forumname][ThreadID][ThreadName]:
                    Post_ID_orderList=content["Forum"][Forumname][ThreadID][ThreadName][PostID_order]
                    date_buffer=""
                    first_loop=True
                    
                    for Post_ID_date in range(len(Post_ID_orderList)):
                        if first_loop:
                            date_buffer=Post_ID_orderList[0]
                            Post_ID_orderList.insert(0,date_str)
                        else:
                            try:
                                date_buffer=Post_ID_orderList[Post_ID_date]
                                Post_ID_orderList[Post_ID_date]=Post_ID_orderList[Post_ID_date+1]
                                Post_ID_orderList[Post_ID_date+1]=date_buffer
                            except:
                                Post_ID_orderList.append(Post_ID_orderList[Post_ID_date])
                    
                else:
                     Post_ID_orderList=content["Forum"][Forumname][ThreadID][ThreadName][PostID_order]=[]
                     Post_ID_orderList.insert(0,date_str)
                    
                if ThreadName in content["Forum"][Forumname][ThreadID]:
                    PostID_List=content["Forum"][Forumname][ThreadID].keys()
                    
                    for ID in PostID_List:
                        length_of_ID=len(ID)
                        position=0
                        
                        for char in range(length_of_ID):
                            if ID[length_of_ID]=="_":
                                position=char
                        PostID_Nr_List.append(ID[position:-1])        
                                
                       
                    PostID_Nr_List.sort()
                    PostID_Nr=int(PostID_List[-1])+1
                    PostID=date_str+"_"+str(PostID_Nr)
                    
                    
                    content["Forum"][Forumname][ThreadID][ThreadName][PostID]={}
                    content["Forum"][Forumname][ThreadID][ThreadName][PostID]["Post"]=Post
                    content["Forum"][Forumname][ThreadID][ThreadName][PostID]["Contributer"]=Contributer
                    content["Forum"][Forumname][ThreadID][ThreadName][PostID]["date"]=date
                    content["Forum"][Forumname][ThreadID][ThreadName][PostID_order]=Post_ID_orderList
                    
                    
                    
                    
        return content
        

        
 
           
#-------------------------------------------------------------------------------
class HeadViewletManager(grok.ViewletManager):
    grok.name('head')
    grok.context(Mycave)

class HeadViewlet(grok.Viewlet):
    grok.viewletmanager(HeadViewletManager)
    grok.context(Mycave)
    grok.template('head')    
#-------------------------------------------------------------------------------    
class ForumViewletManager(grok.ViewletManager):
    grok.name('forum')
    grok.context(Mycave)

class ForumViewlet(grok.Viewlet):
    grok.viewletmanager(ForumViewletManager)
    grok.context(Mycave)
    grok.template('forum')    
#-------------------------------------------------------------------------------
class LeftViewletManager(grok.ViewletManager):
    grok.name('left')
    grok.context(Mycave) 
    
class LeftViewlet(grok.Viewlet):
    grok.viewletmanager(LeftViewletManager)
    grok.context(Mycave)
    grok.template('left')   
    #grok.order(1)
#-------------------------------------------------------------------------------    
class ContentViewletManager(grok.ViewletManager):
    grok.name('content')
    grok.context(Mycave) 
    
class ContentViewlet(grok.Viewlet):
    grok.viewletmanager(ContentViewletManager)
    grok.context(Mycave)
    grok.template('content')   
#-------------------------------------------------------------------------------      
class Content_section_1_ViewletManager(grok.ViewletManager):
    grok.name('content_s1')
    grok.context(Mycave) 
    
class ContentViewlet_section_1(grok.Viewlet):
    grok.viewletmanager(Content_section_1_ViewletManager)
    grok.context(Mycave)
    grok.template('content_s1')   
    #-------------------------------------------------------------------------------      
class Content_section_2_ViewletManager(grok.ViewletManager):
    grok.name('content_s2')
    grok.context(Mycave) 
    
class ContentViewlet_section_2(grok.Viewlet):
    grok.viewletmanager(Content_section_2_ViewletManager)
    grok.context(Mycave)
    grok.template('content_s2')   
    #-------------------------------------------------------------------------------      
class Content_section_3_ViewletManager(grok.ViewletManager):
    grok.name('content_s3')
    grok.context(Mycave) 
    
class ContentViewlet_section3(grok.Viewlet):
    grok.viewletmanager(Content_section_3_ViewletManager)
    grok.context(Mycave)
    grok.template('content_s3')   
    #-------------------------------------------------------------------------------      
class Content_section_4_ViewletManager(grok.ViewletManager):
    grok.name('content_s4')
    grok.context(Mycave) 
    
class ContentViewlet_section_4(grok.Viewlet):
    grok.viewletmanager(Content_section_4_ViewletManager)
    grok.context(Mycave)
    grok.template('content_s4')   
#-------------------------------------------------------------------------------  
class FooterViewletManager(grok.ViewletManager):
    grok.name('footer')
    grok.context(Mycave) 
    
class FooterViewlet(grok.Viewlet):
    grok.viewletmanager(FooterViewletManager)
    grok.context(Mycave)
    grok.template('footer')   
    

#-------------------------------------------------------------------------------        
class MainNavigationViewletManager(grok.ViewletManager):
    grok.name('mainnav')
    grok.context(Mycave) 
    
class MainNavigationViewlet(grok.Viewlet):
    grok.viewletmanager(MainNavigationViewletManager)
    grok.context(Mycave)
    grok.template('mainnav')  

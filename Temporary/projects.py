import datetime
import uuid

class Project:
    def __init__(self, title , Backlog , Todo , Doing , Done, Archived , leader , collabrators):
        self.title = title
        self.__Backlog = Backlog
        self.__Todo = Todo
        self.__Doing = Doing
        self.__Done = Done
        self.__Archived = Archived
        self.__leader = leader

    #Setter
    def setTitle(self , title):
        self.title = title
    def setBacklog(self , backlig):
        self.__Backlog = backlig
    def setTodo(self , todo):
        self.__Todo = todo
    def setDoing(self , doing):
        self.__Doing = doing
    def setDone(self , done):
        self.__Done = done
    def setArchived(self , archived):
        self.__Archived = archived
    def setLeader(self , leader):
        self.__leader = leader

    #Getter
    def getTitle(self):
        return self.title
    def getBachlog(self):
        return self.__Backlog
    def getTodo(self):
        return self.__Todo
    def getDoing(self):
        return self.__Doing
    def getDone(self):
        return self.__Done
    def getArchived(self):
        return self.__Archived
    def grtLeader(self):
        return self.leader

    #other
    def add_collabrator(self , collabrator):
        self.collabrators.append(collabrator)
    
    def __del__(self):
        print("Project is successfully deleted")
    #def setStatus(self , status):
    #    self.status = status
    #def getStatus(self):
    #    return self.status

class Task:
    def __init__(self, title, assignee, status='Backlog', priority='LOW'):
        self.title = title
        self.__assignees = assignee
        self.__status = status
        self.__priority = priority
        self.__taskID = uuid.uuid1()
        self.__endtime = datetime.datetime.now()+datetime.timedelta(hours=24)
        self.__comments = []

    # Setters
    def setTitle(self, title):
        self.title = title
    def setAssignees(self, assignees):
        self.__assignees = assignees
    def setStatus(self, status):
        self.__status = status
    def setPriority(self, priority):
        self.__priority = priority
    def setDescription(self, description):
        self.description = description
    def setEndTime(self, endtime):
        self.__endtime = endtime
    
    # Getters
    def getTitle(self):
        return self.title
    def getStatus(self):
        return self.__status
    def getAssignees(self):
        return self.__assignees
    def getPriority(self):
        return self.__priority
    def getTaskID(self):
        return self.__taskID
    def getComments(self):
        return self.__comments
    def getEndTime(self):
        return self.__endtime
    
    
    # Others
    def addComment(self, comment):
        self.__comments.append(comment)
    def deleteComment(self, comment):
        self.__comments.remove(comment)
    def addAssignee(self, newAssignee):
        self.__assignees.append(newAssignee)
    def removeAssignee(self, assignee):
        self.__assignees.remove(assignee)

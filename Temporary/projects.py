import datetime
import uuid

class Project:
    
    def __init__(self, title):
        # self.status = 'Backlog'
        self.title = title
    def setStatus(self , status):
        self.status = status
    def getStatus(self):
        return self.status

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

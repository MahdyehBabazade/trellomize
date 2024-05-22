import datetime
import uuid
import user
import os
import json
from enum import Enum

class Project:
    def __init__(self, title , leader):
        self.__title = title
        self.__Backlog = []
        self.__Todo = []
        self.__Doing = []
        self.__Done = []
        self.__Archived = []
        self.__leader = leader
        self.__collabrators = leader

    # Setters
    def setTitle(self , title):
        self.__title = title
    def setCollabrator(self , collabrator):
        self.__collabrators.append(collabrator)

    # Getters
    def getTitle(self):
        return self.__title
    def getBacklog(self):
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
        return self.__leader

    # Other
    def addTask(self , Task):
        if Task.getStatus() == Status.BACKLOG.value:
            self.__Backlog.append(Task)
        elif Task.getStatus() == Status.TODO.value:
            self.__Todo.append(Task)
        elif Task.getStatus() == Status.DOING.value:
            self.__Doing.append(Task)
        elif Task.getStatus() == Status.DONE.value:
            self.__Done.append(Task)
        elif Task.getStatus() == Status.ARCHIVED.value:
            self.__Archived.append(Task)
    def add_collabrator(self , collabrator):
        self.__collabrators.append(collabrator)
    
    def __del__(self):
        print("Project is successfully deleted")
    #def setStatus(self , status):
    #    self.status = status
    #def getStatus(self):
    #    return self.status

class Status(Enum):
    BACKLOG = 1
    TODO = 2
    DOING = 3
    DONE = 4
    ARCHIVED = 5

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class Task:
    def __init__(self, title, status=Status.BACKLOG.value, priority=Priority.LOW.value):
        self.__title = title
        self.__status = status # work with value
        self.__priority = priority
        self.__taskID = uuid.uuid1()
        self.__endtime = datetime.datetime.now()+datetime.timedelta(hours=24)
        self.__comments = []

    # Setters
    def setTitle(self, title):
        self.__title = title
    def setStatus(self, status):
        self.__status = status #status is value
    def setPriority(self, priority):
        self.__priority = priority
    def setDescription(self, description):
        self.description = description
    def setEndTime(self, endtime):
        self.__endtime = endtime
    
    # Getters
    def getTitle(self):
        return self.__title
    def getStatus(self): #return value
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


def create_new_project(project, user):
    directory = "AllFiles\\Users"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, f"{user.getEmail()}.json")
    with open(filename, "w") as f:
        json.dump(project.__dict__, f, indent=4)
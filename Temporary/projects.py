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
        self.assignees = assignee
        self.status = status
        self.priority = priority
        self.taskID = uuid.uuid1()
        self.endtime = datetime.datetime.now()+datetime.timedelta(hours=24)
        self.comments = []
    # Setters
    def setTitle(self, title):
        self.title = title
    def setAssignees(self, assignees):
        self.assignees = assignees
    def setStatus(self, status):
        self.status = status
    def setPriority(self, priority):
        self.priority = priority
    def setDescription(self, description):
        self.description = description
    
    # Getters
    def getTitle(self):
        return self.title
    def getStatus(self):
        return self.status
    
    # Others
    def addComment(self, comment):
        self.comments.append(comment)
    def addAssignee(self, newAssignee):
        self.assignees.append(newAssignee)
    def removeAssignee(self, assignee):
        self.assignees.remove(assignee)

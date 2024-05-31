import datetime, GlobalFunctions as GF, uuid, os, json, user as userlib
from enum import Enum

class Project:
    def __init__(self, title, leader, ProjectID = str(uuid.uuid1())):
        self.__title = title
        self.__ProjectID = ProjectID
        self.__leader = leader
        self.__collaborators = [leader]
        self.__tasks = []

    # Setters
    def changeTitle(self, title):
        self.__title = title
        for collaborator_data in GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__collaborators]):
            collaborator_data['projects'][self.__ProjectID]['title'] = self.__title
            GF.write_to_the_file(collaborator_data)
    def changeProjectId(self, id):
        self.__ProjectID = id
        for collaborator_data in GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__collaborators]):
            collaborator_data['projects'][self.__ProjectID]['ProjectID'] = self.__ProjectID
            GF.write_to_the_file(collaborator_data)
    def setCollaborators(self, collabs):
        self.__collaborators = collabs
    def setTask(self, task):
        self.__tasks.append(task)
        
    # Getters
    def getTitle(self):
        return self.__title
    def getLeader(self):
        return self.__leader
    def getProjectID(self):
        return self.__ProjectID
    def getTasks(self):
        return self.__tasks
    def getCollaborators(self):
        return self.__collaborators

    # Other
    def addTask(self, task): # This one adds to the file but setTask doesnt
        self.__tasks.append(task)
        for collaborator_data in GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__collaborators]):
            collaborator_data["projects"][self.__ProjectID]['tasks'] = [task.to_dict() for task in self.__tasks]
            GF.write_to_the_file(collaborator_data)
    def removeTask(self, task):
        self.__tasks.remove(task)
        for collaborator_data in GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__collaborators]):
            collaborator_data['projects'][self.__ProjectID]['tasks'] = [task.to_dict() for task in self.__tasks]
            GF.write_to_the_file(collaborator_data)
    def addCollaborator(self, collaborator): #چون که دستی ایمیل رو وارد میکنیم احتمال خطا و وارد کردن ایمیل کلبریتور هست پس ایف میزاریم
        if collaborator not in self.__collaborators:
            self.__collaborators.append(collaborator)
            for collaborator_data in GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__collaborators]):
                collaborator_data['projects'][self.__ProjectID]['collaborators'] = [collaborator.to_dict() for collaborator in self.__collaborators]
                GF.write_to_the_file(collaborator_data)
    def removeCollaborator(self, collaborator):
        if collaborator in self.__collaborators:
            self.__collaborators.remove(collaborator)
            for collaborator_data in GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__collaborators]):
                collaborator_data['projects'][self.__ProjectID]['collaborators'] = [collaborator.to_dict() for collaborator in self.__collaborators]
                GF.write_to_the_file(collaborator_data)

    def to_dict(self):
        return {
            self.__ProjectID :{
            'title': self.__title,
            'ProjectID': self.__ProjectID,
            'leader': self.__leader.to_dict(),
            'collaborators': [collaborator.to_dict() for collaborator in self.__collaborators],
            'tasks': [task.to_dict() for task in self.__tasks]
            }
        }
    
    def save_to_file(self, user):
        data = GF.load_the_data(user.getEmail())

        if 'projects' not in data:
            data['projects'] = {}
    
        data['projects'][self.__ProjectID] = {
            'title': self.__title,
            'ProjectID': self.__ProjectID,
            'leader': self.__leader.to_dict(),
            'collaborators': [collaborator.to_dict() for collaborator in self.__collaborators],
            'tasks': [task.to_dict() for task in self.__tasks]
        }

        filename = os.path.join("AllFiles\\Users", f"{user.getEmail()}.json")
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def remove_from_file(self, user):
        data = GF.load_the_data(user.getEmail())
        del data['projects'][self.__ProjectID]
        filename = os.path.join("AllFiles\\Users", f"{user.getEmail()}.json")
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

class Status(Enum):
    BACKLOG = 1
    TODO = 2
    DOING = 3
    DONE = 4
    ARCHIVED = 5
    DEFAULT = BACKLOG

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
    DEFAULT = LOW

class Task:
    def __init__(self, title, project, status=Status.BACKLOG.value, priority=Priority.LOW.value):
        self.__title = title
        self.__status = status
        self.__priority = priority
        self.__taskID = str(uuid.uuid1())
        self.__starttime = (datetime.datetime.now()).isoformat()
        self.__endtime = (datetime.datetime.now() + datetime.timedelta(hours=24)).isoformat()
        self.__comments = []
        self.__assignees = []
        self.__description = ''
        self.__project = project
        self.__history = []
        

    # Getters
    def getTitle(self):
        return self.__title
    def getStatus(self):
        return self.__status
    def getPriority(self):
        return self.__priority
    def getTaskID(self):
        return self.__taskID
    def getComments(self):
        return self.__comments
    def getStartTime(self):
        return self.__endtime
    def getEndTime(self):
        return self.__endtime
    def getDescription(self):
        return self.__description
    def getAssignees(self):
        return self.__assignees

    # Setters
    def setEndTime(self, endtime):
        self.__endtime = endtime
    def setStartTime(self, starttime):
        self.__starttime = starttime
    def setComments(self, comments):
        self.__comments = comments
    def setTaskID(self, taskid):
        self.__taskID = taskid
        self.write_to_the_file('taskID', self.__taskID)
    
    # Change Functions
    
    def write_to_the_file(self, field, new):
    
        data = GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__project.getCollaborators()])
        for collaborator_data in data:
            project_tasks = collaborator_data['projects'][self.__project.getProjectID()]["tasks"]
            for task in project_tasks:
                if task["taskID"] == self.__taskID:
                    task[field] = new        
        filename = os.path.join("AllFiles\\Users", f"{collaborator_data['email']}.json")
        with open(filename, 'w') as f:
            json.dump(collaborator_data, f, indent=4)

    def changeTitle(self, title):
        self.__title = title
        self.write_to_the_file('title', self.__title)
    def changeStatus(self, status):
        self.__status = status
        if status == 4:
            self.setEndTime((datetime.datetime.now()).isoformat())
        self.write_to_the_file('status', self.__status)
    def changePriority(self, priority):
        self.__priority = priority
        self.write_to_the_file('priority', self.__priority)
    def changeDescription(self, description):
        self.__description = description
        self.write_to_the_file('description', self.__description)
    def changeEndTime(self, endtime):
        self.__endtime = endtime
        self.write_to_the_file('endtime', self.__endtime)

    
    # Others
    def addComment(self, comment):
        self.__comments.append(comment)
        data = GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__project.getCollaborators()])
        for collaborator_data in data:
            project_tasks = collaborator_data['projects'][self.__project.getProjectID()]["tasks"]
            for task in project_tasks:
                if task["taskID"] == self.__taskID:
                    task['comments'].append(comment.to_dict())
                    GF.write_to_the_file(collaborator_data)
    def editComment(self, comment):        
        data = GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__project.getCollaborators()])
        for collaborator_data in data:
            project_tasks = collaborator_data['projects'][self.__project.getProjectID()]["tasks"]
            for task in project_tasks:
                if task["taskID"] == self.__taskID:
                    comments = [cm for cm in task['comments']]
                    for cm in comments:
                        if cm['commentID'] == comment.getCommentID(): 
                            cm['text'] = comment.getText()
                            GF.write_to_the_file(collaborator_data)
    def deleteComment(self, comment):
        self.__comments.remove(comment)
        data = GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__project.getCollaborators()])
        for collaborator_data in data:
            project_tasks = collaborator_data['projects'][self.__project.getProjectID()]["tasks"]
            for task in project_tasks:
                if task["taskID"] == self.__taskID:
                    task['comments'].remove(comment.to_dict())
                    GF.write_to_the_file(collaborator_data)
                
    def addAssignee(self, assignee):
        self.__assignees.append(assignee)
        data = GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__project.getCollaborators()])
        for collaborator_data in data:
            project_tasks = collaborator_data['projects'][self.__project.getProjectID()]["tasks"]
            for task in project_tasks:
                if task["taskID"] == self.__taskID:
                    task["assignees"].append(assignee.to_dict())
                    GF.write_to_the_file(collaborator_data)
    
    def addHistory(self, action):
        self.__history.append(action)
        data = GF.load_the_collaborators_data(*[collab.getEmail() for collab in self.__project.getCollaborators()])
        for collaborator_data in data:
            project_tasks = collaborator_data['projects'][self.__project.getProjectID()]["tasks"]
            for task in project_tasks:
                if task["taskID"] == self.__taskID:
                    task['history'].append(action.to_dict())
                    GF.write_to_the_file(collaborator_data)
    
    def to_dict(self):
        return {
            'title': self.__title,
            'status': self.__status,
            'priority': self.__priority,
            'taskID': self.__taskID,
            'starttime': self.__starttime,
            'endtime': self.__endtime,
            'comments': [],
            'description' : self.__description,
            'assignees' : [assignee.to_dict() for assignee in self.__assignees],
            'history': []
        }

def load_from_file(project_id, user):
    directory = "AllFiles\\Users"
    filename = os.path.join(directory, f"{user.getEmail()}.json")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            if project_id in data['projects']:
                project_dict = data['projects'][project_id]
                leader = userlib.User(project_dict['leader']["email"], project_dict['leader']["username"], project_dict['leader']["password"], True)
                project = Project(project_dict['title'], leader, project_id)
                collaborators = [userlib.User(collaborator_dict["email"], collaborator_dict["username"], collaborator_dict["password"], True) for collaborator_dict in project_dict['collaborators']]
                project.setCollaborators(collaborators)
                for task_dict in project_dict['tasks']:
                    task = Task(task_dict['title'], project, task_dict['status'], task_dict['priority'])
                    task.setTaskID(task_dict['taskID'])
                    task.setEndTime(task_dict['endtime'])
                    comments = [Comment(comment_dict['text'], 
                                        userlib.User(comment_dict['person']['email'], 
                                                     comment_dict['person']['username'], 
                                                     comment_dict['person']['password'], 
                                                     comment_dict['person']['isActive']), 
                                        comment_dict['time'], comment_dict['commentID']) 
                                for comment_dict in task_dict['comments']]
                    task.setComments(comments)
                    project.setTask(task)

                return project

class Comment:
    def __init__(self, text, person, time=(datetime.datetime.now()).isoformat(), id = str(uuid.uuid1())):
        self.__text = text
        self.__person =  person
        self.__time = time
        self.__id = id

    def getText(self):
        return self.__text
    def getPerson(self):
        return self.__person
    def getTime(self):
        return self.__time
    def getCommentID(self):
        return self.__id
    
    def setText(self, text):
        self.__text = text

    def to_dict(self):
        return {
            'text': self.__text,
            'person': self.__person.to_dict(),
            'time': self.__time,
            'commentID': self.__id
        }
    
class History:
    def __init__(self, username, action, time=(datetime.datetime.now()).isoformat()):
        self.__username = username
        self.__action = action
        self.__time = time
        

    def getAction(self):
        return self.__action
    def to_dict(self):
        return {
            'username': self.__username,
            'action': self.__action,
            'time': self.__time,
        }
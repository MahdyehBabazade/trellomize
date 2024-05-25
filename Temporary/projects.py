import datetime, GlobalFunctions as GF
import uuid
import os
import json, user as userlib
from enum import Enum

def load_the_collaborators_data(*args): # Returns all the collaborators' data in a list
    directory = "AllFiles\\Users"
    data = []
    for collaborator in args:
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory, f"{collaborator.getEmail()}.json")
        with open(filename, "r") as f:
            data.append(json.load(f))
    return data

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
        for collaborator_data in load_the_collaborators_data(self.__collaborators):
            collaborator_data['projects'][self.__ProjectID]['title'] = self.__title

    def changeProjectId(self, id):
        self.__ProjectID = id
        for collaborator_data in load_the_collaborators_data(self.__collaborators):
            collaborator_data['projects'][self.__ProjectID]['ProjectID'] = self.__ProjectID
        
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
    def addTask(self, task, collaborator):
        self.__tasks.append(task)
        self.save_to_file(collaborator)

    def addCollaborator(self, collaborator):
        self.__collaborators.append(collaborator)
        for collaborator_data in load_the_collaborators_data(self.__collaborators):
            collaborator_data['projects'][self.__ProjectID]['collaborators'] = [collaborator.to_dict() for collaborator in self.__collaborators]

    def to_dict(self, user):
        
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
    def __init__(self, title, project, status=Status.BACKLOG.value, priority=Priority.LOW.value):
        self.__title = title
        self.__status = status
        self.__priority = priority
        self.__taskID = str(uuid.uuid1())
        self.__endtime = (datetime.datetime.now() + datetime.timedelta(hours=24)).isoformat()
        self.__comments = []
        self.__assignees = []
        self.__description = ''
        self.__project = project

    # Setters
    
    def changeTitle(self, title):
        self.__title = title
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            collaborator_data['projects'][self.__project.getProjectID()]['title'] = self.__title
            filename = os.path.join("AllFiles\\Users", f"{data["email"]}.json")
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
    def changeStatus(self, status):
        self.__status = status
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            collaborator_data['projects'][self.__project.getProjectID()]['status'] = self.__status
            filename = os.path.join("AllFiles\\Users", f"{data["email"]}.json")
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
    def changePriority(self, priority):
        self.__priority = priority
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            collaborator_data['projects'][self.__project.getProjectID()]['priority'] = self.__priority
            filename = os.path.join("AllFiles\\Users", f"{data["email"]}.json")
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
    
    
    def changeDescription(self, description):
        self.__description = description
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            collaborator_data['projects'][self.__project.getProjectID()]['description'] = self.__description
            filename = os.path.join("AllFiles\\Users", f"{collaborator_data['email']}.json")
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
    def changeEndTime(self, endtime):
        self.__endtime = endtime
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            collaborator_data['projects'][self.__project.getProjectID()]['endtime'] = self.__endtime
            filename = os.path.join("AllFiles\\Users", f"{collaborator_data['email']}.json")
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
    def setTaskID(self, taskid):
        self.__taskID = taskid
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            collaborator_data['projects'][self.__project.getProjectID()]['taskID'] = self.__taskID
            collaborator_data['projects'][self.__project.getProjectID()] = self.__taskID
            filename = os.path.join("AllFiles\\Users", f"{collaborator_data['email']}.json")
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

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
    def getEndTime(self):
        return self.__endtime
    def getDescription(self):
        return self.__description
    def getAssignees(self):
        return self.__assignees

    # Others
    def addComment(self, comment):
        self.__comments.append(comment)
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            for i in range(len(collaborator_data['projects'][self.__project.getProjectID()]["tasks"])):
                collaborator_data['projects'][self.__project.getProjectID()]["tasks"][i]['comments'].append(comment)
                filename = os.path.join("AllFiles\\Users", f"{collaborator_data["email"]}.json")
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)
    def deleteComment(self, comment):
        self.__comments.remove(comment)
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            for i in range(len(collaborator_data['projects'][self.__project.getProjectID()]["tasks"])):
                collaborator_data['projects'][self.__project.getProjectID()]["tasks"][i]['comments'].remove(comment)
                filename = os.path.join("AllFiles\\Users", f"{collaborator_data["email"]}.json")
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)
                
    def addAssignee(self, assignee):
        self.__assignees.append(assignee)
        data = load_the_collaborators_data(*self.__project.getCollaborators())
        for collaborator_data in data:
            for i in range(len(collaborator_data['projects'][self.__project.getProjectID()]["tasks"])):
                collaborator_data['projects'][self.__project.getProjectID()]["tasks"][i]["assignees"].append(assignee.to_dict())
                filename = os.path.join("AllFiles\\Users", f"{collaborator_data["email"]}.json")
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)
                
    
    def to_dict(self):
        return {
            'title': self.__title,
            'status': self.__status,
            'priority': self.__priority,
            'taskID': self.__taskID,
            'endtime': self.__endtime,
            'comments': self.__comments,
            'description' : self.__description,
            'assignees' : [assignee.to_dict() for assignee in self.__assignees]
        }

def load_from_file(project_id, user):  #maybe it has error too
    directory = "AllFiles\\Users"
    filename = os.path.join(directory, f"{user.getEmail()}.json")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            if project_id in data['projects']:
                project_dict = data['projects'][project_id]
                leader = userlib.User(project_dict['leader'])
                project = Project(project_dict['title'], project_id, leader)
                for collaborator_dict in project_dict['collaborators']:
                    collaborator = userlib.User(collaborator_dict)
                    project.addCollaborator(collaborator)
                for task_dict in project_dict['tasks']:
                    task = Task(task_dict['title'], Status[task_dict['status']], Priority[task_dict['priority']])
                    task.setTaskID(task_dict['taskID'])
                    task.setEndTime(task_dict['endtime'])
                    task.setComments(task_dict['comments'])
                    project.addTask(task)
                return project
    return None

import unittest
import user
import projects
import pages
import manager

class testUser(unittest.TestCase):
    def testemail(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        self.assertEqual(user1.getEmail() , "bahar@gmail.com")
    
    def testusername(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        self.assertEqual(user1.getUsername() , 'bahar')

    def testpassword(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        self.assertEqual(user1.getPassword() , 'da553252a7f8d6914a51d09b830604e2a4004394d54345286b5bb5e2903a4a08')

class testSignUp(unittest.TestCase):
    def testemail_isvalid(self):
        self.assertTrue(user.SignUp().email_isvalid('b@gmail.com'))
        with self.assertRaises(ValueError):
            user.SignUp().email_isvalid('bahar@gmail.co')
        #with self.assertRaises(FileExistsError): #fail
        #    user.SignUp().email_isvalid("bahar@gmail.com")

    def test_username_isvalid(self):
        self.assertTrue(user.SignUp().username_isvalid('bahar'))
        with self.assertRaises(ValueError):
            user.SignUp().username_isvalid('')

    def test_password_isvalid(self):
        self.assertTrue(user.SignUp().password_isvalid('13831383'))
        with self.assertRaises(ValueError):
            user.SignUp().password_isvalid('138313')

#class testLogin(unittest.TestCase): #error
#    def testcorrect_email(self): #error
#        self.assertTrue(user.Login().correct_email('bahar@gmail.com'))
#        with self.assertRaises(ValueError):
#            user.Login().correct_email('bahar@gmail.co')
#        with self.assertRaises(FileExistsError):
#            user.Login().correct_email('hi@gmail.com')

#    def testcorrect_password(self): #error
#        self.assertTrue(user.Login().correct_password('bahar@gmail.com' , '13831383'))
#        with self.assertRaises(ValueError):
#            user.Login().correct_password('bahar@gmail.com' , '12345678')
#        with self.assertRaises(ValueError):
#            user.Login().correct_password('bahar@gmail.com' , '123')

class testAdmin(unittest.TestCase):
    def testgetUsername(self):
        admin = manager.Admin('bahar' , '13831383')
        self.assertEqual(admin.getUsername() , 'bahar')

    def getPassword(self):
        admin = manager.Admin('bahar' , '13831383')
        self.assertEqual(admin.getPassword() , 'da553252a7f8d6914a51d09b830604e2a4004394d54345286b5bb5e2903a4a08')

class testProject(unittest.TestCase):
    def testgetTitle(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        project = projects.Project('First project' , user1 , '123456')
        self.assertEqual(project.getTitle() , 'First project')

    def getLeader(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        project = projects.Project('First project' , user1 , '123456')
        self.assertEqual(project.getLeader() , user1)

    def getProjectID(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        project = projects.Project('First project' , user1 , '123456')
        self.assertEqual(project.getProjectID() , '123456')

    def testgetCollaborators(self): 
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        project = projects.Project('First project' , user1 , '123456')
        self.assertEqual(project.getCollaborators() , [user1]) 

class testTask(unittest.TestCase):
    def testgetTitle(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        project = projects.Project('First project' , user1 , '123456')
        task = projects.Task('First task' , project , 1 , 1)
        self.assertEqual(task.getTitle() , 'First task')

    def testgetStatus(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        project = projects.Project('First project' , user1 , '123456')
        task = projects.Task('First task' , project , 1 , 1)
        self.assertEqual(task.getStatus() , 1)

    def testgetPriority(self):
        user1 = user.User('bahar@gmail.com' , 'bahar' , "13831383")
        project = projects.Project('First project' , user1 , '123456')
        task = projects.Task('First task' , project , 1 , 1)
        self.assertEqual(task.getPriority() , 1)

if __name__ == "__main__":
    unittest.main()
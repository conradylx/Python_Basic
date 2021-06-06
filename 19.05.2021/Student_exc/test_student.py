import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.object1 = Student('Jon', 'Snow', 3.5, None)
        self.object2 = Student('Anna', 'Kowalska', 5.0, None)

    def tearDown(self):
        print('Teardown method launched')
        del self.object1
        del self.object2

    def test_email_when_name_changed(self):
        print('Test_email_when_name_changed launched')
        self.assertEqual(self.object1.email, 'jon.snow@university.com')

        self.object1.name = 'John'
        self.assertEqual(self.object1.email, 'john.snow@university.com')

    def test_fullname(self):
        print('Test_fullname launched')

        self.assertEqual(self.object2.fullname, 'Anna Kowalska')

        self.object2.last = 'Nowak'
        self.assertEqual(self.object2.fullname, 'Anna Nowak')

    def test_grant_scholarship(self):
        print('Test_grant_scholarship launched')
        self.object1.grant_scholarship()
        self.object2.grant_scholarship()
        self.assertEqual(self.object1.scholarship, False)
        self.assertEqual(self.object2.scholarship, True)

    def test_change_avg(self):
        print('Test_change_grant_avg')
        self.object1.grant_scholarship()
        self.object1.student_avg = 5.0
        self.object1.grant_scholarship()
        self.assertEqual(self.object1.scholarship, True)


if __name__ == '__main__':
    unittest.main()

import unittest
from main import Main
import re

n = int(input('nhap n : '))
A = Main(n)

def phone():
    return len(A.free_phone())
def email():
    em = A.free_email()
    r = re.compile('[a-zA-Z]@[a-zA-Z][.][a-zA-Z]')
    if r.match(em) is not None:
        return True
    if '.' in em:
        if '@' in em:
            return True
        else:
            return False
    return False
def email_unique():
    emails = A.generation()[1][1]
    j=[]
    for i in emails:
        if i not in j:
            j.append(i)
        else:
            return False
    return True
def phone_unique():
    phones = A.generation()[1][2]
    j = []
    for i in phones:
        if i not in j:
            j.append(i)
        else:
            return False
    return True
class simpletest(unittest.TestCase):
    def test_phone(self):
        self.assertIn(phone(),[10,12])
    def test_email(self):
        self.assertTrue(email(),True)
    def test_email_unique(self):
        self.assertTrue(email_unique(),True)
    def test_phone_unique(self):
        self.assertTrue(phone_unique(),True)
if __name__ == "__main__":
    unittest.main()
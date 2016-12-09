
import unittest
import subprocess
import time
import os
import urllib.request
import random
import pep8

# CONFIGURATION
# change to whatever is python3 on your computer
pythonexec = 'python'

sourcecode = "./w9_wordplayer.py"
#sourcecode = "./w10_wordplayer.cpp"

Wordlist = {}
Input = {}
Output = {}
FileName = {}

# test when all answers are 0 or 1 word long
FileName['unique'] = "unique_word_list.txt"
Wordlist['unique'] = """ice
cream
coffee
apple
banana
applause
"""


Input['unique'] = """macabre 6
macabre 5
macabre 4
leap 5
apoplectic 7
apoplectic 6
apoplectic 5
apoplectic 4
exit 0
"""

Output['unique'] = """.
cream
.
.
.
.
.
apple
.
.
"""

# short word list, multiple answers
FileName['simple'] = "simple_word_list.txt"
Wordlist['simple'] = """bbaacc
aad
aaa
aab
dada
aac
aabb
aabbcc
bbaa
adad
daad
abcd
dcab
"""


Input['simple'] = """abcdabcd 4
abcdabcd 3
aabcbc 3
exit 0
"""

Output['simple'] = """aabb
abcd
adad
bbaa
daad
dada
dcab
.
aab
aac
aad
.
aab
aac
.
"""

TestCases = ['simple', 'unique']


testing = 'py' if sourcecode.endswith('py') else 'cpp'



FilesNeeded = ['big_wordlist.txt','wordplayer_results.txt','wordplayer_testinput.txt']

Dir=os.listdir('.')
for fneeded in FilesNeeded:
    if fneeded not in Dir:
        print('getting',fneeded,'from server')
        req = 'http://128.197.128.203:60216/static/content/'+fneeded
        with urllib.request.urlopen(req) as f:
           p = f.read().decode('utf-8')
           g = open(fneeded,'w')
           g.write(p)
           g.close()


FileName['bigtest'] = FilesNeeded[0]
Input['bigtest'] = open(FilesNeeded[2]).read()
Output['bigtest'] = open(FilesNeeded[1]).read()


# if C++, compile
if testing == 'cpp':
    program = sourcecode[:-4]
    T = subprocess.run(['g++', "-std=c++14", "-O3", sourcecode, "-o", program])

    if T.returncode:
        print(T)
        quit()
else:
    program = sourcecode

# Make the word list files
for case in TestCases:
    f = open(FileName[case], 'w')
    f.write(Wordlist[case])
    f.close()

def runit(case,pytime=0.5):
    if testing == 'py':
        T = subprocess.run([pythonexec,program, FileName[case]],
                           input=Input[case].encode(),
                           stdout=subprocess.PIPE,
                           timeout=pytime)
    else:
        T = subprocess.run([program, FileName[case]],
                           input=Input[case].encode(),
                           stdout=subprocess.PIPE,
                           timeout=pytime/5)
    return T


# this is the spec test case.
class wordplayer_spec_TestCase(unittest.TestCase):
    def test_specs(self):
        for case in TestCases:
            with self.subTest(CASE=case):
                T = runit(case)
                self.assertEqual(T.returncode, 0)
                self.assertEqual(T.stdout.decode(), Output[case])
        #add the passing grade
        if grading:
            grade = 2.0
            print('your score', grade,end=" ")
            Grades.append(grade)




EleganceGoals= {'py':150,'cpp':400}
EfficiencyGoals = {'py':10.0,'cpp':1.0}

#equalize for your processor
st = time.time()
D = {}
for k in range(10000):
    D[k] = random.randint(1,100)
en = time.time()
slow_factor = (en-st)/0.02

Grades =[]

grading = True

class wordplayer_style_TestCase(unittest.TestCase):
    def test_style(self):
        if testing=='py':
            a = pep8.Checker(sourcecode)
            a.check_all()
            self.assertEqual(a.report.total_errors,0)
        else:
            T = subprocess.run(['cpplint',sourcecode],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if T.returncode:
                print()
                print(T.stderr.decode())
            self.assertEqual(T.returncode,0)

        if grading:
            grade = 1.0
            print('your score', grade,end=" ")
            Grades.append(grade)
           


class wordplayer_elegance_TestCase(unittest.TestCase):
    """count the words in the source code"""
    def test_length(self):
        f = open(sourcecode)
        Words = f.read().split()
        f.close()
        if grading:
            grade = min(1.0, EleganceGoals[testing]/len(Words))
            Grades.append(grade)
            print('your words',len(Words),'your score', grade,end=" ")


class wordplayer_efficiency_TestCase(unittest.TestCase):
    """time the program"""
    def test_speed(self):
        case='bigtest'
        st = time.time()
        T = runit(case,pytime=60*slow_factor)
        en = time.time()
        self.assertEqual(T.returncode, 0)
        self.assertEqual(T.stdout.decode(), Output[case])
        your_time = (en-st) / slow_factor


        if grading:
            grade = min(1.0, EfficiencyGoals[testing]/your_time)
            Grades.append(grade)
            print('your time',your_time,'your score', grade,end=" ")


def run_test(name,testcase):
    print('running the {} test'.format(name),end=' ')
    results = unittest.result.TestResult()
    unittest.loader.TestLoader().loadTestsFromTestCase(testcase).run(results)
    passed = results.wasSuccessful()
    print('...passed.' if passed else "...failed.")
    return passed

if __name__ == '__main__':
    passed_spec = run_test('spec',wordplayer_spec_TestCase)
    passed_style = run_test('style',wordplayer_style_TestCase)

    if passed_spec and passed_style:
        run_test('elegance',wordplayer_elegance_TestCase)
        run_test('efficiency',wordplayer_efficiency_TestCase)

    print('total score',sum(Grades),'out of 5.0')

    if sum(Grades)<5:
        print('--------------------------')
        print('now running full unittests')
        print('--------------------------')
        grading = False
        unittest.main()




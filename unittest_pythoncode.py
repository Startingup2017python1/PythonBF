import unittest
import gityghasemi

class Test_pythonbf(unittest.TestCase):
    def test_totalcode(self):
        bfcode='+++++++++++11[->+++++++77>++++++++++110>++++++++++110>++++++++++110>+++++++++99>+++++++++99>+++++++++99>+++33>++++++66>+++++++++99>+++++++++99>++++++++++110>+++++++++99>+++++++++99>++++++++++110>+++++++++99>+++++++++99<<<<<<<<<<<<<<<<<]>.>+.>+++++.>++++++.>--.>+++.>--.>-.>-.>+++++.>--.>.>++++.>--.>++++.>+++++.>--.'
        self.assertEqual(gityghasemi.execute(bfcode), 'Mostafa Ahangarha')

        bfcode='++++[->++++++++<]-[----->>++>++<<<]>>+++++++.>-.+++.<+++++.>-------.+++.<<.>>.+.+++.------.+++++++.-----.<<+.'
        self.assertEqual(gityghasemi.execute(bfcode), 'mehrad dehbid!')

        bfcode='>+++++++[<++++++++++> -]<+.print G>> ++++++++[< +++++++++>-]<+.print I>>+++++++++++++++++++++[<++++>-]< .print T>> +++++++++++[< ++++++++> -]<+.print Y>++++++++++++++++++++++++++++++++.print ''>>+++++++[< ++++++++++> -]<+.print G>> ++++++++[< +++++++++> -]<. print H>> +++++++++++++[< +++++> -]<.print A>> +++++++++++++++++++++[< ++++> -]< -.print S>> +++++++++++++++++++++++[< +++> -]<.print E>> +++++++++++[< +++++++>-]<.print M>>++++++++[<+++++++++>-]<+.print I'
        self.assertEqual(gityghasemi.execute(bfcode), 'GITY GHASEMI')
        
    def test_errors(self):
        #test unbalance bracket
        bfcode='++++[->++++++++<]------>>++>++<<<].'
        self.assertRaises(Exception,gityghasemi.execute,bfcode)
        
        #test overflow pointer
        bfcode='>'*700000 + '++++.'
        self.assertRaises(Exception.gityghasemi.execute,bfcode)
        
        #test underflow pointer
        bfcode='++++>++++<------.'
        self.assertRaises(Exception.gityghasemi.execute,bfcode)
        
        #test Memory overflow
        bfcode='+'*256+'.'
        self.assertRaises(Exception.gityghasemi.execute,bfcode)
        
        #test Memory underflow
        bfcode='++++>++'+'<-----'
        self.assertRaises(Exception.gityghasemi.execute,bfcode)
        

if __name__ == '__main__':
    unittest.main()
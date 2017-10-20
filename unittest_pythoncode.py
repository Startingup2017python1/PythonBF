import unittest
import gityghasemi

class Test_pythonbf(unittest.TestCase):
    def test_totalcode(self):
        bf_code='+++++++++++11[->+++++++77>++++++++++110>++++++++++110>++++++++++110>+++++++++99>+++++++++99>+++++++++99>+++33>++++++66>+++++++++99>+++++++++99>++++++++++110>+++++++++99>+++++++++99>++++++++++110>+++++++++99>+++++++++99<<<<<<<<<<<<<<<<<]>.>+.>+++++.>++++++.>--.>+++.>--.>-.>-.>+++++.>--.>.>++++.>--.>++++.>+++++.>--.'
        self.assertEqual(gityghasemi.python_bf(bf_code),'Mostafa Ahangarha')

        #bf_code='++++[->++++++++<]-[----->>++>++<<<]>>+++++++.>-.+++.<+++++.>-------.+++.<<.>>.+.+++.------.+++++++.-----.<<+.'
        #self.assertEqual(gityghasemi.python_bf(bf_code), 'mehrad dehbid!')

        bf_code='>+++++++[<++++++++++> -]<+.print G>> ++++++++[< +++++++++>-]<+.print I>>+++++++++++++++++++++[<++++>-]< .print T>> +++++++++++[< ++++++++> -]<+.print Y>++++++++++++++++++++++++++++++++.print >>+++++++[< ++++++++++> -]<+.print G>> ++++++++[< +++++++++> -]<. print H>> +++++++++++++[< +++++> -]<.print A>> +++++++++++++++++++++[< ++++> -]< -.print S>> +++++++++++++++++++++++[< +++> -]<.print E>> +++++++++++[< +++++++>-]<.print M>>++++++++[<+++++++++>-]<+.print I'
        self.assertEqual(gityghasemi.python_bf(bf_code), 'GITY GHASEMI')
        
    def test_errors(self):
        #test unbalance bracket
        bf_code='++++[->++++++++<]------>>++>++<<<].'
        self.assertRaises(Exception,gityghasemi.python_bf,bf_code)
        
                
        #test underflow pointer
        bf_code='++++>++++<------.'
        self.assertRaises(Exception,gityghasemi.python_bf,bf_code)
        
        #test Memory overflow
        bf_code='+'*256+'.'
        self.assertRaises(Exception,gityghasemi.python_bf,bf_code)
        
        #test Memory underflow
        bf_code='++++>++'+'<-----.'
        self.assertRaises(Exception,gityghasemi.python_bf,bf_code)
        

if __name__ == '__main__':
    unittest.main()

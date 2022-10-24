


import unittest


from triangle import classify_triangle



class TestTriangles(unittest.TestCase):

    # define multiple sets of tests as functions with names that begin


    def testRightTriangleA(self): 

        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        

    def testRightTriangleB(self): 

        self.assertEqual(classify_triangle(5,12,13),'Right','5,12,13 is a Right triangle')
    

    def testRightTriangleC(self): 

        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    

    def testIsoscelesTriangleA(self): 

        self.assertEqual(classify_triangle(2,2,3),'Isosceles','2,2,3 is a Isosceles triangle')
    

    def testIsoscelesTriangleB(self): 

        self.assertEqual(classify_triangle(4,4,5),'Isosceles','4,4,5 is a Isosceles triangle')


    def testScaleneTriangleA(self):

        self.assertEqual(classify_triangle(10,11,12),'Scalene','10,11,12 is a Scalene triangle')    



    def testScaleneTriangleB(self):

        self.assertEqual(classify_triangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')    


    def testEquilateralTrianglesA(self): 

        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 is a equilateral triangle')


    def testEquilateralTrianglesB(self): 

        self.assertEqual(classify_triangle(2,2,2),'Equilateral','2,2,2 is a equilateral triangle')


    def testInputsA(self):

      self.assertEqual(classify_triangle(-2,-3,-4),'InvalidInput','Only positive values valid' )
    

    def testInputsB(self):

      self.assertEqual(classify_triangle(-2,-3,-4),'InvalidInput','Only positive values valid' )


    def testInputsC(self):

      self.assertEqual(classify_triangle(-2,-3,-4),'InvalidInput','Only positive values valid' )
    



if __name__ == '__main__':
    print('Running unit tests')

    unittest.main()
 


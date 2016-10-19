#coding=utf8

import unittest
from result2 import Result, Ok, Err

class ResultTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetSuccessData(self):
        ok = Ok(1)
        self.assertEqual(ok(), 1, 'test get success data fail')


    def testGetMultiSuccessData(self):
        ok = Ok(1, 2)
        n1, n2 = ok()
        self.assertEqual(n1, 1, 'test get multi success data1 fail')
        self.assertEqual(n2, 2, 'test get multi success data2 fail')


    def testGetErrorData(self):
        err = Err('error')
        self.assertEqual(err(), 'error', 'test get error data fail')


    def testEqSuccess(self):
        rs = Ok()
        self.assertTrue(rs == Result.Ok, 'test result equal success fail')


    def testEqError(self):
        rs = Err("error")
        self.assertTrue(rs == Result.Err, 'test result equal failure fail')

if __name__ == "__main__":
    unittest.main()

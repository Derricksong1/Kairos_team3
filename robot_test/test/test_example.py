#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        # 테스트할 함수 또는 로직
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_subtraction(self):
        # 또 다른 테스트 케이스
        result = 5 - 3
        self.assertEqual(result, 2)

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('robot_test', 'test_example', TestExample)
# -*- coding: utf-8 -*-
import unittest


if __name__ == "__main__":
    suite = unittest.TestLoader().discover('test', pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=3).run(suite)
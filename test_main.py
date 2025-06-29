import unittest 
import main 

class TestFunc(unittest.TestCase): # テストのためのクラス
    def test_func(self): # 関数テストのためのメソッド
        value1 = 1 # 引数1
        value2 = 2 # 引数2
        expected = 3 # 期待値
        actual = main.func(value1, value2) # 関数実行結果
        self.assertEqual(expected, actual) # 合否判断（結果比較）

if __name__ == '__main__':
    unittest.main()

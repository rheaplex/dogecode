import translation

import unittest

# Hello World, from Wikipedia
HELLO_WORLD = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."


class TestTranslation(unittest.TestCase):
        
    def test_to_and_from_tokens(self):
        tokens = translation.source_to_tokens(HELLO_WORLD, True)
        source = translation.token_runs_to_code(tokens)
        self.assertEqual(source, HELLO_WORLD)

    def test_token_list_equality(self):
        t1 = translation.TokenList()
        t1.append("INCB", 8)
        t1.append("JFOR", 1)
        t1.append("INCP", 1)
        t1.append("INCB", 4)
        t1.append("JFOR", 1)
        t2 = translation.TokenList()
        t2.append("INCB", 8)
        t2.append("JFOR", 1)
        t2.append("INCP", 1)
        t2.append("INCB", 4)
        t2.append("JFOR", 1)
        # Identity
        self.assertTrue(t1.equals(t1))
        self.assertTrue(t2.equals(t2))
        # Reflexivity
        self.assertTrue(t1.equals(t2))
        self.assertTrue(t2.equals(t1))

    def test_token_list_subsequence(self):
        t1 = translation.TokenList()
        t1.append("INCB", 8)
        t1.append("JFOR", 1)
        t1.append("INCP", 1)
        t1.append("INCB", 4)
        t1.append("JFOR", 1)
        t2 = translation.TokenList()
        t2.append("INCB", 8)
        t2.append("JFOR", 1)
        t2.append("INCP", 1)
        self.assertTrue(t2.is_subsequence_of(t1))
        self.assertFalse(t1.is_subsequence_of(t2))
        self.assertFalse(t1.is_subsequence_of(t1))
        
if __name__ == '__main__':
    unittest.main()

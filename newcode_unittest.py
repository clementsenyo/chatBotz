import unittest


from newcode import chatbot

correct_question = 'How are the reviews of digit course?'
correct_answers =  [
        "the feedback of the students from digit are excellent",
        "students find digit as a great platform to develop software skills",
    ]

incorrect_question = 'WHY ?'
incorrect_answer ="I don't have suggestions for that keyword."



class TestChatbot(unittest.TestCase):
    def test_incorrect_question(self):
        output = chatbot(incorrect_question)
        self.assertEqual(output, incorrect_answer, 'Incorrect response')
    
    def test_correct_question(self):
        output = chatbot(correct_question)
        self.assertTrue(output in correct_answers, 'Incorrect response')


if __name__ == '__main__':
    unittest.main()
    
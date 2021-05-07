import unittest
import sys, os
if os.name == 'posix':
    sep = '/'
else:
    sep = '\\'
sys.path.append(os.getcwd().rsplit(sep,1)[0])
from core import operations
from operations_tests.util_decorators import timeout

class FunctionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.positive_number_1 = "198"
        self.positive_number_2 = "10"
        self.result_pow_1 = "92608724480901579777024"
        self.result_pow_2 = "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

        self.positive_number_3 = "1840"
        self.positive_number_4 = "5"
        self.result_pow_3 = "21090608742400000"
        self.result_pow_4 = "127294013072422328041236845090446127638340977530666275103409770358200396924617149696992363284388202367417678989068612871866140081788088569875541661813378458412784935205015927936578070341638438516898273140013737141922632210602940553994786333127060070209638375083291838142772160892593271094876812380249088251480981822329933096214451764721894177441697250956117265414914339771554544416805346752490647278429172345544852677950948439811432773377670643725467226168513480158807131478340987176822756474157605699798533404880293011739454437466156075579040882635033016075597802606866951559279482578507462042138207427258059990871818209323858404362141206666708531868956524683246736375800195692440620263320375905265120498704466823131164293090303607104580249371552051971452771672445343445946869053288092913789874920362294068741649509522984197849771767314055733550026442648877633039985290434020329128771717838417098443707918465682761490824515615588669712713317415956326402867195185270465408752900702573059662284572841103286816248694983884338442641439734776471167097078180066689299319880247778917687442920959248129449837086686875628093930124197298904695324237288602032381094137116048810979180684295644799454154712388727717201962034769716808334296976838770945641130839798282892161296331323683261871337890625"

        self.negative_number_1 = "-132"
        self.negative_number_2 = "-356"

        self.wrong_char_number_1 = "dq"
        self.wrong_char_number_2 = "das"

        self.test_object = operations.Operations()

    @timeout(60)
    def test_positive_numbers(self):

        self.assertEqual(self.test_object.power_numbers(first_number=self.positive_number_1,
                                                        second_number=self.positive_number_2),
                         self.result_pow_1)

        self.assertTrue(self.test_object.power_numbers(first_number=self.positive_number_2,
                                                       second_number=self.positive_number_1),
                        self.result_pow_2)

        self.assertEqual(self.test_object.power_numbers(first_number=self.positive_number_3,
                                                        second_number=self.positive_number_4),
                         self.result_pow_3)

        self.assertTrue(self.test_object.power_numbers(first_number=self.positive_number_4,
                                                       second_number=self.positive_number_3),
                        self.result_pow_4)

    @timeout(20)
    def test_negative_numbers(self):

        #aici trebuie gasita o varianta, dare ok si asa
        print(self.test_object.power_numbers(first_number=self.negative_number_1,
                                             second_number=self.negative_number_2))

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.negative_number_1,
                                           second_number=self.negative_number_2)

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.negative_number_1,
                                           second_number=self.positive_number_1)

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.negative_number_2,
                                           second_number=self.positive_number_1)

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.negative_number_1,
                                           second_number=self.positive_number_2)

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.negative_number_2,
                                           second_number=self.positive_number_2)

    def test_wrong_numbers(self):

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.wrong_char_number_1,
                                           second_number=self.wrong_char_number_2)

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.wrong_char_number_1,
                                           second_number=self.positive_number_1)

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.wrong_char_number_2,
                                           second_number=self.positive_number_1)

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.wrong_char_number_1,
                                           second_number=self.positive_number_2)

        with self.assertRaises(ValueError):
            self.test_object.power_numbers(first_number=self.wrong_char_number_2,
                                           second_number=self.positive_number_2)


if __name__ == '__main__':
    unittest.main()
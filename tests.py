# -*- coding: utf-8 -*-
import unittest

from leap.year import is_leap_year
from bob import bob

from wordcount.wordcount import word_count
from rnatranscription.dna import to_rna


class BobTests(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(
            'Whatever.',
            bob.hey('Tom-ay-to, tom-aaaah-to.')
        )

    def test_shouting(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.hey('WATCH OUT!')
        )

    def test_asking_a_question(self):
        self.assertEqual(
            'Sure.',
            bob.hey('Does this cryogenic chamber make me look fat?')
        )

    def test_asking_a_numeric_question(self):
        self.assertEqual(
            'Sure.',
            bob.hey('You are, what, like 15?')
        )

    def test_talking_forcefully(self):
        self.assertEqual(
            'Whatever.',
            bob.hey("Let's go make out behind the gym!")
        )

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            'Whatever.', bob.hey("It's OK if you don't want to go to the DMV.")
        )

    def test_forceful_questions(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('WHAT THE HELL WERE YOU THINKING?')
        )

    def test_shouting_numbers(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('1, 2, 3 GO!')
        )

    def test_only_numbers(self):
        self.assertEqual(
            'Whatever.', bob.hey('1, 2, 3')
        )

    def test_question_with_only_numbers(self):
        self.assertEqual(
            'Sure.', bob.hey('4?')
        )

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.hey('ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!')
        )

    def test_shouting_with_umlauts(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('ÜMLÄÜTS!')
        )

    def test_calmly_speaking_with_umlauts(self):
        self.assertEqual(
            'Whatever.', bob.hey('ÜMLäÜTS!')
        )

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('I HATE YOU')
        )

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            'Whatever.', bob.hey('Ending with ? means a question.')
        )

    def test_prattling_on(self):
        self.assertEqual(
            'Sure.', bob.hey("Wait! Hang on. Are you going to be OK?")
        )

    def test_silence(self):
        self.assertEqual(
            'Fine. Be that way!', bob.hey('')
        )

    def test_prolonged_silence(self):
        self.assertEqual(
            'Fine. Be that way!', bob.hey('    \t')
        )

    def test_starts_with_whitespace(self):
        self.assertEqual(
            'Whatever.', bob.hey('         hmmmmmmm...')
        )

    def test_ends_with_whitespace(self):
        self.assertEqual(
            'Sure.', bob.hey('What if we end with whitespace?   ')
        )


class YearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertIs(is_leap_year(1996), True)

    def test_non_leap_year(self):
        self.assertIs(is_leap_year(1997), False)

    def test_non_leap_even_year(self):
        self.assertIs(is_leap_year(1998), False)

    def test_century(self):
        self.assertIs(is_leap_year(1900), False)

    def test_exceptional_century(self):
        self.assertIs(is_leap_year(2400), True)


class WordCountTests(unittest.TestCase):
    def test_count_one_word(self):
        self.assertEqual(
            {'word': 1},
            word_count('word')
        )

    def test_count_one_of_each(self):
        self.assertEqual(
            {'one': 1, 'of': 1, 'each': 1},
            word_count('one of each')
        )

    def test_count_multiple_occurences(self):
        self.assertEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            word_count('one fish two fish red fish blue fish')
        )

    def test_preserves_punctuation(self):
        self.assertEqual(
            {'car': 1, 'carpet': 1, 'as': 1, 'java': 1, ':': 2, 'javascript!!&@$%^&': 1},
            word_count('car : carpet as java : javascript!!&@$%^&')
        )

    def test_include_numbers(self):
        self.assertEqual(
            {'testing': 2, '1': 1, '2': 1},
            word_count('testing 1 2 testing')
        )

    def test_mixed_case(self):
        self.assertEqual(
            {'go': 1, 'Go': 1, 'GO': 1},
            word_count('go Go GO')
        )

    def test_multiple_spaces(self):
        self.assertEqual(
            {'wait': 1, 'for': 1, 'it': 1},
            word_count('wait for       it')
        )

    def test_newlines(self):
        self.assertEqual(
            {'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
             'want': 1, 'your': 1, 'bad': 1, 'romance': 1},
            word_count('rah rah ah ah ah\nroma roma ma\nga ga oh la la\nwant your bad romance')
        )


class DNATests(unittest.TestCase):
    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual('C', to_rna('G'))

    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual('G', to_rna('C'))

    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual('A', to_rna('T'))

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual('U', to_rna('A'))

    def test_transcribes_all_occurences(self):
        self.assertEqual('UGCACCAGAAUU', to_rna('ACGTGGTCTTAA'))


if __name__ == '__main__':
    unittest.main()
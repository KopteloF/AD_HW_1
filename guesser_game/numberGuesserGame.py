from random import randrange
from .GuesserGame import Guesser

class GuessMyNumber(Guesser):

    """ GuessMyNumber class for calculating the result of arithmetic operations applied to an unknow number
    given by the player


    Attributes:
        numberinMind represents the number a player has in mind at the end of the game
        magicNumber represents the most important number in this game, it will be used to 'guess' the numberinMind

    """

    def __init__(self, number=0):

        Guesser.__init__(self,number)
        self.magicNumber = 2


    def play(self):
        '''Function to play GuessMyNumber
        Args:
            None
        Returns:
            None
        '''
        self.giveInstructions()
        self.numberinMind = self.guessingNumber()
        print('...')
        print('Ваш результат {}'.format(int(self.numberinMind)))



    def giveInstructions(self):
        '''Function to display directions to play
        Args:
            None

        Returns:
            None
        '''

        self.magicNumber = self.generateMagicNumber()
        print('Выполните эти действия, и я угадаю ваш результат')
        input("Нажмите Enter для продолжения...")
        print('Давайте играть!')
        print('Загадайте число больше 0, не говорите.')
        input("Нажмите Enter для продолжения...")
        print('Умножьте ваше число на 2')
        input("Нажмите Enter для продолжения...")
        print('Добавьте {}'.format(self.magicNumber))
        input("Нажмите Enter для продолжения...")
        print('Разделите полученный результат на 2')
        input("Нажмите Enter для продолжения...")
        print('На последнем этапе вычтите из полученного результата число, которое вы изначально загадали')
        input("Нажмите Enter для продолжения...")
        print('...')
        print('Угадываю ваш результат...')


    def generateMagicNumber(self):
        '''Function to generate an even random number between 4 and 24
        Args:
            None

        Returns:
            Integer: An even number between 4 and 24
        '''
        n = randrange(4, 24, 2)
        return int(n)


    def guessingNumber(self):
        '''Function to 'guess' the result of arithmetic operations calculated during the GuessMyNumber
           game.
        Args:
            None

        Returns:
            Integer: the result of arithmetic operations
        '''

        return self.magicNumber / 2
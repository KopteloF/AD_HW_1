import datetime as dt

from application.db.salary import calculate_salary
from application.people import get_employees
from guesser_game import GuessMyNumber

if __name__ == '__main__':
    calculate_salary()
    get_employees()

    my_game = GuessMyNumber()
    my_game.play()

    print(dt.datetime.date(dt.datetime.now()))

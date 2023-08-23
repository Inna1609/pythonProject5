from lesson17.yest_human import Human

class TestHuman:
    def test_check_age(self):
        human = Human('Alfred', 78, 'grey')
        human.grow()
        assert human.age ==79
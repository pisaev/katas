class Year:
	def __init__(self, year):
		self.year = year

	def is_leap(self):
		return self.divisible_by(4) and not (self.divisible_by(100) and not self.divisible_by(400))

	def divisible_by(self, num):
		return self.year % num == 0


def test_year_is_not_a_leap_year_if_not_divisible_by_4():
	assert Year(1997).is_leap() == False

def test_year_is_a_leap_year_if_divisible_by_4():
	assert Year(1996).is_leap() == True

def test_year_is_a_leap_year_if_divisible_by_400():
	assert Year(1600).is_leap() == True

def test_year_is_not_a_leap_year_if_divisible_by_100_but_not_by_400():
	assert Year(1800).is_leap() == False

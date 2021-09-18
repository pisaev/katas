"""
Write the smallest program that outputs the lyrics of the Xmas carol The Twelve Days of Xmas.
You must reproduce the words in the correct order, but case, format, and punctuation are left to your discretion.

The lyrics are as follows:
"""
EXPECTED = '''On the first day of Christmas
My true love gave to me:
A partridge in a pear tree.

On the second day of Christmas
My true love gave to me:
Two turtle doves and
A partridge in a pear tree.

On the third day of Christmas
My true love gave to me:
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the forth day of Christmas
My true love gave to me:
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the fifth day of Christmas
My true love gave to me:
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the sixth day of Christmas,
My true love gave to me:
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the seventh day of Christmas,
My true love gave to me:
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the eight day of Christmas,
My true love gave to me:
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the ninth day of Christmas,
My true love gave to me:
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the tenth day of Christmas,
My true love gave to me:
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the eleventh day of Christmas,
My true love gave to me:
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the Twelfth day of Christmas,
My true love gave to me:
Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves
And a partridge in a pear tree.
'''

lines = [
		'A partridge in a pear tree.',
		'Two turtle doves',
		'Three french hens',
		'Four calling birds',
		'Five golden rings',
		'Six geese a-laying',
		'Seven swans a-swimming',
		'Eight maids a-milking',
		'Nine ladies dancing',
		'Ten lords a-leaping',
		'Eleven pipers piping',
		'Twelve drummers drumming'
	]

def generate_twelve_days_of_xmas_lyrics():
	return '\n'.join([create_verse(verse_idx) for verse_idx in range(0, 12)])

def create_verse( verse_idx):
	return prefixLinesFor(verse_idx) + middleLinesFor(verse_idx) + lastLineFor(verse_idx)

def comma_from_the_forth_day(dayNumber):
	return ',' if dayNumber > 4 else ''

def prefixLinesFor(dayNumber):
	counts = [
		'first',
		'second',
		'third',
		'forth',
		'fifth',
		'sixth',
		'seventh',
		'eight',
		'ninth',
		'tenth',
		'eleventh',
		'Twelfth'
	]
	return f'On the {(counts[dayNumber])} day of Christmas{comma_from_the_forth_day(dayNumber)}\n'\
		   'My true love gave to me:\n'

def middleLinesFor(verse_idx):
	return '\n'.join(lines[verse_idx:0:-1])

def lastLineConnector(index):
	if index ==0 :
		return ''
	elif 0 < index < 11:
		return ' and\n'
	else:
		return '\nAnd '

def lastLineFor(verse_idx):
	return f'{lastLineConnector(verse_idx)}{lines[0] if verse_idx < 11 else lines[0].lower()}\n'

def test_twelve_days_of_xmas():
	assert generate_twelve_days_of_xmas_lyrics() == EXPECTED

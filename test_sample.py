import main as main

def test_filter():
	assert main.filter('') == False
	assert main.filter('123') == False
	assert main.filter('12345') == False
	assert main.filter('12a4') == False
	assert main.filter('1244') == False

	assert main.filter('1234') == True

def test_logic():
	bulls, cows, win = main.gameLogic('1234', '1234')
	assert [bulls, cows, win] == [0, 0, 1]

	bulls, cows, win = main.gameLogic('5678', '1234')
	assert [bulls, cows, win] == [0, 0, 0]

	bulls, cows, win = main.gameLogic('1239', '1234')
	assert [bulls, cows, win] == [3, 0, 0]

	bulls, cows, win = main.gameLogic('1324', '1234')
	assert [bulls, cows, win] == [2, 2, 0]
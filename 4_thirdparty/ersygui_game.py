import easygui as g
import sys

while True:
	g.msgbox('welcome to the first game.\nHave a good taste')

	msg = 'What kind of knowledge do you want to learn at this class?'
	title = 'Little game'
	choices = ['singing', 'programming', 'Writting']

	choice = g.choicebox(msg, title, choices)

	##
	g.msgbox('Your choice is:' + str(choice), title = 'result')

	msg = 'Do you want to play this game again?'
	title  = 'Please make your choice:'

	if g.ccbox(msg, title):		#show a Continue/Cancel dialog
		pass		#user choose Continue
	else:
		sys.exit(0)	#user choose Cancel

from survey import AnonymousSurvey
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("Enter 'q' to quit")
while True:
	response = input('Language:')
	if response == 'q':
		break

	my_survey.store_response(response)

print('\nThank you to everyone who participated in the survey!')
my_survey.show_result()
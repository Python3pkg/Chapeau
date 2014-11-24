import server
import threading


user_answers = {}

def first(request, client):
	print request
	if 'question1' in request['body'].keys():
		header = {'Set-Cookie': 'question1=%s' %request['body']['question1']}
		server.render(client, 'views/question_2.html', user_answers, header)
	else:
		server.render(client, 'views/question_1.html', user_answers)

def second(request, client):
	if 'question2' in request['body'].keys():
		header = {'Set-Cookie': 'question2=%s' %request['body']['question2']}
		server.render(client, 'views/question_3.html', user_answers, header)
	else:
		server.render(client, 'views/question_1.html', user_answers)


def third(request, client):
	if 'question3' in request['body'].keys():
		cookies = request['headers']['Cookie'].split('; ')
		for cookie in cookies:
			temp = cookie.split('=')
			user_answers.update({temp[0] : temp[1]})
		user_answers.update({'question3' : request['body']['question3']})
		print user_answers
		server.render(client, 'views/result.html', user_answers)
	else:
		server.render(client, 'views/question_1.html', user_answers)



# def func(dict):
# 	return "SUPERHERO!"

routing_dict = {'/welcome' : 'views/welcome.html',
				'/first_question': 'views/question_1.html',
				'/first_question_post': first,
				'/second_question':  'views/question_2.html',
				'/second_question_post': second,
				'/third_question':  'views/question_3.html',
				'/third_question_post': third}

server.go(routing_dict)
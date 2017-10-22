import timeit


code_snippets = [
'''
import requests
URL = 'http://139.59.132.185:8080'
requests.get(URL)
''',

'''
import requests
URL = 'http://192.81.216.124:8080'
requests.get(URL)
''',

'''
import requests
URL = 'http://128.199.180.131:8080'
requests.get(URL)
'''
]


def take_time(code_snippet, iter):
	setup = '''print('setup')'''

	total_time = timeit.timeit(setup = setup,
                    	stmt = code_snippet,
                    	number = iter)

	avg_time = total_time / iter

	print('total_time = {}'.format(total_time))
	print()
	print('avg_time = {}'.format(avg_time))


def main():
	for snippet in code_snippets:
		take_time(snippet, 10000)



if __name__ == '__main__': main()







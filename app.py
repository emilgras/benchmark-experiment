import timeit


urls = [
	'http://139.59.132.185:8080',
	'http://192.81.216.124:8080',
	'http://128.199.180.131:8080'
]


snippet = '''
import requests
requests.get('{}')
'''


def take_time(snippet, iter):
	setup = '''print()'''

	total_time = timeit.timeit(setup = setup,
                    	stmt = snippet,
                    	number = iter)

	avg_time = total_time / iter

	print('total_time = {}'.format(total_time))
	print('avg_time = {}'.format(avg_time))


def main():
	for url in urls:
		take_time(snippet.format(url), 100)



if __name__ == '__main__': main()







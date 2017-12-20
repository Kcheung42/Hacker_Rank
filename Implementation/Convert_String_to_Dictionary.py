#!/bin/python3

def jsonHelper(json, i):
	if json[i] != '{':
		return
	d = {}
	while (json[i] != '}'):
		if (json[i] == '{' or json[i] == ','):
			i += 1
		key = ''
		while (json[i] != ':'):
			key += json[i]
			i += 1
		i += 1
		if (json[i] != '{'):
			val = ''
			while (json[i] != ',' and json[i] != '}'):
				val += json[i]
				i += 1
			if json[i] == ',':
				i += 1
		else:
			val, i = jsonHelper(json, i)
		d[key] = val
	i += 1 
	return (d,i)

def jsonToDict(json):
	result = jsonHelper(json, 0)
	return result[0]

json = '{a:apples,b:{ba:bat,bo:boy},d:dog}'
# json = '{a:apples,b:{ba:bat,bo:boy}}'
print(jsonToDict(json))


import psycopg2
import os
from threading import Timer

db_str = "postgres://szrufkxz:IVMZS-UXd1LGHFR8I1PzcrsfwPORnXYf@horton.db.elephantsql.com/szrufkxz"
conn = False #psycopg2.connect(db_str)
cur = False #conn.cursor()

def closeConn ():
	global conn
	global cur
	if not conn :
		return
	cur.close()
	conn.close()
	cur = False
	conn = False
	print("db conn closed !")

def connect ():
	global conn
	global cur
	conn = psycopg2.connect(db_str)
	cur = conn.cursor()

	# auto close connection after 10 minutes
	t1 = Timer(600, closeConn)
	t1.start()

def parseOptions (opts, qid):
	# print(opts)
	options = []
	for i in range(len(opts)):
		option = {'oid' : str(qid)+"."+str(i), 'text' : opts[i]}
		# print(options, option)
		options.append(option)

	# print(options)
	return options;

def getData():
	if  not conn :
		connect()

	cur.execute('SELECT * FROM qqs')
	results = cur.fetchall()

	newResults = []
	for result in results :
		qid = result[0]
		question = result[1]

		option1 = {'oid' : str(qid)+".1" , 'text' : result[2][0] }
		option2 = {'oid' : str(qid)+".2" , 'text' : result[2][1] }
		option3 = {'oid' : str(qid)+".3" , 'text' : result[2][2] }
		option4 = {'oid' : str(qid)+".4" , 'text' : result[2][3] }

		answer = result[3]

		newResult = {
			'qid' : qid, 
			'question' : question,
			'option1' : option1, 
			'option2' : option2,
			'option3' : option3,
			'option4' : option4,
			'answer' : answer
		}
		newResults.append(newResult)

	return newResults

# print(getData())

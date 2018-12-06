"""
	1. Create a mysql table ai_nn_emp to contain empno,name,deptcode,desig,salary and insert some records(10)

	 2. Create another table ai_nn_dept to contain dept_no(values match with deptcode of emp ),dept_name,dept_location and
	 insert some records. (nn must be 01,02,03 etc. i.e. as per your username)
	 3. Open ipython and import the necessary modules for data analysis

	 4. load data from ai_nn_emp and ai_nn_dep into different dataframes

	 5. Print empno,name,deptname,salary and store the same to another dataframe in the ascending order of salary column.

	 6. Write the above dataframe (after step5) into another table in mysql named ai_nn_emp_dept.

		(try 'mysql://ai:ai@127.0.0.1:3306/ai' as the parameter for create_engine of sqlalchemy)
			 (dbms://user:password@hostname:portnumber/database)

	7.From the given csv files(items.csv and sales.csv in common/Python_Exercises folder) create two dataframe objects- idf1 and sdf1

	8.Using idf1 and sdf1 print item name, region and sales quantity and store the same in a new dataframe.

	9.Create two dataframes by applying pivot on the above dataframe with region/item name as index/column.


"""

# importing packages  Q3

import psycopg2 as psql # for postgressql
import pandas as pd
from sqlalchemy import create_engine


def connectMySQL():
	import MySQLdb as db
	return db.connect("127.0.0.1","ai","ai","ai")

def connectPostgreSQL():
	return psql.connect(database='postgres', user ='postgres', password ='postgres')

def insert2EmpTable():
	'''
	#### Table creation script ####

	create table ai_29_emp(empno int NOT NULL,name varchar(20) NOT NULL,deptcode int  NOT NULL,desig varchar(20),salary int,PRIMARY KEY (empno));

	'''
	con = None
	names = list(["Tom", "Raj","Tony""Shibin","Aravind","Akshey","Varun","Amel","Nizam","Roy","Rahul"])

	try:
		con = connectMySQL()
	except Exception ,e :
		con = connectPostgreSQL()

	try:
		cur = con.cursor()

		for i in range(10):
			sql = "insert into ai_29_emp values(%s,%s,%s,%s,%s)",(str(i+100),names[i],str(i*200-i),"Enginner",str(100000))
			cur.execute(*sql)

		con.commit()

	except Exception ,e :
		print e
	finally:
		con.close()

def insert2DeptTable():
	'''
	#### Table creation script ####

	create table ai_29_dept(dept_no int NOT NULL,dept_name varchar(20) NOT NULL,dept_location varchar(30),FOREIGN KEY (dept_no) REFERENCES ai_29_emp(deptcode));

	'''
	con = None
	dept_names = list(["CS", "EC", "MEC", "EE", "CIVIL", "AE", "GE", "BE", "CE", "AE", "BIO"])
	locations = list(
		["Calicut", "Palakad", "Thrisur", "Malapuram", "Ernakulam", "Kottayam", "Kollam", "Iduki", "Trivandrum",
		 "Alapuzha", "Waynad"])

	try:
		con = connectMySQL()
	except Exception ,e :
		con = connectPostgreSQL()

	try:

		for i in range(10):
			sql = "insert into ai_29_dept values(%s,%s,%s,%s,%s)", (str(i * 200 - i), dept_names[i], locations[i])
			cur.execute(*sql)

		con.commit()

	except Exception, e:
		print e
	finally:
		con.close()

def readFromDBasDF():
	con = None
	try:
		con = connectMySQL()
	except Exception ,e :
		con = connectPostgreSQL()

	try:
		empDf = pd.read_sql("select * from ai_29_emp", con)
		print empDf

		deptDf = pd.read_sql("select * from ai_29_dept", con)
		print deptDf

	except Exception, e:
		print e
	finally:
		con.close()


# Main Section -- START
insert2EmpTable() # Q1
insert2DeptTable() # Q2

# database connection object
con = None

try:
	con = db.connect("127.0.0.1", "ai", "ai", "ai")
	empDf = pd.read_sql("select * from ai_29_emp", con) # Q4
	print empDf

	deptDf = pd.read_sql("select * from ai_29_dept", con) # Q4
	print deptDf

	#  5. Print empno,name,deptname,salary and store the same to another dataframe in the ascending order of salary column.
	df = pd.merge(empDf,deptDf, left_on="deptcode", right_on="dept_no", how="outer")[['empno','name','deptname','salary']]
	print df
	df_sorted = df.sort_values('salary', inplace=True, ascending=True)
	print df_sorted

	#  6. Write the above dataframe (after step5) into another table in mysql named ai_nn_emp_dept.
	ce = create_engine('mysql://ai:ai@127.0.0.1:3306/ai')
	df_sorted.to_sql("ai_29_emp_dept", ce, index=False)


except Exception, e:
	print e
finally:
	con.close()

# 7.From the given csv files(items.csv and sales.csv in common/Python_Exercises folder) create two dataframe objects- idf1 and sdf1

idf1 = pd.read_csv("items.csv")
sdf1 = pd.read_csv("sales.csv")
print idf1
print sdf1

# 8.Using idf1 and sdf1 print item name, region and sales quantity and store the same in a new dataframe.
idsdDf = pd.merge(idf1,sdf1, left_on='id', right_on='tid', how='inner')[['name','region','sale_qty']]
print idsdDf


# 9.Create two dataframes by applying pivot on the above dataframe with region/item name as index/column.

pivTable = idsdDf.pivot(index='region', columns='name', values='sale_qty')
print pivTable

# Main Section -- END


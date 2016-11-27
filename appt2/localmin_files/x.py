import urllib
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
urllib.urlretrieve(url,'Userstat_.txt')



'''import sqlite3
connection=sqlite3.connect('filename.db')
print ("opened successfully")
#connection.execute("CREATE TABLE DATA (x,y)")
#connection.execute("INSERT INTO DATA (x,y) VALUES (4,5)");
x2=connection.execute("SELECT x FROM DATA")
y2=connection.execute("SELECT y FROM DATA")
connection.commit()
d3=[]
for d in x2:
	print(d,type(d),d[0])
	d3.append(d[0])
for d2 in y2:
	print(d2)
connection.close()
print(d3)
'''

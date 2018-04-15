from flask import Flask
from flask_mysqldb import MySQL
import datetime


class dao(MySQL):
	def __init__(self, app, host='localhost', port=3306, uname='root', upw='root', dbname='doraemon'):
		app.config['MYSQL_HOST'] = host
		app.config['MYSQL_PORT'] = port
		app.config['MYSQL_DB']   = dbname
		app.config['MYSQL_USER'] = uname
		app.config['MYSQL_PASSWORD'] = upw
		MySQL.__init__(self, app)

	def get_position(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM position")

		data = []
		for element in cursor.fetchall():
			data.append({'id': element[0], 'datetime': str(element[1]), 'position': {'lat': element[2], 'lon': element[3]}})

		return data
		
			

	def get_drive(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM drive")

		data = []
		for element in cursor.fetchall():
			data.append({'id': element[0], 'datetime': str(element[1]), 'fuel_efi': element[2], 'speed': element[3]})

		return data
		
			

	def add_position(self, id, lat, lon):
		cursor = self.connection.cursor()
		cursor.execute('''INSERT INTO position (car_id, pos_time, pos_x, pos_y) VALUES(%s, now(), %s, %s)''', (id, lat, lon))
		self.connection.commit()
		return {'id': id, 'position': {'lat': lat, 'lon': lon}}
		


	def add_drive(self, id, fuel_efi, speed):
		cursor = self.connection.cursor()
		cursor.execute('''INSERT INTO position (car_id, pos_time, pos_x, pos_y) VALUES(%s, now(), %s, %s)''', (id, fuel_efi, speed))
		self.connection.commit()
		return {'id': id, 'fuel_efi': fuel_efi, 'speed': speed}
		

	def set_car(self, id, uid, cname, volume, fuel, fuel_efi):
		query = '''
				INSERT INTO car (car_id, usr_id, car_name, volume, fuel, fuel_efi)
				VALUES ('{id}', '{uid}', '{cname}', '{volume}', '{fuel}', '{fuel_efi}')
				ON DUPLICATE KEY UPDATE
				car_name = '{cname}',
				volume = '{volume}',
				fuel = '{fuel}',
				fuel_efi = '{fuel_efi}'
				'''.format(id=id, uid=uid, cname=cname, volume=volume, fuel=fuel, fuel_efi=fuel_efi)
		cursor = self.connection.cursor()
		cursor.execute(query);
		self.connection.commit()
		return self.get_car()

		

	def get_car(self, id):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM car WHERE car_id LIKE %s", (id,))

		data = []
		for element in cursor.fetchall():
			data.append({'id': element[0], 'uname': str(element[1]), 'cname': element[2], 'volume': element[3], 'fuel': element[4], 'fuel_efi': element[5]})

		return data
		

	def register_user(self, id, name, token):
		query = '''
				INSERT INTO users (usr_id, usr_name, token)
				VALUES ('{id}', '{name}', '{token}')
				ON DUPLICATE KEY UPDATE
				usr_name = '{name}',
				token = '{token}'
				'''.format(id=id, name=name, token=token)
		cursor = self.connection.cursor()
		cursor.execute(query);
		self.connection.commit()

		return self.get_user(id)
		

	def get_user(self, id):
		cursor = self.connection.cursor()
		cursor.execute('''SELECT * FROM users WHERE usr_id LIKE %s''', (id,))
		data = cursor.fetchone()
		return {'id': data[0], 'name': data[1], 'token': data[2]}
		

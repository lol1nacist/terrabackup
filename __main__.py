import shutil, os, time, subprocess, sys
import webbrowser as wb

from datetime import datetime

if 'path.py' in os.listdir():
	pass
else:
	with open('path.py', 'w') as file:
		file.write("path = 'PATH'\ncustompath = 'CUSTOMPATH'\nsavepath = 'SAVEPATH'\nans = 'NANS'")
		pass
time.sleep(0.5)
import path
print('Terrabackup alpha 0.0.1')
print('<For more run with admin rights>')
print()
time.sleep(0.8)
if path.savepath == "SAVEPATH":
	savepath = ''
else:
	savepath = path.savepath
run = True
savecount = False
while run:
	import path
	print('Enter using mode')
	print('0 -- Backup')
	print('1 -- Backup and play')
	print('2 -- Load latest backup')
	print('3 -- Customize save path')
	print('4 -- Just start Terraria')
	print()
	mode = str(input())

	if savecount:
		path.savepath = dsavepath

	if mode == '0':
		if path.custompath == 'CUSTOMPATH':
			paths = [os.path.expandvars('C:/Users/%username%/documents/my games/terraria/players'),
				 	 os.path.expandvars('C:/Users/%username%/documents/my games/terraria/worlds')]
		else:
			paths = [path.custompath + '/players',
					 path.custompath + '/worlds']

		try:
			for i in paths: os.listdir(i)

		except FileNotFoundError:
			print('File not found, please enter manually:')
			if path.custompath == 'CUSTOMPATH':
				custompath = input()
				new_custom_path = ''
				for i in custompath:
					if i not in R'\\':
						new_custom_path += i
					else:
						new_custom_path += '/'
				with open('path.py', 'r') as file:
					pathtext = file.read()
				with open('path.py', 'w') as file:
					file.write(pathtext.replace("'CUSTOMPATH'", new_custom_path))
				print('Please, restart this program to save the changes')
				time.sleep(3)
				quit()


		if path.savepath == 'SAVEPATH' and savepath == '':
			directory = str(datetime.now())[:10]+' '+str(datetime.now().hour)+'-'+str(datetime.now().minute)+'-'+str(datetime.now().second)
			time.sleep(1)
			os.makedirs(directory)
			shutil.copytree(paths[0], directory+'/players')
			shutil.copytree(paths[1], directory+'/worlds')
		else:
			directory = str(datetime.now())[:10]+' '+str(datetime.now().hour)+'-'+str(datetime.now().minute)+'-'+str(datetime.now().second)
			time.sleep(1)
			os.makedirs(savepath +directory)
			shutil.copytree(paths[0], savepath +directory+'/players')
			shutil.copytree(paths[1], savepath +directory+'/worlds')


	if mode == '1':
		name = ['terraria.exe','Terraria.exe']
		new_terraria_path = ''


		if path.path == 'PATH':
			print('Please enter the Terraria.ink path:')
			terraria_path = str(input())
		else:
			terraria_path = path.path



		new_terraria_path = ''

		for i in list(terraria_path):
			if i not in R'\\':
				new_terraria_path += i
			else:
				new_terraria_path += '/'

		terraria_path = new_terraria_path

		if path.custompath == 'CUSTOMPATH':
			paths = [os.path.expandvars('C:/Users/%username%/documents/my games/terraria/players'),
				 	 os.path.expandvars('C:/Users/%username%/documents/my games/terraria/worlds')]
		else:
			paths = [path.custompath + '/players',
					 path.custompath + '/worlds']

		with open('path.py', 'r') as file:
			pathtext = str(file.read())
		with open('path.py', 'w') as file:
			file.write(pathtext.replace("'PATH'", "'"+new_terraria_path+"'"))

		try:
			for i in paths: os.listdir(i)

		except FileNotFoundError:
			print('File not found, please enter manually:')
			if path.custompath == 'CUSTOMPATH':
				custompath = input()
				new_custom_path = ''
				for i in custompath:
					if i not in R'\\':
						new_custom_path += i
					else:
						new_custom_path += '/'
				with open('path.py', 'r') as file:
					pathtext = file.read()
				with open('path.py', 'w') as file:
					file.write(pathtext.replace("'CUSTOMPATH'", new_custom_path))
				print('Please, restart this program to save the changes')
				time.sleep(3)
				quit()


		if path.savepath == 'SAVEPATH' and savepath == '':
			directory = str(datetime.now())[:10]+' '+str(datetime.now().hour)+'-'+str(datetime.now().minute)+'-'+str(datetime.now().second)
			time.sleep(1)
			os.makedirs(directory)
			shutil.copytree(paths[0], directory+'/players')
			shutil.copytree(paths[1], directory+'/worlds')
		else:
			directory = str(datetime.now())[:10]+' '+str(datetime.now().hour)+'-'+str(datetime.now().minute)+'-'+str(datetime.now().second)
			time.sleep(1)
			os.makedirs(savepath +directory)
			shutil.copytree(paths[0], savepath +directory+'/players')
			shutil.copytree(paths[1], savepath +directory+'/worlds')


		if path.ans == 'NANS':
			print('If u wanna support me, u can send me a donation 👉👈')
			print("even u send 1$ i'll be happy")

			print('')

			time.sleep(0.5)
			print('Open donations page? [Y/N]')
			if path.ans == 'NANS':
				ans=input('')
			else:
				ans = path.ans

			if ans == ('Y'):
				wb.open('https://www.donationalerts.com/r/pryzrak538')
				time.sleep(5)
			elif ans == ('N'):
				with open('path.py', 'r') as file:
					pathtext = file.read()
				with open('path.py', 'w') as file:
					file.write(pathtext.replace('NANS', 'N'))
		print('Thanks for using this program')
		print()
		print('Terraria is loading...')
		time.sleep(1)
		os.startfile(terraria_path)
		run = False

	if mode == '2':
		print('Not working at the moment')
		print('Stay tuned for next updates')

	if mode == '3':
		if not savecount: 		
			dsavepath = path.savepath
		print(dsavepath, savepath, path.savepath)
		print('Enter custom save path:')
		print()
		savepath = str(input())
		new_savepath = ''
		for i in list(savepath):
			if not i in R'\\':
				new_savepath += i
			else:
				new_savepath += '/'
		
		with open('path.py', 'r') as file:
			pathtext = file.read()
			file.close()
		print(pathtext)
		with open('path.py', 'w') as file:
			file.write(pathtext.replace("'"+ dsavepath +"'", "'"+new_savepath+"'"))
			file.close()

		savecount = True
		
		if savecount:
			dsavepath = new_savepath
		

	if mode == '4':
		try:
			os.startfile(path.path)
		except Exception:
			print('Launch backup mode for the first time')
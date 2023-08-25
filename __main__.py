import dearpygui.dearpygui as dpg

import shutil, os, importlib, time, tkinter
from datetime import datetime

if not 'path.py' in os.listdir():
	with open('path.py', 'w') as filename:
		filename.write('''path = 'PATH'
terraria_path = 'TERRARIA_PATH' ''')

import path

root = tkinter.Tk()

width = 531
height = 390

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def print_file(file_path):
    file_path = resource_path(file_path)
    with open(file_path) as fp:
        for line in fp:
            print(line)
            
if __name__ == '__main__':
    print_file('path.py')


class gui:

	
	def make_archive(self, src, dst):
		base = os.path.basename(dst)
		name = base.split('.')[0]
		format = base.split('.')[1]
		archive_from = os.path.dirname(src)
		archive_to = os.path.basename(src.strip(os.sep))
		shutil.make_archive(name, format, archive_from, archive_to)
		shutil.move(os.path.expandvars(name+'.'+format), dst)


	def set_path(self, sender, args):
		importlib.reload(path)
	
		with open('path.py', 'r') as filename:
			text = filename.read()

		new_path = ''

		for i in args['current_path']:
			if i in '\\':
				new_path += '/'
			else:
				new_path += i

		with open('path.py', 'w') as filename:
			filename.write(text.replace("'"+ path.path +"'", "'" + new_path + "'"))

	def set_terraria_path(self, sender, args):

		importlib.reload(path)
	
		with open('path.py', 'r') as filename:
			text = filename.read()

		new_path = ''

		for i in args['current_path']:
			if i in '\\':
				new_path += '/'
			else:
				new_path += i

		with open('path.py', 'w') as filename:
			filename.write(text.replace("'"+ path.terraria_path +"'", "'" + new_path + "'"))


	def backup(self):
		importlib.reload(path)

	
		directory = str(datetime.now())[:10]+' '+str(datetime.now().hour)+'-'+str(datetime.now().minute)+'-'+str(datetime.now().second)
		time.sleep(1)
		os.makedirs(directory)
		self.make_archive(path.path + '/players', directory+'/players.zip')
		self.make_archive(path.path + '/worlds', directory+'/worlds.zip')


			


	def backup_and_play(self):
		importlib.reload(path)

		directory = str(datetime.now())[:10]+' '+str(datetime.now().hour)+'-'+str(datetime.now().minute)+'-'+str(datetime.now().second)
		time.sleep(1)
		os.makedirs(directory)
		self.make_archive(path.path + '/players', directory+'/players.zip')
		self.make_archive(path.path + '/worlds', directory+'/worlds.zip')

		os.startfile(path.terraria_path + '/terraria.ink')
		quit()


	def play(self):
		importlib.reload(path)

		os.startfile(path.terraria_path + '/terraria.ink')
		quit()



	def __init__(self):

		importlib.reload(path)


		dpg.create_context()
		
		try:
			dpg.add_file_dialog(tag = 'terraria_saves_path', directory_selector = True, default_path = 'C:/', width = 400, height = 250, show = False, callback = self.set_path)
			dpg.add_file_dialog(tag = 'terraria_path', directory_selector = True, default_path = 'C:/', width = 400, height = 250, show = False, callback = self.set_terraria_path)
		

		with dpg.window(label = "Terrabackup v0.0.3-alpha", width = 640, height = 480, no_move = True, no_resize = True, no_collapse = False):
			dpg.add_text('Firstly set all paths', tag = 'fuck', show = False)
			dpg.add_button(label = 'Backup', width = 500, height = 60, callback = self.backup)
			dpg.add_button(label = 'Backup and Play', width = 500, height = 60, callback = self.backup_and_play)
			dpg.add_button(label = 'Set path Terraria saves [FOLDER ONLY]', width = 500, height = 60,  callback = lambda: dpg.show_item('terraria_saves_path'))
			dpg.add_button(label = 'Set path to Terraria.ink [FOLDER ONLY]', width = 500, height = 60,  callback = lambda: dpg.show_item('terraria_path'))
			dpg.add_button(label = 'Just starts Terraria', width = 500, height = 60, callback = self.play)


		dpg.create_viewport(title ='Some Title', resizable = False, width = width, height = height, x_pos = (root.winfo_screenwidth() // 2) - width//2, y_pos = (root.winfo_screenheight() // 2) - height//2)
		dpg.setup_dearpygui()
		dpg.show_viewport()
		dpg.start_dearpygui()
		dpg.destroy_context()

if __name__ == '__main__':
	g = gui()

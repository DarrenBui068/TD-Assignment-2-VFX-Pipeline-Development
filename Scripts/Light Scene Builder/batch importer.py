import maya.cmds as cmds
import sys


def onMayaDroppedPythonFile(*args):
	FileBatchImport()

def FileBatchImport(*args):
	if CheckForBonusTools:
		multipleFilters =  'Importable file formats (*.abc *.fbx *.mb *.obj )'
	else:
		multipleFilters =  'Importable file formats (*.abc *.fbx *.mb *.obj )'
	files = cmds.fileDialog2(caption = 'Import file in batch', ds = 1, fileMode = 4, okCaption = 'Import', fileFilter = multipleFilters, hideNameEdit = False)
	if files == None or files[0] == None or len(files) < 0:
		sys.exit('Cancelled selection of files.\n')

	for x in files:
			
		if any(y in x for y in ['.mb', '.MB']):
			fileType = 'mayaBinary'
			options = ''
			ImportFiles(fileType, x, options)

		if any(y in x for y in ['.obj', '.OBJ']):
			fileType = 'OBJ'
			options = 'mo=0'
			ImportFiles(fileType, x, options)

		if any(y in x for y in ['.fbx', '.FBX']):
			fileType = 'FBX'
			options = ''
			LoadPlugin('fbxmaya')
			ImportFiles(fileType, x, options)


		if any(y in x for y in ['.abc', '.ABC']):
			fileType = 'Alembic'
			options = ''
			LoadPlugin('AbcImport')
			ImportFiles(fileType, x, options)



def CheckForBonusTools(*args):
	for x in sys.path:
		if 'MayaBonusTools' in x:
			return True
	return False


def LoadPlugin(plugin, *args):
		if not cmds.pluginInfo(plugin, query = True, loaded = True):
			try:
				cmds.loadPlugin(plugin)
				sys.stdout.write('Plugin "' + plugin + '" loaded.\n')
			except(RuntimeError):
				cmds.warning('Could not find "' + plugin + '" plugin or could not load it. Open the Plugin Manager and make sure Maya recognized the plugin and try again.\n')


def ImportFiles(fileType, file, options, *args):
	namespace = file.split('/')
	namespace = namespace[-1].split('.')
	namespace = namespace[0]
	try:
		cmds.file(str(file), i = True, type = fileType, ignoreVersion = True, mergeNamespacesOnClash = False, namespace = namespace, options = options)
		sys.stdout.write('Imported "' + str(file) + '".\n')
	except(UnicodeEncodeError):
		sys.stdout.write('Either the directory path or the file name have some special characters.\n')
		sys.stdout.write('The names will be changed.\n')
		cmds.file(file, i = True, type = fileType, ignoreVersion = True, mergeNamespacesOnClash = False, namespace = namespace, options = options)
		sys.stdout.write('Imported "' + file + '".\n')
	except(ImportError):
		cmds.warning('Could not import ' + file + '.\n')


if __name__ == '__main__':
	if not cmds.about(batch = True):
		FileBatchImport()
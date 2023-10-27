#SPECIFIES FILE LOCATION/ CHECK

#FUNCTION importFiles()
#pathOfFiles = (yadda yadda file name blah blah)   # specifics file path
#fileType = (file types OBJ, Image, SVG, etc)   # initialises function for specific file type

#files = getFileList(folder/directory path) //grabs file list
#	IF files == 0;   # else if statement for finding file
#	print "No Files Found”
#	ELSE
	#	file(pathOfFiles, i = true) 
#END IF
#END FUNCTION

#FUNCTION versionCheck()
#	load SQLite database
	
#	corroborate database

#	IF asset version not matched with one on local system
#		download and replace old asset w/ new
#	ELSE 
#return asset is already latest version
#	END IF
#END FUNCTION

#FUNCTION lightGlobal()
#	set global lighting preset
#END FUNCTION

#FUNCTION lightSpot()
#	set spot lighting preset
#END FUNCTION

#FUNCTION lightGround()
#	set ground lighting preset
##END FUNCTION

def showUI() :

    
    myWindow = cmds.window(title = "Scene Builder", widthHeight =(400,600))
    cmds.columnLayout()
    
    cmds.separator(h=10)
    cmds.text('Specify File Directory')
    cmds.text('Open up file browser box to select desired Maya Scene')
    cmds.separator(h=10)
    
    cmds.button(label = 'Browse/Open File', command = 'openFile()')
    
    cmds.separator(h=30)
    cmds.text('Reference specfic set')
    cmds.text('Specify ')
    cmds.separator(h = 10)
    
    cmds.button(label = 'Change Sequence Lights', command = 'swapSequenceLight()')
    
    cmds.separator(h=30)
    cmds.text('Change out Shot Lighting')
    cmds.text('Swap out shot lights to that of sequence lighting')
    cmds.separator(h = 10)
    
    cmds.button(label = 'Change Shot Lights', command = 'swapShotLight()')
        
    cmds.separator(h=30)
    cmds.text('Export Sequence Lighting to workspace')
    cmds.separator(h = 10)
    
    cmds.button(label = 'Export Sequence Lights', command = 'exportSequence()')
    
    
    
    cmds.showWindow(myWindow)

    
    
    
showUI()    

def openFile:
   cmds.file( fileName, i=True );
   return 1

cmds.fileBrowserDialog( m=0, fc=openFile, ft='image', an='Import_Image', om='Import' )
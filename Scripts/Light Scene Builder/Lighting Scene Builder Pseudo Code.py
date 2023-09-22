SPECIFIES FILE LOCATION/ CHECK

FUNCTION importFiles()
pathOfFiles = (yadda yadda file name blah blah)   # specifics file path
fileType = (file types OBJ, Image, SVG, etc)   # initialises function for specific file type

files = getFileList(folder/directory path) //grabs file list
	IF files == 0;   # else if statement for finding file
	print "No Files Found”
	ELSE
		file(pathOfFiles, i = true) 
END IF
END FUNCTION

FUNCTION versionCheck()
	load SQLite database
	
	corroborate database

	IF asset version not matched with one on local system
		download and replace old asset w/ new
	ELSE 
return asset is already latest version
	END IF
END FUNCTION

FUNCTION lightGlobal()
	set global lighting preset
END FUNCTION

FUNCTION lightSpot()
	set spot lighting preset
END FUNCTION

FUNCTION lightGround()
	set ground lighting preset
END FUNCTION


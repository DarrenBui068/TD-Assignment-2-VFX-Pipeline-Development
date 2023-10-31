import maya.cmds as cmds

def importImage( fileName, fileType):
   cmds.file( fileName, i=True );
   return 1

cmds.fileBrowserDialog( m=0, fc=importImage, ft='image', an='Import_Image', om='Import' )
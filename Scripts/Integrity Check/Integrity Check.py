import maya.cmds as cmds

if cmds.window('IntegrityCheck', exists = True):
    cmds.deleteUI('IntegrityCheck')
window1 = cmds.window('IntegrityCheck', resizeToFitChildren=True)
cmds.columnLayout(columnAttach=("left", 10))
cmds.separator(h=10,style='none')

cmds.text("Select properties to check")
cmds.separator(h=10,style='none')

# General
cmds.checkBox("General", annotation="Selects/deselects all General checks")
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Unused nodes", annotation="Check if theres any empty objects")
cmds.checkBox("Asset naming", annotation="Checks object names with naming convention")
cmds.checkBox("Node hierarchy", annotation="Checks if the layout of the scene is readable for publishing")
cmds.checkBox("Reference errors", annotation="Checks for invalid references")
cmds.checkBox("Very small decimals", annotation="Checks for abnormally long (5+) decimal points")
cmds.separator(h=10,style='none')

# Layout
cmds.setParent("..")
cmds.checkBox("Layout", annotation="Selects/deselects all Layout checks")
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Camera apeture", annotation="Checks if the camera apeture is 16:9 aspect ratio")
cmds.checkBox("Focal length", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
cmds.checkBox("F-Stop", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
cmds.separator(h=10,style='none')

# Set pieces
cmds.setParent("..")
cmds.checkBox("Set Piece", annotation="Selects/deselects all Set Piece checks")
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Transform", annotation="Checks if the transform is at the origin")
cmds.checkBox("Pivot", annotation="Checks if the pivot is at the origin")
cmds.separator(h=10,style='none')

# Sets
cmds.setParent("..")
cmds.checkBox("Set", annotation="Selects/deselects all Set checks")
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Transform", annotation="Checks if the transform is at the origin")
cmds.checkBox("Pivot", annotation="Checks if the pivot is at the origin")
cmds.checkBox("Asset version", annotation="Checks if each referenced asset is the latest version")
cmds.separator(h=10,style='none')

cmds.showWindow(window)

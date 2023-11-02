import maya.cmds as cmds

if cmds.window('IntegrityCheck', exists = True):
    cmds.deleteUI('IntegrityCheck')
window1 = cmds.window('IntegrityCheck', resizeToFitChildren=True)
#cmds.columnLayout(columnAttach=("left", 10))
cmds.columnLayout(adjustableColumn=True, columnOffset=("both", 10))
cmds.separator(h=10,style='none')

cmds.text("Select properties to check")
cmds.separator(h=10,style='none')

# General
def generalOn(*args):
    cmds.checkBox("Unused_nodes", edit=True, value=True)
    cmds.checkBox("Asset_naming", edit=True, value=True)
    cmds.checkBox("Node_hierarchy", edit=True, value=True)
    cmds.checkBox("Reference_errors", edit=True, value=True)
    cmds.checkBox("Very_small_decimals", edit=True, value=True)
def generalOff(*args):
    cmds.checkBox("Unused_nodes", edit=True, value=False)
    cmds.checkBox("Asset_naming", edit=True, value=False)
    cmds.checkBox("Node_hierarchy", edit=True, value=False)
    cmds.checkBox("Reference_errors", edit=True, value=False)
    cmds.checkBox("Very_small_decimals", edit=True, value=False)
def generalChildOff(*args):
    cmds.checkBox("General", edit=True, value=False)
cmds.checkBox("General", annotation="Selects/deselects all General checks", onCommand=generalOn, offCommand=generalOff)
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Unused nodes", annotation="Check if theres any empty objects", offCommand=generalChildOff)
cmds.checkBox("Asset naming", annotation="Checks object names with naming convention", offCommand=generalChildOff)
cmds.checkBox("Node hierarchy", annotation="Checks if the layout of the scene is readable for publishing", offCommand=generalChildOff)
cmds.checkBox("Reference errors", annotation="Checks for invalid references", offCommand=generalChildOff)
cmds.checkBox("Very small decimals", annotation="Checks for abnormally long (5+) decimal points", offCommand=generalChildOff)
cmds.separator(h=10,style='none')

# Layout
def layoutOn(*args):
    cmds.checkBox("Camera_apeture", edit=True, value=True)
    cmds.checkBox("Focal_length", edit=True, value=True)
    cmds.checkBox("F_Stop", edit=True, value=True)
def layoutOff(*args):
    cmds.checkBox("Camera_apeture", edit=True, value=False)
    cmds.checkBox("Focal_length", edit=True, value=False)
    cmds.checkBox("F_Stop", edit=True, value=False)
def layoutChildOff(*args):
    cmds.checkBox("Layout", edit=True, value=False)
cmds.setParent("..")
cmds.checkBox("Layout", annotation="Selects/deselects all Layout checks", onCommand=layoutOn, offCommand=layoutOff)
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Camera apeture", annotation="Checks if the camera apeture is 16:9 aspect ratio", offCommand=layoutChildOff)
cmds.checkBox("Focal length", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)", offCommand=layoutChildOff)
cmds.checkBox("F-Stop", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)", offCommand=layoutChildOff)
cmds.separator(h=10,style='none')

# Set pieces
def setPieceOn(*args):
    cmds.checkBox("Transform_Set_Piece", edit=True, value=True)
    cmds.checkBox("Pivot_Set_Piece", edit=True, value=True)
def setPieceOff(*args):
    cmds.checkBox("Transform_Set_Piece", edit=True, value=False)
    cmds.checkBox("Pivot_Set_Piece", edit=True, value=False)
def setPieceChildOff(*args):
    cmds.checkBox("Set_Piece", edit=True, value=False)
cmds.setParent("..")
cmds.checkBox("Set Piece", annotation="Selects/deselects all Set Piece checks", onCommand=setPieceOn, offCommand=setPieceOff)
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Transform Set Piece", label="Transform", annotation="Checks if the transform is at the origin", offCommand=setPieceChildOff)
cmds.checkBox("Pivot Set Piece", label="Pivot", annotation="Checks if the pivot is at the origin", offCommand=setPieceChildOff)
cmds.separator(h=10,style='none')

# Sets
def setOn(*args):
    cmds.checkBox("Transform_Set", edit=True, value=True)
    cmds.checkBox("Pivot_Set", edit=True, value=True)
    cmds.checkBox("Asset_version", edit=True, value=True)
def setOff(*args):
    cmds.checkBox("Transform_Set", edit=True, value=False)
    cmds.checkBox("Pivot_Set", edit=True, value=False)
    cmds.checkBox("Asset_version", edit=True, value=False)
def setChildOff(*args):
    cmds.checkBox("Set", edit=True, value=False)
cmds.setParent("..")
cmds.checkBox("Set", annotation="Selects/deselects all Set checks", onCommand=setOn, offCommand=setOff)
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Transform Set", label="Transform", annotation="Checks if the transform is at the origin", offCommand=setChildOff)
cmds.checkBox("Pivot Set", label="Pivot", annotation="Checks if the pivot is at the origin", offCommand=setChildOff)
cmds.checkBox("Asset version", annotation="Checks if each referenced asset is the latest version", offCommand=setChildOff)
cmds.separator(h=10,style='none')
    
cmds.setParent("..")
cmds.button("Continue")

cmds.showWindow(window1)
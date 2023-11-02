import maya.cmds as cmds
import os
from os import listdir
import re
from pathlib import Path
from os.path import isfile, join

def getVersion(path, prop):
    count = 0
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print(prop)
    for fileName in files:
        print(fileName)
        if re.search(prop + "\.v...\.mb" , fileName):
            count += 1
    return count
    
def versionToString(version):
    return "%03d" % (version)

if cmds.window('SelectChecks', exists = True):
    cmds.deleteUI('SelectChecks')
if cmds.window('Verify', exists = True):
    cmds.deleteUI('Verify')
    
cmds.window('SelectChecks', resizeToFitChildren=True)
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

checkUnusedNodes = False
checkAssetNaming = False
checkNodeHierarchy = False
checkReferenceErrors = False
checkVerySmallDecimals = False
checkCameraApeture = False
checkFocalLength = False
checkFStop = False
checkTransformSetPiece = False
checkPivotSetPiece = False
checkTransformSet = False
checkPivotSet = False
checkAssetVersion = False
def onContinue(*args):
    global checkUnusedNodes
    global checkAssetNaming
    global checkNodeHierarchy
    global checkReferenceErrors
    global checkVerySmallDecimals
    global checkCameraApeture
    global checkFocalLength
    global checkFStop
    global checkTransformSetPiece
    global checkPivotSetPiece
    global checkTransformSet
    global checkPivotSet
    global checkAssetVersion
    checkUnusedNodes = cmds.checkBox("Unused_nodes", query=True, value=True)
    checkAssetNaming = cmds.checkBox("Asset_naming", query=True, value=True)
    checkNodeHierarchy = cmds.checkBox("Node_hierarchy", query=True, value=True)
    checkReferenceErrors = cmds.checkBox("Reference_errors", query=True, value=True)
    checkVerySmallDecimals = cmds.checkBox("Very_small_decimals", query=True, value=True)
    checkCameraApeture = cmds.checkBox("Camera_apeture", query=True, value=True)
    checkFocalLength = cmds.checkBox("Focal_length", query=True, value=True)
    checkFStop = cmds.checkBox("F_Stop", query=True, value=True)
    checkTransformSetPiece = cmds.checkBox("Transform_Set_Piece", query=True, value=True)
    checkPivotSetPiece = cmds.checkBox("Pivot_Set_Piece", query=True, value=True)
    checkTransformSet = cmds.checkBox("Transform_Set", query=True, value=True)
    checkPivotSet = cmds.checkBox("Pivot_Set", query=True, value=True)
    checkAssetVersion = cmds.checkBox("Asset_version", query=True, value=True)
    verify()
    cmds.showWindow("Verify")


cmds.setParent("..")
cmds.button("Continue", command=onContinue)

# fckin main window
cmds.window('Verify', resizeToFitChildren=True)
cmds.columnLayout(adjustableColumn=True, columnOffset=("both", 10))
cmds.separator(h=10,style='none')

def getSet():
    for set in cmds.ls(assemblies=True):
        cameraChildren = cmds.listRelatives(set, children=True, type="camera")
        if cameraChildren:
            continue
        return set
def getCamera():
    for camera in cmds.ls(type="camera"):
        if camera != "perspShape" and camera != "frontShape" and camera != "topShape" and camera != "sideShape":
            return camera

unusedNodesValid = None
assetNamingValid = None
nodeHierarchyValid = None
referenceErrorsValid = None
verySmallDecimalsValid = None
cameraApetureValid = None
focalLengthValid = None
fStopValid = None
transformSetPieceValid = None
pivotSetPieceValid = None
transformSetValid = None
pivotSetValid = None
assetVersionValid = None
def verify():
    global unusedNodesValid
    global assetNamingValid
    global nodeHierarchyValid
    global referenceErrorsValid
    global verySmallDecimalsValid
    global cameraApetureValid
    global focalLengthValid
    global fStopValid
    global transformSetPieceValid
    global pivotSetPieceValid
    global transformSetValid
    global pivotSetValid
    global assetVersionValid
    if checkCameraApeture:
        camera = getCamera()
        cameraApetureValid = round(cmds.getAttr(camera + ".horizontalFilmAperture")/cmds.getAttr(camera + ".verticalFilmAperture"), 3) == round(16/9, 3)
    if checkFocalLength:
        camera = getCamera()
        focalLengthValid = cmds.getAttr(camera + ".focalLength") in [12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150]
    if checkFStop:
        camera = getCamera()
        fStopValid = cmds.getAttr(camera + ".fStop") in [1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22]
    if checkTransformSet:
        set = getSet()
        transformSetValid = cmds.getAttr(set + ".translate")[0] == (0, 0, 0)
    if checkPivotSet:
        set = getSet()
        pivotSetValid = cmds.getAttr(set + ".rotatePivot")[0] == (0, 0, 0) and cmds.getAttr(set + ".scalePivot")[0] == (0, 0, 0)
    if checkTransformSetPiece:
        set = getSet()
        transformSetPieceValid = cmds.getAttr(set + ".translate")[0] == (0, 0, 0)
    if checkPivotSetPiece:
        set = getSet()
        pivotSetPieceValid = cmds.getAttr(set + ".rotatePivot")[0] == (0, 0, 0) and cmds.getAttr(set + ".scalePivot")[0] == (0, 0, 0)
    if checkAssetVersion:
        for reference in cmds.ls(rf=True):
            fullPath = cmds.referenceQuery(reference, filename = True)
            fileName = os.path.basename(fullPath)
            propName = fileName.split(".")[0]
            path = Path(fullPath)
            path = path.parent.as_posix() + "/"
            versionToString(getVersion(path, propName))
            
        
    showValidation()
        
def showValidation():
    global pivotSetValid
    if pivotSetValid:
        cmds.text("<font color=green>good</font>")
    else:
        cmds.text("<font color=red>bad</font>")
    
        



cmds.showWindow('SelectChecks')
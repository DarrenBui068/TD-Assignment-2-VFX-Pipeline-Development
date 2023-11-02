import maya.cmds as cmds
import os
from os import listdir
import re
from pathlib import Path
from os.path import isfile, join

# helper functions
def getVersion(path, prop):
    count = 0
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for fileName in files:
        if re.search(prop + "\.v...\.mb" , fileName):
            count += 1
    return count
def versionToString(version):
    return "%03d" % (version)

if cmds.window('Select_Checks', exists = True):
    cmds.deleteUI('Select_Checks')
if cmds.window('Verify', exists = True):
    cmds.deleteUI('Verify')
if cmds.window('Error_Info', exists = True):
    cmds.deleteUI('Error_Info')
    
cmds.window('Select Checks', resizeToFitChildren=True)
#cmds.columnLayout(columnAttach=("left", 10))
cmds.columnLayout(adjustableColumn=True, columnOffset=("both", 10))
cmds.separator(h=10,style='none')
cmds.text("Select properties to check")
cmds.separator(h=10,style='none')
cmds.columnLayout(adjustableColumn=True, columnOffset=("both", 10), enableBackground=True, backgroundColor=(.2,.2,.2))
cmds.separator(h=5,style='none')

# General
def generalOn(*args):
    cmds.checkBox("Unknown_nodes", edit=True, value=True)
    cmds.checkBox("Asset_naming", edit=True, value=True)
    #cmds.checkBox("Node_hierarchy", edit=True, value=True)
    cmds.checkBox("Reference_errors", edit=True, value=True)
    #cmds.checkBox("Very_small_decimals", edit=True, value=True)
def generalOff(*args):
    cmds.checkBox("Unknown_nodes", edit=True, value=False)
    cmds.checkBox("Asset_naming", edit=True, value=False)
    #cmds.checkBox("Node_hierarchy", edit=True, value=False)
    cmds.checkBox("Reference_errors", edit=True, value=False)
    #cmds.checkBox("Very_small_decimals", edit=True, value=False)
def generalChildOff(*args):
    cmds.checkBox("General", edit=True, value=False)
cmds.checkBox("General", annotation="Selects/deselects all General checks", onCommand=generalOn, offCommand=generalOff)
cmds.columnLayout(columnAttach=("left", 35))
cmds.checkBox("Unknown nodes", annotation="Check if theres any unknown nodes", offCommand=generalChildOff)
cmds.checkBox("Asset naming", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)", offCommand=generalChildOff)
cmds.checkBox("Node hierarchy", annotation="Checks if the layout of the scene is readable for publishing", offCommand=generalChildOff, enable=False)
cmds.checkBox("Reference errors", annotation="Checks for invalid references", offCommand=generalChildOff)
cmds.checkBox("Very small decimals", annotation="Checks for abnormally long (5+) decimal points", offCommand=generalChildOff, enable=False)
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
cmds.separator(h=5,style='none')

checkUnknownNodes = False
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
def onValidate(*args):
    global checkUnknownNodes
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
    checkUnknownNodes = cmds.checkBox("Unknown_nodes", query=True, value=True)
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


cmds.setParent("..")
cmds.setParent("..")
cmds.separator(h=10,style='none')
cmds.button("Validate", command=onValidate)

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

unknownNodesValid = None
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
    global unknownNodesValid
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
    if checkUnknownNodes:
        unknownNodesValid = True
        unknownNodes = cmds.ls(type="unknown")
        if len(unknownNodes) >= 1:
            unknownNodesValid = unknownNodes[0]
    if checkAssetNaming:
        assetNamingValid = True
        for asset in cmds.ls(assemblies=True):
            cameraChildren = cmds.listRelatives(asset, children=True, type="camera")
            if cameraChildren:
                continue
            word = "[a-z]+([A-Z][a-z]*)*\d*"
            regex = "^((" + word + ")(_" + word + ")*(:" + word + ")?)$" # book02_model_v002:book02
            if re.match(regex, asset) == None:
                assetNamingValid = asset
                break
    if checkReferenceErrors:
        referenceErrorsValid = True
        for reference in cmds.ls(rf=True):
            fullPath = cmds.referenceQuery(reference, filename = True)
            if os.path.isfile(fullPath) == False:
                referenceErrorsValid = reference
                break
    if checkCameraApeture:
        camera = getCamera()
        if camera == None:
            cameraApetureValid = "Can't find camera"
        else:
            if round(cmds.getAttr(camera + ".horizontalFilmAperture")/cmds.getAttr(camera + ".verticalFilmAperture"), 3) == round(16/9, 3):
                cameraApetureValid = True
            else:
                cameraApetureValid = camera
    if checkFocalLength:
        camera = getCamera()
        if camera == None:
            focalLengthValid = "Can't find camera"
        else:
            if cmds.getAttr(camera + ".focalLength") in [12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150]:
                focalLengthValid = True
            else:
                focalLengthValid = camera
    if checkFStop:
        camera = getCamera()
        if camera == None:
            fStopValid = "Can't find camera"
        else:
            if cmds.getAttr(camera + ".fStop") in [1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22]:
                fStopValid = True
            else:
                fStopValid = camera
    if checkTransformSet:
        set = getSet()
        if cmds.getAttr(set + ".translate")[0] == (0, 0, 0):
            transformSetValid = True
        else:
            transformSetValid = set
    if checkPivotSet:
        set = getSet()
        if cmds.getAttr(set + ".rotatePivot")[0] == (0, 0, 0) and cmds.getAttr(set + ".scalePivot")[0] == (0, 0, 0):
            pivotSetValid = True
        else:
            pivotSetValid = set
    if checkTransformSetPiece:
        set = getSet()
        if cmds.getAttr(set + ".translate")[0] == (0, 0, 0):
            transformSetPieceValid = True
        else:
            transformSetPieceValid = set
    if checkPivotSetPiece:
        set = getSet()
        if cmds.getAttr(set + ".rotatePivot")[0] == (0, 0, 0) and cmds.getAttr(set + ".scalePivot")[0] == (0, 0, 0):
            pivotSetPieceValid = True
        else:
            pivotSetPieceValid = set
    if checkAssetVersion:
        assetVersionValid = True
        for reference in cmds.ls(rf=True):
            fullPath = cmds.referenceQuery(reference, filename = True)
            fileName = os.path.basename(fullPath)
            propName = fileName.split(".")[0]
            path = Path(fullPath)
            path = path.parent.as_posix() + "/"
            latestVersion = versionToString(getVersion(path, propName))
            if (latestVersion in fileName) == False:
                print("BAAAD")
                assetVersionValid = reference
                break
    showValidation()
        
# Validation window
cmds.window('Verify', resizeToFitChildren=True)
cmds.columnLayout(adjustableColumn=True, columnOffset=("both", 10))
cmds.separator(h=10,style='none')
cmds.columnLayout(adjustableColumn=True, columnOffset=("both", 10), enableBackground=True, backgroundColor=(.2,.2,.2))
cmds.separator(h=5,style='none')
cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
cmds.text("Check name")
cmds.text("Status")
cmds.text("Error node")
cmds.setParent("..")
cmds.separator(h=5,style='none')

def showValidation():
    global unknownNodesValid
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if unknownNodesValid==True:
        cmds.text("<font color=green>Unknown nodes</font>", annotation="Check if theres any unknown nodes")
        cmds.text("<font color=green>OK</font>", annotation="Check if theres any unknown nodes")
        cmds.text("<font color=green>N/A</font>", annotation="Check if theres any unknown nodes")
    elif unknownNodesValid==None:
        cmds.text("<font color=gray>Unknown nodes</font>", annotation="Check if theres any unknown nodes")
        cmds.text("<font color=gray>N/A</font>", annotation="Check if theres any unknown nodes")
        cmds.text("<font color=gray>N/A</font>", annotation="Check if theres any unknown nodes")
    else:
        cmds.text("<font color=red>Unknown nodes</font>", annotation="Check if theres any unknown nodes")
        cmds.text("<font color=red>Invalid</font>", annotation="Check if theres any unknown nodes")
        cmds.text("<font color=red>" + unknownNodesValid + "</font>", annotation="Check if theres any unknown nodes")
    
    global assetNamingValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if assetNamingValid==True:
        cmds.text("<font color=green>Asset naming</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
        cmds.text("<font color=green>OK</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
        cmds.text("<font color=green>N/A</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
    elif assetNamingValid==None:
        cmds.text("<font color=gray>Asset naming</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
    else:
        cmds.text("<font color=red>Asset naming</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
        cmds.text("<font color=red>" + assetNamingValid + "</font>", annotation="Checks object names with naming convention (e.g. camelCase, camelCase01_model:v001)")
        
        
    global referenceErrorsValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if referenceErrorsValid==True:
        cmds.text("<font color=green>Reference errors</font>", annotation="Checks for invalid references")
        cmds.text("<font color=green>OK</font>", annotation="Checks for invalid references")
        cmds.text("<font color=green>N/A</font>", annotation="Checks for invalid references")
    elif referenceErrorsValid==None:
        cmds.text("<font color=gray>Reference errors</font>", annotation="Checks for invalid references")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks for invalid references")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks for invalid references")
    else:
        cmds.text("<font color=red>Reference errors</font>", annotation="Checks for invalid references")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks for invalid references")
        
        
    global cameraApetureValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if cameraApetureValid==True:
        cmds.text("<font color=green>Camera apeture</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
        cmds.text("<font color=green>OK</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
        cmds.text("<font color=green>N/A</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
    elif cameraApetureValid==None:
        cmds.text("<font color=gray>Camera apeture</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
    else:
        cmds.text("<font color=red>Camera apeture</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
        cmds.text("<font color=red>" + cameraApetureValid + "</font>", annotation="Checks if the camera apeture is 16:9 aspect ratio")
        
    global focalLengthValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if focalLengthValid==True:
        cmds.text("<font color=green>Focal length</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
        cmds.text("<font color=green>OK</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
        cmds.text("<font color=green>N/A</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
    elif focalLengthValid==None:
        cmds.text("<font color=gray>Focal length</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
    else:
        cmds.text("<font color=red>Focal length</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
        cmds.text("<font color=red>" + focalLengthValid + "</font>", annotation="Checks if the camera focal length is an appropriate value (12, 14, 16, 18, 21, 25, 27, 32, 35, 40, 50, 65, 75, 100, 135, 150)")
        
    global fStopValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if fStopValid==True:
        cmds.text("<font color=green>F-Stop</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
        cmds.text("<font color=green>OK</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
        cmds.text("<font color=green>N/A</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
    elif fStopValid==None:
        cmds.text("<font color=gray>F-Stop</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
    else:
        cmds.text("<font color=red>F-Stop</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
        cmds.text("<font color=red>" + fStopValid + "</font>", annotation="Checks if the camera f-stop is an appropriate value (1.3, 2, 2.8, 4, 5.6, 8, 11, 16, 22)")
        
    global transformSetPieceValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if transformSetPieceValid==True:
        cmds.text("<font color=green>Transform (set piece)</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=green>OK</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=green>N/A</font>", annotation="Checks if the transform is at the origin")
    elif transformSetPieceValid==None:
        cmds.text("<font color=gray>Transform (set piece)</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the transform is at the origin")
    else:
        cmds.text("<font color=red>Transform (set piece)</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=red>" + transformSetPieceValid + "</font>", annotation="Checks if the transform is at the origin")
        
    global pivotSetPieceValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if pivotSetPieceValid==True:
        cmds.text("<font color=green>Pivot (set piece)</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=green>OK</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=green>N/A</font>", annotation="Checks if the pivot is at the origin")
    elif pivotSetPieceValid==None:
        cmds.text("<font color=gray>Pivot (set piece)</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the pivot is at the origin")
    else:
        cmds.text("<font color=red>Pivot (set piece)</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=red>" + pivotSetPieceValid + "</font>", annotation="Checks if the pivot is at the origin")
        
    global transformSetValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if transformSetValid==True:
        cmds.text("<font color=green>Transform (set)</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=green>OK</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=green>N/A</font>", annotation="Checks if the transform is at the origin")
    elif transformSetValid==None:
        cmds.text("<font color=gray>Transform (set)</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the transform is at the origin")
    else:
        cmds.text("<font color=red>Transform (set)</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks if the transform is at the origin")
        cmds.text("<font color=red>" + transformSetValid + "</font>", annotation="Checks if the transform is at the origin")
        
    global pivotSetValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if pivotSetValid==True:
        cmds.text("<font color=green>Pivot (set)</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=green>OK</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=green>N/A</font>", annotation="Checks if the pivot is at the origin")
    elif pivotSetValid==None:
        cmds.text("<font color=gray>Pivot (set)</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if the pivot is at the origin")
    else:
        cmds.text("<font color=red>Pivot (set)</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks if the pivot is at the origin")
        cmds.text("<font color=red>" + pivotSetValid + "</font>", annotation="Checks if the pivot is at the origin")
        
    global assetVersionValid
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(150,150,150), columnAttach3=("left", "both", "right"))
    if assetVersionValid==True:
        cmds.text("<font color=green>Asset version</font>", annotation="Checks if each referenced asset is the latest version")
        cmds.text("<font color=green>OK</font>", annotation="Checks if each referenced asset is the latest version")
        cmds.text("<font color=green>N/A</font>", annotation="Checks if each referenced asset is the latest version")
    elif assetVersionValid==None:
        cmds.text("<font color=gray>Asset version</font>", annotation="Checks if each referenced asset is the latest version")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if each referenced asset is the latest version")
        cmds.text("<font color=gray>N/A</font>", annotation="Checks if each referenced asset is the latest version")
    else:
        cmds.text("<font color=red>Asset version</font>", annotation="Checks if each referenced asset is the latest version")
        cmds.text("<font color=red>Invalid</font>", annotation="Checks if each referenced asset is the latest version")
        cmds.text("<font color=red>" + assetVersionValid + "</font>", annotation="Checks if each referenced asset is the latest version")
    
    cmds.setParent("..")
    cmds.separator(h=5,style='none')
    cmds.showWindow("Verify")
    cmds.window("Verify", e=True, h=220, w=495)
    
    
cmds.showWindow('Select_Checks')
cmds.window('Select_Checks', e=True, h=415, w=150)
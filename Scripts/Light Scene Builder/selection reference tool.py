import maya.cmds as cmds

sel = cmds.ls(sl=True)

path = cmds.workspace (rd = True , q = True)
print(path)

def selectAll():
    cmds.select(allDagObjects=True) 
    
def deselectAll():
    cmds.select(clear = True)
    
def referenceSelected():
    for obj in cmds.ls(assemblies=True):
        print(obj)
        cmds.setAttr(obj + '.v', 1)
        cmds.select(obj)
        cmds.file(path + obj + '.mb', 
            es = True,
            type = 'mayaBinary')
        cmds.setAttr(obj + '.v', 0)
    
    
def showUI():
    
    myWindow = cmds.window(title = "Selection and Referencing Tool", widthHeight =(250,200))
    cmds.columnLayout()
    
    
    cmds.separator(h=10)      
    cmds.text('Click to select all selectable asssets')
    cmds.separator(h=5) 
    cmds.button(label = "Select all assets", command = "selectAll()")
    cmds.separator(h=20)
    
    cmds.text('Click to deselect all currently selected asssets')
    cmds.separator(h=5) 
    cmds.button(label = "Deselect all assets", command = "deselectAll()")
    cmds.separator(h=20)
    
    cmds.text('Click to reference all current selected assets')
    cmds.separator(h=5) 
    cmds.button(label = "Convert selected assets to references", command = "referenceSelected()")
    cmds.separator(h=20)
    
    cmds.showWindow(myWindow)
    
showUI()


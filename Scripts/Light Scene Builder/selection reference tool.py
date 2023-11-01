import maya.cmds as cmds

sel = cmds.ls(sl=True)

path = cmds.workspace (rd = True , q = True)
print(path)

def selectAll():
    cmds.select(all = True) 
    
def deselectAll():
    cmds.select(clear = True)
    
def referenceSelected():
    for obj in sel:
        cmds.setAttr(obj + '.v', 1)
        cmds.select(obj)
        cmds.file(path + '_' + '.mb', 
            es = True,
            type = 'MBexport')
        cmds.setAttr(mb + '.v', 0)
    
    
def showUI():
    
    myWindow = cmds.window(title = "Selection and Referencing Tool", widthHeight =(200,200))
    cmds.columnLayout()
  
    cmds.button(label = "Select all assets", command = "selectAll()")
    cmds.separator(h=10)
    
    cmds.button(label = "Deselect all assets", command = "deselectAll()")
    cmds.separator(h=10)
    
    cmds.button(label = "Convert selected assets to references", command = "referenceSelected()")
    cmds.separator(h=10)
    cmds.showWindow(myWindow)
    
showUI()


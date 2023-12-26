import maya.cmds as cmds

def showUI():
    txtGrpName = ""
    myWin = cmds.window("lookdev_window",sizeable = True,title="Lookdev Toolkit", )
    cmds.rowColumnLayout(numberOfColumns = 6, columnWidth = [(1,50),(2,100),(3,100),(4,300),(5,50),(6,50)], adjustableColumn = True)
    
    rowTextElement("Diffuse","diffusePath","setDiffText")
    
    separatorFunc()
     
    rowTextElement("Roughness","roughnessPath","setRoughText")
    
    separatorFunc()
    
    rowTextElement("Metalness","metalnessPath","setMetalText")
    
    separatorFunc()
    
    rowTextElement("Normal","normalPath","setNormalText")
    
    
    
    
    
    cmds.showWindow(myWin)

def rowTextElement(textureType,texturePath,textureFuncCall):
    cmds.checkBox( label='Enable' )
    cmds.text(label = "%s" % textureType, width = 75)
    cmds.checkBox( label='UDIM')
    cmds.textFieldGrp('%s' % texturePath, placeholderText ="Set Texture Path" )
    cmds.button(label="Open", width = 25,c='%s()' % textureFuncCall)   
    cmds.separator(style = 'none')
    
    
    
def openDialogBox(txtGrpName):
    print("Dialog opened")
    print("after button press:"+txtGrpName)
    filename = cmds.fileDialog2(fileMode=1, caption="Import Image")
    cmds.textFieldGrp("%s" % txtGrpName, edit=True, text=filename[0])
    
def setDiffText():
    txtGrpName = "diffusePath"
    openDialogBox(txtGrpName)
   
def setRoughText():
    txtGrpName = "roughnessPath"
    openDialogBox(txtGrpName) 
    
def setMetalText():
    txtGrpName = "metalnessPath"
    openDialogBox(txtGrpName)

def setNormalText():
    txtGrpName = "normalPath"
    openDialogBox(txtGrpName)

def separatorFunc():
    separatorHeight = 15
    cmds.separator(style = 'none', h=separatorHeight)
    cmds.separator(style = 'none', h=separatorHeight)
    cmds.separator(style = 'none', h=separatorHeight)
    cmds.separator(style = 'none', h=separatorHeight)
    cmds.separator(style = 'none', h=separatorHeight)
    cmds.separator(style = 'none', h=separatorHeight)
    
if cmds.window("lookdev_window", exists = True):
        cmds.deleteUI("lookdev_window")    
showUI()
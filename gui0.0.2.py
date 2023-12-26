from functools import partial
import maya.cmds as cmds
txtGrpName = ""

def showGUI():
    
    myWin = cmds.window("lookdev_window",sizeable = True, title = "Lookdev Toolkit")
    
    projectPanel()
    cmds.scrollLayout(
	horizontalScrollBarThickness=0,
	verticalScrollBarThickness=16, width = 550, height = 500)   
    rowTextElement("Diffuse", True, "setDiffText", "diffusePath", False)
    rowTextElement("Roughness", False, "setRoughText", "roughnessPath", True) 
    rowTextElement("Metalness", False, "setMetalText", "metalnessPath", True)
    rowTextElement("Normal", False, "setNormalText", "normalPath", True)
    
    mtlAssignType()
    generateButton()

    
    cmds.showWindow(myWin)
    
def rowTextElement(textureType, checkFlag, textureFuncCall, texturePath, collapseFrame):
     
    cmds.columnLayout()
    frameTop = cmds.frameLayout( label='%s' %textureType, cll=True, width = 500, collapse = collapseFrame)
    form = cmds.formLayout(numberOfDivisions=100)
    
    rowLayoutState =cmds.rowColumnLayout(numberOfColumns = 3, columnWidth=[(1,150),(2,275),(3,50)], columnOffset =[(1,'left',50),(2,'both',15),(3,'right',30)], width =500)
    
    
    # cmds.text(label = " ")
    # cmds.text(label = " ")
    
    texturePathLabel=cmds.text(label = "Texture Path", enable = checkFlag)
    cmds.textFieldGrp('%s' % texturePath, placeholderText ="Select Texture" )
    openIcon = cmds.iconTextButton( style='iconOnly', image1='xgBrowse.png', label='open' ,enable = checkFlag, c='%s()' % textureFuncCall)
    
    udimCheck =cmds.checkBox( label='UDIM', enable = checkFlag)
    cmds.text(label = " ")
    cmds.text(label = " ")
    
    colorSpaceLabel =cmds.text(label = "Color Space", enable = checkFlag)
    colorSpaceDropdown = cmds.optionMenu( width = 1, enable = checkFlag)
    cmds.menuItem( label='sRGB' )
    cmds.menuItem( label='ACES' )
    cmds.menuItem( label='Raw' )
    cmds.text(label = " ")
    
    
    checkBoxState = cmds.checkBox( label='Enable' , parent = form , height = 10, 
                                  offCommand= partial(disableUIelements,texturePathLabel,openIcon,udimCheck,colorSpaceLabel,colorSpaceDropdown), 
                                  onCommand = partial(enableUIelements,texturePathLabel,openIcon,udimCheck,colorSpaceLabel,colorSpaceDropdown),
                                  value = checkFlag) 
    cmds.formLayout(form, edit = True, attachForm =[(checkBoxState,'top', 10)],
                    attachControl = [(rowLayoutState,'top',5,checkBoxState)],
                    attachPosition=[(rowLayoutState,'bottom',5,50),(checkBoxState,'right',5,15)])
    cmds.setParent('..')
    cmds.setParent('..')  
    cmds.setParent('..')
    cmds.setParent('..') 

    
                   


def openDialogBox(txtGrpName):
    print("Dialog opened")
    print("after button press:"+txtGrpName)
    filename = cmds.fileDialog2(fileMode=1, caption="Import Image", dir= "\\athelas\Shared\Sagar")
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
    



    
def disableUIelements(texturePathLabel,openIcon,udimCheck,colorSpaceLabel,colorSpaceDropdown,*args):
    cmds.text(texturePathLabel, edit=True ,enable = False )
    cmds.iconTextButton(openIcon, edit = True, enable = False)
    cmds.checkBox(udimCheck,edit = True, enable = False)
    cmds.textFieldGrp(edit=True, enable = False)
    cmds.text(colorSpaceLabel,edit=True, enable = False)
    cmds.optionMenu(colorSpaceDropdown,edit = True, enable = False)
      
def enableUIelements(texturePathLabel,openIcon,udimCheck,colorSpaceLabel,colorSpaceDropdown,*args):
    cmds.text(texturePathLabel, edit=True ,enable = True )  
    cmds.iconTextButton(openIcon, edit = True, enable = True)
    cmds.checkBox(udimCheck,edit = True, enable = True)
    cmds.textFieldGrp(edit=True, enable = False)
    cmds.text(colorSpaceLabel,edit=True, enable = True)
    cmds.optionMenu(colorSpaceDropdown,edit = True, enable = True)
    
def generateButton():
    cmds.rowColumnLayout(numberOfColumns = 1,columnWidth=[(1,500)],width = 500, columnOffset= [(1,"both",150)], rowOffset = [((1,"top",20))])
    cmds.button(label = 'Generate shader graph')

def mtlAssignType():
    cmds.rowColumnLayout(numberOfColumns = 2, columnWidth=[(1,250),(2,250)], width =500, columnOffset = [(1,"both",10),(2,"both",10)], rowOffset = [(1,"top",20),(2,"both",5),(3,"both",10)])
    cmds.text(label = "Material Assign Type:")

    cmds.optionMenu( width = 1)
    cmds.menuItem( label='Object Based' )
    cmds.menuItem( label='Face Based' )



def projectPanel():
    cmds.columnLayout(columnWidth = 500, columnAlign='center') 
    cmds.formLayout(numberOfDivisions=100)
    cmds.rowColumnLayout(numberOfColumns = 2, columnWidth=[(1,250),(2,250)], width =500, columnOffset = [(1,"both",10),(2,"both",10)], rowOffset = [(1,"both",1),(2,"both",5),(3,"both",10)])

    #---------------ROW 1------------------------#    
    cmds.text(label = 'Project', align = "center")
    cmds.text(label = 'Assets', align = "center")

    #---------------ROW 2------------------------#
    cmds.textScrollList( numberOfRows=8, allowMultiSelection=True,
			append= projectListGenerate(),
			)
    cmds.textScrollList( numberOfRows=8, allowMultiSelection=True,
			append= assetListGenerate(),
			)
    
    cmds.optionMenu( width = 1)
    cmds.menuItem( label='chr' )
    cmds.menuItem( label='props' )
    cmds.menuItem( label='sets' )
    cmds.text(label = " ")
    


    cmds.setParent('..')
    cmds.setParent('..')  

def projectListGenerate():

    projectsIras =  ['GVN', 'TTMNT', 'LVM'] 
    for x in projectsIras:
        return x
    
def assetListGenerate():

    assetIras =  ['Bir', 'Aisha', 'Blade'] 
    for x in assetIras:
        return x
    


    
if cmds.window("lookdev_window", exists = True):
    cmds.deleteUI("lookdev_window")
showGUI()




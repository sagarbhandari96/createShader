import maya.cmds as cmds
import maya.mel as MEL

diffuseTex="Bir_diffuse_1001"       #TO_DO:UI for selecting textures and udim,color space types
roughnessTex="Bir_roughness_1001"   #ignore color space file rules
metallicTex="Bir_metallic_1001"
normalTex="Bir_normal_1001"

rawFlag=True
normalFlag = True


def create_shader(name, node_type):
    #lambert PREV and SG
    material = cmds.shadingNode(node_type, name="%sPREV" % name, asShader=True)
    sg = cmds.sets(name="%sSG" % name, empty=True, renderable=True, noSurfaceShader=True)
    cmds.connectAttr("%s.outColor" % material, "%s.surfaceShader" % sg)
    #add vray material override to node
    MEL.eval('vray addAttributesFromGroup "%s" "vray_specific_mtl" 1;' %material)
    MEL.eval('setAttr "GVN_bir_diffuse_PREV.vrayEnableGIMaterial" 0;')
    MEL.eval('setAttr "GVN_bir_diffuse_PREV.vrayEnableReflectMaterial" 0;')
    MEL.eval('setAttr "GVN_bir_diffuse_PREV.vrayEnableRefractMaterial" 0;')
    MEL.eval('setAttr "GVN_bir_diffuse_PREV.vrayEnableShadowMaterial" 0;',)
    MEL.eval('setAttr "GVN_bir_diffuse_PREV.vrayEnableEnvironmentOverride" 0;')
   
   
    return material, sg

def create_sd(name, node_type):
   #vray SD
    material = cmds.shadingNode(node_type, name="%sSD" % name, asShader=True) 
    return material


def place2d(textureNode):   
   
   print(textureNode)
   place2dNode = "place2dTexture"
   tex = cmds.shadingNode('file', name="%s" %textureNode, asTexture=True, isColorManaged=True)
   p2d = cmds.shadingNode('place2dTexture',name = "%s" % place2dNode, asTexture=True)
   
   cmds.connectAttr("%s.outUV" % place2dNode, "%s.uvCoord" % textureNode)
   cmds.connectAttr("%s.outUvFilterSize" % place2dNode, "%s.uvFilterSize" % textureNode)
   cmds.connectAttr("%s.vertexCameraOne" % place2dNode, "%s.vertexCameraOne" % textureNode)
   cmds.connectAttr("%s.vertexUvOne" % place2dNode, "%s.vertexUvOne" % textureNode)
   cmds.connectAttr("%s.vertexUvThree" % place2dNode, "%s.vertexUvThree" % textureNode)
   cmds.connectAttr("%s.vertexUvTwo" % place2dNode, "%s.vertexUvTwo" % textureNode)
   cmds.connectAttr("%s.coverage" % place2dNode, "%s.coverage" % textureNode)
   cmds.connectAttr("%s.mirrorU" % place2dNode, "%s.mirrorU" % textureNode)
   cmds.connectAttr("%s.mirrorV" % place2dNode, "%s.mirrorV" % textureNode)
   cmds.connectAttr("%s.noiseUV" % place2dNode, "%s.noiseUV" % textureNode)
   cmds.connectAttr("%s.offset" % place2dNode,"%s.offset" % textureNode)
   cmds.connectAttr("%s.repeatUV" % place2dNode, "%s.repeatUV" % textureNode)
   cmds.connectAttr("%s.rotateFrame" % place2dNode, "%s.rotateFrame" % textureNode)
   cmds.connectAttr("%s.rotateUV" % place2dNode, "%s.rotateUV" % textureNode)
   cmds.connectAttr("%s.stagger" % place2dNode, "%s.stagger" % textureNode)
   cmds.connectAttr("%s.translateFrame" % place2dNode, "%s.translateFrame" % textureNode)
   cmds.connectAttr("%s.wrapU" % place2dNode, "%s.wrapU" % textureNode)
   cmds.connectAttr("%s.wrapV" % place2dNode, "%s.wrapV" % textureNode)





cmds.polyCube()
color = [1, 0, 0]
mtl_name="GVN_bir_diffuse_"
meshes = cmds.ls(selection=True, dag=True, type="mesh", noIntermediate=True)
mtl, sg = create_shader(mtl_name,"lambert")
sd = create_sd(mtl_name,"VRayMtl")
cmds.connectAttr("%sSD.outColor" % mtl_name,"%sPREV.vraySpecificSurfaceShader" % mtl_name)
cmds.setAttr(mtl + ".color", color[0], color[1], color[2], type="double3")
cmds.sets(meshes, forceElement=sg)

place2d(diffuseTex)
cmds.connectAttr("%s.outColor" % diffuseTex, "%sSD.diffuseColor" % mtl_name)

if(rawFlag):
    place2d(roughnessTex)
    cmds.shadingNode('remapHsv',name = "remapNode", asTexture=True)
    cmds.connectAttr("%s.outColor.outColorR" % roughnessTex, "%sSD.reflectionGlossiness" % mtl_name)
    
#hyperShadePanelBuildEditMenu hyperShadePanel1 hyperShadePanelMenuEditMenu;
#hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");



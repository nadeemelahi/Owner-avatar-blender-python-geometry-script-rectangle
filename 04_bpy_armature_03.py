
#
# author: Nadeem Elahi
# nadeem.elahi@gmail.com
# nad@3deem.com
# license: gpl v3
#

import bpy
from math import sin
from math import cos
from math import atan 
from math import radians
from math import sqrt

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj)



print ( atan ( 1 ) ) # expect 45deg
print ( radians ( 45 ) )


# Settings 
name = 'coilAxel' 

xlft = 3
xrgt = 8

ytop = 0.5 
ybtm = -0.5

coilCnt = 5

faces = []
verts = []


def verts2d_at_3dz0_rot ( xloc , yloc , rot ) :

	rad = sqrt ( xloc * xloc + yloc * yloc )
	ang = atan ( yloc / xloc )

	verts.append ( [ 
		rad * cos ( ang + rot ) , 
		rad * sin ( ang + rot ) , 
		0 
		] )





def vertsByRot ( rot ) :

	verts2d_at_3dz0_rot ( xlft , ybtm , rot ) # bottom left
	verts2d_at_3dz0_rot ( xrgt , ybtm , rot ) # bottom right

	verts2d_at_3dz0_rot ( xrgt , ytop , rot ) # top right
	verts2d_at_3dz0_rot ( xlft , ytop , rot ) # top left


currentIdx = 0
vertsPerCoil = 4
for idx in range ( coilCnt ):
	rot = radians ( idx * 360 / coilCnt )
	vertsByRot ( rot );

	offset = idx * vertsPerCoil
	faces.append( [ offset , offset + 1 , offset + 2 , offset + 3 ] )









# FINALLY

# Create Mesh Datablock 
mesh = bpy.data.meshes.new ( name ) 
mesh.from_pydata ( verts, [], faces ) 
# mesh from vertices, edges and faces. 
# if you pass a faces list you can skip edges


# Create Object and link to scene 
obj = bpy.data.objects.new(name, mesh) 
bpy.context.scene.collection.objects.link ( obj ) 


# Select the object 
bpy.context.view_layer.objects.active = obj 
obj.select_set ( True )
bpy.ops.object.mode_set(mode='EDIT')




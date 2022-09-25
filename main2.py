import bpy
from blenderbim.bim.ifc import IfcStore
import ifcopenshell
import bpy
from blenderbim.bim.ifc import IfcStore

file = IfcStore get_file()
spaces = file_by_type["IfcSpace"]

for space in spaces:
    print(space.longname)
    
#properties

for beam in beams:
    for defintion in beam IsDefinedBy:
        if definition_is_a('IfcRelDefinedByProperties')
        property_set = definition.realtingPropertyDefinition
            
            print(dir(property_set))
            
            if property_set_name== 'Pset_BeamCommon'
                for property in property_set HasProperties:
                    
                    if property name == 
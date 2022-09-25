
import ifcopenshell
import ifcopenshell.geom 

f = ifcopenshell.open("/Users/simoncabraliversen/Documents/Subjets/Advanced BIM/Duplex_A_20110907.ifc")

# Counting number of different walls in the IFC project
walls_required = 0
walls_in_model = len(f.by_type("IfcWall"))
if (walls_required <= walls_in_model):
    print("\nThere are "+str(walls_in_model)+" walls in the model, the area of those are:")
    
    for entity in f.by_type("IfcWall"):
    #we need to get the attributes
        for relDefinesByProperties in entity.IsDefinedBy:
            for wall_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
    #and then get the attribute we are looking for
                if wall_prop.Name == 'Area':


                    print(wall_prop.NominalValue.wrappedValue)


# Gathering the the combined area of all walls
    total_wall_area = 0
    for entity in f.by_type("IfcWall"):
        for relDefinesByProperties in entity.IsDefinedBy:
            for wall_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                if wall_prop.Name == 'Area':
                    total_wall_area += wall_prop.NominalValue.wrappedValue

    print('the total area of those walls are '+ str(total_wall_area) + '$m^2$')

# Gathering the beam materials. Not yet able do figure out how to extract this part yet.
    
else:
    print ('There are no walls in the model')



# Counting number of different slabs in the IFC project
slabs_required = 0
slabs_in_model = len(f.by_type("IfcSlab"))
if (slabs_required <= slabs_in_model):
    print("\nThere are "+str(slabs_in_model)+" slabs in the model, the area of those are:")
    
    for entity in f.by_type("IfcSlab"):
    #we need to get the attributes
        for relDefinesByProperties in entity.IsDefinedBy:
            for slab_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
    #and then get the attribute we are looking for
                if slab_prop.Name == 'Area':


                    print(slab_prop.NominalValue.wrappedValue)


# Gathering the combined area of all slabs
    total_slab_area = 0
    for entity in f.by_type("IfcSlab"):
        for relDefinesByProperties in entity.IsDefinedBy:
            for slab_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                if slab_prop.Name == 'Area':
                    total_slab_area += slab_prop.NominalValue.wrappedValue

    print('the total area of those slabs are '+ str(total_slab_area) + '$m^2$')

# Gathering the slab materials. Same as walls, still figuring this out.
    
else:
    print ('There are no slabs in the model')



# Counting number of beams in the IFC project
beams_required = 1
beams_in_model = len(f.by_type("IfcBeam"))
if (beams_required <= beams_in_model):
    print("\nThere are "+str(beams_in_model)+" beams in the model, the lenght of the beams in meters are:")
    
    for entity in f.by_type("IfcBeam"):
    #we need to get the attributes
        for relDefinesByProperties in entity.IsDefinedBy:
            for beam_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
    #and then get the attribute we are looking for
                if beam_prop.Name == 'Length':


                    print(beam_prop.NominalValue.wrappedValue)


# Gathering the the combined length of all beams
    total_beam_length = 0
    for entity in f.by_type("IfcBeam"):
        for relDefinesByProperties in entity.IsDefinedBy:
            for beam_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                if beam_prop.Name == 'Length':
                    total_beam_length += beam_prop.NominalValue.wrappedValue

    print('the total length of those beams are '+ str(total_beam_length) + 'm')

# Gathering the beam materials
    for entity in f.by_type("IfcBeam"):
        for relDefinesByProperties in entity.IsDefinedBy:
            for beam_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                if beam_prop.Name == 'Beam Material':
                    
                    print('they consist of '+str(beam_prop.NominalValue.wrappedValue))
else:
    print ('There are no beams in the model')


# The plan is to use the extracted information to draw up a rough cost estimations at early stages of the project development. 
# Potentially this can also be used in analysis to discover where the cost of a project can be cut at early stages of development. 




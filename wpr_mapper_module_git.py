#-------------------------------------------------------------------------------
# Name:         wpr_mapper_wu_module.py
# Purpose:      This module contains functions called in wpr_mapper_lists_git.py
#               and wpr_mapper_dictionaries_git.py. Module must be saved alongside
#               these scripts in order for both to run properly.
# Requirements: ArcGIS Pro, one script to reconstruct a car's path (either
#               wpr_mapper_lists_git.py or wpr_mapper_dictionaries_git.py) and
#               WPRtrack file.
# Author:       Tara Wu
# Created:      07/09/2025
#-------------------------------------------------------------------------------



# Function 1: creates feature class using Create Feature Class tool; adds lap
# field to its attribute table

def wpRacewayFC(out_path, out_name):

    import arcpy
    sr = arcpy.SpatialReference(4326)
    arcpy.management.CreateFeatureclass(out_path, out_name, "POLYLINE", "", "", "",  sr)

    # Add field for lap
    arcpy.management.AddField(out_name, "Lap", "SHORT")



# Function 2: adds polyline to feature class created above

def addPolyline(cursor, lap, coords):

    import arcpy
    cursor.insertRow((lap, coords))
    del coords[:]

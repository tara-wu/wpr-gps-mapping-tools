#-------------------------------------------------------------------------------
# Name:         wpr_mapper_lists_git.py
# Purpose:      This script turns auto racing GPS device data (CSV file) into a
#               vector dataset, creating multiple polylines. It uses a dictionary
#               instead of a list. Note that this script uses  wpr_mapper_module_git.py.
#               Both files must be located in the same folder when running this script.

# Requirements: ArcGIS Pro, wpr_mapper_module_git.py and WPRtrack file
# Author:       Tara Wu
# Created:      07/09/2025
#-------------------------------------------------------------------------------


# import modules and define workspace
import arcpy
arcpy.env.overwriteOutput = True
import wpr_mapper_module_git




# define workspace
arcpy.env.workspace = r"./"
arcpy.env.overwriteOutput = True

# define variables
wprTrack = r"WPRtrack.csv"
polylineGDB = arcpy.env.workspace
polylineFC = "WPRacewayGPSDictionary"


# create feature class
try:
    wpr_mapper_module_git.wpRacewayFC(polylineGDB, polylineFC)
    print("Successfully created feature class for race data.")

except:
    print("Failed to create feature class for race data.")


# open the input file

try:
    with open(wprTrack, "r") as gpsTrack:

        # Set up CSVreader and process the header
        csvReader = csv.reader(gpsTrack)
        header = next(csvReader)
        timeIndex = header.index("Time")
        latIndex = header.index("Latitude")
        lonIndex = header.index("Longitude")
        lapIndex = header.index("Lap")


        # write the lap and coordinates to the feature class as a polyline
        fieldsToUpdate = ('Lap', 'SHAPE@')
        with arcpy.da.InsertCursor(polylineFC, fieldsToUpdate) as cursor:

            # create an empty vertex list
            vertices = []

            # create an empty dictionary for lap (key) and vertices (values)
            completedLaps = {}

            # create a lap counter
            currentLap = 0

            # loop through lines in file and get each vertex / lap number
            try:
                for row in csvReader:

                    # skip extraneous rows without pertinent data
                    if row[timeIndex].startswith("#"):
                        continue

                    else:
                        # add vertices for a particular lap to vertices list


                        if int(row[lapIndex]) != currentLap:
                            completedLaps[currentLap] = vertices

                            # add 1 to existing lap number; start collecting vertices for this new lap
                            currentLap += 1
                            vertices = []

                        lat = float(row[latIndex])
                        lon = float(row[lonIndex])

                        # add coordinate pair to the vertex list
                        vertices.append((lon, lat))
            except:
                print("Reading through file to retrieve vertices and lap numbers did not work.")

            # add final lap to dictionary
            completedLaps[currentLap] = vertices

            # call function to create polylines
            for item in completedLaps:
                wpr_mapper_module_git.addPolyline(cursor, item, completedLaps[item])

    print("Successfully created shapefile contianing all laps from GPS data.")

except:
    print("Failed to create shapefile containing all laps from GPS data.")

# delete cursor
del cursor




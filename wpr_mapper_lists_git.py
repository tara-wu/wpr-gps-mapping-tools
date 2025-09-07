#-------------------------------------------------------------------------------
# Name:         wpr_mapper_lists_git.py
# Purpose:      Script turns auto racing GPS device data (CSV file) obtained from
#               the Walefield Park Raceway into a vector dataset, creating
#               multiple polylines. Note that this script uses the
#               wpr_mapper_module_git.py. As this code is currently written, both
#               files must be located in the same folder when running this script.
# Requirements: ArcGIS Pro, wpr_mapper_module_git.py and WPRtrack file
# Author:       Tara Wu
# Created:      07/09/2025
#-------------------------------------------------------------------------------

# import modules
import arcpy
import csv
import wpr_mapper_module_git


# define workspace and variables
arcpy.env.workspace = r"./"
arcpy.env.overwriteOutput = True
wprTrack = r"./data/WPRtrack.csv"
if not os.path.exists(wprTrack):
    raise FileNotFoundError(f"Input GPS CSV file not found at {wprTrack}. Did you extract the data?")
polylineGDB = arcpy.env.workspace
polylineFC = "WPRacewayGPS"


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

        # write lap and coordinates to the feature class as a polyline
        fieldsToUpdate = ('Lap', 'SHAPE@')

        with arcpy.da.InsertCursor(polylineFC, fieldsToUpdate) as cursor:

            # create an empty vertex list
            vertices = []

            # create a lap counter
            currentLap = 0

            # loop through lines in file and get each vertex / lap number
            try:
                for row in csvReader:

                    # Skip extraneous rows without pertinent data
                    if row[timeIndex].startswith("#"):
                        continue

                    else:
                        # add vertices for a particular lap to vertices list

                        if int(row[lapIndex]) != currentLap:
                            wpr_mapper_module_git.addPolyline(cursor, currentLap, vertices)

                            # Add 1 to existing lap number and start collecting vertices for this new lap
                            currentLap += 1

                        lat = float(row[latIndex])
                        lon = float(row[lonIndex])

                        # add coordinate pair to the vertex list
                        vertices.append((lon, lat))

                # print("All coordinate pairs for all laps were added to the vertex list.")

            except:
                print("Failed to create polylines for all but last lap.")

            try:
                # add the final polyline to the shapefile
                wpr_mapper_module_git.addPolyline(cursor, currentLap, vertices)

            except:
                print("Failed to add final lap polyline to shapefile.")

    print("Successfully created shapefile containing all laps from GPS data.")

except:
    print("Failed to create shapefile containing all laps from GPS data.")

# delete cursor
del cursor



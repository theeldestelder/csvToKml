import csv

def removeCharacter(text, badCharacter):
    if badCharacter in str(text): #filters out the '&' character in name strings
        for character in text:
            if character != '&':
                kml.write(str(character))
    else:
        kml.write(text)

with open("Combined Data Set.csv", newline='') as f:
    reader = csv.reader(f)
    next(f) #skips first line


    kml = open("Combined_Data_Set.kml", 'w')
    kml.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    kml.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n")
    kml.write("\t<NetworkLink>\n")
    kml.write("\t\t<Link>\n")
    kml.write("\t\t\t<href>https://sites.google.com/site/654wqz9n3ksldo9xn/Combined%20Data%20Set.kml</href>\n")
    kml.write("\t\t</Link>\n")
    kml.write("\t</NetworkLink>\n")

    #kml.write("<KML_File>\n")
    kml.write("\t<Document>\n")

    print("Writing file...")

    for row in reader:
        kml.write("\t\t<Placemark>\n")
        kml.write("\t\t\t<name>")

        removeCharacter(row[2], '&')

        kml.write("</name>\n")
        kml.write("\t\t\t<description>")

        removeCharacter(row[3], '&')

        kml.write("</description>\n")
        kml.write("\t\t\t<Point>\n")
        kml.write("\t\t\t\t<coordinates>" + str(row[0]) + "," + str(row[1]) + ",0" + "</coordinates>\n")
        kml.write("\t\t\t</Point>\n")
        kml.write("\t\t</Placemark>\n")
    kml.write("\t</Document>\n")
    kml.write("</kml>\n")
    kml.close()
    print("All done!")

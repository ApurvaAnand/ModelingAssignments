
fileGene = open("genes_GWAS", 'r');
filePathway = open("new_reactome",'r')
outputFile = open("genePathwayMap.csv", "w")
genePathWayString = "Reactome Pathway"
genePathWayMap={}

for line in filePathway:
	line = line.strip()
	if line=='':
		continue
	lineSplits = line.strip().split(genePathWayString)
	pathWayName = lineSplits[0].strip()
	print lineSplits
	for geneName in lineSplits[1].strip().split("\t"):
		if geneName.strip() in genePathWayMap:
			genePathWayMap[geneName.strip()] = genePathWayMap[geneName.strip()] + ", " + pathWayName + " " + genePathWayString
		else:
			genePathWayMap[geneName.strip()] = pathWayName + " " + genePathWayString

filePathway.close()

for line in fileGene:
	geneName = line.strip()
	if geneName in genePathWayMap:
		outputFile.write(geneName+", "+genePathWayMap[geneName]+"\n")

fileGene.close()
outputFile.close()

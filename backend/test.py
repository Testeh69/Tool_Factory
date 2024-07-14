from functionJson import inJsonGetSpecificData,inJsonUpdateSpecificData

print(inJsonGetSpecificData("historique"))
inJsonUpdateSpecificData("historique", 6)
print(inJsonGetSpecificData("historique"))

scan_status = inJsonGetSpecificData("scan_status")
print(scan_status)
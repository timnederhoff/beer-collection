-- noinspection SqlNoDataSourceInspectionForFile

-- noinspection SqlDialectInspectionForFile

DROP TABLE IF EXISTS bieren;

CREATE TABLE "bieren"
(
    "id"                   INTEGER NOT NULL UNIQUE,
    "brouwerij"            TEXT,
    "naam"                 TEXT    NOT NULL UNIQUE,
    "soort"                TEXT,
    "botteljaarAanwezig"   INTEGER,
    "plekOpflesBotteljaar" TEXT,
    "aantalJarenRijpen"    INTEGER,
    "aantalJarenTotTHT"    INTEGER,
    PRIMARY KEY ("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS voorraad;

CREATE TABLE "voorraad" (
    "id"                    INTEGER NOT NULL UNIQUE,
	"bier"	                INTEGER,
	"aankoopDatum"	        INTEGER,
	"bottelDatum"	        INTEGER,
	"aantal"	            INTEGER,
	"tenMinsteHoudbaarTot"  INTEGER,
	"flesnummer"	        TEXT,
	"prijsInkoop"	        INTEGER,
	"doel"	                TEXT,
	"opmerking"	            TEXT,
    PRIMARY KEY ("id" AUTOINCREMENT),
	FOREIGN KEY("bier") REFERENCES "bieren"("id")
);
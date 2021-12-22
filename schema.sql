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
)

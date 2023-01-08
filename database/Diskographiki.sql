PRAGMA synchronous = OFF;
PRAGMA journal_mode = MEMORY;
BEGIN TRANSACTION;
CREATE TABLE "CONTRACT" (
	"contract_id"	integer NOT NULL,
	"artist_id"	INTEGER,
	"start_date"	date DEFAULT NULL,
	"end_date"	date DEFAULT NULL,
	"sign_date"	date DEFAULT NULL,
	"estimated_end"	date,
	CONSTRAINT "CONTRACT_pk" PRIMARY KEY("contract_id"),
	CONSTRAINT "CONTRACT_fk0" FOREIGN KEY("artist_id") REFERENCES "ARTIST"("artist_id") ON DELETE CASCADE ON UPDATE CASCADE

);

CREATE TABLE "AGENT" (
	"agent_id"	integer NOT NULL,
	"First_name"	string NOT NULL,
	"Middle_name"	string DEFAULT NULL,
	"Last_name"	string NOT NULL,
	"partnership_type"	string DEFAULT 'signed',
	"ssn"	varchar(12) NOT NULL,
	"phone"	varchar(14) NOT NULL,
	"street"	TEXT DEFAULT NULL,
	"city"	string DEFAULT NULL,
	"area"	string DEFAULT NULL,
	"zip"	integer DEFAULT NULL,
	"birthdate"	date DEFAULT NULL,
	"passingdate"	date DEFAULT NULL,
	"sex"	string DEFAULT NULL,
	CONSTRAINT "AGENT_pk" PRIMARY KEY("agent_id")
);


CREATE TABLE "MANAGES" (
	"artist_id"	INTEGER,
	"agent_id"	INTEGER,
	"stat_date"	date,
	"end_date"	date,
	CONSTRAINT "MANAGES_fk0" FOREIGN KEY("artist_id") REFERENCES "ARTIST"("artist_id") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "MANAGES_fk1" FOREIGN KEY("agent_id") REFERENCES "AGENT"("agent_id") ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE "ARTIST" (
	"artist_id"	INTEGER NOT NULL,
	"genre"	string DEFAULT NULL,
	"Name"	TEXT,
	CONSTRAINT "ARTIST_pk" PRIMARY KEY("artist_id")
);


CREATE TABLE "SOLO_ARTIST" (
	"artist_id"	integer NOT NULL,
	"First_name"	string NOT NULL,
	"Middle_name"	string DEFAULT NULL,
	"Last_name"	string NOT NULL,
	"ssn"	integer NOT NULL,
	"phone"	integer NOT NULL,
	"street"	string DEFAULT NULL,
	"city"	string DEFAULT NULL,
	"area"	string DEFAULT NULL,
	"zip"	integer DEFAULT NULL,
	"birthdate"	date DEFAULT NULL,
	"passingdate"	date DEFAULT NULL,
	"sex"	TEXT DEFAULT NULL,
	CONSTRAINT "SOLO_ARTIST_pk" PRIMARY KEY("artist_id"),
	CONSTRAINT "SOLO_ARTIST_fk0" FOREIGN KEY("artist_id") REFERENCES "ARTIST"("artist_id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "BAND" (
	"band_id"	integer NOT NULL,
	"band_name"	string NOT NULL,
	"formation_date"	date DEFAULT CURRENT_DATE,
	CONSTRAINT "BAND_pk" PRIMARY KEY("band_id"),
	CONSTRAINT "BAND_fk0" FOREIGN KEY("band_id") REFERENCES ARTIST("artist_id")
);

CREATE TABLE "BELONGS_TO" (
	"band_id"	INTEGER DEFAULT NULL,
	"solo_artist_id"	INTEGER,
	"join_date"	date DEFAULT CURRENT_DATE,
	"leave_date"	date DEFAULT NULL,
	"role"	TEXT,
	CONSTRAINT "BELONGS_TO_fk0" FOREIGN KEY("band_id") REFERENCES BAND("band_id")
	CONSTRAINT "BELONGS_TO_fk1" FOREIGN KEY("solo_artist_id") REFERENCES SOLO_ARTIST("artist_id")

);


CREATE TABLE IF NOT EXISTS "SONG" (
	"song_id"	integer NOT NULL,
	"name"	string NOT NULL,
	"genre"	TEXT DEFAULT NULL,
	CONSTRAINT "SONG_pk" PRIMARY KEY("song_id")
);

CREATE TABLE "RECORDS" (
	"record_id"	integer NOT NULL,
	"artist_id"	integer NOT NULL,
	"song_id"	integer NOT NULL,
	"start_date"	date NOT NULL DEFAULT CURRENT_DATE,
	"end_date"	date,
	CONSTRAINT "RECORDS_pk" PRIMARY KEY("record_id"),
	CONSTRAINT "RECORDS_fk0" FOREIGN KEY("artist_id")REFERENCES ARTIST("artist_id") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "RECORDS_fk1" FOREIGN KEY("song_id")REFERENCES SONG("song_id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "RELEASE" (
	"record_id"	integer NOT NULL,
	"status"	TEXT DEFAULT NULL,
	"studio_id"	integer DEFAULT NULL,
	"hrs_worked"	time NOT NULL,
	"album_id"	integer DEFAULT NULL,
	"track_no"	integer NOT NULL DEFAULT 0,
	"release_date"	date,
	CONSTRAINT "RELEASE_pk" PRIMARY KEY("record_id"),
	CONSTRAINT "RELEASE_fk0" FOREIGN KEY("record_id") REFERENCES RECORDS("record_id") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "RELEASE_fk1" FOREIGN KEY("studio_id") REFERENCES STUDIO("studio_id") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "RELEASE_fk2" FOREIGN KEY("album_id") REFERENCES ALBUM("album_id") ON DELETE CASCADE ON UPDATE CASCADE

);


CREATE TABLE "STUDIO" (
	"studio_id"	integer NOT NULL,
	"studio_name"	string NOT NULL,
	"phone"	integer,
	"street"	TEXT,
	"city"	TEXT,
	"area"	TEXT,
	"zip"	integer DEFAULT NULL,
	"hrly_cost"	integer DEFAULT NULL,
	CONSTRAINT "STUDIO_pk" PRIMARY KEY("studio_id")
);


CREATE TABLE "ALBUM" (
	"album_id"	integer NOT NULL,
	"name"	string NOT NULL,
	"date_released"	date DEFAULT NULL,
	"unit_price"	float DEFAULT NULL,
	CONSTRAINT "ALBUM_pk" PRIMARY KEY("album_id")
);



CREATE TABLE "COMPOSED" (
	"song_id"	integer NOT NULL,
	"writer_id"	integer NOT NULL,
	"composition_date"	date NOT NULL,
	CONSTRAINT "COMPOSED_fk0" FOREIGN KEY("writer_id") REFERENCES WRITER("writer_id") ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT "COMPOSED_fk1" FOREIGN KEY("song_id") REFERENCES SONG("song_id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "WRITER" (
	"writer_id"	integer NOT NULL,
	"First_name"	string NOT NULL,
	"Middle_name"	string DEFAULT NULL,
	"Last_name"	string NOT NULL,
	"ssn"	integer NOT NULL,
	"phone"	integer NOT NULL,
	"street"	string DEFAULT NULL,
	"city"	string DEFAULT NULL,
	"area"	string DEFAULT NULL,
	"zip"	integer DEFAULT NULL,
	"birthdate"	date DEFAULT NULL,
	"passingdate"	date DEFAULT NULL,
	"sex"	string DEFAULT NULL,
	CONSTRAINT "WRITTER_pk" PRIMARY KEY("writer_id")
);

INSERT INTO "ARTIST"  VALUES (1,'Hip-hop,dance-pop,pop,rnb,pop-rap','Black Eyed Peas'),(2,NULL,'David Guetta'),(3,NULL,'Drake'),(4,NULL,'Lady Gaga'),(5,'rnb,Soul,pop','John Legend'),
 (6,'Hip-hop,pop,rap-pop,rnb','will.i.am'),(7,'electro,Hip-house,Hip-hop,alternative','apl.de.ap'),(8,'electro,Hip-hop,alternative','Taboo '),(9,'pop,Hip-hop','Fergie'),(10,'Soul,rnb,gospel,funk,Hip-hop','Kim Hill'),
 (11,NULL,'Celine Dion');

INSERT INTO "SOLO_ARTIST" VALUES (2,'Pierre','David','Guetta','261-92-6511','+1-206-238-5650','852 Broaddus Avenue','Bowling Green','Kentucky',42101,'1967-11-7',NULL,'Male'),
 (3,'Aubrey','Drake','Graham','409-07-1019','+1-865-549-7640','866 Berkshire Circle','Knoxville','Tennessee',37917,'1986-10-24',NULL,'Male'),(4,'Stefani','Joanne Angelina','Germanotta','503-82-5804','+1-413-253-6876','128 Frank Avenue','Amherst','Massachusetts',1002,'1986-03-28',NULL,'Female'),
 (5,'John','Roger','Stephens','221-26-1280','+1-262-878-0136','554 Joseph Street','Union Grove','Wisconsin',53182,'1978-12-28',NULL,'Male'),(6,'William','James','Adams','009-03-1451','+1-978-204-1361','1439 Pearlman Avenue','Bolton','Massachusetts',1740,'1975-03-15',NULL,'Male'),
 (7,'Allan','Pineda','Lindo','252-20-7467','+1-970-313-0538','2430 Rose Avenue','New Orleans','Louisiana',70112,'1974-11-28',NULL,'Male'),(8,'James','Luis','Gomez','532-42-0963','+1-626-363-3044','4281 Timberbrook Lane','Denver','Colorado',80202,'1974-11-28',NULL,'Male'),
 (9,'Stacy','Ann','Ferguson','318-84-6393','+1-504-285-2069','940 Wood Duck Drive','Iron Mountain','Michigan',49801,'1975-03-27','','Female'),(10,'Kimberly','Allise','Hill','525-46-1678','+1-906-367-7070','1557 Middleville Road','Los Angeles','California',90017,'1972-01-14',NULL,'Female'),
 (11,'Celine','Marie Claudette','Dion','409-21-6361','+1-707-763-9919','2985 Davis Avenue','Porter','Minnesota',56280,'1968-03-30',NULL,'Female');

INSERT INTO "BAND" VALUES (1,'Black Eyed Peas','1975-07-14');

INSERT INTO "BELONGS_TO" VALUES (1,6,1995,2011,'vocals, piano, synthesizer, bass'),(1,7,1995,2011,'vocals, drums'),
 (1,8,1995,2011,'vocals, DJ, guitar'),(1,10,1995,2000,'vocals'),(1,9,2002,2011,'vocals'),(1,6,2015,'NULL','vocals, piano, synthesizer, bass'),(1,7,2015,'NULL','vocals, drums'),
 (1,8,2015,'NULL','vocals, DJ, guitar'),(1,9,2015,2018,'vocals');

INSERT INTO "WRITER" VALUES (1,'Pierre','David','Guetta','261-92-6511','+1-206-238-5650','852 Broaddus Avenue','Bowling Green','Kentucky',42101,'1967-11-7','','Male'),
 (2,'Aubrey','Drake','Graham','409-07-1019','+1-865-549-7640','866 Berkshire Circle','Knoxville','Tennessee',37917,'1986-10-24',NULL,'Male'),(3,'William','James','Adams','009-03-1451','+1-978-204-1361','1439 Pearlman Avenue','Bolton','Massachusetts',1740,'1975-03-15',NULL,'Male'),
 (4,'Kanye','Omari','West','002-78-8875','+1-724-383-2767','2028 Stuart Street','Pittsburgh','Pennsylvania',15222,'1978-12-28','','Male'),(5,'Stefani','Joanne Angelina','Germanotta','503-82-5804','+1-413-253-6876','128 Frank Avenue','Amherst','Massachusetts',1002,'1986-03-28',NULL,'Female'),
 (6,'John','Roger','Stephens','221-26-1280','+1-262-878-0136','554 Joseph Street','Union Grove','Wisconsin',53182,'1978-12-28',NULL,'Male'),(7,'Will','H.','Jennings','400-47-1962','+1-858-546-8546','4391 Pike Street','San Diego','California',92111,'1944-06027',NULL,'Male');

INSERT INTO "CONTRACT" VALUES (1,1,'2018-09-02','2020-09-02','2018-08-01','2020-09-02'),(2,2,'2021-08-13','NULL','2021-06-21','2023-12-31'), (3,3,'2015-01-01','2017-02-15','2014-11-03','2017-02-15'),(4,4,'2007-10-02','2009-10-02','2007-07-12','2009-10-02'),(5,5,'2003-02-10','2005-12-31','2003-01-10','2005-12-31'),(6,11,'1995-02-01','1998-03-10','1995-02-01','1998-10-02'),
 (7,6,'2019-01-01','NULL','2018-12-02','2024-12-31'),(8,5,'2005-12-31','2007-12-31','2005-11-01','2007-12-31');


INSERT INTO "AGENT" VALUES (0,'Scooter',NULL,'Braun','signed','303-27-7732','+1-760-210-7954','3754 Tenmile','San Diego','California',92103,'1981-06-18',NULL,'Male'),
(1,'Troy',NULL,'Carter','signed','479-84-7441','+1-816-213-4210','3305 Nutter Street','Wilmer','Alabama',36587,'1972-11-14',NULL,'Male'),(2,'Kevin',NULL,'Liles','signed','269-28-3989','+1-503-871-7472','1971 Heron Way','Salem','Oregon',97301,'1968-02-27',NULL,'Male'),(3,'Rene',NULL,'Angelil','signed','576-34-3880','+1-270-655-2265','852 Broaddus Avenue','Bowling Green','Kentucky',42101,'1942-01-16','2016-01-14','Male');

INSERT INTO "STUDIO" VALUES (1,'winterland studios','+1-761-971-8952','5417 Boone Ave N','Minneapolis','MN',55428,265),(2,'kopperhead',0,'935 Schneider St. SE','North Canton','OH',44720,530),(3,'Discosapien','+1-720-804-0460','10000 West 100th Ave','Westminister','CO',80021,380);

INSERT INTO "SONG" VALUES (1,'Gods Plan','Pop,trap'),(2,'I''m upset','Hip-hop'),(3,'Hotline Bling','Pop,Rnb'),(4,'Audios','pop'),(5,'Dance4U','pop'),(6,'Guarantee','pop'),
 (7,'Ritmo','Hip-hop,Pop,Reggaeton'),(8,'I''m Good','House'),(9,'When Love Takes Over','Synth-pop,Dance-pop'),(10,'Just Dance','Electro-pop,Synth-pop,Dance-pop'),(11,'Paparazzi','Techno-pop,Dance-pop'),
 (12,'Poker Face','Synth-pop,Dance-pop'),(13,'Love Game','Synth-pop,Electro-rnb'),(14,'Used To Love You','rnb,Hip-hop,Soul'),(15,'Number One','rnb,Hip-hop,Soul'),(16,'My Heart Will Go On','Pop'),
 (17,'It''s All Coming Back To Me Now','Power Ballad'),(18,'Because You Loved Me','Pop');


INSERT INTO "MANAGES" VALUES (1,0,'2018-09-02','2020-09-02'),(2,0,'2021-08-13','NULL'),(3,0,'2015-01-01','2017-02-15'),(4,1,'2007-10-02','2009-10-02'),
 (5,1,'2005-12-31','2007-12-31'),(11,3,'1995-02-01','1998-03-10'),(6,2,'2019-01-01','NULL');

INSERT INTO "COMPOSED" VALUES (1,2,'2018-05-23'),(2,2,'2018-03-13'),(3,2,'2017-07-16'),(4,3,'2022-04-12'),(5,3,'2022-04-12'),(6,3,'2022-04-09'),
 (7,3,'2019-02-11'),(8,1,'2022-04-26'),(9,1,'2018-10-03'),(10,5,'2008-02-26'),(11,5,'2008-02-26'),(12,5,'2008-02-26'),(13,5,'2008-02-26'),(14,6,'2003-09-18'),(15,6,'2003-09-18'),(16,7,'1995-07-18'),
(17,7,'1995-07-18'),(18,7,'1995-07-18'),(15,4,'2003-09-18');

INSERT INTO "ALBUM" VALUES (1,'Elavation','2022-11-11',9.99),(2,'Scorpion','2018-06-29',17.98),(3,'The Fame','2008-08-19',7.97),
 (4,'Get Lifted','2004-12-28',4.99),(5,'Falling Into You','1996-03-11',8.48);

INSERT INTO "RECORDS" VALUES (1,1,4,'2018-06-24','2018-06-25'),(2,1,5,'2018-06-23','2018-06-23'),(3,1,6,'2019-07-25','2019-07-25'),
 (4,1,7,'2022-11-06','2022-11-09'),(5,2,8,'2022-11-08','2022-11-09'),(6,2,9,'2022-11-05','2022-11-07'),(7,3,1,'2019-02-08','2019-02-08'),(8,3,2,'2022-08-17','2022-08-20'),(9,3,3,'2019-04-13','2019-04-18'),
 (10,4,10,'2008-04-02','2008-04-06'),(11,4,11,'2008-08-15','2008-08-19'),(12,4,12,'2008-08-12','2008-08-14'),(13,4,13,'2008-08-14','2008-08-19'),(14,5,14,'2004-12-23','2004-12-25'),(15,5,15,'2004-12-26','2004-12-28'),
 (16,11,16,'1997-11-07','1997-11-11'),(17,11,17,'1996-02-26','1996-03-01'),(18,11,18,'1996-02-26','1996-03-05');


INSERT INTO "RELEASE" VALUES (1,'Released',2,10,2,5,'2018-06-29'),
 (2,'Released',2,6,2,6,'2018-06-29'),
 (3,'Released',3,4,NULL,0,'2019-07-31'),
 (4,'Released',1,2,1,3,'2022-11-11'),
 (5,'Released',1,3,1,7,'2022-11-11'),
 (6,'Released',1,10,1,8,'2022-11-11'),
 (7,'Released',2,7,NULL,0,'2019-02-11'),
 (8,'Released',2,5,NULL,0,'2022-08-26'),
 (9,'Released',1,13,NULL,0,'2019-04-21'),
 (10,'Released',3,8,3,1,'2008-04-08'),
 (11,'Released',3,12,3,3,'2008-08-19'),
 (12,'Released',3,5,3,4,'2008-08-19'),
 (13,'Released',3,10,3,2,'2008-08-19'),
 (14,'Released',2,16,4,3,'2004-12-28'),
 (15,'Released',2,9,4,6,'2004-12-28'),
 (16,'Released',1,11,NULL,0,'1997-11-11'),
 (17,'Released',1,10,5,1,'1996-03-11'),
 (18,'Released',1,5,5,2,'1996-03-11');




COMMIT;

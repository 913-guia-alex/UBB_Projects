Create database GymFinal
go
use GymFinal
go

--COACH , CLIENT AND THE NUTRITION PLAN TABLES

CREATE TABLE CoachGymM(
idCo int NOT NULL PRIMARY KEY IDENTITY,
Name varchar(50) NULL,
Price int NULL,
)

CREATE TABLE ClientGymM(
idCl int NOT NULL PRIMARY KEY IDENTITY,
Name varchar(50) NULL,
Age int NULL,
gendre varchar(50) NULL,
idCo int FOREIGN KEY REFERENCES CoachGymM(idCo)
)

CREATE TABLE NutritionPlanM(
idN int NOT NULL PRIMARY KEY IDENTITY,
Type varchar(50) NULL,
Duration int NULL,
idCo int FOREIGN KEY REFERENCES CoachGymM(idCo),
)


--EXERCISE AND TRAINING TABLE


CREATE TABLE ExerciseM(
idEx int NOT NULL PRIMARY KEY IDENTITY,
Name varchar(50) NULL,
NrOfReps varchar(50) NULL,
RestTime int NULL,
)

CREATE TABLE TrainingM(
TipeOfProduct varchar(50) NULL,
idCl INT FOREIGN KEY REFERENCES ClientGymM(idCl),
idEx INT FOREIGN KEY REFERENCES ExerciseM(idEx)
CONSTRAINT PK_ClientAndExercise PRIMARY KEY(idCl,idEx)
)


--SHOP AND PRODUCT TABLE


CREATE TABLE ShopGymM(
idS int NOT NULL PRIMARY KEY IDENTITY,
Name varchar(50) NULL,
)

CREATE TABLE ProductM(
TipeOfProduct varchar(50) NULL,
idCl INT FOREIGN KEY REFERENCES ClientGymM(idCl),
idS INT FOREIGN KEY REFERENCES ShopGymM(idS)
CONSTRAINT PK_ClientAndShop PRIMARY KEY(idCl,idS)
)


--GYM , GYMCARD AND EQUIPMENT TABLES


CREATE TABLE GymBuildingM(
idG int NOT NULL PRIMARY KEY IDENTITY,
Name varchar(50) NULL,
Adress varchar(50) NULL,
)

CREATE TABLE GymCardM(
NrOfEntries int NULL,
idCl INT FOREIGN KEY REFERENCES ClientGymM(idCl),
idG INT FOREIGN KEY REFERENCES GymBuildingM(idG)
CONSTRAINT PK_ClientAndGymBuilding PRIMARY KEY(idCl,idG)
)

CREATE TABLE EquipmentM(
idEq int NOT NULL PRIMARY KEY IDENTITY,
Name varchar(50) NULL,
Type varchar(50) NULL,
idG int FOREIGN KEY REFERENCES GymBuildingM(idG)
)









-------------------------------------------LAB 2 ASSIGMENT STARTS HERE--------------------------------------------









-- THE SELECT PART FOR ALL THE TABLE---------------------------------------------------------------------------

SELECT * FROM CoachGymM
SELECT * FROM ClientGymM
SELECT * FROM NutritionPlanM
SELECT * FROM ExerciseM
SELECT * FROM TrainingM
SELECT * FROM ShopGymM
SELECT * FROM ProductM
SELECT * FROM GymBuildingM
SELECT * FROM GymCardM
SELECT * FROM EquipmentM



--IMPLEMENTAATION OF INSERT ------------------------------------------------------------------------------


INSERT INTO ShopGymM VALUES ('ProteinBar')
INSERT INTO ShopGymM VALUES ('WheyProtein')
INSERT INTO ShopGymM VALUES ('Carnitine')
INSERT INTO ShopGymM VALUES ('Creatine')
INSERT INTO ShopGymM VALUES ('BCAA')



INSERT INTO CoachGymM VALUES ('Andrei' , 300)
INSERT INTO CoachGymM VALUES ('Dan' , 400)
INSERT INTO CoachGymM VALUES ('Victor' , 250)
INSERT INTO CoachGymM VALUES ('Maria',800)
INSERT INTO CoachGymM VALUES ('Dana',0)


INSERT INTO ClientGymM VALUES ('Marius',14,'Masculin',3)
INSERT INTO ClientGymM VALUES ('Dan',22,'Masculin',1)
INSERT INTO ClientGymM VALUES ('Andreea',17,'Feminin',2)
INSERT INTO ClientGymM VALUES ('Ana',16,'Feminin',3)


INSERT INTO GymBuildingM VALUES('24Gym','Dunarii50')
INSERT INTO GymBuildingM VALUES('18Gym','Zorilor30')
INSERT INTO GymBuildingM VALUES('WorldClass','IuliusMall12')
INSERT INTO GymBuildingM VALUES('BambooFitness','MihaiViteazul34')


INSERT INTO GymCardM VALUES (20,2,1)
INSERT INTO GymCardM VALUES (30,2,2)
INSERT INTO GymCardM VALUES (15,3,1)
INSERT INTO GymCardM VALUES (80,3,3)


INSERT INTO NutritionPlanM VALUES('Bulk',20,2)
INSERT INTO NutritionPlanM VALUES('Cut',30,2)
INSERT INTO NutritionPlanM VALUES('Maintain',40,7)
INSERT INTO NutritionPlanM VALUES('Cut',30,4)
INSERT INTO NutritionPlanM VALUES('Bulk',0,6)



INSERT INTO ExerciseM VAlUES('Squat',10,20)
INSERT INTO ExerciseM VAlUES('DeadLift',8,40)
INSERT INTO ExerciseM VAlUES('BenchPress',12,50)
INSERT INTO ExerciseM VAlUES('MilitaryPress',4,60)


INSERT INTO TrainingM VALUES('Hard',2,4)
INSERT INTO TrainingM VALUES('Easy',4,4)
INSERT INTO TrainingM VALUES('Medium',2,1)
INSERT INTO TrainingM VALUES('Hard',3,2)




--IMPLEMENTAATION OF UPDATE---------------------------------------------------------------------------------



UPDATE ClientGymM
SET Name='Dragos'
WHERE Age >16 OR gendre ='Masculin'
Select * from ClientGymM


UPDATE CoachGymM
SET Name = 'Cristina'
WHERE Price >= 300 AND Price <400
SELECT * from CoachGymM


UPDATE CoachGymM
SET Price =  1000
WHERE Price IS NULL
SELECT * FROM CoachGymM


UPDATE GymCardM
SET NrOfEntries = 100
WHERE NrOfEntries IS NOT NULL
SELECT * FROM GymCardM


UPDATE GymCardM
SET NrOfEntries = 300
WHERE NrOfEntries IN (50,100,200,400)
SELECT * FROM GymCardM


UPDATE GymCardM
SET NrOfEntries = 200
WHERE NrOfEntries BETWEEN 50 AND 400
SELECT * FROM GymCardM


UPDATE ClientGymM
SET Age = 20
WHERE Name LIKE '_ra%'
SELECT * FROM ClientGymM



--IMPLEMENTATION OF DELETE-----------------------------------------------------------------------------



DELETE FROM CoachGymM
WHERE Name LIKE '_ra%' 
SELECT * FROM CoachGymM


DELETE FROM NutritionPlanM
WHERE Type IS NULL OR idCo > 2
SELECT * FROM NutritionPlanM


DELETE FROM NutritionPlanM
WHERE Duration IN (0,10,20,30,40)
SELECT * FROM NutritionPlanM


DELETE FROM NutritionPlanM
WHERE Duration BETWEEN 0 AND 30
SELECT * FROM NutritionPlanM


DELETE FROM CoachGymM
WHERE Name LIKE '_a%' AND Price = 0
SELECT * FROM CoachGymM



-- IMPLEMENTATION OF UNION -----------------------------------------------------------------------------------



SELECT * FROM ClientGymM
WHERE Name LIKE '_ra%'
UNION
SELECT * FROM ClientGymM
WHERE Age >=20
ORDER BY Age


SELECT Co1.Price
FROM CoachGymM Co1
WHERE Name LIKE 'An%'
UNION
SELECT Co2.Price
FROM CoachGymM Co2
WHERE Price <300
ORDER BY Price


SELECT C1.Age
FROM ClientGymM C1
WHERE Name LIKE '_ar%'
UNION ALL
SELECT C2.idCl
FROM ClientGymM C2
WHERE Age <17
ORDER BY C1.Age



-- IMPLEMENTATION OF INTERSECT AND IN ------------------------------------------------------------------



SELECT * FROM ClientGymM
WHERE Name LIKE 'D_%'
INTERSECT
SELECT * FROM ClientGymM
WHERE gendre LIKE 'Masculin'
ORDER BY idCl


SELECT * FROM ClientGymM
WHERE Age IN (10,22,30,40)
INTERSECT
SELECT * FROM ClientGymM
WHERE Name LIKE 'D__'
ORDER BY  idCl



--IMPLEMENTATION OF EXCEPT AND NOT IN--------------------------------------------------------------------



SELECT * FROM  NutritionPlanM
WHERE Type LIKE 'Cut'
EXCEPT
SELECT * FROM NutritionPlanM
WHERE Duration < 50
ORDER BY idN


SELECT * FROM GymCardM
WHERE NrOfEntries NOT IN (100,300,400)
EXCEPT
SELECT * FROM GymCardM
WHERE idCl <3
ORDER BY idG



--IMPLEMETATION OF  INNER JOIN, LEFT JOIN, RIGHT JOIN and FULL JOIN------------------------------------------



SELECT * FROM ClientGymM Cl INNER JOIN CoachGymM Co ON
Cl.idCl = Co.idCo
INNER JOIN GymBuildingM Gm ON Gm.idG = cL.idCl


SELECT * FROM TrainingM , GymCardM
SELECT * FROM TrainingM Tr LEFT OUTER JOIN GymCardM Gm ON 
Tr.idEx = Gm.idG


SELECT * FROM TrainingM , GymCardM
SELECT * FROM TrainingM Tr RIGHT OUTER JOIN GymCardM Gm ON 
Tr.idCl = Gm.idCl


SELECT * FROM TrainingM , GymCardM
SELECT * FROM TrainingM Tr FULL OUTER JOIN GymCardM Gm ON 
Tr.idCl = Gm.idG



--IMPLEMENTATION OF e)---------------------------------------------------------------------------------



SELECT Co.idCo , Co.Price
FROM CoachGymM Co
WHERE Price >300 AND Co.idCo IN (SELECT Cl.idCl FROM ClientGymM Cl)


SELECT Cl.Age , Cl.idCl , Cl.gendre
FROM ClientGymM Cl
WHERE Age >14 AND Cl.idCl IN (SELECT Co.idCo FROM CoachGymM Co WHERE Cl.gendre LIKE 'Masculin')



--IMPLEMENTATION OF f)----------------------------------------------------------------------------------



SELECT Cl.Age , Cl.idCl , Cl.gendre
FROM ClientGymM Cl
WHERE Age <22 AND EXISTS (SELECT Co.Price FROM CoachGymM Co WHERE Co.price < 400)


SELECT Co.idCo , Co.Price
FROM CoachGymM Co
WHERE Price >300 AND EXISTS (SELECT * FROM ClientGymM Cl WHERE Cl.idCl = Co.idCo)



--IMPLEMENTATION OF g)--------------------------------------------------------------------------------



SELECT Cl.idCo , Cl.idN
FROM (SELECT Co.IdCo , Co.Price , Np.idN 
			FROM CoachGymM Co INNER JOIN NutritionPlanM Np ON Co.idCo = Np.idN
			WHERE Co.Price = 300) Cl


SELECT  CO.idCl , CO.Name 
FROM( SELECT  CL.IdCl , CL.Name  , CL.Age
			FROM ClientGymM CL INNER JOIN NutritionPlanM NP ON CL.idCl = NP.idN
			WHERE CL.Age > 14) CO



--IMPLEMENTATION OF h)-----------------------------------------------------------------------------------------



SELECT CL.Name 
FROM ClientGymM CL INNER JOIN CoachGymM CO ON 
CL.idCo = CO.idCo
GROUP BY CL.Name , CO.Name


SELECT CL.Name , AVG(CO.price) AS AveragePrice
FROM ClientGymM CL INNER JOIN CoachGymM CO ON 
CL.idCo = CO.idCo
GROUP BY CL.Name 


SELECT CL.Name , AVG(CO.price) 
FROM ClientGymM CL INNER JOIN CoachGymM CO ON 
CL.idCo = CO.idCo
GROUP BY CL.Name 
HAVING AVG(CO.Price)>200


SELECT CL.idCl , CL.Name , AVG(CL.Age)
FROM ClientGymM CL INNER JOIN CoachGymM CO ON
CL.idCl = CO.idCo
GROUP BY CL.idCl , CL.Name
HAVING AVG(CL.Age)>=(SELECT min(Age) FROM ClientGymM)


SELECT CO.Name , CO.Price 
FROM CoachGymM CO INNER JOIN ClientGymM CL ON
CO.Name = CL.Name
GROUP BY CO.Name , CO.Price
HAVING AVG(CO.Price)<=(SELECT max(Price) FROM CoachGymM)



--IMPLEMENTATION OF i)--------------------------------------------------------------------------------

---  (>) ALL EQUIVALENCE WITH MAX--------------------------------------------------------------------



SELECT  CL.idCl , CL.Name , CL.Age
FROM ClientGymM CL
WHERE CL.Age>ALL( SELECT CL2.Age FROM ClientGymM CL2 WHERE CL.idCl = CL2.idCl)


SELECT  CL.idCl , CL.Name , CL.Age
FROM ClientGymM CL
WHERE CL.Age>( SELECT MAX(CL2.Age) FROM ClientGymM CL2 WHERE CL.Age = CL2.Age)



-- (<) ANY EQUIVALENCE WITH MIN ----------------------------------------------------------------------------



SELECT CO.Name , CO.Price
FROM CoachGymM CO
WHERE CO.Price<Any( SELECT CO2.Price FROM CoachGymM CO2 WHERE CO.idCo = CO2.idCo)


SELECT CO.Name , CO.Price
FROM CoachGymM CO
WHERE CO.Price<(SELECT MIN(CO2.Price) FROM CoachGymM CO2 WHERE CO.idCo = CO2.idCo)



-- (<>) ALL EQUIVALENCE WITH NOT IN --------------------------------------------------------------------------



SELECT NP.Type , NP.Duration
FROM NutritionPlanM NP
WHERE NP.Duration<>ALL( SELECT NP2.DURATION FROM NutritionPlanM NP2 WHERE NP.idN = NP2.idN)


SELECT NP.Type , NP.Duration
FROM NutritionPlanM NP
WHERE NP.Duration NOT IN( SELECT NP2.DURATION FROM NutritionPlanM NP2 WHERE NP.idN = NP2.idN)



-- (=) ANY EQUIVALENCE WITH IN ---------------------------------------------------------------------------



SELECT EX.Name , EX.NrOfReps
FROM ExerciseM EX
WHERE EX.NrOfReps =ANY ( SELECT EX2.NrOfReps FROM ExerciseM EX2 WHERE EX.idEx = EX2.idEx)


SELECT EX.Name , EX.NrOfReps
FROM ExerciseM EX
WHERE EX.NrOfReps IN ( SELECT EX2.NrOfReps FROM ExerciseM EX2 WHERE EX.idEx = EX2.idEx)



--EXTRA PARTS--------------------------------------------------------------------------------------------------

--arithmetic expressions in the SELECT clause in at least 3 queries--------------------------------------------



SELECT CL.NAME , (CL.Age-3)/3 AS AgeArithmetic
FROM ClientGymM CL


SELECT CO.Name , (CO.Price+4)/5 AS PriceArithmetic
FROM CoachGymM CO


SELECT EX.Name , (EX.NrOfReps+12)*7 AS NrOfRepsArithmetic
FROM ExerciseM EX



--conditions with AND, OR, NOT and parantheses in the WHERE clause in at least 3 queries----------------------



SELECT CL.idCl , CL.Name
FROM ClientGymM CL
WHERE (CL.Age >10 AND CL.Name LIKE '_an')


SELECT NP.Type , NP.Duration
FROM NutritionPlanM NP
WHERE (NP.Type LIKE 'Cut' OR NP.Duration = 20)


SELECT CO.idCo , CO.Price
FROM CoachGymM CO
WHERE (CO.Price NOT IN (20,40,60,80,100,200,300,400))



--DISTINCT in at least 3 queries ------------------------------------------------------------------------------



SELECT DISTINCT CL.Name , CL.Age , CL.Gendre 
FROM ClientGymM CL


SELECT DISTINCT CO.idCo , CO.Name 
FROM CoachGymM CO


SELECT DISTINCT EX.Name , EX.NrOfReps
FROM ExerciseM EX



--ORDER BY in at least 2 queries -------------------------------------------------------------------------



SELECT * FROM GymCardM
WHERE idCl = idG
ORDER BY idCl


SELECT* FROM ExerciseM
WHERE RestTime >30
ORDER BY Name



--TOP in at least 2 queries ----------------------------------------------------------------------------------



SELECT TOP 2 CL.Name , CL.Age , CL.gendre
FROM ClientGymM CL


SELECT TOP 4 CO.Name , CO.Price
FROM CoachGymM CO



--USING VIEW IN THE OTHER TAB------------------------------------------------------------------------------





-------------------------------------------------- FINISHED :) --------------------------------------------







--------------------------------------------LAB 3 ASSIGMENT STARTS HERE---------------------------------------



--Drop all the procedures from the procedures table in case we need it


--drop procedure ChangeTypeColumn
--drop procedure DropColumn
--drop procedure AddColumn
--drop procedure AddConstrain
--drop procedure DropConstrain
--drop procedure AddPrimaryKey
--drop procedure DropPrimaryKey
--drop procedure AddCandidateKey
--drop procedure DropCandidateKey
--drop procedure AddOrderShop
--drop procedure DropOrderShop
--drop procedure AddForeignKey
--drop procedure DropForeignKey
--drop procedure goToVersion



--MODIFY THE TYPE OF A COLUMN----------------------------------------------------------------------------------------



--A.1) Changing the type of the column "Name" from the table ShopGymM 


create procedure ChangeTypeColumn as
	ALTER TABLE NutritionPlanM
	ALTER COLUMN Duration VarChar(50)
execute ChangeTypeColumn
go

--A.2) Changing back the type of the column "Name" from the table ShopGymM 


create procedure ChangeTypeColumnBack as
	ALTER TABLE NutritionPlanM
	ALTER COLUMN Duration int NOT NULL
execute ChangeTypeColumnBack
go


--ADD/REMOVE A COLUMN FROM A TABLE---------------------------------------------------------------------------------



--B.1) Dropping the column "Namee" from the table ShopGymM

drop procedure DropColumn

create procedure DropColumn as
	ALTER TABLE ShopGymM
	DROP COLUMN Namee
execute DropColumn
go


--B.2) Adding the column "Namee" in the table ShopGymM


create procedure AddColumn as
	ALTER TABLE ShopGymM
	ADD Namee VARCHAR(50) 
execute AddColumn
go



--ADD/REMOVE A DEFAULT CONSTRAIN-----------------------------------------------------------------------------



--C.1) Adding a default constrain to the table ShopGymM


create procedure AddConstrain as
	ALTER TABLE ShopGymM
	ADD constraint DefaultConstraint default(0) for Namee
execute AddConstrain
go


--C.2) Dropping a default constrain from the table ShopGymM


create procedure DropConstrain as
	ALTER TABLE ShopGymM
	DROP CONSTRAINT DF__ShopGymM__Price__36B12243
execute DropConstrain
go



--ADD/REMOVE A PRIMARY KEY-------------------------------------------------------------------------------------



--D.1) Add a primary key in the table ProductM


create procedure AddPrimaryKey as
	ALTER TABLE ProductM
	DROP CONSTRAINT PK_ClientAndShop
	ALTER TABLE ProductM
	ADD CONSTRAINT PK_ClientAndShop primary key(idCl,idS)
execute AddPrimaryKey
go


--D.2) Remove a primary key from the table ProductM


create procedure DropPrimaryKey as
	ALTER TABLE ProductM
	DROP CONSTRAINT PK_ClientAndShop
	ALTER TABLE ProductM
	ADD CONSTRAINT PK_ClientAndShop primary key(idCl)
execute DropPrimaryKey
go



--ADD/REMOVE A CANDIDATE KEY------------------------------------------------------------------------------------



--E.1) Add a canditate key in the ClientGymM table


create procedure AddCandidateKey as
	ALTER TABLE ClientGymM ADD CONSTRAINT Client_Candidate_Key unique(idCL,Age)
execute AddCandidateKey
go


--E.2) remove a candidate key from the ClientGymM table


create procedure DropCandidateKey as
	ALTER TABLE ClientGymM DROP CONSTRAINT Client_Candidate_Key
execute DropCandidateKey
go



--CREATE/DROP A NEW TABLE-----------------------------------------------------------------------------------------



--F.1) create a new table


CREATE TABLE ShopGymM(
idS int NOT NULL PRIMARY KEY IDENTITY,
Name varchar(50) NULL,
)

CREATE TABLE Furnizor(
idF INT PRIMARY KEY IDENTITY NOT NULL, --aid
Name VARCHAR(50),
)


create procedure AddOrderShop as
	CREATE TABLE OrderShop(
	idO INT PRIMARY KEY IDENTITY NOT NULL,
	idF INT FOREIGN KEY REFERENCES Furnizor(idF) NOT NULL,
	idS INT FOREIGN KEY REFERENCES ShopGymM(idS) NOT NULL,
	Weight INT NOT NULL
	)
execute AddOrderShop
go


--F.2) drop a table


create procedure DropOrderShop as
	DROP TABLE OrderShop
execute DropOrderShop
go


--ADD/REMOVE A FOREIGN KEY-------------------------------------------------------------------------------------------



--G.1) add a foreign key in the OrderShop table


create procedure AddForeignKey as
	ALTER TABLE OrderShop ADD CONSTRAINT idS foreign key(idS) references ShopGymM(idS)
execute AddForeignKey
go



--G.2) Remove a foreign key in the OrderShop table


create procedure DropForeignKey as
	ALTER TABLE OrderShop DROP CONSTRAINT idS
execute DropForeignKey
go







-----------------------------------------------Procedure Table-----------------------------------------------------


create table proceduresTable (
    fromVersion int,
    toVersion int,
    primary key (fromVersion, toVersion),
    nameProc varchar(max)
)

SELECT * FROM proceduresTable

--drop table proceduresTable



------------------------------------------------Version Table--------------------------------------------------

create table versionTable (
    version int
)

SELECT * FROM versionTable
SELECT * FROM proceduresTable

--insert into versionTable values (1)

--drop table versionTable



insert into proceduresTable values(1,2, 'ChangeTypeColumn')
insert into proceduresTable values(2,1, 'ChangeTypeColumnBack')
insert into proceduresTable values(2,3, 'AddColumn')
insert into proceduresTable values(3,2, 'DropColumn')
insert into proceduresTable values(3,4, 'AddConstrain')
insert into proceduresTable values(4,3, 'DropConstrain')
insert into proceduresTable values(4,5, 'AddPrimaryKey')
insert into proceduresTable values(5,4, 'DropPrimaryKey')
insert into proceduresTable values(5,6, 'AddCandidateKey')
insert into proceduresTable values(6,5, 'DropCandidateKey')
insert into proceduresTable values(6,7, 'AddOrderShop')
insert into proceduresTable values(7,6, 'DropOrderShop')
insert into proceduresTable values(7,8, 'AddForeignKey')
insert into proceduresTable values(8,7, 'DropForeignKey')



--SELECT * FROM proceduresTable
--SELECT * FROM versionTable


--------------------------------
-- goToVersion procedure

create procedure goToVersion(@newVersion int) as
    declare @curr int
    declare @var varchar(max)
    select @curr=version from versionTable


    if @newVersion > (select max(toVersion) from proceduresTable)
        raiserror ('Bad version', 10, 1)
		return 

    while @curr > @newVersion begin
        select @var=nameProc from proceduresTable where fromVersion=@curr and toVersion=@curr-1
        exec (@var)
        set @curr=@curr-1
    end

    while @curr < @newVersion begin
        select @var=nameProc from proceduresTable where fromVersion=@curr and toVersion=@curr+1
        exec (@var)
        set @curr=@curr+1
    end

    update versionTable set version=@newVersion


execute goToVersion 2
go

--SELECT * FROM ShopGymM

--SELECT * FROM versionTable

--SELECT * FROM proceduresTable
--------------------------






----------------------------- LAB5 ------------------------------------------------


-- CREATING THE NECESARY TABLES FOR THE ASSIGMENT


-- First Table------------------------

CREATE TABLE NutritionPlanM(
idN int NOT NULL PRIMARY KEY IDENTITY,
Type varchar(50) NULL,
Duration int NULL,
idCo int FOREIGN KEY REFERENCES CoachGymM(idCo),
)

-- Second Table--------------------------

CREATE TABLE Furnizor(
idF INT PRIMARY KEY IDENTITY NOT NULL, 
Name VARCHAR(50),
Age int,
)

-- Third Table---------------------------

CREATE TABLE OrderShop2(
idO INT PRIMARY KEY IDENTITY NOT NULL,
idF INT FOREIGN KEY REFERENCES Furnizor(idF) NOT NULL,
idS INT FOREIGN KEY REFERENCES ShopGymM(idS) NOT NULL,
Weight INT NOT NULL
)


-- CREATING PROCEDURES TO INSERT INTO TABLES A NUMBER OF ROWS -----------------------


-- procedure to insert into the Furnizor table --------------

create procedure insertIntoFurnizor(@rows int) as
    declare @max int
    set @max = @rows*2 + 100
    while @rows > 0 begin
        insert into Furnizor values ('Dan', @max)
        set @rows = @rows-1
        set @max = @max-2
    end
execute insertIntoFurnizor 200
go

-- procedure to insert into the NutritionPlanM table --------------

create procedure insertIntoNutritionPlanM(@rows int) as
    while @rows > 0 begin
        insert into NutritionPlanM values ('Hard',@rows%870,3)
        set @rows = @rows-1
    end
execute insertIntoNutritionPlanM 100
go

-- procedure to insert into the OrderShop2 table --------------

create procedure insertIntoOrderShop2(@rows int) as
    declare @aid int
    declare @bid int
    while @rows > 0 begin
        set @aid = (select top 1 idN from NutritionPlanM order by NEWID())
        set @bid = (select top 1 idF from Furnizor order by NEWID())
        insert into OrderShop2 values  (@aid, @bid,20)
        set @rows = @rows-1
    end
execute insertIntoOrderShop2 120
go

--SELECT * FROM OrderShop2
--SELECT * FROM NutritionPlanM
--SELECT * FROM Furnizor    

--A) CREATING ALL THE OPERATIONS FOR THE TABLES


select * from Furnizor order by idF -- Clustered Index Scan
select * from Furnizor where idF = 1 -- Clustered Index Seek
select Age from Furnizor order by Age -- Nonclustered Index Scan
select Age from Furnizor where Age = 102 -- Nonclustered Index Seek
select idCo from NutritionPlanM where Duration = 100 -- Key Lookup


--B.1) CLUSTERED INDEX SCAN WITH THE WHERE CLAUSE FOR THE SECOND TABLE OF FORM b2 = value


create nonclustered index index1 on Furnizor(Age)
select * from NutritionPlanM where Duration = 100 -- Clustered Index Scan 0.003 cost
drop index index1 on Furnizor
go

--B.2) NONCLUSTERED INDEX SEEK WITH THE WHERE CLAUSE FOR THE FIRST TABLE OF FORM a1 = value


create nonclustered index index2 on NutritionPlanM(idN) include (idCO, Duration)
select * from NutritionPlanM where idN = 40 -- Nonclustered Index Seek 0.003 cost
drop index index2 on NutritionPlanM
go

--C)  CREATING A VIEW THAT JOINS 2 TABLES AND RETURNS THE FIRST TABLES AGE AND THE SECOND
--    TABLES DURATION WHERE AGE < 500 AND DURATION < 15

create view view1 as
    select F1.Age, N2.Duration
    from OrderShop2 O3 join Furnizor F1 on O3.idF = F1.idF join NutritionPlanM N2 on O3.idN = N2.idN
    where F1.Age < 500 and N2.Duration < 15
go

drop view view1

select * from view1

-- 0.24 total cost without indexes
-- 0.18 total cost with indexes

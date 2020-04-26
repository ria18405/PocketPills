create database Health;
use Health;
create table Userr
(UID int ,
UName varchar(20) NOT NULL,
Age int NOT null,
Gender char(1) NOT NULL,
Phone varchar(20) NOT NULL Unique,
EmailID varchar(100) NOT NULL UNIQUE,
StreetAdress varchar(100)not null,
city varchar(50)not null,
PostalCode varchar(20)not null,
primary key(UID),
CHECK (Gender in ('M','F','O')),
CHECK (Phone not like '%[^0-9-]%'),
check (EmailID not like '%[^A-Za-z0-9@._]%'));


create table Doctor
(DID int UNIQUE,
DName varchar(20) NOT NULL,
Age int NOT NULL,
Gender char(1)NOT NULL,
StreetAdress varchar(100) NOT NULL,
city varchar(50)NOT NULL,
PostalCode varchar(20)NOT NULL,
Phone varchar(20)NOT NULL UNIQUE,
Qualifications varchar(20)NOT NULL,
Specialization varchar(20)NOT NULL,
primary key(DID),
CHECK (Gender in ('M','F','O')),
CHECK (Phone not like '%[^0-9-]%'),
check (PostalCode not like '%[^A-Za-z0-9- ]%'));

create table Lab
(
LabID int,
LName varchar(40)NOT NULL,
Phone varchar(20)NOT NULL UNIQUE,
StreetAdress varchar(100)NOT NULL,
city varchar(50)NOT NULL,
PostalCode varchar(20)NOT NULL,
Tests varchar(100)NOT NULL,
primary key(LabID),
CHECK (Phone not like '%[^0-9-]%'),
check (PostalCode not like '%[^A-Za-z0-9- ]%'));


create table Company
( CID int,
CName varchar(40)not null,
Phone varchar(40)not null unique,
StreetAdress varchar(100)not null,
city varchar(50)not null,
PostalCode varchar(20)not null,
primary key(CID),
CHECK (Phone not like '%[^0-9-]%'),
check (PostalCode not like '%[^A-Za-z0-9- ]%'));

create table Drug
(DrID int,
DrName varchar(100) not null,
Prescription_req boolean not null,
Quantity int not null,
Sickness varchar(100)not null,
Symptoms varchar(80)not null,
CID int not null,
Price decimal(10,3) not null,
primary key (DrID),
foreign key(CID) references Company(CID) on delete cascade);

create table DeliveryAgency
(
DAID int,
DAName varchar(40)not null,
Phone varchar(20)not null unique,
StreetAdress varchar(100)not null,
city varchar(50)not null,
PostalCode varchar(20)not null,
primary key(DAID),
CHECK (Phone not like '%[^0-9-]%'),
check (PostalCode not like '%[^A-Za-z0-9- ]%'));

create table OpenSlots
(
SID int,
DID int not null,
STime time not null,
SDate date not null,
primary key(SID),
foreign key(DID) references Doctor(DID) on delete cascade);

create table Appointment
(
AID int,
SID int not null,
UID int not null,
primary key (AID),
foreign key(SID) references OpenSlots(SID),
foreign key (UID) references Userr(UID) on delete cascade);
create Table Test
(
TID int,
UID int not null,
DID int not null,
LabID int not null,
TTime time not null,
TDate date not null,
Tests varchar(50) not null,
primary key(TID),
foreign key(UID) references Userr(UID),
foreign key(DID) references Doctor(DID),
foreign key(LabID) references Lab(LabID) on delete cascade);

create table DiagnosticReports
(
DiRID int,
TID int not null,
DiRDate date not null,
Remarks varchar(30) not null,
primary key(DiRID),
foreign key(TID) references Test(TID));

create table Prescription
(
PrID int,
DrID int not null,
UID int not null,
DID int not null,
primary key(PrID),
foreign key(DrID) references Drug(DrID),
foreign key(UID) references Userr(UID) on delete cascade,
foreign key(DID) references Doctor(DID));

create table DeliveryArea
(
DeAID int,
DAID int not null,
PostalCode varchar(20) not null,
primary key(DeAID),
foreign key(DAID) references DeliveryAgency(DAID) on delete cascade,
check (PostalCode not like '%[^A-Za-z0-9- ]%'));

create table Orderr
(
OID int,
UID int not null,
DrID int not null,
OTime time not null,
ODate date not null,
StreetAdress varchar(100) not null,
city varchar(50)not null,
PostalCode varchar(20)not null,
price float(0)not null,
primary key(OID),
foreign key(UID) references Userr(UID),
foreign key(DrID) references Drug(DrID),
check (PostalCode not like '%[^A-Za-z0-9- ]%'));

create table Delivery
(
DeID int,
OID int not null,
DAID int null,
DeStatus varchar(30)not null,
ETA date not null,
primary key(DeID),
foreign key(OID) references Orderr(OID),
foreign key(DAID) references DeliveryAgency(DAID));

create table DoctorReviews
(
DReID int,
AID int not null,
Rating float(0)not null,
Review varchar(500),
primary key(DReID),
foreign key(AID) references Appointment(AID),
Check (Rating<=5 and Rating>=0));

create table DrugReviews
(
DrReID int,
OID int not null,
Rating float(0)not null,
Review varchar(500),
primary key(DrReID),
foreign key(OID) references Orderr(OID),
Check (Rating<=5 and Rating>=0));

create table DeliveryReviews
(
DeReID int,
DeID int not null,
Rating float(0)not null,
Review varchar(500),
primary key(DeReID),
foreign key(DeID) references Delivery(DeID),
Check (Rating<=5 and Rating>=0));

create table LabReviews
(
LRID int,
TID int not null,
Rating float(0)not null,
Review varchar(500),
primary key(LRID),
foreign key(TID) references Test(TID),
Check (Rating<=5 and Rating>=0));
-- drop database health;
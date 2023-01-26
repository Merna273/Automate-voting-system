Create database automated_voting_system;

use automated_voting_system;

Create table Candidate(
National_ID varchar(14) not null,
First_Name varchar(50) not null,
Middle_Name varchar(50) not null,
Last_Name varchar(50) not null,
Description varchar(200),
Vote_Count int(50) null,
Primary Key (National_ID)
);

Create table Voter(
C_National_ID varchar(14) not null,
First_Name varchar(50) not null,
Middle_Name varchar(50) not null,
Last_Name varchar(50) not null,
Address varchar(100) not null,
Birth_Date timestamp not null,
Job varchar(50) not null,
Religion varchar(50) not null,
Gender varchar(50) not null,
Family_Stand varchar(50) not null,
National_ID varchar(14) null,
Primary Key (C_National_ID),
Foreign Key (National_ID) REFERENCES Candidate (National_ID)
);

Create table Log_In(
C_National_ID varchar(14) not null,
C_Password varchar(50) not null,
Primary Key (C_National_ID),
Foreign Key (C_National_ID) REFERENCES Voter(C_National_ID)
);

Insert into Candidate VALUES 
('90019411201435', 'Menna', 'Mohamed', 'Mabrouk', 'Together to innovate', 0),
('90018573913802', 'Mostafa', 'Magdy', 'Youssed', 'Let my experience work for you', 0),
('90012122345879', 'Ahmed', 'Youssef', 'Aly', 'It is time for actions, not words', 0);

Insert into Voter (C_National_ID, First_Name, Middle_Name, Last_Name, Address, Birth_Date, Job, Religion, Gender, Family_Stand) VALUES 
    ('90017931936403', 'Youssef', 'Salem', 'Ahmed', '34 Salah Salem, Nasr City, Cairo', '2001-06-22', 'Student', 'Muslim', 'Male', 'Single'),
    ('90047265945376', 'Mennatallah', 'Ahmed', 'Ali', '130 Tahreer Street, Dokki, Giza', '2001-02-04', 'Student', 'Muslim', 'Female', 'Single'),
    ('90015648359010', 'Habiba', 'Sherif', 'Adam', 'Villa 15 Group 12, Rehab City, Cairo', '1999-08-02', 'Computer Engineer', 'Muslim', 'Female', 'Married'),
    ('90073559162057', 'John', 'Youssef', 'Andrew', '12 Tahreer Square, Downtown, Cairo', '1989-07-23', 'Business Manager', 'Christian', 'Male', 'Married'),
    ('90016845916953', 'Anne', 'Christian', 'John', 'Villa 32 Group 4, Madinaty, Cairo', '2000-12-01', 'Student', 'Christian', 'Male', 'Single'),
    ('90036582694174', 'Adam', 'Abdelrahman', 'Mohamed', '25 Al-Amal Street, Sheikh Zayed City, Giza', '1972-04-02', 'Mechanical Engineer', 'Muslim', 'Male', 'Widow'),
    ('90046182772530', 'Malak', 'Benjamin', 'Andrew', '5 Street, 6th October City, Giza', '1980-09-30', 'Accountant', 'Christian', 'Female', 'Married'),
    ('90026385991534', 'Youssef', 'Mohamed', 'Aly', '23 Talaat Harb Street, Downtown, Cairo', '2001-01-01', 'Student', 'Muslim', 'Male', 'Single'),
    ('90064736490014', 'Magdy', 'Hamed', 'Mabrouk', '65 Rod El-Farag, Shobra, Cairo', '1980-09-30', 'Doctor', 'Muslim', 'Male', 'Married'),
    ('90027453829517', 'Mostafa', 'Gamal', 'Ashraf', '67 Nuweibaa, South Sinai', '1971-05-21', 'Nurse', 'Muslim', 'Male', 'Widow'),
    ('90012345678910', 'Mariam', 'Malek', 'Adib', '10 Tahrir street, Dokki, Giza', '1999-09-6', 'lawyer', 'Muslim', 'Female','Single'),
    ('90022345678910', 'Mahmoud', 'Moustafa', 'Emam', '19 Charle de Gualle street, Giza', '1978-09-06','Doctor','Muslim','Male','Single'),
    ('90022345670987', 'Salma', 'Magdy','Mabrouk', '87 North 90 street, Cairo', '2001-02-06', 'Student', 'Muslim','Female', 'Single'),
    ('90022345678975', 'Mona', 'Amgad', 'Adam', 'Villa 276 Yasmine 5, Cairo', '1985-12-20', 'Nurse', 'Muslim', 'Female','Widow'),
    ('90022365478977', 'Youstina', 'Ashraf', 'Farid', 'Villa 66 zayed 2000, Giza', '2001-05-15','Banker','Christian','Female','Married'),
    ('90022365412400', 'Karim', 'Maurice', 'George', 'Montaza, Alex', '1974-04-30', 'Writer', 'Christian', 'Male', 'Married'),
    ('90022365412422', 'Mohamed', 'Hassan', 'Kamal', 'Gouna, Hurghada', '1993-09-13', 'Driver', 'Muslim', 'Male', 'Divorced'),
    ('90016963581075', 'Farida', 'Ibrahim', 'Hatem', '9 street, Maadi, Cairo', '1982-08-27', 'Pilot', 'Muslim', 'Female', 'Married'),
    ('90016963715269', 'Hend', 'Safy', 'Selim', 'Huda shaarawy, Zamalek, Cairo', '1985-05-11', 'Scientist', 'Muslim', 'Female', 'Widow'),
    ('90051215269266', 'Nathalie', 'Fikry', 'Youssef', 'Villa 55, 6th of october, Cairo', '1987-11-29', 'Teacher', 'Christan', 'Female', 'Single'),
    ('90022398461095', 'Samir', 'William', 'Marwan', 'Villa 29, Mansoura, Dakahlia', '2002-05-05', 'Accountant', 'Christan','Male', 'Single'),
    ('90075382072526','Habiba', 'Hamza', 'Hazem', '30 el taref, Luxor', '1978-08-04','Tour Guide', 'Muslim', 'Female', 'Married'),
    ('90097264282990','Logina', 'Ehab', 'Sameh', '65 Ahmed Oraby, Beni sueif', '1987-06-29', 'Architect', 'Muslim', 'Female', 'Single');
    
Insert into Log_In VALUES 
('90017931936403','Youssef333'),
('90047265945376','MennaAly'),
('90015648359010','bibaAdam'),
('90073559162057', 'John'),
('90016845916953','Anne99'),
('90036582694174','Adam00897'),
('90046182772530','Maloukaa'),
('90026385991534','YoussefAly122'),
('90064736490014','MabroukFam'),
('90027453829517', 'Mostafa322'),
('90012345678910', 'Marouma'),
('90022345678910','DrMahmoud'),
('90022345670987','Saloumaa'),
('90022345678975','Momona'),
('90022365478977','Yousss'),
('90022365412400', 'Karim'),
('90022365412422','Mido'),
('90016963581075', 'Fifa2022'),
('90016963715269','Hend1234'),
('90051215269266','Nathalie33353'),
('90022398461095','SWY8979'),
('90075382072526','Habiba?Q@'),
('90097264282990','Logi*()');
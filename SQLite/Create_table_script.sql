
CREATE TABLE Province (
id int,
Name varchar(255),
Country varchar(255),
PRIMARY KEY (Province_id)
)

ALTER TABLE Province 
RENAME Province_id TO id



CREATE TABLE City (
id int,
Name varchar(255),
Province_id int,
PRIMARY KEY (City_id),
FOREIGN KEY (Province_id) REFERENCES Province(Province_id)
)

ALTER TABLE City 
RENAME City_id TO id

CREATE TABLE Neigborhood (
id int,
Name varchar(255),
City_id int,
PRIMARY KEY (Neighborhood_id),
FOREIGN KEY (City_id) REFERENCES City (City_id)
)

ALTER TABLE Neigborhood 
RENAME Neighborhood_id  TO id


CREATE TABLE Building (
id int,
Name varchar(255),
Address varchar(255),
Postal Code varchar (255),
Neighborhood_id int,
PRIMARY KEY (id),
FOREIGN KEY (Neighborhood_id) REFERENCES Neighborhood (id)


)

CREATE TABLE Headquater (
CUIT INT NOT NULL,
Name varchar(255),
Building_id int,
Owner_id int,
PRIMARY KEY (CUIT)

)

DROP TABLE Headquater 

CREATE TABLE Retail (
id int,
CUIT INT,
Stockroom_id int,
Employee_id int,
PRIMARY KEY(id),
FOREIGN KEY (Stockroom_id) REFERENCES Stockroom (id)
)


CREATE TABLE Stockroom (
id int,
Stockroom_Manager_id int,
product_id int,
PRIMARY KEY (id)

)


CREATE TABLE Product (
id int,
Model varchar(255),
Type varcar (255),
Price float,
Manufacturer varchar (255),
PRIMARY KEY (id) )

CREATE TABLE Warehouse (
id INT,
Product_id int,
PRIMARY KEY (id))

DROP TABLE Stockroom 




)




CREATE TABLE Person (
DNI int,
Name varchar(255),
Last_Name varchar(255),
Telephone int,
PRIMARY KEY (DNI)
)




CREATE TABLE PROVINCE (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(255),
COUNTRY VARCHAR(255)
);

CREATE TABLE CITY (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(255),
PROVINCE_ID INT,
FOREIGN KEY (PROVINCE_ID) REFERENCES PROVINCE (ID)
);

CREATE TABLE NEIGHBORHOOD (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(255),
CITY_ID INT,
FOREIGN KEY (CITY_ID) REFERENCES City (ID)
);


CREATE TABLE BUILDING (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(255),
ADDRESS VARCHAR(255),
POSTAL_CODE VARCHAR (255),
NEIGHBORHOOD_ID INT,
FOREIGN KEY (NEIGHBORHOOD_ID) REFERENCES NEIGHBORHOOD (ID)

);


CREATE TABLE PERSON (
DNI INT,
NAME VARCHAR(255),
LAST_NAME VARCHAR(255),
TELEPHONE INT,
PRIMARY KEY (DNI)
);



CREATE TABLE OWNER (
DNI INT,
PRIMARY KEY (DNI),
FOREIGN KEY (DNI) REFERENCES PERSON (DNI)
);


CREATE TABLE HEADQUARTER (
CUIT INT,
NAME VARCHAR(255),
BUILDIND_ID INT,
OWNER_ID INT,
PRIMARY KEY (CUIT),
FOREIGN KEY (BUILDIND_ID) REFERENCES BUILDING (ID),
FOREIGN KEY (OWNER_ID) REFERENCES OWNER (ID)
);

CREATE TABLE STOCKROOM (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
STOCKROOM_MANAGER_ID INT,
FOREIGN KEY (STOCKROOM_MANAGER_ID) REFERENCES EMPLOYEE (ID)
);

CREATE TABLE RETAIL (
CUIT INT,
STOCKROOM_ID INT,
PRIMARY KEY(CUIT),
FOREIGN KEY (CUIT) REFERENCES HEADQUARTER (CUIT)
);


CREATE TABLE EMPLOYEE (
DNI INT,
HIRE_DATE TEXT,
RETAIL_ID INT,
PRIMARY KEY (DNI),
FOREIGN KEY (DNI) REFERENCES PERSON (DNI),
FOREIGN KEY (RETAIL_ID) REFERENCES RETAIL (ID)

);

CREATE TABLE PRODUCT (
SERIAL INT,
MODEL VARCHAR(255),
PRODUCT_TYPE VARCHAR (255),
PRICE FLOAT,
MANUFACTURER VARCHAR (255),
PRIMARY KEY (SERIAL) );



CREATE TABLE STOCKROOM_PRODUCT (
STOCKROOM_ID INT,
PRODUCT_ID INT,
PRIMARY KEY (STOCKROOM_ID,PRODUCT_ID),
FOREIGN KEY (STOCKROOM_ID) REFERENCES STOCKROOM (ID),
FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCT (SERIAL)
);



CREATE TABLE WAREHOUSE (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
PRODUCT_ID INT
);


CREATE TABLE WAREHOUSE_PRODUCT (
WAREHOUSE_ID INT,
PRODUCT_ID INT,
PRIMARY KEY (WAREHOUSE_ID,PRODUCT_ID),
FOREIGN KEY (WAREHOUSE_ID) REFERENCES WAREHOUSE(ID),
FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCT (SERIAL)
)







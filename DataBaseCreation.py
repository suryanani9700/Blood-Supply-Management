import sqlite3
import sys


def CreateDatabase():
    connection = sqlite3.connect('bloodbank.db')
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    table1 = """CREATE TABLE Bloodbank(
        bank_id INTEGER PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        address VARCHAR(20) NOT NULL,
        stock INTEGER NOT NULL);"""
    cursor.execute(table1)

    table2 = """CREATE TABLE Employee (
        employee_id INTEGER PRIMARY KEY,
        contact_no INTEGER,
        name VARCHAR(20) NOT NULL,
        email_address VARCHAR(20),
        login_id VARCHAR(10),
        password VARCHAR(15),
        bank_id INTEGER NOT NULL,
        FOREIGN KEY (bank_id) REFERENCES Bloodbank (bank_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE );"""
    cursor.execute(table2)

    table3 = """CREATE TABLE Medicalassistant(
    employee_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES Employee (employee_id) 
    ON UPDATE CASCADE
    ON DELETE CASCADE );"""
    cursor.execute(table3)

    table4 = """CREATE TABLE Receptionist(
    employee_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES Employee (employee_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE);"""
    cursor.execute(table4)
            
    table5 = """CREATE TABLE BBT(
    employee_id INTEGER,
    bank_id INTEGER NOT NULL,
    FOREIGN KEY (bank_id) REFERENCES Bloodbank (bank_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES Employee (employee_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE );"""
    cursor.execute(table5)
                
    table6 = """CREATE TABLE ADMIN(
    employee_id INTEGER,
    bank_id INTEGER NOT NULL,
    FOREIGN KEY (bank_id) REFERENCES Bloodbank (bank_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES Employee (employee_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE );"""
    cursor.execute(table6)

    table7 = """CREATE TABLE Donor(
    donor_id INTEGER PRIMARY KEY,
    login_id INTEGER NOT NULL,
    name VARCHAR(20),
    age INTEGER,
    blood_group VARCHAR(3),
    address VARCHAR(20),
    password VARCHAR(15)
    );"""
    cursor.execute(table7)

    table8 = """CREATE TABLE Patient(
    patient_id INTEGER PRIMARY KEY,
    login_id INTEGER NOT NULL,
    name VARCHAR(20),
    contact_no INTEGER,
    blood_group VARCHAR(3),
    address VARCHAR(20),
    password VARCHAR(15)
    );"""
    cursor.execute(table8)

    table9 = """CREATE TABLE BloodBankInventory(
    bloodtype VARCHAR(3) PRIMARY KEY,
    bank_id INTEGER PRIMARY KEY,
    volume INTEGER NOT NULL,
    FOREIGN KEY (bank_id) REFERENCES Bloodbank (bank_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    );"""
    cursor.execute(table9)

    table10 = """CREATE TABLE Donate(
    donor_id INTEGER,
    employee_id INTEGER,
    date DATE NOT NULL,
    volume INTEGER NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES Donor (donor_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES BBT (employee_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    );"""
    cursor.execute(table10)

    table11 = """CREATE TABLE Provides(
    patient_id INTEGER NOT NULL,
    bank_id INTEGER NOT NULL,
    date DATE NOT NULL,
    volume INTEGER NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patient (patient_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
    FOREIGN KEY (bank_id) REFERENCES Bloodbank (bank_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    );"""
    cursor.execute(table11)
    connection.commit()
    connection.close()

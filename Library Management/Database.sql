create database db1;

CREATE TABLE book (
    bid VARCHAR(20) PRIMARY KEY,
    title VARCHAR(30),
    author VARCHAR(30),
    status VARCHAR(30)
);

CREATE TABLE book_issued1 (
    bid VARCHAR(20) PRIMARY KEY,
    issuedto VARCHAR(30)
);
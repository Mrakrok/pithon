- create table uziv(id int primary key, login varchar(15) not null, heslo varchar(32),email varchar(40));

- create table vtip(id int primary key, id_kateg int not null, id_uziv int not null, datum date, obsah text not null);

- create table kateg(id int primary key, nazev varchar(30));
CREATE TABLE alamat (
    id_alamat    SERIAL NOT NULL,
    jalan        VARCHAR(55) NOT NULL,
    kecamatan    VARCHAR(55) NOT NULL,
    kabupaten    VARCHAR(55) NOT NULL
);


ALTER TABLE alamat ADD CONSTRAINT alamat_pk PRIMARY KEY ( id_alamat );

CREATE TABLE detail_transaksi_layanan (
    id_detail_transaksi_layanan SERIAL NOT NULL,
    id_transaksi                INTEGER NOT NULL,
    id_pc                       INTEGER NOT NULL,
    id_layanan                  INTEGER NOT NULL
);

ALTER TABLE detail_transaksi_layanan ADD CONSTRAINT detail_transaksi_layanan_pk PRIMARY KEY ( id_detail_transaksi_layanan );

CREATE TABLE detail_transaksi_produk (
    id_detail_transaksi_produk SERIAL NOT NULL,
    kuantitas                  INTEGER NOT NULL,
    id_transaksi               INTEGER NOT NULL,
    id_produk                  INTEGER NOT NULL
);

ALTER TABLE detail_transaksi_produk ADD CONSTRAINT detail_transaksi_produk_pk PRIMARY KEY ( id_detail_transaksi_produk );

CREATE TABLE jenis_produk (
    id_jenis_produk   SERIAL NOT NULL,
    nama_jenis_produk VARCHAR(55) NOT NULL
);

ALTER TABLE jenis_produk ADD CONSTRAINT jenis_produk_pk PRIMARY KEY ( id_jenis_produk );


ALTER TABLE jenis_produk ADD CONSTRAINT jenis_produk_nama_jenis_produk_un UNIQUE ( nama_jenis_produk );

CREATE TABLE layanan (
    id_layanan   SERIAL NOT NULL,
    nama_layanan VARCHAR(35) NOT NULL,
    harga        INTEGER NOT NULL
);

ALTER TABLE layanan ADD CONSTRAINT layanan_pk PRIMARY KEY ( id_layanan );

ALTER TABLE layanan ADD CONSTRAINT layanan_nama_layanan_un UNIQUE ( nama_layanan );

CREATE TABLE metode_pembayaran (
    id_metode_pembayaran   SERIAL NOT NULL,
    nama_metode_pembayaran VARCHAR(22) NOT NULL
);

ALTER TABLE metode_pembayaran ADD CONSTRAINT metode_pembayaran_pk PRIMARY KEY ( id_metode_pembayaran );


ALTER TABLE metode_pembayaran ADD CONSTRAINT nama_metode_pembayaran_unique UNIQUE ( nama_metode_pembayaran );

CREATE TABLE pc (
    id_pc        SERIAL NOT NULL,
    nama_pc      VARCHAR(55) NOT NULL,
    id_pelanggan INTEGER NOT NULL
);

ALTER TABLE pc ADD CONSTRAINT pc_pk PRIMARY KEY ( id_pc );

CREATE TABLE pelanggan (
    id_pelanggan   SERIAL NOT NULL,
    nama_pelanggan VARCHAR(55) NOT NULL,
    no_telp        VARCHAR(15) NOT NULL,
    id_alamat      INTEGER NOT NULL
);

CREATE UNIQUE INDEX pelanggan__idx ON
    pelanggan (
        id_alamat
    ASC );

ALTER TABLE pelanggan ADD CONSTRAINT pelanggan_pk PRIMARY KEY ( id_pelanggan );

ALTER TABLE pelanggan ADD CONSTRAINT pelanggan_no_telp_un UNIQUE ( no_telp );

CREATE TABLE pengguna (
    id_pengguna   SERIAL NOT NULL,
    username      VARCHAR(22) NOT NULL,
    nama_pengguna VARCHAR(55) NOT NULL,
    password      VARCHAR(30) NOT NULL,
    id_role       INTEGER NOT NULL
);

ALTER TABLE pengguna ADD CONSTRAINT pengguna_pk PRIMARY KEY ( id_pengguna );

ALTER TABLE pengguna ADD CONSTRAINT pengguna_username_un UNIQUE ( username );

CREATE TABLE produk (
    id_produk       SERIAL NOT NULL,
    nama_produk     VARCHAR(55) NOT NULL,
    harga           INTEGER NOT NULL,
    id_jenis_produk INTEGER NOT NULL
);

ALTER TABLE produk ADD CONSTRAINT produk_pk PRIMARY KEY ( id_produk );

ALTER TABLE produk ADD CONSTRAINT produk_nama_produk_un UNIQUE ( nama_produk );

CREATE TABLE role (
    id_role   SERIAL NOT NULL,
    nama_role VARCHAR(15) NOT NULL
);

ALTER TABLE role ADD CONSTRAINT role_pk PRIMARY KEY ( id_role );

ALTER TABLE role ADD CONSTRAINT role_nama_role_un UNIQUE ( nama_role );

CREATE TABLE transaksi (
    id_transaksi         SERIAL NOT NULL,
    keterangan           TEXT,
    tgl_dibuat           DATE NOT NULL,
    id_pengguna          INTEGER NOT NULL,
    id_pelanggan         INTEGER NOT NULL,
    id_metode_pembayaran INTEGER NOT NULL
);

ALTER TABLE transaksi ADD CONSTRAINT transaksi_pk PRIMARY KEY ( id_transaksi );

ALTER TABLE detail_transaksi_layanan
    ADD CONSTRAINT detail_transaksi_layanan_fk1 FOREIGN KEY ( id_layanan )
        REFERENCES layanan ( id_layanan );

ALTER TABLE detail_transaksi_layanan
    ADD CONSTRAINT detail_transaksi_layanan_pc_fk FOREIGN KEY ( id_pc )
        REFERENCES pc ( id_pc );

ALTER TABLE detail_transaksi_layanan
    ADD CONSTRAINT detail_transaksi_layanan_fk2 FOREIGN KEY ( id_transaksi )
        REFERENCES transaksi ( id_transaksi );

ALTER TABLE detail_transaksi_produk
    ADD CONSTRAINT detail_transaksi_produk_fk1 FOREIGN KEY ( id_produk )
        REFERENCES produk ( id_produk );

ALTER TABLE detail_transaksi_produk
    ADD CONSTRAINT detail_transaksi_produk_fk2 FOREIGN KEY ( id_transaksi )
        REFERENCES transaksi ( id_transaksi );

ALTER TABLE pc
    ADD CONSTRAINT pc_pelanggan_fk FOREIGN KEY ( id_pelanggan )
        REFERENCES pelanggan ( id_pelanggan );

ALTER TABLE pelanggan
    ADD CONSTRAINT pelanggan_alamat_fk FOREIGN KEY ( id_alamat )
        REFERENCES alamat ( id_alamat );

ALTER TABLE pengguna
    ADD CONSTRAINT pengguna_role_fk FOREIGN KEY ( id_role )
        REFERENCES role ( id_role );

ALTER TABLE produk
    ADD CONSTRAINT produk_jenis_produk_fk FOREIGN KEY ( id_jenis_produk )
        REFERENCES jenis_produk ( id_jenis_produk );

ALTER TABLE transaksi
    ADD CONSTRAINT transaksi_metode_pembayaran_fk FOREIGN KEY ( id_metode_pembayaran )
        REFERENCES metode_pembayaran ( id_metode_pembayaran );

ALTER TABLE transaksi
    ADD CONSTRAINT transaksi_pelanggan_fk FOREIGN KEY ( id_pelanggan )
        REFERENCES pelanggan ( id_pelanggan );

ALTER TABLE transaksi
    ADD CONSTRAINT transaksi_pengguna_fk FOREIGN KEY ( id_pengguna )
        REFERENCES pengguna ( id_pengguna );
		
insert into role (nama_role) 
values 
('owner'),('teknisi');


insert into pengguna (username,nama_pengguna,password,id_role)
values
	('Almashuda34','Huda','huda34678',1),
	('Asnur34','Nur','nur345676',2),
	('Widy4aa','Widya','Widya34678',2),
	('NazrilCoi12','Nazril','nazril123',2),
	('Fauzann123','Fauzan','Fauzan123',2)
	;


insert into alamat (jalan, kecamatan, kabupaten)
values
    ( 'Jl. Merdeka No. 123', 'Wuluhan', 'Jember'),
    ( 'Jl. Pahlawan No. 456', 'Ambulu', 'Jember'),
    ( 'Jl. Sudirman No. 789', 'Puger', 'Jember'),
    ( 'Jl. Pahlawan No. 456', 'Wuluhan', 'Jember'),
    ( 'Jl. Pahlawan No. 456', 'Ambulu', 'Jember');


insert into pelanggan (nama_pelanggan, no_telp, id_alamat)
values
    ('Widya','085230369011',1),
    ('Jhonson','085230369015',2),
    ('Rendy','085230369014',3),
    ('Thoriq','085230369013',4),
    ('Rafky','085230369012',5);


insert into pc (nama_pc, id_pelanggan)
values 
	('Asus X441UV',1),
	('Asus ROG ',2),
	('Acer Nitro ',2),
	('Acer Nitro gaming 8/512',4),
	('Acer ROG gaming 12',4);

insert into jenis_produk (nama_jenis_produk)
values
	('GPU'),
	('RAM'),
	('CPU'),
	('Cooler'),
	('PSU');

insert into produk (nama_produk, harga, id_jenis_produk)
values
	(' Asus Rog Strix Nvidia RTX 3060 TI',16000000,1),
	('Intel i3 1200f',1200000,3),
	('Amd Ryzen 5 5600G',120000,3),
	('cooler master fan 12x12',750000,4),
	('Corsair 2x8GB DDR4',1000000,2);

insert into layanan (nama_layanan, harga)
values 
	('Install ulang Windwos',750000),
	('Repasta',75000),
	('Storage Recovery',250000),
	('Hapus Password Windows',150000),
	('Install Aplikasi',10000);


insert into metode_pembayaran (nama_metode_pembayaran) 
values 
	('Cash'),
	('Debit');


insert into transaksi (keterangan, tgl_dibuat, id_pengguna,id_pelanggan, id_metode_pembayaran)
values 
	('','2024-1-2',1,1,1),
	('','2024-1-3',1,3,1),
	('','2024-1-5',2,2,2),
	('','2024-1-6',3,5,1),
	('','2024-1-6',1,1,2);
	

insert into detail_transaksi_layanan (id_transaksi,id_pc,id_layanan)
values
	(1,1,1),
	(2,2,2);

insert into detail_transaksi_produk (kuantitas, id_transaksi, id_produk)
values
	(1,1,1),
	(2,4,2),
	(2,3,2);

		

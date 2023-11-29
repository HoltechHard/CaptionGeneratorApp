-- Database: db_caption

-- DROP DATABASE IF EXISTS db_caption;

CREATE DATABASE db_caption
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
-- Table: public.ImageData

-- DROP TABLE IF EXISTS public."ImageData";

CREATE TABLE IF NOT EXISTS public."ImageData"
(
    id_image bigint NOT NULL,
    create_time date,
    description character varying(400) COLLATE pg_catalog."default" DEFAULT NULL::character varying,
    file_path character varying(255) COLLATE pg_catalog."default" DEFAULT NULL::character varying,
    CONSTRAINT "ImageData_pkey" PRIMARY KEY (id_image)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."ImageData"
    OWNER to postgres;
	
CREATE SEQUENCE public."ImageData_id_image_seq"
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807 -- This is the max value for a bigint
    CACHE 1;	

ALTER TABLE public."ImageData"
    ALTER COLUMN id_image SET DEFAULT nextval('public."ImageData_id_image_seq"'::regclass);


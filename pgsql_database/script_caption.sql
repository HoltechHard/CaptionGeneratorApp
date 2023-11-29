-- script for db_caption 

select * from "public"."ImageData";

insert into "public"."ImageData"(create_time, description, file_path)
values(now()::date, 'the image', '/static/image.jpg');

delete from "public"."ImageData"

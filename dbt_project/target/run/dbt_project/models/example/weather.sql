
  
    

  create  table "mydatabase"."public"."weather__dbt_tmp"
  as (
    

select *
from "mydatabase"."public"."weather_data"
  );
  
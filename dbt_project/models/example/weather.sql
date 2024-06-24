{{ config(
    materialized='table'
) }}

select *
from {{ source('my_database', 'weather_data') }}

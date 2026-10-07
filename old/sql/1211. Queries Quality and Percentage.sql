select query_name, round(avg(rating::float/position::float)::numeric, 2) as quality, round((sum((rating<3)::int)::float / count(*) * 100)::numeric, 2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name
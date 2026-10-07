select  r.contest_id, ROUND(((count(distinct r.user_id)::float / (select count(distinct user_id) from Users)::float) * 100)::numeric, 2) as percentage 
from Users u join Register r
on u.user_id = r.user_id
group by r.contest_id 
order by percentage desc, r.contest_id ASC
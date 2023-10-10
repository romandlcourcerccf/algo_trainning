# Write your MySQL query statement below
-- select w1.id from Weather as w1
-- where w1.temperature > (select temperature from Weather where recordDate = w1.recordDate-1)


select w1.id
from Weather w1, Weather w2
where w1.temperature > w2.temperature  and DATEDIFF( w1.recordDate, w2.recordDate) = 1

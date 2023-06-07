-- https://leetcode.com/problems/rising-temperature
-- concepts: join, left join, self join, date comparision, date_add
-- runtime: 81.8%
select
  w.id as "Id"
from
  Weather w
  left join 
    Weather w_yes
    on 
      w.recordDate = DATE_ADD(w_yes.recordDate, Interval 1 day)
where 
  w.temperature > w_yes.temperature
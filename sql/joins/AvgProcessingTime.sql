-- problem: https://leetcode.com/problems/average-time-of-process-per-machine
-- concepts: joins, inner join, same table join, aggregation, group by, average - avg, ROUND
-- runtime: 14.9%
-- todo: improve performance

select 
  a_start.machine_id as machine_id,
  ROUND(AVG(a_end.timestamp - a_start.timestamp), 3) as processing_time
from Activity a_start
  inner join 
    Activity a_end
    on 
      a_start.machine_id = a_end.machine_id
      and 
      a_start.process_id = a_end.process_id
      and 
      a_start.activity_type = 'start' and a_end.activity_type = 'end'
group by 
  a_start.machine_id;
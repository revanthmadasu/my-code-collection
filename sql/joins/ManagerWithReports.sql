-- Problem: https://leetcode.com/problems/managers-with-at-least-5-direct-reports
-- Concepts: Join, inner sql query, group by, count
-- runtime: 34.92%
select E2.name
from
(select managerId, count(managerId) as reports_count
from Employee
where managerId is not null
group by managerId) MR
left join
  Employee E2
  on
    E2.id = MR.managerId
where 
  MR.reports_count >= 5
  and
  E2.name is not null;
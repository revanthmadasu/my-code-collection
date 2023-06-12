-- problem: https://leetcode.com/problems/employee-bonus
-- concepts: join, null comparision
-- runtime: 5.29%
-- todo: improve performance
select 
    E.name as name,
    B.bonus as bonus
from 
    Employee E
    left join
        Bonus B
        on 
            E.empId = B.empId
where
    B.bonus < 1000 or B.bonus is null;
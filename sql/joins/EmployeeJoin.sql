-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier
-- concepts: left outer join
  select unique_id, name
  from 
    Employees E
    left join 
      EmployeeUNI EU
    on
    E.id = EU.id;
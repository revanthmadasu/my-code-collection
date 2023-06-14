-- problem: https://leetcode.com/problems/students-and-examinations
-- concepts: cross join, left join, aggregation, count
-- runtime: 23.2%

select 
    STU.student_id,
    STU.student_name,
    SUB.subject_name,
    count(EX.subject_name) AS attended_exams
from 
    Students STU
    cross join
        Subjects SUB
    left join
        Examinations EX
        on 
            EX.student_id = STU.student_id and EX.subject_name = SUB.subject_name
group by STU.student_id, EX.subject_name, SUB.subject_name
order by 
    STU.student_id,
    SUB.subject_name;
    
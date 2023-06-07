-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
-- Concepts: Left Join, Group by, count
select 
  customer_id, count(customer_id) as count_no_trans
from 
  Visits V
  left join
    Transactions T
    on
      V.visit_id = T.visit_id
where 
  transaction_id is null
group by 
  customer_id;
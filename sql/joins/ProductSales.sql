-- https://leetcode.com/problems/product-sales-analysis-i/
-- Concepts: left join
  select 
    product_name, year, price
  from 
    Sales S
    left join
      Product P
      on
        S.product_id = P.product_id
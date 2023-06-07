-- https://leetcode.com/problems/article-views-i
-- concepts: distinct, order by, select

    select distinct author_id as id
    from Views
    where author_id = viewer_id
    order by author_id;
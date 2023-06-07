-- https://leetcode.com/problems/invalid-tweets/
-- concepts: length, select

    select tweet_id 
    from Tweets
    where length(content) > 15;
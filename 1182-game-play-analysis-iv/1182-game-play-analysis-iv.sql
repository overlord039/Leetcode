# Write your MySQL query statement below
select round(count(a1.player_id)/(select count(distinct player_id) from activity),2) as fraction
from activity a1 
join (select player_id,min(event_date) as first_login from activity group by player_id) a2 
on a1.player_id=a2.player_id and datediff(a1.event_date,a2.first_login)=1

# Write your MySQL query statement below
select s.student_id,s.student_name,st.subject_name,count(e.subject_name) as attended_exams from Students s  cross join Subjects st left join Examinations e on s.student_id=e.student_id and e.subject_name=st.subject_name 
group by s.student_id,s.student_name,st.subject_name
order by s.student_id,s.student_name
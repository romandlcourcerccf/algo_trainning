select st.student_id, st.student_name 
from Students st 
join  Examinations ex
  on st.student_id = ex.student_id
join Subjects sb
  on ex.subject_name = sb.subject_name



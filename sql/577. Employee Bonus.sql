select emp.name, bon.bonus from 
Employee  emp left join Bonus  bon
on emp.empId = bon.empId
where bon.bonus < 1000 or bon.bonus is null

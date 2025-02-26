# Write your MySQL query statement below
#pour chaque département, récupérer le max salaris

SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM Employee e
INNER JOIN DepartmenT d ON e.departmentId = d.id
WHERE e.salary = (SELECT MAX(salary)    #We will only show if it's the best salary from its own department
                  FROM Employee
                  WHERE departmentId = d.id);
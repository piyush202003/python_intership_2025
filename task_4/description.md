# 1. Create a class 'Student' with attributes name, roll_no, marks.
* Created a class Students and declared the variables name, roll_no, marks as private.
* Due the variables are private it can only be used in the declared class. Hence, printed this variable using funtion student in same class

# 2. Implement encapsulation using private variables.
* For encapsulation we can execute it by declaring the variables as private.
* Hence, created the class Subject and declared 5 variable as private which can't be used outside of the class.

# 3. Create inheritance using a class 'GraduateStudent'.
* Here, first declared the class StudentList in which created the database containting the list of students which are graduated or not.
* Then, created GraduateStudent class and inherited data from StudentList and printed it.

# 4. Write a decorator to measure execution time of a function.
* In this i first created function named measure_time which have *args and **kwargs which helps as to take any no. of parameters as input
* then used time library to start the timer then excurte the function which we want to check the time then again use time library to check time and subtract the those time to get time required for the function.
* @measure_time it is like greet = measure_time(greet)

# 5. Create a generator that generates even numbers up to 50.
* Generator is like a system which can be executed using the yield.
* It is like if the function contain 'yield' then it does not executes the entire code at the same time. But executed it one by one.
* Like if yield is present in the for loop of 1-10 then it will first return 1 then it will stop.
* When we again executes the funtion then that funtion will strat from where it stop last time hence this time it will return 2 and will stop and remembers the status.

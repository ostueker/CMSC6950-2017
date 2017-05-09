#!/bin/bash              
# Commands are in /bin/bash


echo "Factorial part ................"

getfactorial(){
counter=$1                                     # Get the factorial of the input ($1)
factorial=1                                    # Initialize factorial
while [ $counter -gt 0 ]                       # While counter > 0    
do
   factorial=$(( $factorial * $counter ))      
   counter=$(( $counter - 1 ))
done
echo $factorial
}

getfactorial 4


# ====================================

echo "Simple for loop ................"

forloop(){
for i in {0..4}
do
echo $i
done
}

forloop


# ====================================

echo "For loop with var ................"

forloopvar(){
echo " $$ — PID number (\$$)"
echo " $? — exit status of last command (\$?)"
echo " $# — number of options/arguments (\$#)"
echo " $0, $1, $2, $3  — name of calling program, its arguments (\$0, \$1...\$n)"
echo " $*, $@ — list of all arguments (man bash for details) ( \$*, \$@)"
for i in `seq $1 $2 $3`
do
echo $i
done
}

forloopvar 1 2 9


# ====================================

echo "If statement ................"



Noofarguments(){
if [ "$#" -eq "3" ]
then
echo correct
else
echo wrong
fi
}

Noofarguments 2 4 2


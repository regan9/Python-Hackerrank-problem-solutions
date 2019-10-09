def is_leap(year):
    leap = False
    a=True
    if(year%4==0 and( year%100!=0 or year%400==0)):
        return a
    return leap
    

year = int(input())

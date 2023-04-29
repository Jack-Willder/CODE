# Program using while loop

first = 0
second = 1
nextterm = 0
print "Enter the number of terms : "
n = gets.chomp.to_i
if (n > 100)
    puts "Can't calculate series is too Big;"
elsif (n < 1)
    puts "Can't calculate series is too Small;"
else
    c = 1
    puts "The first #{n} terms of Fibonacci series are : "
    n = n + 1
    while (c <= n)
        if (c <= 1)
            nextterm = 1
        else 
            puts nextterm 
            nextterm = first + second 
            first = second
            second = nextterm
        end
        c += 1
    end
end

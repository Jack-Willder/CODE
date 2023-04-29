a = 0
b = 1
print "Enter the Limit : "
limit = gets.chomp.to_i
while b < limit
    puts b
    a = b
    b = a + b
end

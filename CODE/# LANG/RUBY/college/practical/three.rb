i = 30
while (i < 50)
	puts "Value of i is #{i}"
	i += 1
	redo if i == 50
end
retry_again = 1
for i in 1..5
	begin
		puts "i = #{i}"
		raise if i >= 3
	rescue
	retry if (retry_again += 1) < 5
	end
end

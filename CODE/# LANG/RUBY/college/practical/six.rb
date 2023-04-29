module MyAdd
	def MyAdd.addition(x, y)
		z = x + y
		return z
	end
end

a = 10
b = 11
c = MyAdd.addition(a, b)
puts "Result #{c}"

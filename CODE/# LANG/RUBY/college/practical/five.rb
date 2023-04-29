class States
	@@noofstates = 0
	def initialize(name)
		@statesname=name
		@@noofstates+=1
	end
	def display()
		puts "state name #{@statesname}"
	end
	def totalno()
		puts "Total #@@noofstates"
	end
end
first=States.new("Assam")
first.totalno()


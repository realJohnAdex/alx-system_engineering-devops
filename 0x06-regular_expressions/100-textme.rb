#!/usr/bin/env ruby
# Define a regex pattern to match the required information
pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

# Iterate through command-line arguments
ARGV.each do |arg|
  # Find matches in the argument
  match_data = arg.match(pattern)
  
  # Extract sender, receiver, and flags if match is found
  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]
    puts "#{sender},#{receiver},#{flags}"
  end
end

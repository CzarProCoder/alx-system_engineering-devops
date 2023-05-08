#!/usr/bin/env ruby
# Script to output [sender],[receiver],[flags] from Logfile

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")

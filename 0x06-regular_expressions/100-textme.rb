#!/usr/bin/env ruby
# Script to output [sender],[receiver],[flags] from Logfile

puts ARGV[0].scan(/\[from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/).join(",")

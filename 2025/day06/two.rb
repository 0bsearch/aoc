data = File.readlines(
  File.expand_path("../../../data/2025/day06/#{ARGV[-1]}", __FILE__),
  chomp: true
)

require 'debug'

def naive(data)
  ops = data
    .pop
    .split
    .map!(&:to_sym)
  tasks = data
    .map { |s| s.split('') }
    .transpose
    .map!(&:join)
    .map!(&:strip)
    .slice_after("")
  total = 0
  tasks.zip(ops).each do |task, op|
    total += task
      .reject(&:empty?)
      .map(&:to_i)
      .reduce(op)

  end
  return total
end


# 12608160008022
puts naive(data)

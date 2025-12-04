require 'debug'

data = File.readlines(
  File.expand_path("../../../data/2015/day02/#{ARGV[-1]}", __FILE__)
)
  .map!(&:strip)
  .map!{ |e| e.split('x').map!(&:to_i) }

def naive(dimensions)
  total = 0
  dimensions.each do |(a, b, c)|
    sides = [a*b, b*c, c*a]
    total += 2 * sides.sum + sides.min
  end

  return total
end

# 1598415
puts naive(data)

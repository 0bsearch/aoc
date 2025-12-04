data = File.readlines(
  File.expand_path("../../../data/2015/day02/#{ARGV[-1]}", __FILE__)
)
  .map!(&:strip)
  .map!{ |e| e.split('x').map!(&:to_i) }

def naive(dimensions)
  dimensions.sum { |d| 2 * d.min(2).sum + d.inject(&:*) }
end

# 3812909
puts naive(data)

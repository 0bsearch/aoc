data = File.readlines(
  File.expand_path("../../../data/2025/day06/#{ARGV[-1]}", __FILE__)
).map! { |s| s.split.map!(&:strip) }

def naive(data)
  tasks = data.transpose
  total = 0
  tasks.each do |ary|
    op = ary.pop.to_sym
    total += ary.map(&:to_i).reduce(&op)
  end
  return total
end


# 6209956042374
puts naive(data)

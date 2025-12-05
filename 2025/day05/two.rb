data = File.readlines(
  File.expand_path("../../../data/2025/day05/#{ARGV[-1]}", __FILE__)
).map!(&:strip)

ranges = data.take_while { |e| e != '' }
ranges
  .map! { |s| s.split('-').map!(&:to_i) }
  .sort!

def naive(ranges)
  total = 0
  agg_start = ranges.first.first
  agg_end = ranges.first.last
  ranges.each do |(s,e)|
    if s > agg_end
      total += agg_end - agg_start + 1
      agg_start = s
      agg_end = e
    elsif e > agg_end
      agg_end = e
    end
  end
  total += agg_end - agg_start + 1
  return total
end


# 344423158480189
puts naive(ranges)

data = File.readlines(
  File.expand_path("../../../data/2025/day05/#{ARGV[-1]}", __FILE__)
).map!(&:strip)

ranges, values = data.slice_after("").to_a

values.map!(&:to_i)

ranges.pop
ranges
  .map! { |s| s.split('-').map!(&:to_i) }
  .sort_by! { |(a, b)| [a, -b] }


def naive(ranges, values)
  fresh = 0
  values.each do |v|
    ranges.each do |(low, high)|
      if v > high
        next
      elsif v < low
        break
      else
        fresh += 1
        break
      end
    end
  end
  return fresh
end


puts naive(ranges, values)

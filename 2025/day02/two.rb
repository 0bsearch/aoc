require 'debug'

data = File.readlines(
  File.expand_path("../../../data/2025/day02/#{ARGV[-1]}", __FILE__),
  sep=',',
)
  .map! { |s| Range.new(*s.split('-').map!(&:to_i)) }

def count_jigajolts(ranges)
  sum = 0
  ranges.each do |range|
    range.each do |number|
      s = number.to_s
      len = s.length
      (1..len/2).each do |width|
        if len % width != 0
          next
        end
        if s[0, width] * (len / width) == s
          sum += number
          break
        end
      end
    end
  end
  return sum
end


puts count_jigajolts(data)
# 33986149340
# 4174379265

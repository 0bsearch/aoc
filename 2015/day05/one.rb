data = File.readlines(
  File.expand_path("../../../data/2015/day05/#{ARGV[-1]}", __FILE__)
).map!(&:strip)


def regex(strings)
  strings.count do |s|
    s.match? /[aeiou].*[aeiou].*[aeiou]/ and
    s.match? /(.)\1/ and
    !s.match? /ab|cd|pq|xy/
  end
end


# 238
puts regex(data)

data = File.readlines(
  File.expand_path("../../../data/2015/day05/#{ARGV[-1]}", __FILE__)
).map!(&:strip)


def regex(strings)
  strings.count do |s|
    s.match? /(.)(.).*\1\2/ and
    s.match? /(.).\1/
  end
end


# 69
puts regex(data)

data = File.readlines(
  File.expand_path("../../../data/2015/day08/#{ARGV[-1]}", __FILE__),
  chomp: true,
)


def regex(lines)
  encoded = 0
  original = 0
  lines.each do |line|
    original += line.size
    encoded += line.inspect.size
  end
  return encoded, original, encoded - original
end


# 2074
puts regex(data)

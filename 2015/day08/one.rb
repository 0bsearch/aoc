data = File.readlines(
  File.expand_path("../../../data/2015/day08/#{ARGV[-1]}", __FILE__),
  chomp: true,
)


def regex(lines)
  code = 0
  memory = 0
  lines.each do |line|
    puts line
    code += line.size
    memory += line
      .gsub(/^"|"$/, '')
      .gsub(/(\\\\)/, '_')
      .gsub(/\\\"/, '_')
      .gsub(/\\x../, '_')
      .tap { |s| puts s }
      .size
    puts
  end
  return code, memory, code-memory
end


# 1342
puts regex(data)

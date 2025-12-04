data = File.read(
  File.expand_path("../../../data/2015/day03/#{ARGV[-1]}", __FILE__)
).strip!


def naive(commands)
  d = {
    '>' => [  1,  0],
    'v' => [  0, -1],
    '<' => [ -1,  0],
    '^' => [  0,  1]
  }
  visited = Hash.new { Set.new }
  x = 0
  y = 0
  visited[y] = visited[y].add(x)
  commands.each_char do |c|
    dx, dy = d[c]
    x += dx
    y += dy
    visited[y] = visited[y].add(x)
  end

  return visited.values.sum { |s| s.size }
end
    

# 2572
puts naive(data)


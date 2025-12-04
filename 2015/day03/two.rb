data = File.read(
  File.expand_path("../../../data/2015/day03/#{ARGV[-1]}", __FILE__)
).strip!


Vec2 = Struct.new(:x, :y)
def naive(commands)
  d = {
    '>' => Vec2.new(  1,  0),
    'v' => Vec2.new(  0, -1),
    '<' => Vec2.new( -1,  0),
    '^' => Vec2.new(  0,  1),
  }
  santa = Vec2.new(0, 0)
  robot = Vec2.new(0, 0)
  map = Hash.new { Set.new }
  visitors = [santa, robot].cycle
  map[0] = map[0].add(0)

  commands.each_char do |c|
    visitor = visitors.next
    visitor.x += d[c].x
    visitor.y += d[c].y
    map[visitor.y] = map[visitor.y].add(visitor.x)
  end

  return map.values.sum { |s| s.size }
end
    

# 2631
puts naive(data)


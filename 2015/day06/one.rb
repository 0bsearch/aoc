require 'matrix'


data = File.readlines(
  File.expand_path("../../../data/2015/day06/#{ARGV[-1]}", __FILE__)
)
  .map! {|s| s.match(/(\D+) (\d+),(\d+) through (\d+),(\d+)/) }
  .map! {|m| [m.captures[0], m.captures[1..].map(&:to_i)] }


def naive(data)
  m = Matrix.zero(1000, 1000)
  ops = {
    'turn on'  => Proc.new {|x| 1},
    'turn off' => Proc.new {|x| 0},
    'toggle'   => Proc.new {|x| x ^ 1},
  }

  data.each do |(instruction, (x1, y1, x2, y2))|
    (y1..y2).each do |y|
      (x1..x2).each do |x|
        m[y,x] = ops[instruction].call(m[y,x])
      end
    end
  end
  return m.sum
end


# 400410
puts naive(data)


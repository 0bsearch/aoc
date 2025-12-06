require 'matrix'


data = File.readlines(
  File.expand_path("../../../data/2015/day06/#{ARGV[-1]}", __FILE__)
)
  .map! {|s| s.match(/(\D+) (\d+),(\d+) through (\d+),(\d+)/) }
  .map! {|m| [m.captures[0], m.captures[1..].map(&:to_i)] }


def naive(data)
  m = Matrix.zero(1000, 1000)
  ops = {
    'turn on'  => Proc.new {|x| x + 1 },
    'turn off' => Proc.new {|x| [x - 1, 0].max },
    'toggle'   => Proc.new {|x| x + 2},
  }

  data.each do |(instruction, (x1, y1, x2, y2))|
    (y1..y2).each do |y|
      (x1..x2).each do |x|
        case instruction
        when 'turn on'
          m[y,x] += 1
        when 'turn off'
          if m[y,x] > 0
            m[y,x] -= 1
          end
        when 'toggle'
          m[y,x] += 2
        end
      end
    end
  end
  return m.sum
end


def colwise(data)
  ops = {
    'turn on'  => Proc.new {|x| x + 1 },
    'turn off' => Proc.new {|x| [x - 1, 0].max },
    'toggle'   => Proc.new {|x| x + 2},
  }
  total = 0
  (0..999).each do |row_i|
    row = Array.new(1000, 0)
    data.each do |(instruction, (x1, y1, x2, y2))|
      next if row_i < y1 or row_i > y2
      op = ops[instruction]
      row[x1..x2] = row[x1..x2].map(&op)
    end
    total += row.sum
  end
  return total
end


# 15343601
# puts naive(data)
puts colwise(data)


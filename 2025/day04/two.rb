# data: 138x138
# ideas:
#   - day1 + loop
#     - convolute 2D with 3x3 kernel
#     - elementwise slide & add 8 times
#     - convolute 2x1D with 1x3 > 3x1
#   - permutate coords, use as queue, append kerner coords on deletion
require 'debug'
require 'matrix'

data = File.readlines(
  File.expand_path("../../../data/2025/day04/#{ARGV[-1]}", __FILE__)
).map(&:strip)

WIDTH = data.first.length
HEIGHT = data.length


def naive_convo_2D(data)
  total = 0
  rolls = Matrix.zero(HEIGHT+2, WIDTH+2)
  data.each.with_index(1) do |row, y|
    row.each_char.with_index(1) do |value, x|
      rolls[y, x] = value == '@' ? 1 : 0
    end
  end
  kernel = [[-1, -1], [-1,  0], [-1, +1],
            [ 0, -1],           [ 0, +1],
            [+1, -1], [+1,  0], [+1, +1]]
  
  loop do
    removed = 0
    (1..HEIGHT).each do |y|
      (1..WIDTH).each do |x|
        if rolls[y,x] != 1
            next
        end
        neighbours = kernel.inject(0) { |m, (dy, dx)| m + rolls[y+dy, x+dx] }
        if neighbours < 4
          rolls[y,x] = 0
          removed += 1
        end
      end
    end
    total += removed
    if removed == 0
      break
    end
  end
  
  return total
end


# 8713
puts naive_convo_2D(data)

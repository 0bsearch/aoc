# data: 138x138
# ideas:
#   - convolute 2D with 3x3 kernel
#   - elementwise slide & add 8 times
#   - convolute 2x1D with 1x3 > 3x1
require 'debug'
require 'matrix'

data = File.readlines(
  File.expand_path("../../../data/2025/day04/#{ARGV[-1]}", __FILE__)
).map(&:strip)

WIDTH = data.first.length
HEIGHT = data.length


def convo_2D(data)
  accessible = 0
  rolls = Matrix.zero(HEIGHT+2, WIDTH+2)
  data.each.with_index(1) do |row, y|
    row.each_char.with_index(1) do |value, x|
      rolls[y, x] = value == '@' ? 1 : 0
    end
  end
  kernel = [[-1, -1], [-1,  0], [-1, +1],
            [ 0, -1],           [ 0, +1],
            [+1, -1], [+1,  0], [+1, +1]]

  (1..HEIGHT).each do |y|
    (1..WIDTH).each do |x|
      if rolls[y,x] != 1
          next
      end
      neighbours = kernel.inject(0) { |m, (dy, dx)| m + rolls[y+dy, x+dx] }
      if neighbours < 4
        accessible += 1
      end
    end
  end
  
  return accessible
end


# 1356
puts convo_2D(data)

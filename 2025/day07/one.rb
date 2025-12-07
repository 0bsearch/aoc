# data:
#   - splitters # is "monotonic"
#   - no splitters at the edge => we can be sloppy with boundaries
#   - no splittes at the bottom
#   - single starting point


data = File.readlines(
  File.expand_path("../../../data/2025/day07/#{ARGV[-1]}", __FILE__),
  chomp: true
)
WIDTH = data[0].size
HEIGHT = data.size

def naive(field)
  splits = 0
  field[1] = field[0].tr('S', '|')
  
  (2..HEIGHT-1).each do |row|
    (1..WIDTH-1).each do |col|
      current = field[row][col]
      above = field[row-1][col]
      if above == '|'
        if current == '.'
          field[row][col] = above
        elsif current == '^' and above = '|'
          field[row][col-1] = above
          field[row][col+1] = above
          splits += 1
        end
      end
    end
  end

  puts field
  return splits
end


# 1504
puts naive(data)

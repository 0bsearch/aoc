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

def naive(data)
  splits = 0
  field = data
    .map { |s| s.split('') }
  field.each do |a|
    a.map! do |s|
      case s
      when 'S' then 1
      when '.' then 0
      else s
      end
    end
  end
  (1..HEIGHT-2).each do |row|
    (1..WIDTH-2).each do |col|
      current = field[row][col]
      above = field[row-1][col]
      if current == '^'
        field[row][col-1] += above
        field[row][col+1] += above
      elsif above != '^'
        field[row][col] += above
      end
    end
  end

  return field[-2].sum
end


puts naive(data)

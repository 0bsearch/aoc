# data:
#   - 0 < coords < 100k
# ideas:
#   - KD
#   - grid with hypot culling

data = File.readlines(
  File.expand_path("../../../data/2025/day09/#{ARGV[-1]}", __FILE__),
  chomp: true
)
  .map { |s| s.split(',').map!(&:to_i) }


def naive(points)
  max_area = 0
  points.each do |x1, y1|
    points.each do |x2, y2|
      area = ((x1-x2).abs + 1) * ((y1-y2).abs + 1)
      if area > max_area
        max_area = area
      end
    end
  end
  return max_area
end


puts naive(data)

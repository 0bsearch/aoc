# ideas:
#   - every line is guaranteed to have different colors to sides
#     => any segment intersecting rect sides invalidates it
#     this also needs check for rect vertices to be inside polygon
#
#
#   - check how GIS does polygon `in`
#     - N*M segment intersections?
#     - parallel projections of outer segments onto inner?


data = File.readlines(
  File.expand_path("../../../data/2025/day09/#{ARGV[-1]}", __FILE__),
  chomp: true
)
  .map { |s| s.split(',').map!(&:to_i) }


def segment_intersects?(segment, rect_bounds)
  (x1, y1), (x2, y2) = segment
  left, top, right, bottom = rect_bounds
  
  if x1 == x2
    # vertical segment
    if x1 > left and x1 < right
      # both ends should be on either side of rect
      if not ( (y1 >= top and y2 >= top) or (y1 <= bottom or y2 <= bottom) )
        return true
      end
    end
  elsif y1 == y2
    # horizontal segment
    if y1 > bottom and y1 < top
      # both ends should be on either side of rect
      if not ( (x1 <= left and x2 <= left) or (x1 >= right and x2 >= right) )
        return true
      end
    end
  else
    raise "wtf? (#{x1}:#{y1}) -> (#{x2}:#{y2})"
  end
  return false
end


def update_corners(corners, rect_bounds, point)
  before = corners.map(&:clone)
  left, right, top, bottom = rect_bounds
  x, y = point
  # top left -> corners[0]
  corners[0] = corners[0] || (x <= left and y >= top)
  # top right -> corners[1]
  corners[1] = corners[1] || (x >= right and y >= top)
  # bottom left -> corners[2]
  corners[2] = corners[2] || (x <= left and y <= bottom)
  # bottom right -> corners[3]
  corners[3] = corners[3] || (x >= right and y <= bottom)
  # puts "#{before.inspect} & #{point.inspect} -> #{corners}"
end


def naive(points)
  max_area = 0
  points.each_with_index do |(x1, y1), i|
    points.lazy.drop(i).each do |x2, y2|
      left, right = [x1, x2].minmax
      bottom, top = [y1, y2].minmax
      area = (right - left + 1) * (top - bottom + 1)
      if area > max_area
        # puts
        # puts "area #{area} / #{max_area} max"
        # puts "(#{x1}, #{y1}) -> (#{x2}, #{y2})"
        corners_inside = [false, false, false, false]
        solid = true
        points.each_cons(2) do |segment|
          if segment_intersects?(segment, [left, top, right, bottom])
            # puts "segment #{segment.inspect} intersects #{[left, top, right, bottom].inspect}"
            solid = false
            break
          end
          # this is stupid af. We should just check if hypot is drawn
          # within colored angle between segment vectors
          if not corners_inside.all?
            update_corners(corners_inside, [left, right, top, bottom], segment[0])
          end
        end
        max_area = area if (solid && corners_inside.all?)
      end
    end
  end
  return max_area
end


# 1529675217
puts "result: #{naive(data)}"

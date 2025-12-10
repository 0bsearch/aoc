data = File.readlines(
  File.expand_path("../../../data/2025/day08/#{ARGV[-1]}", __FILE__),
  chomp: true
)
  .map { |s| s.split(',').map!(&:to_i) }


def dist(a, b)
  Math.sqrt a.zip(b).sum { |(c1, c2)| (c1 - c2) ** 2 }
end


def naive(points)
  edges = []
  color = Array.new(points.size)
  (0..points.size-2).each do |from|
    (from+1..points.size-1).each do |to|
      distance = dist(points[from], points[to])
      edges.append([distance, from, to])
    end
  end
  edges.sort!

  last_from, last_to = nil
  edges.each do |distance, from, to|
    from_color = color[from]
    to_color = color[to]
    if (from_color and to_color and from_color == to_color)
      # already same color
      next
    elsif (from_color and to_color and from_color != to_color)
      # recolor right group
      color.map! { |c| c == to_color ? from_color : c }
    else
      # color both groups
      circuit_color = (from_color or to_color or from)
      color[from] = circuit_color
      color[to] = circuit_color
    end

    if color.all? { |e| e == color.first }
      last_from = from
      last_to = to
      break
    end
  end

  return points[last_from][0] * points[last_to][0]
end


# 59039696
puts naive(data)

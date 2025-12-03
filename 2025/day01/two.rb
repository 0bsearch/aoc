data = File.open(
  File.expand_path("../../../data/2025/day01/#{ARGV[-1]}", __FILE__),
  'rt'
) { |f| data = f.readlines() }


def count_clicks(instructions)
  position = 50
  clicks = 0

  instructions
    .map { |s| [s[0] == 'L' ? -1 : 1, s[1..].to_i] }
    .each do |sign, shift|
      start = position
      full_rotas, shift = shift.divmod(100)
      clicks += full_rotas
      position += shift * sign
      if (not position.between?(1, 99)) and start != 0
          clicks += 1
      end
      position %= 100
    end

  return clicks
end

# 5782
puts(count_clicks(data))

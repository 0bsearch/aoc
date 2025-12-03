def count_zeros(instructions)
  current = 50
  clicks = 0

  instructions.map(&:strip).each do |instruction|
    sign = instruction[0] == 'R' ? +1 : -1
    rotation = instruction[1..].to_i

    current += sign * rotation
    current %= 100

    if current == 0
      clicks += 1
    end

  end
  return clicks
end


if __FILE__ == $0
  data = File.open(ARGV[-1], 'rt') { |f| data = f.readlines() }
  puts(count_zeros(data))
end
  

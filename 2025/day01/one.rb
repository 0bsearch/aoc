data = File.readlines(
  File.expand_path("../../../data/2025/day01/#{ARGV[-1]}", __FILE__),
)


def count_zeros(instructions)
  position = 50

  instructions
    .each{ |s| s.sub!(/[LR]/, 'L' => '-', 'R' => '+') }
    .map!( &:to_i )
    .map!{ |i| (position += i) }
    .count{ |i| i % 100 == 0 }

end


puts(count_zeros(data))

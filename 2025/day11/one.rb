data = File.readlines(
  File.expand_path("../../../data/2025/day11/#{ARGV[-1]}", __FILE__),
  chomp: true
).map do |line|
  md = /^(.+): (.+)$/.match(line)
  [md[1].to_sym, md[2].split.map(&:to_sym)]
end


def naive(data)
  connections = Hash[data]
  paths = Hash.new { |h, k| [false, Hash.new(0)] }
  paths[:you] = [true, { you: 1 }]

  loop do
    this, (should_update, upstreams) = paths
      .filter { |k, (su, ups)| su && k != :out }
      .first
    break if !this

    paths[this][0] = false
    paths_to_this = upstreams.values.sum

    connections[this].each do |downstream|
      _, upstreams = paths[downstream]
      upstreams[this] = paths_to_this
      paths[downstream] = [true, upstreams]
    end
  end
  return paths[:out][1].values.sum
end


# 431
puts naive(data)

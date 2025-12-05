# ideas
#   - ~~Ractor?~~ looks like overhead is >> parallelism boost
Require 'digest'


data = File.read(
  File.expand_path("../../../data/2015/day04/#{ARGV[-1]}", __FILE__)
).strip!


def naive(prefix)
  (0..).each do |number|
    digest = Digest::MD5.hexdigest("#{prefix}#{number}")
    if digest.start_with?('000000')
      return number, digest
    end
  end
end


# 9962624
puts naive(data)

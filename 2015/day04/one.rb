require 'digest'


data = File.read(
  File.expand_path("../../../data/2015/day04/#{ARGV[-1]}", __FILE__)
).strip!


def naive(prefix)
  (1..).each do |number|
    digest = Digest::MD5.hexdigest("#{prefix}#{number}")
    if digest.start_with?('00000')
      return number, digest
    end
  end
end


# 282749
puts naive(data)

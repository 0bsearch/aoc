data = File.readlines(
  File.expand_path("../../../data/2015/day07/#{ARGV[-1]}", __FILE__),
  chomp: true,
)

require 'debug'
OPS = {
  "AND"    => :&,
  "OR"     => :|,
  "NOT"    => :~,
  "LSHIFT" => :<<,
  "RSHIFT" => :>>,
}
def recurse(var, wired, expressions)
    if var.match? /\d+/
      return var.to_i
    elsif wired[var]
      return wired[var]
    end

    expr = expressions[var]
    if m = /^(?<scalar>\w+)$/.match(expr)
      wired[var] = recurse(m[:scalar], wired, expressions)
      return wired[var]
    elsif m = /^(?<op>NOT) (?<right>\w+)$/.match(expr)
      wired[var] = ((2 << 15) - 1) ^ recurse(m[:right], wired, expressions)
      return wired[var]
    elsif m = /^(?<left>\w+) (?<op>\w+) (?<right>\w+)$/.match(expr)
      left = recurse(m[:left], wired, expressions)
      right = recurse(m[:right], wired, expressions)
      op = OPS[m[:op]]
      wired[var] = left.send(op, right)
      return wired[var]
    end
end

def naive(instructions)
  wired = {}
  expressions = {}

  instructions.each do |i|
    m = /^(?<expr>.+) -> (?<var>\w+)/.match(i)
    expressions[m[:var]] = m[:expr]
  end

  a = recurse('a', wired, expressions)
  wired = {'b' => a}
  res = recurse('a', wired, expressions)
  return res
end


# 40149
puts naive(data)

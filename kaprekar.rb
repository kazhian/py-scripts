
# This function takes an integer n, converts it to a 4-digit string with leading zeros if necessary,
# sorts the digits in descending order to form the largest possible number,
# and returns the resulting integer.

def largest_number(n)
    n.to_s.rjust(4, '0').split('').sort { |a, b| b + a <=> a + b }.join.to_i
end
# This function takes an integer n, converts it to a 4-digit string with leading zeros if necessary,
# sorts the digits in ascending order to form the smallest possible number,
# and returns the resulting integer.
  def smallest_number(n)
    n.to_s.rjust(4, '0').split('').sort.join.to_i
  end

  def kaprekar(a)
    largest, smallest = [largest_number(a), smallest_number(a)]
    [largest, smallest, (largest - smallest)]
  end

  def kaprekar?(p)
    p == 6174
  end

 
  def all_digits_same?(n)
   n.to_s.rjust(4, '0').chars.uniq.size == 1
  end

  (1000..9999).each do |i|
    next if all_digits_same?(i)
  
    attempts = 1
    current_value = i
    loop do
      largest, smallest, k = kaprekar(current_value)
      puts "#{i}. Attempt ##{attempts}.  #{largest}-#{smallest}=#{k}#{kaprekar?(k) ? "*\n" : ""}"
      if kaprekar?(k)
        puts "\n"
        break
      end
      attempts += 1
      current_value = k
    end
  end

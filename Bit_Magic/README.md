<a href="https://github.com/raqeebhamza"><a href="https://github.com/raqeebhamza"><img style="position: absolute; top: 0; left: 0; border: 0;" src="https://github.com/raqeebhamza/DSA/blob/main/Bit_Magic/bit_magic.png" width="600" height="250"/>

# Bit_Magic : :triangular_flag_on_post:
Remember Few Things : 
```
- (1 << n) = 2^n . Generalised : n << x = n * 2^x

- Similarly, n >> x = n / 2^x

- if ( (x & (1 << i)) == 0 ) , then ith bit of x is set (i.e. 1)
  This will help you find subset using bit manipulation. 
  
- If we subtract a power of 2 number by 1 then all unset bits after the
  only set bit become set, and the set bit becomes unset.
  For example for 4 (100) and 16(10000), we get the following after subtracting 1 
      3 –> 011 
      15 –> 01111

   So, if( (n&(n-1)) == 0) - n is even
```
<h1>Questions</h1>
<table id = "example" class="SectionTable display" >
		<thead>
      <th>Problem Name</th>
		</thead>
		<tbody>
			<tr>
       			<td>
					<a href="https://github.com/raqeebhamza/DSA/blob/main/Bit_Magic/counting_bits.py">Counting Bits (Leetcode-338)</a>
				</td>
			</tr>
		</tbody>
</table>
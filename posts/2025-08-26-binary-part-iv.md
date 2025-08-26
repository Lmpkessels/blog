---
title: Binary division explained
html_title: Binary part-IV
description: Understand binary long division from first principles. Walk through bit-by-bit division with clear tables, logic, and CPU perspective.
section: math
image: /assets/binary-div-thumb.png
alternative: Thumbnail graphic titled ‘Binary Division Explained’ in black, white. It shows the binary division example 10001 ÷ 101 = 11 remainder 10.
date: 2025-08-26
slug: binary-part-iv
---

Now we've seen how [binary starts at registers flows trough gates](https://lmpkessels.com/content/2025/2025-06/binary-part-0) to, [add](https://lmpkessels.com/content/2025/2025-07/binary-part-i), [subtract](https://lmpkessels.com/content/2025/2025-08/binary-part-ii), and [multiply](https://lmpkessels.com/content/2025/2025-08/binary-part-iii) let's take a look at the last layer (for this series) **division**.

## 1st principles of binary division

CPUs don’t magically divide, they use the following logical operations.

<ul class="post-ul">
  <li><b>if...else</b>: to check if the growing remainder >= divisor, to write down the quotient.</li>
  <li><b>subtract</b>: to get the remainder.</li>
  <li><b>shift</b>: to shift left by each index position moved down to write down the next LSB.</li>
</ul>

We always start at the **MSB of the dividend** and use **if...else...** to check if the **growing remainder >= the divisor** if that's true we write down **1 at the quotient else 0**.

If and only **if the growing remainder >= the divisor** we subtract the divisor from the growing remainder to calculate the remainder, else we take the remainder with us down and shift left by 1 index position and append the next LSB of the divisor then we repeat the process.

Let's walk through an example,

We take 10001 / 101 (17 / 5) and go through binary division bit-by-bit in **figure 1.0**.

<ul class="post-ul">
  <li><b>A:</b> is <b>dividend</b>10001 (17)</li>
  <li><b>B:</b> is <b>divisor</b> 101 (5)</li>
</ul>

<figure>
  <table>
    <thead>
      <tr>
        <th>Step</th>
        <th>Bring down bit</th>
        <th>Remainder before</th>
        <th>Compare (≥ divisor?)</th>
        <th>Quotient bit</th>
        <th>Remainder after</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>0</td><td>1</td><td>0</td><td>1 ≥ 101? </br> no</td><td>0</td><td>1</td></tr>
      <tr><td>1</td><td>0</td><td>10</td><td>11 ≥ 101? no</td><td>0</td><td>11</td></tr>
      <tr><td>2</td><td>0</td><td>100</td><td>100 ≥ 101? no</td><td>0</td><td>100</td></tr>
      <tr><td>3</td><td>0</td><td>1000</td><td>1000 ≥ 101? </br> yes → 1000 − 101</td><td>1</td><td>11</td></tr>
      <tr><td>4</td><td>1</td><td>111</td><td>111 ≥ 101? yes → </br> 111 − 101</td><td>1</td><td>10</td></tr>
    </tbody>
  </table>
  <figcaption><b>Figure 1.0:</b> Step-by-step binary long division of 10001 (17) ÷ 101 (5). Quotient = 11 (3), Remainder = 10 (2).</figcaption>
</figure>

As discussed above you can see that **subtraction is conditional**. It's only used when the divisor fits into current remainder. Otherwise, you carry on shifting the dividend down by one position.

If you're not familiar with **binary subtraction** check out [binary part-II](https://lmpkessels.com/content/2025/2025-08/binary-part-ii) where I'll **walk you through binary subtraction bit-by-bit**, then you’ll be able to do row 3 and 4 yourself (if you aren’t already).

Well that was binary long division, division closes out this binary series.

You now have **add, subtract, multiply, and divide at the bit level**. With these, you’ve built the full arithmetic core of a CPU.

If you want to stay updated follow me on [X/Twitter](https://x.com/lmpkessels).

Want to see coded examples? [Click ALU](https://github.com/Lmpkessels/axiom.git) a 32-bit Arithmetic Logic Unit that goes from integers to **bit-by-bit simulations through logic gates**, supports ADD, SUB, MULTIPLY, DIV.

Till next time.

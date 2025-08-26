---
title: Binary multiplication explained
html_title: Binary part-IV
description: Binary multiplication from first principles: AND, SHIFT, ADD. Full worked example 5×10, plus short recap on addition logic
section: math
image: assets/binary-multiply-thumb.png
alternative: Binary multiplication: AND • SHIFT • ADD with 0101 × 1010 = 0110010 (50)
date: 2025-08-23
slug: binary-part-iv
---

At the heart of computer performance lies binary multiplication, the process of combining numbers bit-by-bit.

Let's take a look at how it works.

## 1st principles of binary multiplication

To break it down, here you have the three logical operations used in binary multiplication, **AND, SHIFT, ADD**.

<ul class="post-ul">
  <li><b>AND</b>: takes <b>each bit of B in isolation</b> and applies <b>AND</b> on the entire string of A <b>bit-by-bit</b>.</li>
  <li><b>SHIFT</b>: Shift Left is performed every move down starting from 0, till all moves <i>(based on the range of B)</i> are performed.</li>
  <li><b>ADD</b>: is used to add up the whole and get the product Sum in return.</li>
</ul>

For each bit of **B** (index i) we perform a move down, every move down is a Shift Left (starting at index 0) which creates a partial. Every partial is summed up using addition logic to get the multiplication end product.

Let me walk you through an example using 5 X 10 (0101 X 1010) starting at _figure 1.0_.

<ul class="post-ul">
  <li><b>A</b> is 0101 (5)</li>
  <li><b>B</b> is 1010 (10)</li>
</ul>

<figure>
  <table>
    <thead>
      <tr>
        <th>Bit position</th>
        <th>B[i]</th>
        <th>(B[i] AND A)</th>
        <th>Shift (<< i)</th>
        <th>Partial product (7b)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>0</td><td>0</td><td>0000</td><td><< 0</td><td>XXX0000</td></tr>
      <tr><td>1</td><td>1</td><td>0101</td><td><< 1</td><td>XX01010</td></tr>
      <tr><td>2</td><td>0</td><td>0000</td><td><< 2</td><td>X000000</td></tr>
      <tr><td>3</td><td>1</td><td>0101</td><td><< 3</td><td>0101000</td></tr>
    </tbody>
  </table>
  <figcaption><b>Figure 1.0:</b> Step table: for each bit of B, AND it with A, then shift left by its index to form a partial product.</figcaption>
</figure>

We mark unused positions with **X which act as placeholders, in actual hardware these become 0s in register**. So that the ALU can work with the same range in every bit-by-bit addition calculation, to get Sum and Carry out.

If you're not familiar with binary addition check out [binary part-II](https://lmpkessels.com/content/2025/2025-07/binary-part-ii).

Now let's apply binary addition row-by-row on each partial product.

## Binary addition applied on Partial product

Short recap of Sum, and Carry out:

<ul class="post-ul">
  <li><b>Sum:</b> A XOR B XOR Carry in</li>
  <li><b>Carry out:</b> (A AND B) OR (Carry in AND (A XOR B))</li>
</ul>

_**Example:** 1 + 1 with carry-in 0 gives sum = 0, carry = 1_

Starting bit-by-bit at **Partial 0, and 1** in _figure 1.1_, to get the Sum column then we repeat that process two more times.

<figure>
  <table>
    <thead>
      <tr>
        <th>Bit position</th>
        <th>Running sum</th>
        <th>Next partial</th>
        <th>Carry in</th>
        <th>Sum</th>
        <th>Carry out</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
      <tr><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>3</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
      <tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    </tbody>
  </table>
  <figcaption><b>Figure 1.1:</b> Ripple-carry addition: adding Partial 0 and Partial 1 from Figure 1.0.</figcaption>
</figure>

**NOTE:** Bit 0 is rightmost least significant bit (LSB) moving to leftmost most significant bit (MSB).

Now in _figure 1.2_ we take Sum from _figure 1.0_ and apply addition logic bit-by-bit with **Partial 2** of _figure 1.0_.

<figure>
  <table>
    <thead>
      <tr>
        <th>Bit position</th>
        <th>Running sum</th>
        <th>Next partial</th>
        <th>Carry in</th>
        <th>Sum</th>
        <th>Carry out</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
      <tr><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>3</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
      <tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    </tbody>
  </table>
  <figcaption><b>Figure 1.2:</b> Ripple-carry addition: adding the previous sum with Partial 2 from Figure 1.0.</figcaption>
</figure>

Arriving at the last Partial, **Partial 3** in _figure 1.0_, we repeat addition logic for Sum and Carry out one last time.

<figure>
  <table>
    <thead>
      <tr>
        <th>Bit position</th>
        <th>Running sum</th>
        <th>Next partial</th>
        <th>Carry in</th>
        <th>Sum</th>
        <th>Carry out</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
      <tr><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>3</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>
      <tr><td>4</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr>
      <tr><td>5</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr>
      <tr><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
    </tbody>
  </table>
  <figcaption><b>Figure 1.3:</b> Ripple-carry addition: adding the running sum with Partial 3 from Figure 1.0 to produce the final product.</figcaption>
</figure>

After applying addition logic on all four arrays we end up with **'0110010'** (you can read it in the Sum column), which is integer **50**.

That was binary multiplication.

Like to stay updated and learn about Systems, Rust, Math, and more? Then you can follow me on [X/Twitter](https://x.com/lmpkessels) where I'll be posting when a blog goes live.

Want to see coded examples? Check, [ALU](https://github.com/Lmpkessels/axiom.git) a 32-bit Arithmetic Logic Unit that goes from integers to bit-by-bit simulations through logic gates, supports ADD, SUB, MULTIPLY, DIV.

Now go practice some _binary multiplication_ till next time.

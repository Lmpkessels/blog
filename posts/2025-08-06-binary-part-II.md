---
title: Binary Subtraction Explained
html_title: Binary part-II
description: Learn how binary subtraction works inside your CPU using logic gates like XOR, AND, OR, and NOT. This blog breaks down difference and borrow logic step-by-step with diagrams, truth tables, and 1’s & 2’s coACmplement examples.
section: math
image: /assets/binary-part-ii-Luke-blog.png
date: 2025-08-06
slug: binary-part-ii
---

Today you’ll learn how binary subtraction works at the lowest level in your machine.

If you’re not familiar with binary check out [binary part-0](https://www.lukefi.com/content/2025/2025-06/binary-part-0) here you’ll find out why binary is used and how it flows through components of your PC.

## The 5 components in binary subtraction

In binary part-I, you used 5 components input A input B, Carry in, Sum and Carry out.

For binary subtraction Carry in, Sum, and Carry out, become Borrow in, Difference and Borrow out.

Input A. and B, remain a byte.
<br />

## How subtraction happens in your CPU

You already know your CPU uses logic gates to perform bit-by-bit operations.

In subtraction we use a following combination of gates:

For Difference: ((a XOR b) XOR borrow_in)
And BorrowOut: (NOT(a) AND b) OR (NOT( a XOR b) AND borrow in)
<br />

## Difference explained

Difference is used to return the output after applying a bit-by-bit operation.

When the operation is done; difference is used to store the remaining byte and give it in return.

ex. When you subtract 17 - 1 using the calculator on your phone, your CPU goes to work, starting at a transistor, each bit flows bit-by-bit through logic gates, each difference is stored and a byte is returned.

Now that we’ve covered what ‘difference’ means, let’s break it down and see how CPUs handle subtraction at the logic gate level.
<br />

## Difference under the hood

Figure 1.0 displays the difference in a diagram using 2X logic gate XOR this is the exact route your CPU follows when transiting bits.

<figure>
<img
src="/assets/difference_gate.png"
alt="Figure 1.0: Difference logic simulation applying the XOR gate two times"
class="default-img-setting"
/>

<figcaption>
<b>Figure 1.0:</b> Difference logic simulation applying the
XOR gate two times only one, if <code>a &lt; b</code> OR Borrow out.
</figcaption>
</figure>

Bit A and bit B flow through the logic gate XOR which then returns a bit, that bit then flows to the next gate, XOR logic is applied again with Borrow in, and the final output is returned.
<br />

## Why XOR is used in Difference

XOR is used to compare two bits, it returns 1 if the bits are different and 0 if they’re the same. That’s why it’s ideal for calculating the bitwise difference.

If you’re not familiar with XOR check out [binary-part-I](https://www.lukefi.com/content/2025/2025-07/binary-part-i) where you walk through a bit-by-bit XOR simulation using the basic gates, AND, NOT, and OR.

Now let’s move to borrow out.
<br />

## Why Borrow out is needed

Because computers only store bits (0s and 1s) , going below 0 will cause underflow, which will cause us to borrow out.

Borrow-out checks whether subtraction at a bit column requires borrowing.

We need to borrow when input A is less than input B at that bit column.
<br />

## How borrow out flows through your CPU

Figure 1.1 shows Borrow out in a circuit simulation, using for different gates NOT, AND, OR, and XOR.

<figure>
<img
src="/assets/borrow-out-logic-simulation.png"
alt="Figure 1.1: Borrow out logic of a 1-bit full subtraction adder using basic gates. Output is 1 when (NOT (A) AND B) or (CarryIn AND (NOT (A XOR B))) is 1."
class="default-img-setting"
/>

<figcaption>
<b>Figure 1.1:</b> Borrow out logic of a 1-bit full
subtraction adder using basic gates. Output is 1 when (NOT (A)
AND B) or (CarryIn AND (NOT (A XOR B))) is 1.
</figcaption>
</figure>

Starting at the top A flows through the NOT gate to the transistor of the AND gate where B is waiting together they flow through AND and a final bit is returned. If a bit is stored we need to borrow else we follow the next logic.

A and B flow through XOR a bit is returned which then flows through not borrow in is waiting at the transistor of the AND gate where both bits now flow through together, if the return value is 1 bit then we need to borrow if not we don’t.

Now you know how both Difference and Borrow out flow through logic gates lets walk through a table.
<br />

## Full table walkthrough

Figure 1.2 shows a subtraction full 8 bit adder with all five components. On the left hand side each bit’s index position is shown.

<figure>
  <table>
    <thead>
      <tr>
        <th>Bit Position</th>
        <th>A</th>
        <th>B</th>
        <th>Borrow In</th>
        <th>Difference</th>
        <th>Borrow Out</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Bit_0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>Bit_1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
      <tr><td>Bit_2</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>
      <tr><td>Bit_3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
      <tr><td>Bit_4</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>
      <tr><td>Bit_5</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>
      <tr><td>Bit_6</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>
      <tr><td>Bit_7</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr>
    </tbody>
  </table>
  <figcaption><b>Figure 1.2:</b> 8-Bit full subtraction adder.
  </figcaption>
</figure>

For this example let’s take the row of bit_2.

<figure>
  <table class="table-350px">
    <tr>
      <td>Bit_A</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Bit_B</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Borrow in</td>
      <td>0</td>
    </tr>
  </table>
  <figcaption>Table 1: Binary subtraction inputs</figcaption>
</figure>

We start at calculating the difference so we know what to write down at the Bit_2 column's position, so `((0 XOR 1) = 1) XOR 0) = 1`, and we now know 1 needs to be written down in the column of Bit_2.

Next, we check if a borrow is needed: (NOT 0 = 1) AND 1 = 1. This already signals a borrow, but let’s complete the logic. (0 AND (0 XOR 1)) = 0.

So, 1 OR 0 = 1, this confirms that borrow-out is 1.

Based on the math you’re using the CPU decides if it’s unassigned, if it’s unassigned mathematics then the CPU calls an error called underflow and a borrow out is needed.

If you’re using assigned math you'll simply go below zero using 2's complement.
<br />

## What is 1’s and 2’s complement

Since memory only stores 0s and 1s, going below 0 directly isn’t possible without causing an error while compiling.

So if we need to represent a negative number, we use 1s complement and 2s complement.

1’s complement flips all bits, e.x. 10101 becomes → 01010, when you look at the pattern you simply see that all 1s have become 0s and all 0s have become 1s.

2’s complement flips all bits + adds 1 bit, e.x. 00110 becomes 11001 then one is added so it becomes 11010.
<br />

## Closure

If you’re interested in Systems, Rust, Comp-sci, Blockchain, and more follow along. To stay tuned in on the blog check out: [X/Twitter](https://x.com/lukefi_) where I’ll be posting when a blog goes live.

If you want programmed example where i simulate logic using functions check out: [binarySeries](https://github.com/Lmpkessels/binarySeries) where I have built an ALU from the gates up.

That’s it for now, keep in mind, “every program is an ALU at its lowest level” till the next one.

---
title: What is binary
html_title: Binary part-0 | LukeFi
description: Introduction to binary. How your computer uses 0s and 1s, logic gates, and transistors to show data on your screen.
section: math
image: assets/binary-part-0-thumb.png
date: 2025-06-28
slug: binary-part-0
---

Imagine it’s Friday morning and you're reading the news on your laptop, then, suddenly, you wonder…

"How are all these letters and images displayed to me?”

That’s binary going through logic gates in your CPU.

At the end of this blog you know exactly why binary is used in computer science and gets the right data on your screen.

In binary, we only have 0 and 1, to represent all numbers and data by combining powers of two. That’s different from decimal where we use 0-9.

Binary is the foundation of computer systems and digital communication.

CPUs use binary in logic gates; you can see each logic gate as a mathematical function, you have input, logic, output. The core gates are AND, OR, and NOT. If we combine these, we can create more complex logic gates, like XOR, NAND, and 2 more. These gates obey Boolean logic and are physically built with transistors.

A transistor acts like a digital switch:

- 1 = Electricity flows (ON)
- 0 = No flow (OFF)

If you’re reading this blog from your macbook with a K2 chip then your chip contains “~20 Billion transistors, each acting as an on/off switch letting your computer process data lightning-fast.” so you can read the right message from your screen.

“Your computer reads each tiny switch – a bit – as either 1 (on) or 0 (off).”

Each bit has a weight. Starting at the right, Least Significant Bit (LSB) moving to left, Most Significant Bit (MSB), their values are:

<figure>
  <table class="table-350px">
    <tr>
        <td>(MSB) 2<sup>7</sup>  2<sup>6</sup>  2<sup>5</sup>  2<sup>4</sup>  2<sup>3</sup>  2<sup>2</sup>  2<sup>1</sup>  0<sup>2</sup> (LSB)</td>
    </tr>
  </table>
  <figcaption><b>Figure 1.0:</b> String of 8 bits (byte)</figcaption>
</figure>

(in an 8-bit byte).

In Computer Science we start counting from 0, so in this example we go from index 0 to index 7, in decimal that would be 1 to 8.

As you can see in this example each bit value is calculated as 2 raised to the power of its position. Its index position tells us how many times we need to do a calculation to the power of two starting from zero.

So if we take the Most Significant Bit (MSB) all the way on the left, then we would need to do two to the power two seven times and then we would net a decimal number 256.

All thanks to logic gates in your CPU that groups 8 bits into one byte. With a byte we can create a total of 256 unique combinations and store data.

Enough to represent characters, colors, numbers, and more.

Here I say Bye to you using three bytes that are assigned to the ASCII (American Standard Code For Information Interchange) standard.

<figure>
  <table class="table-350px">
    <thead>
      <tr>
        <th>Binary</th>
        <th>ASCII</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>01000010</td><td>B</td>
      <tr><td>01100101</td><td>y</td>
      <tr><td>01111001</td><td>e</td>
    </tbody>
  </table>
  <figcaption><b>Figure 1.1:</b> ASCII Table</figcaption>
</figure>

That’s it for now.

I hope you like binary part 0, it’s part of my deeper journey into logic and computer systems. I’ll revisit and expand on it soon. If you have something to add, or see a gap in my thinking feel free to reach out.

You can find me by clicking one of these links LinkedIn or, X/Twitter.

If you want to see programmed examples where I simulate logic gates using Rust, then check out: binarySeries

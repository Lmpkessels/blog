---
title: Explanation of a Virtual Machine
html_title: Explanation of a Virtual Machine | Lmpkessels
description: A first-principles explanation of a minimal virtual machine, focusing on execution, state, and structure.
section: comp-sci
image: /assets/virtual-machine-thumb.png
alternative: Simplified diagram of a virtual machine illustrating the stack, program counter, ALU, and execution loop.
date: 2025-12-18
slug: virtual-machine
---

## Explanation of a Virtual Machine

A **virtual machine (VM)** is a system that follows a strict, predefined set of rules to execute a program step-by-step.

Rather than directly manipulating hardware, a VM interprets instructions and operates on an abstract model of computation. This abstraction allows programs to be portable, predictable, and analyzable, while still reflecting how real machines operate at a lower level.

At its core, a virtual machine **stores state**, **selects instructions**, **executes operations**, and **advances through a program**. Each of these actions happens repeatedly inside a tight execution loop, forming the fundamental behavior of computation itself.

A minimal virtual machine is defined by **structure**. Here follow the essential components:

<!-- Unordered list for full posts -->
<ul class="post-ul">
  <li>A <b>Stack</b> for storing values</li>
  <li>A <b>Program Counter</b> for selecting which instruction comes next</li>
  <li>An <b>Arithmetic Logic Unit (ALU)</b> for executing arithmetic and logical operations</li>
  <li>A fixed set of <b>operations (opcodes)</b></li>
  <li>An <b>execution loop</b> that coordinates all components</li>
</ul>

Together, these components form a complete computational system.

## The Stack

A **stack** is a memory discipline that stores values in **last-in-first-out (LIFO)** order. This means the most recently added value is the first one to be used. Stacks are typically implemented in RAM and managed using a **stack pointer**, which tracks the current top of the stack.

The stack supports two fundamental operations:

<ol class="post-ul">
  <li><b>Push</b>, to store a value on the stack</li>
  <li><b>Pop</b>, to get the most recently stored value</li>
</ol>

For example, if we push the value **"1"** onto the stack, the binary representation **"00000001"** is stored at the memory location pointed to by the stack pointer. When we later pop, the stack pointer moves back and the stored value is selected and returned.

The stack itself does not perform computation. Its role is to **store intermediate values** so that other components, especially the ALU, can operate on them.

**NOTE:** This separation of concerns is critical: storage is distinct from execution.

Because of the LIFO discipline, stacks naturally support nested computation. Temporary values are automatically resolved in the correct order without requiring explicit bookkeeping by the programmer. This is why stacks are central to expression evaluation, function calls, and virtual machines.

## The Program Counter

The **Program Counter (PC)** is responsible for selecting which instruction is executed next. It stores the address of the current instruction in the program.

On each cycle, the program counter can perform one of three actions:

<ul class="post-ul">
  <li><b>Increment</b>, move to the next instruction</li>
  <li><b>Load</b>, use a new instruction address</li>
  <li><b>Reset</b>, return to the initial state '0'</li>
</ul>

Most of the time, the program counter simply increments, advancing sequentially through the program. When control-flow instructions such as jumps or branches occur, the PC loads a new address instead. When the program halts, the PC may reset to its initial value.

The program counter is driven by **clock cycles**, which provide a shared notion of time across all components. Each cycle represents one step in execution, ensuring that instruction selection, execution, and state updates happen in order.

Without a program counter, there is no notion of order. The PC gives computation its **temporal structure**, allowing the machine to move forward step-by-step.

## Example Program

```text
Push 2
Push 3
Add
Halt
```

This program pushes two values onto the stack, selects the **"Add"** operation, pops the values, executes the addition, pushes the result back onto the stack, and then halts. Even in this tiny example, all core components of the virtual machine are active.

## The Arithmetic Logic Unit (ALU)

The **Arithmetic Logic Unit** is the component that executes computation. It performs both arithmetic operations (such as addition and subtraction) and logical operations (such as AND, OR, and XOR).

At the hardware level, an ALU is built from **logic gates** and **registers**. Every arithmetic operation ultimately reduces to combinations of simple logical operations. For example, binary addition is implemented using XOR and AND gates to propagate sums and carries.

In a virtual machine, the ALU does not operate directly on memory. Instead, it consumes values popped from the stack, executes the selected operation based on the current opcode, and produces a result that is pushed back onto the stack.

From the VM’s perspective, the ALU is an execution engine: it **selects the operation**, **executes it**, and returns the result. High-level operators such as **"+"** or **"\*"** are simply symbolic representations of these lower-level behaviors.

## The Execution Loop

The **execution loop** is the heart of the virtual machine. It is the repeating cycle that coordinates all components and gives the VM its dynamic behavior.

Each iteration of the loop follows the same general pattern:

<ol class="post-ul">
  <li><b>Select</b> the next instruction using the program counter</li>
  <li><b>Decode</b> the instruction to determine which operation to perform</li>
  <li><b>Execute</b> the operation using the stack and ALU</li>
  <li><b>Advance</b> the program counter</li>
  <li><b>Repeat</b></li>
</ol>

This loop continues until a halting condition is reached.

The execution loop is where storage, selection, execution, and advancement come together. The stack provides data, the program counter selects instructions, the ALU executes logic, and the loop advances the machine through time.

## Why This Matters

Understanding a virtual machine at this level reveals a deep truth: **computation is fundamentally about controlled state transitions**. Every program, no matter how abstract, reduces to a sequence of steps that manipulate stored values according to fixed rules.

Virtual machines expose this reality clearly. They are not just tools for running code, but **models of computation**. The same principles apply to CPUs, interpreters, blockchain virtual machines, and programming language runtimes.

By building and understanding a minimal VM, you gain insight into how real systems work under the hood.

## Closing

This explanation walked through the essential components of a virtual machine: the stack, the program counter, the ALU, and the execution loop. Together, these elements form a system capable of executing programs.

If you want to see these ideas translated into real code, you can explore a minimal implementation in Rust here:  
[virtual-machine](https://github.com/Lmpkessels/virtual-machine)

Until the next one.

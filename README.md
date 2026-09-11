# Binary Sequence Permutations & Graph Traversal Tool

A Python CLI tool for generating binary sequence permutations, constructing state graphs, and performing Depth-First Search (DFS) traversals.

## Overview

This project analyzes binary sequences with a fixed number of zeros (`0`) and ones (`1`):
- **Graph Mode (`graph`):** Builds and displays the adjacency list of the permutation graph.
- **DFS Mode (`dfs`):** Performs Depth-First Search to explore paths through the graph topology.
- **BTS Mode (`bts`):** Uses block/symbolic transformations (`+`, `-`, `0`) to generate successor states and represent them in binary, decimal, and index forms.

## Usage

```
python main.py <s> <t> <mode> [start]
```

### Command Line Arguments

- `s` *(int)*: Number of zero symbols (`0`)
- `t` *(int)*: Number of one symbols (`1`)
- `mode` *(str)*: Execution mode: `graph`, `dfs`, or `bts`
- `start` *(int, optional)*: Starting node index/decimal value for DFS

## Examples

- **Build and display graph:**
  `python main.py 2 3 graph`

- **Run DFS starting from a specific node:**
  `python main.py 2 3 dfs 7`

- **Generate Block Transition States (BTS):**
  `python main.py 2 3 bts`

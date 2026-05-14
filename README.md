# CCS2226 Foundations of AI Practicals

This repository contains practical tasks for foundational AI topics:

- Task 1: digit classification using scikit-learn's digits dataset
- Task 2: CSP map colouring for Australia and Nairobi
- Task 3: Prolog family tree relationships
- Task 4: BFS and DFS graph search

## Requirements

Use Python 3.12 on this machine:

```powershell
py -3.12 -m pip install -r requirements.txt
```

## Run The Python Tasks

```powershell
py -3.12 Task_1_MNIST\mnist_classifier.py
py -3.12 Task_2_CSP_Map_Colouring.py\australia_map_colouring.py
py -3.12 Task_2_CSP_Map_Colouring.py\nairobi_map_colouring.py
py -3.12 Task_4_Search_BFS_DFS\bfs_dfs_search.py
```

Task 1 downloads and caches MNIST data in `Task_1_MNIST/data/`.
Generated visualizations are saved in each task's own `output/` folder.

## Run The Prolog Task

Install SWI-Prolog, then load:

```prolog
?- [family_tree].
```

Example queries are listed in `Task_3_Prolong_Family_Tree/sample_queries.txt`.

On this Windows machine, SWI-Prolog is installed at:

```powershell
C:\Program Files\swipl\bin\swipl.exe
```

If `swipl` is not recognized immediately after installation, close and reopen
the terminal so Windows refreshes PATH.

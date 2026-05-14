# CCS 2226 Foundations of Artificial Intelligence Practicals

## Student Details

Name: James Ndung'u Kinyua  
Registration Number: CIT-223-033/2024  
Unit: CCS 2226 Foundations of Artificial Intelligence

## Tasks Included

1. MNIST digit classification
2. Constraint Satisfaction map colouring
3. Prolog family tree
4. Breadth First Search and Depth First Search

## Requirements

Use Python 3.12 for the Python tasks. Do not use plain `python` if it points
to Python 3.14, because the required packages may not be installed or supported
there.

Check your Python versions:

```powershell
python --version
py -3.12 --version
```

Install the required Python packages from the project root:

```powershell
py -3.12 -m pip install -r requirements.txt
```

Install SWI-Prolog for the Prolog family tree task.

## How To Run

Run these commands from the project root:

```powershell
py -3.12 Task_1_MNIST\mnist_classifier.py
py -3.12 Task_2_CSP_Map_Colouring.py\australia_map_colouring.py
py -3.12 Task_2_CSP_Map_Colouring.py\nairobi_map_colouring.py
py -3.12 Task_4_Search_BFS_DFS\bfs_dfs_search.py
```

Task 1 downloads and caches MNIST data in `Task_1_MNIST/data/`.
Generated visualizations are saved in each task's own `output/` folder.

## How To Run The Prolog Task

Open SWI-Prolog and load the file:

```prolog
?- [family_tree].
```

Example queries are listed in:

```text
Task_3_Prolong_Family_Tree/sample_queries.txt
```

If `swipl` is not recognized immediately after installation, close and reopen
the terminal so Windows refreshes PATH.

## Tools Used

- Python
- VS Code
- GitHub
- SWI-Prolog
- scikit-learn
- matplotlib
- networkx

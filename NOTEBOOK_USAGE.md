# Using `dummycalc` in Jupyter Notebook

## 1) Import directly (if notebook is opened from this project folder)

```python
from dummycalc import add, quick_report, square_root

add(4, 6)
square_root(49)
quick_report(8, 2)
```

## 2) If import fails, ensure current working directory is in `sys.path`

```python
import os
import sys

project_root = os.getcwd()
if project_root not in sys.path:
    sys.path.append(project_root)

from dummycalc import current_time, factorial, list_current_dir, python_info
factorial(6), python_info(), current_time(), list_current_dir()[:3]
```

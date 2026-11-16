# Operating Systems Laboratory Algorithms

A curated collection of Operating Systems Lab implementations, covering fundamental OS concepts including Linux command utilities, CPU scheduling algorithms, process synchronization, memory management (page replacement), file system operations, and disk scheduling.

---

## 📋 Table of Contents

| S.No | File Name | Description | Language / Environment |
|:---:|:---|:---|:---:|
| 1 | `01_Lab1_Linux_Ubuntu_Commands.sh` | Basic Linux/Ubuntu File & Directory Commands | Bash / Linux Shell |
| 2 | `02_Lab3a_FCFS_CPU_Scheduling.py` | First-Come, First-Served (FCFS) CPU Scheduling | Python 3 |
| 3 | `03_Lab3b_SJF_Non_Preemptive.py` | Shortest Job First (SJF) Non-Preemptive Scheduling | Python 3 |
| 4 | `04_Lab3c_Priority_Non_Preemptive.py` | Priority CPU Scheduling (Non-Preemptive) | Python 3 |
| 5 | `05_Lab3d_Round_Robin_Scheduling.py` | Round Robin (RR) CPU Scheduling with Time Quantum | Python 3 |
| 6 | `06_Lab4_Producer_Consumer_Semaphores.py` | Producer-Consumer Problem using Mutex & Semaphores | Python 3 (Threading) |
| 7 | `07_Lab7_FIFO_Page_Replacement.py` | First-In, First-Out (FIFO) Page Replacement Algorithm | Python 3 |
| 8 | `08_Lab8_File_System_Simulator.py` | File System Simulator (Create, Read, Append, Rename, Delete) | Python 3 |
| 9 | `09_Lab9_FCFS_Disk_Scheduling.py` | First-Come, First-Served (FCFS) Disk Scheduling | Python 3 |
| 10 | `10_Lab10_Linux_Ubuntu_System_Commands.sh` | Linux System Monitoring and Hardware Status Commands | Bash / Linux Shell |

---

## 🚀 Algorithm Details & Usage

### 1. Basic Linux/Ubuntu Commands (`01_Lab1_Linux_Ubuntu_Commands.sh`)
- **Concepts**: Navigation, directory creation, file creation/manipulation, permissions (`chmod`), and process viewing.
- **Run**:
  ```bash
  bash 01_Lab1_Linux_Ubuntu_Commands.sh
  ```

### 2. FCFS CPU Scheduling (`02_Lab3a_FCFS_CPU_Scheduling.py`)
- **Concepts**: Allocates CPU to processes in the arrival order. Calculates Completion Time (CT), Turnaround Time (TAT), and Waiting Time (WT).
- **Run**:
  ```bash
  python3 02_Lab3a_FCFS_CPU_Scheduling.py
  ```

### 3. SJF Non-Preemptive CPU Scheduling (`03_Lab3b_SJF_Non_Preemptive.py`)
- **Concepts**: Selects the available process with the lowest burst time. Calculates CT, TAT, and WT.
- **Run**:
  ```bash
  python3 03_Lab3b_SJF_Non_Preemptive.py
  ```

### 4. Priority CPU Scheduling (Non-Preemptive) (`04_Lab3c_Priority_Non_Preemptive.py`)
- **Concepts**: Executes the highest-priority available process first (lower numerical value indicates higher priority).
- **Run**:
  ```bash
  python3 04_Lab3c_Priority_Non_Preemptive.py
  ```

### 5. Round Robin CPU Scheduling (`05_Lab3d_Round_Robin_Scheduling.py`)
- **Concepts**: Time-shared scheduling allocating a fixed time quantum ($q$) cyclically across ready processes.
- **Run**:
  ```bash
  python3 05_Lab3d_Round_Robin_Scheduling.py
  ```

### 6. Producer-Consumer Problem using Semaphores (`06_Lab4_Producer_Consumer_Semaphores.py`)
- **Concepts**: Classic concurrency and synchronization synchronization using `threading.Semaphore` (counting semaphore for bounded buffer) and `threading.Lock` (mutual exclusion).
- **Run**:
  ```bash
  python3 06_Lab4_Producer_Consumer_Semaphores.py
  ```

### 7. FIFO Page Replacement Algorithm (`07_Lab7_FIFO_Page_Replacement.py`)
- **Concepts**: Memory management simulation tracking memory frames, page hits, and page faults using a FIFO queue.
- **Run**:
  ```bash
  python3 07_Lab7_FIFO_Page_Replacement.py
  ```

### 8. File System Simulator (`08_Lab8_File_System_Simulator.py`)
- **Concepts**: File manipulation routines demonstrating file creation, writing, appending, reading, renaming, and removal.
- **Run**:
  ```bash
  python3 08_Lab8_File_System_Simulator.py
  ```

### 9. FCFS Disk Scheduling (`09_Lab9_FCFS_Disk_Scheduling.py`)
- **Concepts**: Disk arm scheduling servicing I/O track requests sequentially, computing total head movements and total seek time.
- **Run**:
  ```bash
  python3 09_Lab9_FCFS_Disk_Scheduling.py
  ```

### 10. Linux System Monitoring Commands (`10_Lab10_Linux_Ubuntu_System_Commands.sh`)
- **Concepts**: Inspection of processes (`ps`), CPU info (`lscpu`), memory (`free`, `/proc/meminfo`), disk (`df`, `lsblk`), uptime, and kernel info (`uname`).
- **Run**:
  ```bash
  bash 10_Lab10_Linux_Ubuntu_System_Commands.sh
  ```

---

## 🛠️ Prerequisites
- **Python**: Python 3.8 or higher.
- **Operating System / Shell**: Ubuntu/Linux, macOS, or WSL (Windows Subsystem for Linux) for the Bash scripts.

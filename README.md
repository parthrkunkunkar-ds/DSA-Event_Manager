Event Management System Using Data Structures and Algorithms

A comprehensive event planning and execution system built with Python Tkinter, demonstrating practical implementation of core data structures and algorithms.

 📋 Project Overview

This Event Management System provides a complete solution for organizing events from initial planning to live execution. The application demonstrates real-world usage of Stack, Queue, LinkedList, BST, and HashMap data structures through an intuitive GUI interface.

🚀 Features

### 6 Core Modules:
1. Meeting Schedule & Agenda - Stack-based undo functionality
2. Principal Permission / Day Fixing - Queue-based approval workflow + BST date management
3. Notices & Announcements - LinkedList for dynamic announcements + HashMap for responsibilities
4. Needs for Execution - Logistics management with vendor mapping
5. Rehearsal - Performance scheduling and event flow control
6. Execution Day - Live event management with last-minute modifications

### Key Technical Features:
- Undo Operations: Stack implementation for agenda and logistics items
- Sequential Processing: Queue-based FIFO workflows
- Dynamic Data Management: LinkedList for flexible announcements
- Efficient Searching: BST for O(log n) date and step lookups
- Fast Mappings: HashMap for O(1) responsibility and vendor assignments
- Hybrid Operations: Queue-to-List conversion for last-minute changes

## 🛠️ Technology Stack

- Language: Python 3.x
- GUI Framework: Tkinter with TTK widgets
- Theme: Professional 'clam' theme styling
- Storage: In-memory data structures (session-based)
- Code Size: 700+ lines of functional code

## 📊 Data Structures Implemented

```python
# Custom implementations
class Stack:          # LIFO operations for undo functionality
class Queue:          # FIFO operations for sequential processing  
class LinkedList:     # Dynamic node-based storage
class BST:           # Binary search tree for efficient searching

# Global data containers
execution_queue = deque()        # Main event execution flow
agenda_stack = Stack()           # Agenda undo operations
approval_queue = Queue()         # Permission requests
dates_bst = BST()               # Event dates storage
announcements = LinkedList()     # Dynamic announcements
responsibility_map = {}          # Member-task HashMap
vendor_map = {}                 # Item-vendor HashMap
volunteer_map = {}              # Volunteer duty HashMap
```

## 🖥️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes with Python)

### Running the Application
1. Clone the repository:
```bash
git clone https://github.com/yourusername/event-management-system.git
cd event-management-system
```

2. Run the main file:
```bash
python main.py
```

## 💡 Usage Guide

### Getting Started
1. Launch the application - main menu displays 6 modules
2. Navigate through modules sequentially for complete event planning
3. Use the professional GUI interface with consistent styling

### Module Workflow
1. Meeting → Plan agenda with undo capabilities
2. Permission → Queue approval requests + manage dates
3. Notices → Handle announcements + assign responsibilities  
4. Logistics → Manage items + map vendors
5. Rehearsal → Schedule performances + control event flow
6. Execution → Live event management + emergency modifications

### Key Operations
- Add items: Input validation with real-time GUI updates
- Undo actions: Stack-based rollback for agenda and logistics
- Search functionality: Efficient BST and HashMap lookups
- Last-minute changes: Dynamic queue modifications during live events

## 🔧 Code Architecture

### Global Variables (17 total)
- Primary execution containers
- Module-specific data structures
- Mapping dictionaries for relationships

### Custom Classes (4 implementations)
- Stack, Queue, LinkedList, BST with full method implementations
- Professional GUI class with 6 integrated modules

 Key Algorithms
- Time Complexity: O(1) HashMap, O(log n) BST, O(1) Queue operations
- Space Complexity: O(n) linear storage across all structures
- Hybrid Logic: Queue↔List conversions for operational flexibility

 📈 Performance Characteristics

- HashMap Operations: O(1) for responsibility/vendor assignments
- BST Operations: O(log n) for date searching and event steps
- Queue Operations: O(1) for FIFO processing
- Memory Usage: Session-based storage with automatic garbage collection

 🎯 Educational Objectives

This project demonstrates:
- Practical application of theoretical DSA concepts
- When to choose specific data structures for different problems
- GUI development with professional styling
- Real-world problem-solving using algorithms
- Hybrid data structure operations for complex requirements

🔮 Future Enhancements

- Persistence: JSON/CSV file storage for data between sessions
- Database Integration: Multi-user support with SQL database
- Networking: Remote event coordination capabilities
- Analytics: Event performance metrics and reporting
- Mobile App: Cross-platform mobile version

 🐛 Known Limitations

- Single-user session-based storage (no data persistence)
- BST can become unbalanced (would benefit from AVL/Red-Black implementation)
- No concurrent access handling (single-threaded GUI application)

🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

 📝 License

This project is open source and available under the [MIT License](LICENSE).

 👨‍💻 Author

Parth. R. Kunkunkar
- Course: Data Structures and Algorithms
- Institution: MVLU
- Contact: parth.r.kunkunkar@gmail.com

---

Project Stats: 700+ lines of code | 17 global variables | 6 GUI modules | 5 data structures

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from collections import deque

# Global data structures
execution_queue = deque()
fix_queue = deque()
volunteers = []
feedback_ratings = []

# DSA Classes
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def display(self):
        return self.stack

class Queue:
    def __init__(self):
        self.q = deque()
    
    def enqueue(self, item):
        self.q.append(item)
    
    def dequeue(self):
        return self.q.popleft() if self.q else None
    
    def display(self):
        return list(self.q)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    
    def remove(self, key):
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            if prev:
                prev.next = temp.next
            else:
                self.head = temp.next
    
    def display(self):
        res = []
        temp = self.head
        while temp:
            res.append(temp.data)
            temp = temp.next
        return res

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    
    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.key)
            self.inorder(root.right, result)
    
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

# Data structures initialization
agenda = []
agenda_stack = Stack()
approval_queue = Queue()
dates_bst = BST()
dates_root = None
announcements = LinkedList()
responsibility_map = {}
logistics = []
vendor_map = {}
logistics_stack = Stack()
rehearsal_queue = Queue()
event_flow = BST()
event_root = None
rehearsal_list = LinkedList()
event_queue = Queue()
fixes_stack = Stack()
volunteer_map = {}
feedback_bst = BST()
feedback_root = None
performance_map = {}
event_flow_map = {}

class EventManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), background='#f0f0f0')
        
        self.create_main_menu()
    
    def create_main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title_label = ttk.Label(self.root, text="Event Management System", style='Title.TLabel')
        title_label.pack(pady=20)
        
        # Button frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Menu buttons
        buttons = [
            ("Meeting Schedule & Agenda", self.meeting_menu),
            ("Principal Permission / Day Fixing", self.permission_menu),
            ("Notices & Announcements", self.notices_menu),
            ("Needs for Execution", self.logistics_menu),
            ("Rehearsal", self.rehearsal_menu),
            ("Execution Day", self.execution_menu)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(button_frame, text=text, command=command, width=30)
            btn.pack(pady=5)
        
        # Exit button
        exit_btn = ttk.Button(button_frame, text="Exit", command=self.root.quit, width=30)
        exit_btn.pack(pady=20)
    
    def meeting_menu(self):
        self.clear_window()
        
        ttk.Label(self.root, text="Meeting Schedule & Agenda", style='Title.TLabel').pack(pady=10)
        
        # Input frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="Agenda Point:").grid(row=0, column=0, padx=5, sticky='w')
        self.agenda_entry = ttk.Entry(input_frame, width=40)
        self.agenda_entry.grid(row=0, column=1, padx=5)
        
        ttk.Button(input_frame, text="Add", command=self.add_agenda).grid(row=0, column=2, padx=5)
        ttk.Button(input_frame, text="Undo Last", command=self.undo_agenda).grid(row=0, column=3, padx=5)
        
        # Search frame
        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=5)
        
        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, padx=5)
        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.grid(row=0, column=1, padx=5)
        ttk.Button(search_frame, text="Search", command=self.search_agenda).grid(row=0, column=2, padx=5)
        
        # Display area
        self.agenda_display = scrolledtext.ScrolledText(self.root, height=15, width=80)
        self.agenda_display.pack(pady=10)
        
        self.update_agenda_display()
        
        ttk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)
    
    def add_agenda(self):
        point = self.agenda_entry.get().strip()
        if not point:
            messagebox.showerror("Error", "Agenda point cannot be empty.")
            return
        
        agenda.append(point)
        agenda_stack.push(point)
        self.agenda_entry.delete(0, tk.END)
        self.update_agenda_display()
        messagebox.showinfo("Success", f"Added: '{point}'. Total points: {len(agenda)}")
    
    def undo_agenda(self):
        removed = agenda_stack.pop()
        if removed is None:
            messagebox.showerror("Error", "No agenda point to undo.")
        else:
            if removed in agenda:
                agenda.remove(removed)
            self.update_agenda_display()
            messagebox.showinfo("Success", f"Undo successful: '{removed}'. Remaining points: {len(agenda)}")
    
    def search_agenda(self):
        point = self.search_entry.get().strip()
        if point in agenda:
            messagebox.showinfo("Search Result", f"Found: '{point}'")
        else:
            messagebox.showinfo("Search Result", "Not Found")
    
    def update_agenda_display(self):
        self.agenda_display.delete(1.0, tk.END)
        self.agenda_display.insert(tk.END, "Current Agenda:\n\n")
        for i, item in enumerate(agenda, 1):
            self.agenda_display.insert(tk.END, f"{i}. {item}\n")
    
    def permission_menu(self):
        global dates_root
        self.clear_window()
        
        ttk.Label(self.root, text="Principal Permission / Day Fixing", style='Title.TLabel').pack(pady=10)
        
        # Request frame
        req_frame = ttk.LabelFrame(self.root, text="Approval Requests", padding=10)
        req_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(req_frame, text="Request:").grid(row=0, column=0, padx=5, sticky='w')
        self.request_entry = ttk.Entry(req_frame, width=40)
        self.request_entry.grid(row=0, column=1, padx=5)
        ttk.Button(req_frame, text="Add Request", command=self.add_request).grid(row=0, column=2, padx=5)
        ttk.Button(req_frame, text="Approve Next", command=self.approve_request).grid(row=0, column=3, padx=5)
        
        # Date frame
        date_frame = ttk.LabelFrame(self.root, text="Event Dates", padding=10)
        date_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(date_frame, text="Date (DD-MM-YYYY):").grid(row=0, column=0, padx=5, sticky='w')
        self.date_entry = ttk.Entry(date_frame, width=20)
        self.date_entry.grid(row=0, column=1, padx=5)
        ttk.Button(date_frame, text="Insert Date", command=self.insert_date).grid(row=0, column=2, padx=5)
        ttk.Button(date_frame, text="Search Date", command=self.search_date).grid(row=0, column=3, padx=5)
        ttk.Button(date_frame, text="View All Dates", command=self.view_dates).grid(row=0, column=4, padx=5)
        
        # Display area
        self.permission_display = scrolledtext.ScrolledText(self.root, height=12, width=80)
        self.permission_display.pack(pady=10)
        
        self.update_permission_display()
        
        ttk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)
    
    def add_request(self):
        req = self.request_entry.get().strip()
        if not req:
            messagebox.showerror("Error", "Request cannot be empty.")
            return
        
        approval_queue.enqueue(req)
        self.request_entry.delete(0, tk.END)
        self.update_permission_display()
        messagebox.showinfo("Success", f"Request queued. Queue size: {len(approval_queue.q)}")
    
    def approve_request(self):
        approved = approval_queue.dequeue()
        if approved is None:
            messagebox.showerror("Error", "No requests pending.")
        else:
            self.update_permission_display()
            messagebox.showinfo("Success", f"Approved: {approved}. Remaining in queue: {len(approval_queue.q)}")
    
    def insert_date(self):
        global dates_root
        date = self.date_entry.get().strip()
        if not date:
            messagebox.showerror("Error", "Date cannot be empty.")
            return
        
        dates_root = dates_bst.insert(dates_root, date)
        self.date_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Date inserted: {date}")
    
    def search_date(self):
        date = self.date_entry.get().strip()
        found = dates_bst.search(dates_root, date)
        result = "Available" if found else "Not Available"
        messagebox.showinfo("Search Result", result)
    
    def view_dates(self):
        res = []
        dates_bst.inorder(dates_root, res)
        if res:
            messagebox.showinfo("All Dates", "\n".join(res))
        else:
            messagebox.showinfo("All Dates", "No dates added yet.")
    
    def update_permission_display(self):
        self.permission_display.delete(1.0, tk.END)
        self.permission_display.insert(tk.END, "Pending Requests:\n\n")
        for i, req in enumerate(approval_queue.display(), 1):
            self.permission_display.insert(tk.END, f"{i}. {req}\n")
    
    def notices_menu(self):
        self.clear_window()
        
        ttk.Label(self.root, text="Notices & Announcements", style='Title.TLabel').pack(pady=10)
        
        # Announcement frame
        ann_frame = ttk.LabelFrame(self.root, text="Announcements", padding=10)
        ann_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(ann_frame, text="Message:").grid(row=0, column=0, padx=5, sticky='w')
        self.announcement_entry = ttk.Entry(ann_frame, width=50)
        self.announcement_entry.grid(row=0, column=1, padx=5)
        ttk.Button(ann_frame, text="Add", command=self.add_announcement).grid(row=0, column=2, padx=5)
        ttk.Button(ann_frame, text="Remove", command=self.remove_announcement).grid(row=0, column=3, padx=5)
        
        # Responsibility frame
        resp_frame = ttk.LabelFrame(self.root, text="Responsibilities", padding=10)
        resp_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(resp_frame, text="Member:").grid(row=0, column=0, padx=5, sticky='w')
        self.member_entry = ttk.Entry(resp_frame, width=20)
        self.member_entry.grid(row=0, column=1, padx=5)
        ttk.Label(resp_frame, text="Task:").grid(row=0, column=2, padx=5, sticky='w')
        self.task_entry = ttk.Entry(resp_frame, width=30)
        self.task_entry.grid(row=0, column=3, padx=5)
        ttk.Button(resp_frame, text="Assign", command=self.assign_responsibility).grid(row=0, column=4, padx=5)
        
        # Display area
        self.notices_display = scrolledtext.ScrolledText(self.root, height=12, width=80)
        self.notices_display.pack(pady=10)
        
        self.update_notices_display()
        
        ttk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)
    
    def add_announcement(self):
        msg = self.announcement_entry.get().strip()
        if not msg:
            messagebox.showerror("Error", "Announcement cannot be empty.")
            return
        
        announcements.add(msg)
        self.announcement_entry.delete(0, tk.END)
        self.update_notices_display()
        messagebox.showinfo("Success", f"Announcement added: '{msg}'")
    
    def remove_announcement(self):
        msg = self.announcement_entry.get().strip()
        current = announcements.display()
        if msg in current:
            announcements.remove(msg)
            self.announcement_entry.delete(0, tk.END)
            self.update_notices_display()
            messagebox.showinfo("Success", f"Announcement removed: '{msg}'")
        else:
            messagebox.showerror("Error", "Announcement not found.")
    
    def assign_responsibility(self):
        name = self.member_entry.get().strip()
        task = self.task_entry.get().strip()
        if not name or not task:
            messagebox.showerror("Error", "Name and responsibility are required.")
            return
        
        responsibility_map[name] = task
        self.member_entry.delete(0, tk.END)
        self.task_entry.delete(0, tk.END)
        self.update_notices_display()
        messagebox.showinfo("Success", f"Assigned: {name} -> {task}")
    
    def update_notices_display(self):
        self.notices_display.delete(1.0, tk.END)
        
        self.notices_display.insert(tk.END, "Announcements:\n")
        for i, ann in enumerate(announcements.display(), 1):
            self.notices_display.insert(tk.END, f"{i}. {ann}\n")
        
        self.notices_display.insert(tk.END, "\nResponsibilities:\n")
        for name, task in responsibility_map.items():
            self.notices_display.insert(tk.END, f"• {name}: {task}\n")
    
    def logistics_menu(self):
        self.clear_window()
        
        ttk.Label(self.root, text="Needs for Execution", style='Title.TLabel').pack(pady=10)
        
        # Item frame
        item_frame = ttk.LabelFrame(self.root, text="Logistics Items", padding=10)
        item_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(item_frame, text="Item:").grid(row=0, column=0, padx=5, sticky='w')
        self.item_entry = ttk.Entry(item_frame, width=30)
        self.item_entry.grid(row=0, column=1, padx=5)
        ttk.Button(item_frame, text="Add Item", command=self.add_item).grid(row=0, column=2, padx=5)
        ttk.Button(item_frame, text="Undo Last", command=self.undo_item).grid(row=0, column=3, padx=5)
        
        # Vendor frame
        vendor_frame = ttk.LabelFrame(self.root, text="Vendor Mapping", padding=10)
        vendor_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(vendor_frame, text="Item:").grid(row=0, column=0, padx=5, sticky='w')
        self.vendor_item_entry = ttk.Entry(vendor_frame, width=20)
        self.vendor_item_entry.grid(row=0, column=1, padx=5)
        ttk.Label(vendor_frame, text="Vendor:").grid(row=0, column=2, padx=5, sticky='w')
        self.vendor_entry = ttk.Entry(vendor_frame, width=20)
        self.vendor_entry.grid(row=0, column=3, padx=5)
        ttk.Button(vendor_frame, text="Map", command=self.map_vendor).grid(row=0, column=4, padx=5)
        
        # Display area
        self.logistics_display = scrolledtext.ScrolledText(self.root, height=12, width=80)
        self.logistics_display.pack(pady=10)
        
        self.update_logistics_display()
        
        ttk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)
    
    def add_item(self):
        item = self.item_entry.get().strip()
        if not item:
            messagebox.showerror("Error", "Item cannot be empty.")
            return
        
        logistics.append(item)
        logistics_stack.push(item)
        self.item_entry.delete(0, tk.END)
        self.update_logistics_display()
        messagebox.showinfo("Success", f"Item added: '{item}'. Total items: {len(logistics)}")
    
    def undo_item(self):
        removed = logistics_stack.pop()
        if removed is None:
            messagebox.showerror("Error", "No item to undo.")
        else:
            if removed in logistics:
                logistics.remove(removed)
            self.update_logistics_display()
            messagebox.showinfo("Success", f"Removed: '{removed}'. Remaining items: {len(logistics)}")
    
    def map_vendor(self):
        item = self.vendor_item_entry.get().strip()
        vendor = self.vendor_entry.get().strip()
        if not item or not vendor:
            messagebox.showerror("Error", "Item and vendor are required.")
            return
        
        vendor_map[item] = vendor
        self.vendor_item_entry.delete(0, tk.END)
        self.vendor_entry.delete(0, tk.END)
        self.update_logistics_display()
        messagebox.showinfo("Success", f"Mapped: {item} -> {vendor}")
    
    def update_logistics_display(self):
        self.logistics_display.delete(1.0, tk.END)
        
        self.logistics_display.insert(tk.END, "Logistics Items:\n")
        for i, item in enumerate(logistics, 1):
            self.logistics_display.insert(tk.END, f"{i}. {item}\n")
        
        self.logistics_display.insert(tk.END, "\nVendor Mappings:\n")
        for item, vendor in vendor_map.items():
            self.logistics_display.insert(tk.END, f"• {item} -> {vendor}\n")
    
    def rehearsal_menu(self):
        self.clear_window()
        
        ttk.Label(self.root, text="Rehearsal", style='Title.TLabel').pack(pady=10)
        
        # Performance frame
        perf_frame = ttk.LabelFrame(self.root, text="Performances", padding=10)
        perf_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(perf_frame, text="Performance:").grid(row=0, column=0, padx=5, sticky='w')
        self.performance_entry = ttk.Entry(perf_frame, width=25)
        self.performance_entry.grid(row=0, column=1, padx=5)
        ttk.Label(perf_frame, text="Participant:").grid(row=0, column=2, padx=5, sticky='w')
        self.participant_entry = ttk.Entry(perf_frame, width=25)
        self.participant_entry.grid(row=0, column=3, padx=5)
        ttk.Button(perf_frame, text="Add", command=self.add_performance).grid(row=0, column=4, padx=5)
        ttk.Button(perf_frame, text="Next", command=self.next_performance).grid(row=0, column=5, padx=5)
        
        # Event flow frame
        flow_frame = ttk.LabelFrame(self.root, text="Event Flow", padding=10)
        flow_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(flow_frame, text="Flow No:").grid(row=0, column=0, padx=5, sticky='w')
        self.step_entry = ttk.Entry(flow_frame, width=10)
        self.step_entry.grid(row=0, column=1, padx=5)
        ttk.Label(flow_frame, text="Performance:").grid(row=0, column=2, padx=5, sticky='w')
        self.flow_perf_entry = ttk.Entry(flow_frame, width=25)
        self.flow_perf_entry.grid(row=0, column=3, padx=5)
        ttk.Button(flow_frame, text="Add Step", command=self.add_event_step).grid(row=0, column=4, padx=5)
        ttk.Button(flow_frame, text="Search Step", command=self.search_event_step).grid(row=0, column=5, padx=5)
        
        # Display area
        self.rehearsal_display = scrolledtext.ScrolledText(self.root, height=12, width=80)
        self.rehearsal_display.pack(pady=10)
        
        self.update_rehearsal_display()
        
        ttk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)
    
    def add_performance(self):
        perf = self.performance_entry.get().strip()
        part = self.participant_entry.get().strip()
        if not perf or not part:
            messagebox.showerror("Error", "Both performance and participant are required.")
            return
        
        rehearsal_queue.enqueue(perf)
        performance_map[perf] = part
        self.performance_entry.delete(0, tk.END)
        self.participant_entry.delete(0, tk.END)
        self.update_rehearsal_display()
        messagebox.showinfo("Success", f"Queued '{perf}' by '{part}'. Queue size: {len(rehearsal_queue.q)}")
    
    def next_performance(self):
        nxt = rehearsal_queue.dequeue()
        if nxt is None:
            messagebox.showerror("Error", "No performances in queue.")
        else:
            performer = performance_map.get(nxt, "Unknown")
            self.update_rehearsal_display()
            messagebox.showinfo("Next Performance", f"Next: {nxt} by {performer}. Remaining in queue: {len(rehearsal_queue.q)}")
    
    def add_event_step(self):
        try:
            key = int(self.step_entry.get().strip())
            perf = self.flow_perf_entry.get().strip()
            if not perf:
                messagebox.showerror("Error", "Performance cannot be empty.")
                return
            
            event_flow_map[key] = perf
            self.step_entry.delete(0, tk.END)
            self.flow_perf_entry.delete(0, tk.END)
            self.update_rehearsal_display()
            messagebox.showinfo("Success", f"Event step {key} -> '{perf}' added.")
        except ValueError:
            messagebox.showerror("Error", "Step must be a number.")
    
    def search_event_step(self):
        try:
            key = int(self.step_entry.get().strip())
            if key in event_flow_map:
                messagebox.showinfo("Search Result", f"Step {key} is assigned to '{event_flow_map[key]}'")
            else:
                messagebox.showinfo("Search Result", f"Step {key} is empty / not assigned yet.")
        except ValueError:
            messagebox.showerror("Error", "Step must be a number.")
    
    def update_rehearsal_display(self):
        self.rehearsal_display.delete(1.0, tk.END)
        
        self.rehearsal_display.insert(tk.END, "Performance Queue:\n")
        for i, perf in enumerate(rehearsal_queue.display(), 1):
            participant = performance_map.get(perf, "Unknown")
            self.rehearsal_display.insert(tk.END, f"{i}. {perf} by {participant}\n")
        
        self.rehearsal_display.insert(tk.END, "\nEvent Flow (sorted):\n")
        for k in sorted(event_flow_map.keys()):
            self.rehearsal_display.insert(tk.END, f"Step {k}: {event_flow_map[k]}\n")
    
    def execution_menu(self):
        self.clear_window()
        
        ttk.Label(self.root, text="Execution Day", style='Title.TLabel').pack(pady=10)
        
        # Performance management frame
        perf_mgmt_frame = ttk.LabelFrame(self.root, text="Performance Management", padding=10)
        perf_mgmt_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(perf_mgmt_frame, text="Performance:").grid(row=0, column=0, padx=5, sticky='w')
        self.exec_perf_entry = ttk.Entry(perf_mgmt_frame, width=30)
        self.exec_perf_entry.grid(row=0, column=1, padx=5)
        ttk.Button(perf_mgmt_frame, text="Add", command=self.add_exec_performance).grid(row=0, column=2, padx=5)
        ttk.Button(perf_mgmt_frame, text="Next", command=self.next_exec_performance).grid(row=0, column=3, padx=5)
        ttk.Button(perf_mgmt_frame, text="Delete", command=self.delete_performance).grid(row=0, column=4, padx=5)
        
        # Last minute fixes frame
        fix_frame = ttk.LabelFrame(self.root, text="Last-Minute Fixes", padding=10)
        fix_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(fix_frame, text="New Performance:").grid(row=0, column=0, padx=5, sticky='w')
        self.new_perf_entry = ttk.Entry(fix_frame, width=20)
        self.new_perf_entry.grid(row=0, column=1, padx=5)
        ttk.Label(fix_frame, text="Insert After:").grid(row=0, column=2, padx=5, sticky='w')
        self.after_perf_entry = ttk.Entry(fix_frame, width=20)
        self.after_perf_entry.grid(row=0, column=3, padx=5)
        ttk.Button(fix_frame, text="Insert", command=self.insert_performance).grid(row=0, column=4, padx=5)
        
        # Volunteer frame
        vol_frame = ttk.LabelFrame(self.root, text="Volunteers", padding=10)
        vol_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(vol_frame, text="Name:").grid(row=0, column=0, padx=5, sticky='w')
        self.vol_name_entry = ttk.Entry(vol_frame, width=20)
        self.vol_name_entry.grid(row=0, column=1, padx=5)
        ttk.Label(vol_frame, text="Duty:").grid(row=0, column=2, padx=5, sticky='w')
        self.vol_duty_entry = ttk.Entry(vol_frame, width=20)
        self.vol_duty_entry.grid(row=0, column=3, padx=5)
        ttk.Button(vol_frame, text="Assign", command=self.assign_volunteer).grid(row=0, column=4, padx=5)
        
        # Feedback frame
        feedback_frame = ttk.LabelFrame(self.root, text="Audience Feedback", padding=10)
        feedback_frame.pack(pady=10, padx=20, fill='x')
        
        ttk.Label(feedback_frame, text="Rating (1-5):").grid(row=0, column=0, padx=5, sticky='w')
        self.rating_entry = ttk.Entry(feedback_frame, width=10)
        self.rating_entry.grid(row=0, column=1, padx=5)
        ttk.Button(feedback_frame, text="Add Feedback", command=self.add_feedback).grid(row=0, column=2, padx=5)
        ttk.Button(feedback_frame, text="View Feedback", command=self.view_feedback).grid(row=0, column=3, padx=5)
        
        # Display area
        self.execution_display = scrolledtext.ScrolledText(self.root, height=8, width=80)
        self.execution_display.pack(pady=10)
        
        self.update_execution_display()
        
        ttk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack(pady=10)
    
    def add_exec_performance(self):
        perf = self.exec_perf_entry.get().strip()
        if not perf:
            messagebox.showerror("Error", "Performance cannot be empty.")
            return
        
        execution_queue.append(perf)
        self.exec_perf_entry.delete(0, tk.END)
        self.update_execution_display()
        messagebox.showinfo("Success", f"Performance scheduled: '{perf}'. Queue size: {len(execution_queue)}")
    
    def next_exec_performance(self):
        if execution_queue:
            now = execution_queue.popleft()
            self.update_execution_display()
            messagebox.showinfo("Now Playing", f"Now: {now}. Remaining in queue: {len(execution_queue)}")
        else:
            messagebox.showerror("Error", "No performances scheduled.")
    
    def delete_performance(self):
        to_delete = self.exec_perf_entry.get().strip()
        if not to_delete:
            messagebox.showerror("Error", "Enter performance name to delete.")
            return
        
        temp = list(execution_queue)
        if to_delete in temp:
            temp.remove(to_delete)
            execution_queue.clear()
            execution_queue.extend(temp)
            self.exec_perf_entry.delete(0, tk.END)
            self.update_execution_display()
            messagebox.showinfo("Success", f"Deleted performance: '{to_delete}'.")
        else:
            messagebox.showerror("Error", f"Performance '{to_delete}' not found in the schedule.")
    
    def insert_performance(self):
        new_perf = self.new_perf_entry.get().strip()
        after_perf = self.after_perf_entry.get().strip()
        
        if not new_perf:
            messagebox.showerror("Error", "New performance cannot be empty.")
            return
        
        temp = list(execution_queue)
        if after_perf in temp:
            idx = temp.index(after_perf) + 1
            temp.insert(idx, new_perf)
            execution_queue.clear()
            execution_queue.extend(temp)
            messagebox.showinfo("Success", f"Inserted '{new_perf}' after '{after_perf}'.")
        else:
            execution_queue.append(new_perf)
            messagebox.showinfo("Info", f"'{after_perf}' not found in current queue. Adding '{new_perf}' at end.")
        
        self.new_perf_entry.delete(0, tk.END)
        self.after_perf_entry.delete(0, tk.END)
        self.update_execution_display()
    
    def assign_volunteer(self):
        name = self.vol_name_entry.get().strip()
        duty = self.vol_duty_entry.get().strip()
        if not name or not duty:
            messagebox.showerror("Error", "Name and duty cannot be empty.")
            return
        
        volunteer_map[name] = duty
        self.vol_name_entry.delete(0, tk.END)
        self.vol_duty_entry.delete(0, tk.END)
        self.update_execution_display()
        messagebox.showinfo("Success", f"Volunteer '{name}' assigned duty '{duty}'.")
    
    def add_feedback(self):
        try:
            rating = int(self.rating_entry.get().strip())
            if 1 <= rating <= 5:
                feedback_ratings.append(rating)
                feedback_ratings.sort()
                self.rating_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Feedback added.")
            else:
                messagebox.showerror("Error", "Rating must be between 1 and 5.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")
    
    def view_feedback(self):
        if feedback_ratings:
            avg_rating = sum(feedback_ratings) / len(feedback_ratings)
            feedback_text = f"Ratings: {feedback_ratings}\nAverage Rating: {avg_rating:.2f}"
            messagebox.showinfo("Feedback Summary", feedback_text)
        else:
            messagebox.showinfo("Feedback Summary", "No feedback ratings yet.")
    
    def update_execution_display(self):
        self.execution_display.delete(1.0, tk.END)
        
        self.execution_display.insert(tk.END, "Performance Schedule:\n")
        for i, perf in enumerate(execution_queue, 1):
            self.execution_display.insert(tk.END, f"{i}. {perf}\n")
        
        self.execution_display.insert(tk.END, "\nVolunteers:\n")
        for name, duty in volunteer_map.items():
            self.execution_display.insert(tk.END, f"• {name}: {duty}\n")
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    app = EventManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

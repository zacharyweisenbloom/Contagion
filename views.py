import observer
import time

class View(observer.Observer):
    """Abstract view class (cannot create view objects from it, but can 
    extend it through inheritance, e.g., class MyCoolView(View). This 
    ensures that all views are Observable and also that they implement 
    the update method. 
    """
    
    def __init__(self, width: int, height: int):
        """Initialize the view"""
        self.width = width
        self.height = height
    
    def update(self): 
        """Update the display. Subclasses MUST implement this method."""
        raise NotImplementedError("This is an abstract base class, cannot be called directly.")
    
    
class TextView(View):
    """A concrete class implementing the View interface. 
    """
    
    def __init__(self, width: int = 0, height: int = 0, delay: int = 0.5):
        """Initialize a purely text view, which simply prints to stdout"""
        super().__init__(width, height)
        self.contents = []    # A list of strings to print
        self.delay = delay     # Delay after updates (in seconds)
        
    def add_info(self, info: str):
        """Add a string to the contents list."""
        self.contents.append(info)
        
    def receive_notification(self, subject: observer.Observable, event: str):
        """Receive notifications from objects that are being observed,
        for example the model.
        
        Args:
            subject: the Observable object that has changed
            event: the event that occurred
        """
        self.add_info(f"{subject} changed: {event}")
        
    def update(self):
        """Print all the accumulated contents, one element per line."""
        print('\n'.join(self.contents))
        time.sleep(self.delay)
        
    def clear(self):
        self.contents = []
        
        
class GraphicalView(View):
    """OPTIONAL!! A concrete class implementing the View interface. OPTIONAL!!"""
    
    def __init__(self, width: int, height: int):
        """Initialize a purely text view, which simply prints to stdout"""
        super().__init__(width, height)
        self.contents = []    # A list of strings to print

    def update(self):
        pass
  